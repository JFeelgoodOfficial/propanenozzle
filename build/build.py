#!/usr/bin/env python3
"""Generates guide pages, the knowledge base, llms.txt, sitemap.xml and the chat/agent KB module.
Run from anywhere: python3 build/build.py   (writes into ../public and ../functions/_lib/kb.js)"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import ARTICLES, SRC, UPDATED

ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
FN = os.path.join(os.path.dirname(__file__), "..", "functions")
D = "propanenozzle.com"; B = "Propane Nozzle"; PD = "555-666-7777"; P164 = "+15556667777"; EM = "sales@propanenozzle.com"

def strip(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", h, flags=re.S)
    h = re.sub(r"</(p|li|tr|h2|h3|dt|dd|ol|ul|table)>", "\n", h)
    h = re.sub(r"<t[hd][^>]*>", " | ", h)
    h = re.sub(r"<li>", "- ", h)
    h = re.sub(r"<h2>", "\n## ", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h)
    return re.sub(r"\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", h)).strip()

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {B}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://{D}{path}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://{D}{path}">
<meta property="og:image" content="https://{D}/gg20.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header class="site"><div class="wrap">
  <a class="brand" href="/">{B}</a>
  <nav class="site" aria-label="Site"><a href="/">GG20 nozzle</a><a href="/guides/">Guides</a><a href="/#faq">FAQ</a><a class="btn btn-primary" href="/#quote">Get a quote</a></nav>
</div></header>
"""
FOOT = """
<footer><div class="wrap">
  <span>© 2026 BRAND · <a href="tel:PHONE164">PHONEDISP</a> · <a href="mailto:EMAIL">EMAIL</a></span>
  <span>BRAND is an independent reseller, not affiliated with or endorsed by ELAFLEX. ELAFLEX and GasGuard are trademarks of their respective owners. Specifications per ELAFLEX documentation, subject to change.</span>
</div></footer>
<script src="/assets/chat.js" defer></script>
</body></html>""".replace("BRAND", B).replace("PHONE164", P164).replace("PHONEDISP", PD).replace("EMAIL", EM)

def page(a, idx):
    path = f"/guides/{a['slug']}.html"
    graph = [
      {"@type":"TechArticle","headline":a["title"],"description":a["desc"],"dateModified":UPDATED,
       "author":{"@type":"Organization","name":B,"url":f"https://{D}/"},
       "publisher":{"@type":"Organization","name":B},
       "about":{"@id":f"https://{D}/#product"},"mainEntityOfPage":f"https://{D}{path}",
       "citation":[SRC[s][1] for s in a["sources"]]},
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"GG20 nozzle","item":f"https://{D}/"},
        {"@type":"ListItem","position":2,"name":"Guides","item":f"https://{D}/guides/"},
        {"@type":"ListItem","position":3,"name":a["nav"],"item":f"https://{D}{path}"}]}]
    if a["faqs"]:
        graph.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":t}} for q,t in a["faqs"]]})
    ld = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False)
    out = HEAD.format(title=html.escape(a["title"]), desc=html.escape(a["desc"]), D=D, B=B, path=path, ld=ld)
    out += f"""<main class="wrap article">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">GG20 nozzle</a> / <a href="/guides/">Guides</a> / {html.escape(a['nav'])}</nav>
<h1>{html.escape(a['title'])}</h1>
<p class="meta">Updated {UPDATED} · Sourced from ELAFLEX documentation</p>
<div class="answer"><strong>Short answer:</strong> {html.escape(a['summary'])}</div>
{a['body']}
"""
    if a["faqs"]:
        out += "<h2>Quick answers</h2>\n" + "".join(f"<details><summary>{html.escape(q)}</summary><div>{html.escape(t)}</div></details>\n" for q,t in a["faqs"])
    out += "<h2>Sources</h2><ol class=\"sources\">" + "".join(f'<li><a href="{SRC[s][1]}" rel="noopener" target="_blank">{html.escape(SRC[s][0])}</a></li>' for s in a["sources"]) + "</ol>"
    others = [x for x in ARTICLES if x is not a][:6]
    out += '<aside class="cta"><div><strong>Need a GG20?</strong> Tell us the version, inlet and quantity and we\'ll quote price and lead time.</div><a class="btn btn-primary" href="/#quote">Request a quote</a></aside>'
    out += '<h2>More GG20 guides</h2><ul class="related">' + "".join(f'<li><a href="/guides/{x["slug"]}.html">{html.escape(x["title"])}</a></li>' for x in others) + "</ul></main>"
    out += FOOT
    return path, out

