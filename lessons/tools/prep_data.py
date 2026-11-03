"""Turn the raw daily parquet files into small JSON series for the lesson pages.
Source: github.com/aswinv90/indian-market-historical-data (daily NSE/BSE data, Yahoo-derived).
Run: python3 prep_data.py <raw_dir> <out_dir>
Prices are 'as traded' unless a name ends in _adj (split/bonus adjusted)."""
import sys, json, pandas as pd
raw, out = sys.argv[1], sys.argv[2]

def load(n):
    d = pd.read_parquet(f"{raw}/{n}.parquet").dropna(subset=["Close"])
    d.index = pd.to_datetime(d.index)
    return d

def unadjust(d):
    """Undo split/bonus adjustment so prices match what was quoted that day."""
    if "Stock Splits" not in d: return d
    f = pd.Series(1.0, index=d.index)
    for dt, r in d.loc[d["Stock Splits"] > 0, "Stock Splits"].items():
        f[d.index < dt] *= r
    d = d.copy()
    for c in ["Open", "High", "Low", "Close"]: d[c] = d[c] * f
    d["Volume"] = d["Volume"] / f
    return d

def r(x, n=2): return round(float(x), n)
def monthly(d, start=None):
    m = d["Close"].resample("ME").last().dropna()
    if start: m = m[m.index >= start]
    return [[i.strftime("%Y-%m"), r(v)] for i, v in m.items()]
def daily(d, a, b, vol=False):
    s = d[(d.index >= a) & (d.index <= b)]
    rows = []
    for i, x in s.iterrows():
        row = [i.strftime("%Y-%m-%d"), r(x.Open), r(x.High), r(x.Low), r(x.Close)]
        if vol: row.append(int(x.Volume))
        rows.append(row)
    return rows

S = {}
nifty, sensex = load("NIFTY_50"), load("SENSEX")
bank, it = load("NIFTY_BANK"), load("NIFTY_IT")
S["nifty_m"] = monthly(nifty)
S["sensex_m"] = monthly(sensex, "2000-01-01")
S["bank_m"] = monthly(bank)
S["it_m"] = monthly(it)
S["nifty_2008"] = daily(nifty, "2007-12-01", "2009-06-30")
S["nifty_2020"] = daily(nifty, "2020-01-01", "2020-12-31")
S["nifty_jun2024"] = daily(nifty, "2024-05-20", "2024-06-14")
S["nifty_last"] = daily(nifty, "2026-09-01", "2026-12-31")
S["sensex_last"] = daily(sensex, "2026-09-01", "2026-12-31")

cpi = pd.read_csv(f"{raw}/cpi.csv", parse_dates=["Date"])
cpi = cpi[cpi.Date >= "2000-01-01"]
S["cpi_m"] = [[d.strftime("%Y-%m"), r(v, 3), (None if pd.isna(y) else r(y))] for d, v, y in zip(cpi.Date, cpi.CPI_Index, cpi.Inflation_YoY_Pct)]
g = pd.read_parquet(f"{raw}/GOLD_INR.parquet"); g.index = pd.to_datetime(g.index)
S["gold_y"] = [[i.strftime("%Y-%m-%d"), r(v)] for i, v in g["Gold_24K_10g"].items() if i.year >= 2000]

stocks = {}
for n in ["RELIANCE_NS", "TCS_NS", "INFY_NS", "HDFCBANK_NS", "ETERNAL_NS", "PAYTM_NS", "LICI_NS", "IRCTC_NS", "YESBANK_NS", "ADANIENT_NS"]:
    stocks[n] = load(n)
for n in ["RELIANCE_NS", "TCS_NS", "INFY_NS", "HDFCBANK_NS"]:
    S[n.split("_")[0].lower() + "_m_adj"] = monthly(stocks[n], "2005-01-01")
u = {n: unadjust(d) for n, d in stocks.items()}
S["eternal_ipo"] = daily(u["ETERNAL_NS"], "2021-07-23", "2022-07-31", True)
S["paytm_ipo"] = daily(u["PAYTM_NS"], "2021-11-18", "2022-11-30", True)
S["lic_ipo"] = daily(u["LICI_NS"], "2022-05-17", "2023-05-31", True)
S["irctc_ipo"] = daily(u["IRCTC_NS"], "2019-10-14", "2020-10-31", True)
S["reliance_oct2024"] = daily(u["RELIANCE_NS"], "2024-10-14", "2024-11-08", True)
S["reliance_d"] = daily(u["RELIANCE_NS"], "2026-08-01", "2026-12-31", True)
S["yesbank_2020"] = daily(u["YESBANK_NS"], "2020-02-20", "2020-03-31", True)
S["adani_2023"] = daily(u["ADANIENT_NS"], "2023-01-16", "2023-02-28", True)
S["tcs_d"] = daily(u["TCS_NS"], "2026-08-01", "2026-12-31", True)
S["yesbank_d"] = daily(u["YESBANK_NS"], "2026-08-01", "2026-12-31", True)

for k, v in S.items():
    json.dump(v, open(f"{out}/{k}.json", "w"), separators=(",", ":"))
    print(k, len(v), v[0], v[-1])
