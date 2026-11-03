# Your Trading Curriculum: Beginner to Expert (Indian Market)

Nov 3, 2026 · Ramyasri. Exported from the [curriculum doc](https://claude.ai/artifact/56icvrSfDii52S12ZcVftY); the doc is the version to edit.

## How this course works

You go through 6 levels in order, about 60 lessons in total, and you only unlock the next level when you pass its goals. At roughly 1 hour a day, plan for 9 to 12 months to reach the end, plus at least 3 months of paper trading before any real money.

1. **Level 1, Market basics:** what a share is, how NSE/BSE work, opening a demat account, placing your first (paper) order.
2. **Level 2, Fundamentals and valuation:** reading a company like a business owner, so you never trade junk.
3. **Level 3, Technical analysis:** reading charts, the main skill of short-term trading.
4. **Level 4, Short-term strategies:** intraday and swing trading setups with exact rules.
5. **Level 5, Risk management and psychology:** the part that decides whether you keep your money.
6. **Level 6, Expert:** futures and options (to understand only, never to trade), backtesting with code, and building your own trading system.

Every lesson follows the same shape: one idea, a real NSE example from history, a short quiz, and a practice task. Every level ends with a checkpoint test. Your coding skills become a superpower from Level 3 onward, where you'll write small scripts to test ideas on real data.

**Three rules for the whole journey:** you never risk money you can't afford to lose, you paper trade every strategy before using it live, and you keep a trading journal from Level 1.

## Level 1: Market basics (India)

You learn what the stock market is, who runs it, and how a buy order actually travels from your phone to the exchange. About 10 lessons, 2 to 3 weeks.

**Lessons**

1. Money, inflation and why people invest (₹100 today vs in 10 years)
2. What a share is: owning a slice of a company like Reliance or TCS
3. How a company lists: IPOs, the primary vs secondary market
4. NSE, BSE and SEBI: who does what, and how SEBI protects you
5. Indices: Nifty 50, Sensex, Bank Nifty, and sector indices
6. Brokers, demat and trading accounts, CDSL/NSDL, and choosing a broker (Zerodha, Groww, Upstox, Angel One)
7. Market timings: pre-open (9:00 to 9:15), normal session (9:15 to 3:30), holidays
8. Order types: market, limit, stop-loss (SL and SL-M), GTT, and product types (CNC, MIS, NRML)
9. Settlement (T+1), circuits, bid/ask, volume and liquidity
10. Costs and taxes: brokerage, STT, GST, stamp duty, DP charges, and how short-term gains and intraday profits are taxed

**Key terms:** share, equity, IPO, index, broker, demat, DP, SEBI, T+1, bid, ask, spread, circuit limit, market order, limit order, stop-loss, CNC, MIS, STT, STCG, LTCG.

**Goals before moving on**

- [ ] Explain in your own words what happens when you press Buy
- [ ] Calculate the full cost (brokerage, STT, GST, stamp duty) of a ₹10,000 trade
- [ ] Know the difference between CNC and MIS and when each is used
- [ ] Score 80% or more on the Level 1 checkpoint

**Practice tasks**

- Look up the Nifty 50's closing value for the last 5 days on nseindia.com and note the daily change
- Read one real NSE stock page (for example INFY) and name every number on it
- Place 5 paper orders (one of each order type) in the practice tool and start your trading journal

**Real data used:** historical Nifty 50 levels since 2000 (the 2008 crash, the March 2020 crash and recovery) to show what markets do over time.

## Level 2: Fundamentals and valuation

You learn to judge whether a company is healthy and fairly priced, so that even as a short-term trader you pick strong stocks and understand why results days move prices. About 9 lessons, 3 to 4 weeks.

**Lessons**

1. How a business makes money: revenue, costs, profit
2. Reading the profit and loss statement (using a real annual report, such as HDFC Bank or Asian Paints)
3. Reading the balance sheet: assets, debt, equity
4. Cash flow: why cash matters more than reported profit
5. Key ratios: P/E, P/B, EPS, ROE, ROCE, debt-to-equity, dividend yield
6. Valuation basics: cheap vs expensive, comparing peers within a sector
7. Quarterly results, management commentary, and why stocks gap on results day
8. Corporate actions: dividends, bonus, splits, buybacks, rights issues
9. Red flags: promoter pledging, falling margins, auditor resignations, governance issues

**Key terms:** revenue, EBITDA, net profit, EPS, P/E, P/B, ROE, ROCE, debt-to-equity, free cash flow, market cap, large/mid/small cap, promoter holding, pledge, FII/DII.

**Goals before moving on**

- [ ] Read a real company's quarterly results and say whether they were good or bad, with numbers
- [ ] Compare 3 companies in one sector on 5 ratios and pick the strongest
- [ ] Spot at least 2 red flags in a case study
- [ ] Score 80% or more on the Level 2 checkpoint

**Practice tasks**

- Build a watchlist of 20 fundamentally strong Nifty 100 stocks, with a one-line reason for each
- Track one company through a results announcement and log how the price reacted the next day

**Real data used:** real annual reports and quarterly filings from NSE/BSE, and case studies of real collapses (for example Yes Bank 2018 to 2020) and steady compounders.

## Level 3: Technical analysis

You learn to read price charts, which is the core skill of short-term trading. This is the longest level: about 12 lessons, 5 to 6 weeks, almost all on real NSE charts.

**Lessons**

1. What a chart shows: line vs candlestick, timeframes (1-minute to monthly)
2. Candlestick basics: body, wicks, doji, hammer, engulfing, and what they say about buyers vs sellers
3. Trends: higher highs and higher lows, trendlines, trading with the trend
4. Support and resistance: why prices pause at certain levels, breakouts and fake breakouts
5. Volume: confirming moves, volume spikes, delivery percentage on NSE
6. Moving averages: SMA, EMA, the 20/50/200, crossovers
7. Momentum indicators: RSI, MACD, and divergence
8. Volatility: Bollinger Bands, ATR (you'll use ATR for stop-losses later)
9. Intraday tools: VWAP, opening range, previous day high/low, pivot points
10. Chart patterns: flags, triangles, double tops/bottoms, head and shoulders, cup and handle
11. Multi-timeframe analysis: daily for direction, 15-minute for entry
12. Your first code: download real NSE data with Python and plot candles plus indicators yourself

**Key terms:** OHLC, candlestick, timeframe, trend, support, resistance, breakout, volume, delivery %, SMA, EMA, RSI, MACD, Bollinger Bands, ATR, VWAP, pivot, gap up/down, divergence.

**Goals before moving on**

- [ ] On 10 unseen real charts, correctly mark trend, support and resistance
- [ ] Explain what RSI, MACD, VWAP and ATR measure, and one weakness of each
- [ ] Write a script that fetches 2 years of daily data for a stock and computes 3 indicators
- [ ] Score 80% or more on the Level 3 checkpoint

**Practice tasks**

- "Chart replay": the tool hides the future on a real past chart; you predict up or down and see the result (aim for 50 replays)
- Mark support and resistance on Nifty, Bank Nifty and 5 watchlist stocks every weekend

**Real data used:** real daily and intraday candles from NSE stocks and indices, including famous moves (for example Adani group stocks in Jan 2023, Nifty on election result day in June 2024).

## Level 4: Short-term strategies (swing and intraday)

This is the main focus of the course. You learn a small set of proven setups, each with exact rules for entry, stop-loss, target and exit, and you test each one on real data before trusting it. About 11 lessons, 6 to 8 weeks. Swing trading is your main style because it fits a 9-to-6 job: you plan trades in the evening and place orders (with stop-losses) before work. Intraday is still taught and practised, so you understand it fully, but only on days off.

**Lessons**

1. Trading styles compared: scalping, intraday, swing, positional, and which fits a working person
2. Anatomy of a trading plan: setup, entry trigger, stop-loss, target, position size, exit
3. Stock selection: scanners, liquidity filters, sector strength, news and results calendars
4. Swing setup 1: pullback to the 20 EMA in an uptrend
5. Swing setup 2: breakout from a base with volume
6. Swing setup 3: support bounce with a reversal candle
7. How the intraday day works: pre-market, the first 15 minutes, lunch lull, the last hour, MIS auto square-off
8. Intraday setup 1: Opening Range Breakout (ORB)
9. Intraday setup 2: VWAP pullback and VWAP reclaim
10. Gaps: gap-and-go vs gap fill, and trading results-day moves
11. Reviewing trades: win rate, average win vs average loss, expectancy

**Key terms:** setup, trigger, entry, stop-loss, target, risk-reward ratio, trailing stop, scanner, ORB, VWAP pullback, gap-and-go, square-off, win rate, expectancy, slippage.

**Goals before moving on**

- [ ] Write a full one-page trading plan for one swing and one intraday setup
- [ ] Manually backtest each setup on 30 real past examples and record the results
- [ ] Paper trade at least 40 trades over 4 weeks, every one logged in the journal
- [ ] Show positive expectancy on paper, or explain clearly why it isn't working

**Practice tasks**

- Daily: run the scanner after market close, pick 0 to 3 swing candidates, write the plan before 9:15 next day
- Intraday practice: paper trade the ORB live on days off, and on chart replay at weekends
- Weekly: review the journal and calculate win rate and expectancy

**Real data used:** real past setups on Nifty 100 stocks (good trades and failed ones), then live market data in the paper trading tool.

## Level 5: Risk management and psychology

This level decides whether you survive as a trader: most beginners lose money not because their setups are bad, but because they risk too much and break their own rules. About 9 lessons, 3 to 4 weeks. Lessons 1 to 3 also open alongside Level 4, because you must size positions from your first paper trade.

**Lessons**

1. The 1% rule: never risk more than 1% of your capital on one trade
2. Position sizing: shares to buy = (capital × risk %) ÷ (entry minus stop-loss), with worked ₹ examples
3. Risk-reward and expectancy: why a 40% win rate can still make money
4. Daily and weekly loss limits, and when to stop trading for the day
5. Drawdowns: the maths of recovery (a 50% loss needs a 100% gain)
6. Leverage and margin: how MIS leverage and F&O magnify losses
7. Trading psychology: fear, greed, FOMO, revenge trading, overconfidence after a win streak
8. The trading journal as a mirror: tagging mistakes and emotions
9. Building routines: pre-market checklist, post-market review, rules you never break

**Key terms:** risk per trade, position size, R-multiple, expectancy, drawdown, max loss limit, leverage, margin, margin call, FOMO, revenge trading, tilt.

**Goals before moving on**

- [ ] Size any trade correctly in under a minute
- [ ] Write your personal risk rules (max risk per trade, per day, per month)
- [ ] Complete 30 more paper trades with zero rule breaks
- [ ] Score 80% or more on the Level 5 checkpoint

**Practice tasks**

- A position-size calculator built into the site, used on every paper trade
- Monthly review: your biggest 3 mistakes and the rule that would have prevented each

**Real data used:** your own paper trading journal, plus real examples of sharp moves that wiped out over-leveraged traders (for example the March 2020 crash).

## Level 6: Expert: understanding F&O, backtesting, your own system

You learn derivatives and turn everything so far into a tested, rule-based system written in code. About 12 lessons, 8 to 10 weeks. F&O is learn-only: you will never trade it. SEBI's 2024 study found about 9 in 10 individual F&O traders lost money over three years, and it needs screen time a 9-to-6 job can't give. You learn it because option data (open interest, India VIX) tells you a lot about market mood for your swing trades, and so no one can ever sell you an F&O "opportunity" you don't understand.

**Lessons: futures and options**

1. Futures: lot size, margin, expiry, rollover, mark-to-market
2. Options basics: calls, puts, strike, premium, ITM/ATM/OTM, buyer vs seller risk
3. Option pricing and the Greeks: delta, theta, vega, gamma, and implied volatility (India VIX)
4. Reading the option chain: open interest, PCR, max pain, and what they really tell you
5. Option strategies with defined risk: spreads, straddles, strangles, iron condors
6. SEBI's F&O rules: lot sizes, weekly expiries, margin and peak margin rules, and how F&O profits are taxed

**Lessons: backtesting and your own system**

7. Backtesting properly: clean data, transaction costs, slippage, and avoiding look-ahead bias
8. Code a backtester in Python (pandas, plus a library such as backtrader or vectorbt) using real NSE data
9. Measuring a strategy: CAGR, max drawdown, Sharpe ratio, profit factor
10. Overfitting and walk-forward testing: why a perfect backtest usually fails live
11. Algo trading in India: broker APIs, SEBI's retail algo framework, and order automation
12. Capstone: design, backtest, paper trade and document your own system

**Key terms:** futures, lot size, expiry, rollover, MTM, call, put, strike, premium, OI, PCR, IV, India VIX, delta, theta, vega, gamma, spread, backtest, slippage, look-ahead bias, overfitting, walk-forward, Sharpe ratio, CAGR, profit factor.

**Goals to call yourself "expert"**

- [ ] Explain any option position's maximum profit, maximum loss and break-even before entering it
- [ ] Backtest a strategy over 5+ years of real data, including costs, and show realistic results
- [ ] Paper trade your own system for 3 months with results close to the backtest
- [ ] Present your system as a written document a stranger could follow

**Practice tasks**

- For 4 weeks, read the Nifty option chain and India VIX before planning your swing trades, and note in your journal what they told you
- Publish your backtester and capstone results on your own site

**Real data used:** historical Nifty option chains and futures data, years of NSE daily and intraday prices for backtests, and live data for the capstone.

## Real market data: what we'll use and when

Yes, real-time data is worth having, and we'll add it, but at the right moment: from Level 4 onward, when you start paper trading. In Levels 1 to 3 you learn faster from real historical charts, because you can replay years of real moves in minutes and see what happened next, which a live chart can't show you.

| Source | What you get | Delay | Cost | Limits |
| --- | --- | --- | --- | --- |
| NSE daily archives (bhavcopy) | Official end-of-day prices for every stock | End of day | Free | No intraday data; bulk files, not an API |
| yfinance (Yahoo, symbols like INFY.NS) | Years of daily and some intraday history | About 15 minutes | Free | Unofficial, can break, intraday history only goes back weeks |
| Broker API: Zerodha Kite Connect | Live tick-by-tick prices, history, order placement | Real-time | Monthly fee for the data plan (check current price) | Needs a Zerodha account; login token expires every day |
| Broker API: Upstox, Angel One SmartAPI, Dhan | Live prices, history, order placement | Real-time | Free or low cost with an account | Needs a KYC'd account; rate limits; quality varies |
| Scraping nseindia.com | Live-ish quotes, option chains | Varies | Free | Against NSE's terms, blocks bots often; we won't rely on it |

**The plan:**

1. **Levels 1 to 3:** real historical NSE data (NSE archives plus yfinance), saved into the site so lessons always load. This powers chart replay.
2. **Level 4 onward:** a paper trading tool on live data from a broker API. I recommend starting with a free broker API (Upstox or Angel One) and moving to Zerodha Kite later if you want it. You'll need a demat account by then anyway.
3. **Level 6:** the same API feeds your backtester and, only after the capstone, real automated orders.

Two technical notes for when we build it: broker API keys must live on a small backend, never in browser code, and broker data is licensed for your personal use only, so the site stays private.

## From paper trading to real money

You move to real money in small steps, and each step has a gate you must pass first. Paper trading feels easy because no money is at stake, so the first real trades are kept tiny on purpose.

1. **Paper trading (at least 3 months, from Level 4).** Gate: 100+ logged trades, positive expectancy, no rule breaks in the last 30.
2. **Tiny real money: ₹10,000 to ₹25,000, swing trades only, no leverage (CNC).** Gate: 2 months, following the plan, results close to paper.
3. **Optional: intraday on days off only, with small size.** Gate: 2 more months within your daily loss limit every day.
4. **Grow capital slowly,** never adding more than you could lose without stress.
5. **No F&O trading, ever.** You learn it in Level 6 to understand the market, not to trade it.

**Safety rules that never change**

- Never trade with borrowed money, savings you need, or emergency funds
- Ignore tips from Telegram, WhatsApp and YouTube "gurus"; SEBI regularly acts against unregistered advisers
- Use only SEBI-registered brokers and check any adviser on the SEBI website
- If you hit your monthly loss limit, stop and go back to paper trading