def hub():
    ld = json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":"GasGuard GG20 guides","url":f"https://{D}/guides/",
        "hasPart":[{"@type":"TechArticle","headline":a["title"],"url":f"https://{D}/guides/{a['slug']}.html"} for a in ARTICLES]}, ensure_ascii=False)
    out = HEAD.format(title="GasGuard GG20 Manual and Guides", desc="The complete GasGuard GG20 reference: selection, specifications, part numbers, installation, operation, maintenance, repair, troubleshooting and compliance.", D=D, B=B, path="/guides/", ld=ld)
    out += '<main class="wrap article"><nav class="crumbs"><a href="/">GG20 nozzle</a> / Guides</nav><h1>GasGuard GG20 manual and guides</h1><p class="lede">Everything published about the ELAFLEX GasGuard GG20, organized by the job you are doing. Each guide cites the ELAFLEX document it comes from.</p><div class="grid">'
    for a in ARTICLES:
        out += f'<a class="gcard" href="/guides/{a["slug"]}.html"><span class="eyebrow">{html.escape(a["nav"])}</span><strong>{html.escape(a["title"])}</strong><small>{html.escape(a["desc"])}</small></a>'
    out += '</div><p class="meta" style="margin-top:28px">Machine-readable version: <a href="/knowledge/gg20-kb.md">gg20-kb.md</a></p></main>' + FOOT
    return out

def kb():
    parts = [f"# ELAFLEX GasGuard GG20 knowledge base\nSeller: {B} (independent reseller, not affiliated with ELAFLEX). Updated {UPDATED}.\nQuotes: https://{D}/#quote · Phone {PD} · Email {EM}\n"]
    for a in ARTICLES:
        parts.append(f"\n# {a['title']}\nURL: https://{D}/guides/{a['slug']}.html\n\nSummary: {a['summary']}\n\n{strip(a['body'])}\n")
        for q,t in a["faqs"]:
            parts.append(f"Q: {q}\nA: {t}\n")
        parts.append("Sources: " + "; ".join(f"{SRC[s][0]} <{SRC[s][1]}>" for s in a["sources"]) + "\n")
    return "\n".join(parts)

def main():
    paths = ["/", "/guides/"]
    for i,a in enumerate(ARTICLES):
        p, h = page(a, i); paths.append(p)
        open(os.path.join(ROOT, p.lstrip("/")), "w").write(h)
    open(os.path.join(ROOT, "guides/index.html"), "w").write(hub())
    k = kb()
    open(os.path.join(ROOT, "knowledge/gg20-kb.md"), "w").write(k)
    open(os.path.join(FN, "_lib/kb.js"), "w").write("// Generated by build/build.py. Do not edit by hand.\nexport const KB = " + json.dumps(k, ensure_ascii=False) + ";\n")
    llms = f"# {B}: ELAFLEX GasGuard GG20 LPG nozzle\n\n> Independent US reseller of the ELAFLEX GasGuard GG20 long-reach 1¾\" ACME propane nozzle (GG20, GG20H, GG20DN). Full technical reference sourced from ELAFLEX documentation.\n\n## Product\n- [GG20 product page and quote](https://{D}/)\n- [Full knowledge base, plain text](https://{D}/knowledge/gg20-kb.md)\n\n## Guides\n" + "".join(f"- [{a['title']}](https://{D}/guides/{a['slug']}.html): {a['desc']}\n" for a in ARTICLES)
    open(os.path.join(ROOT, "llms.txt"), "w").write(llms)
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>https://{D}{p}</loc><lastmod>{UPDATED}</lastmod></url>\n" for p in paths) + "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
    print(f"built {len(ARTICLES)} guides, kb {len(k)} chars (~{len(k)//4} tokens)")

if __name__ == "__main__":
    main()
