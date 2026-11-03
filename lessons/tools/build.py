"""Build Level lesson pages from src/template.html + src/<id>.html + src/data/*.json.
Writes dist/<id>.html (the exact file published as a claude.ai artifact) and
../site/lessons/<id>.html (the same file inside a doctype skeleton, for the repo).
Run from lessons/: python3 tools/build.py"""
import json, re, os
HUB = "https://claude.ai/artifact/NJnbjXy51bvhszCCBjsuuZ"
ASOF = "30 Oct 2026"
L = json.load(open("src/lessons.json")); URLS = json.load(open("src/urls.json"))
tpl = open("src/template.html").read()
SKEL = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n</head>\n<body>\n'
os.makedirs("dist", exist_ok=True); os.makedirs("../site/lessons", exist_ok=True)
def slug(i): return i.replace(".", "-")
def link(l, cls, text):
    if not l: return ""
    u = URLS.get(l["id"])
    return f'<a class="{cls}" href="{u}" target="_blank" rel="noopener">{text}</a>' if u else f'<a class="{cls} off" aria-disabled="true">{text}</a>'
for k, l in enumerate(L):
    p = L[k - 1] if k else None; n = L[k + 1] if k + 1 < len(L) else None
    body = open(f"src/{slug(l['id'])}.html").read()
    names = set()
    for m in re.findall(r'data-series="([^"]+)"', body): names.update(m.split(","))
    for m in re.findall(r'<!-- data: ([^>]+) -->', body): names.update(x.strip() for x in m.split(","))
    data = {x: json.load(open(f"src/data/{x}.json")) for x in sorted(names)}
    out = (tpl.replace("{{CONTENT}}", body)
        .replace("{{TITLE}}", l["title"]).replace("{{ID}}", l["id"]).replace("{{NUM}}", str(k + 1))
        .replace("{{HUB}}", HUB + "#level-1").replace("{{ASOF}}", ASOF)
        .replace("{{PREV}}", link(p, "prev", "← Prev")).replace("{{NEXT}}", link(n, "next", "Next →"))
        .replace("{{PREVP}}", link(p, "", f"← {p['id']} {p['title']}") if p else "<span></span>")
        .replace("{{NEXTP}}", link(n, "", f"{n['id']} {n['title']} →") if n else '<a href="' + HUB + '#level-1" target="_blank" rel="noopener">Back to Level 1 in the hub →</a>')
        .replace("{{NEXTFINISH}}", link(n, "", f"Next: {n['title']} →") if n else "")
        .replace("{{DATA}}", json.dumps(data, separators=(",", ":")).replace("</", "<\\/")))
    open(f"dist/{slug(l['id'])}.html", "w").write(out)
    open(f"../site/lessons/{slug(l['id'])}.html", "w").write(SKEL + out + "\n</body>\n</html>\n")
    print(l["id"], len(out) // 1024, "KB", sorted(names))
