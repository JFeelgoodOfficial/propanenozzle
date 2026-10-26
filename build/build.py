#!/usr/bin/env python3
"""Generates guide pages, the knowledge base, llms.txt, sitemap.xml and the chat/agent KB module.
Run from anywhere: python3 build/build.py   (writes into ../public and ../functions/_lib/kb.js)
Refuses to build while any "TBD" placeholder remains in the content unless ALLOW_TBD=1 is set."""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import ARTICLES, SRC, UPDATED

ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
FN = os.path.join(os.path.dirname(__file__), "..", "functions")
D = "propanenozzle.com"; B = "Propane Nozzle"; PD = "555-666-7777"; P164 = "+15556667777"; EM = "sales@propanenozzle.com"

# Products: "gg40" and "hose" are sold; "gg20" and "family" are reference material.
def product(a):
    if "product" in a: return a["product"]
    s = a["slug"]
    if s.startswith("gg40"): return "gg40"
    if s.startswith("autogas-hose"): return "hose"
    if s.startswith("gasguard-family"): return "family"
    return "gg20"
SOLD = {"gg40", "hose"}
GROUPS = [("gg40", "GG40 K15 nozzle and hose kits", "The nozzle we sell, the hose kits that go with it, and what the K15 rule means for your fleet."),
          ("gg20", "GG20 1¾\" ACME reference", "Kept for owners of existing GG20 nozzles. We no longer sell the GG20; these guides are reference only.")]
def group_of(a):
    return "gg40" if product(a) in SOLD else "gg20"

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
<meta property="og:image" content="https://{D}/gg40.webp">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#d6ebf8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#14213a" media="(prefers-color-scheme: dark)">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<script src="/assets/theme.js" defer></script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header class="site"><div class="wrap">
  <a class="brand" href="/">{B}</a>
  <nav class="site" aria-label="Site"><a href="/">GG40 nozzle</a><a href="/#hosekits">Hose kits</a><a href="/guides/">Guides</a><a href="/gg20/">GG20 reference</a><button type="button" class="theme-toggle" data-theme-toggle aria-label="Theme: Auto (follows your device)."></button><a class="btn btn-primary" href="/#quote">Get a quote</a></nav>
</div></header>
"""
FOOT = """
<footer><div class="wrap">
  <span>© 2026 BRAND · <a href="tel:PHONE164">PHONEDISP</a> · <a href="mailto:EMAIL">EMAIL</a></span>
  <span>BRAND is an independent reseller, not affiliated with or endorsed by ELAFLEX. ELAFLEX and GasGuard are trademarks of their respective owners. Specifications per ELAFLEX documentation, subject to change.</span>
</div></footer>
<script src="/assets/chat.js" defer></script>
</body></html>""".replace("BRAND", B).replace("PHONE164", P164).replace("PHONEDISP", PD).replace("EMAIL", EM)

CTA_SOLD = '<aside class="cta"><div><strong>Need a GG40 or a hose kit?</strong> Tell us latched or unlatched, the hose length and your dispenser, and we\'ll quote price and lead time.</div><a class="btn btn-primary" href="/#quote">Request a quote</a></aside>'
CTA_REF = '<aside class="cta"><div><strong>Reference only.</strong> We no longer sell the GG20. For K15 vehicles we sell the GasGuard GG40 and matching hose kits.</div><a class="btn btn-primary" href="/">See the GG40</a></aside>'

def page(a, idx):
    path = f"/guides/{a['slug']}"
    about = f"https://{D}/#product" if product(a) in SOLD else f"https://{D}/gg20/#product"
    graph = [
      {"@type":"TechArticle","headline":a["title"],"description":a["desc"],"dateModified":UPDATED,
       "author":{"@type":"Organization","name":B,"url":f"https://{D}/"},
       "publisher":{"@type":"Organization","name":B},
       "about":{"@id":about},"mainEntityOfPage":f"https://{D}{path}",
       "citation":[SRC[s][1] for s in a["sources"]]},
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":B,"item":f"https://{D}/"},
        {"@type":"ListItem","position":2,"name":"Guides","item":f"https://{D}/guides/"},
        {"@type":"ListItem","position":3,"name":a["nav"],"item":f"https://{D}{path}"}]}]
    if a["faqs"]:
        graph.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":t}} for q,t in a["faqs"]]})
    ld = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False)
    out = HEAD.format(title=html.escape(a["title"]), desc=html.escape(a["desc"]), D=D, B=B, path=path, ld=ld)
    out += f"""<main class="wrap article">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">{B}</a> / <a href="/guides/">Guides</a> / {html.escape(a['nav'])}</nav>
<h1>{html.escape(a['title'])}</h1>
<p class="meta">Updated {UPDATED} · Sourced from manufacturer documentation</p>
<div class="answer"><strong>Short answer:</strong> {html.escape(a['summary'])}</div>
{a['body']}
"""
    if a["faqs"]:
        out += "<h2>Quick answers</h2>\n" + "".join(f"<details><summary>{html.escape(q)}</summary><div>{html.escape(t)}</div></details>\n" for q,t in a["faqs"])
    out += "<h2>Sources</h2><ol class=\"sources\">" + "".join(f'<li><a href="{SRC[s][1]}" rel="noopener" target="_blank">{html.escape(SRC[s][0])}</a></li>' for s in a["sources"]) + "</ol>"
    same = [x for x in ARTICLES if x is not a and group_of(x) == group_of(a)]
    others = same[:6]
    out += CTA_SOLD if product(a) in SOLD else CTA_REF
    label = "More GG40 and hose-kit guides" if group_of(a) == "gg40" else "More GG20 reference guides"
    out += f'<h2>{label}</h2><ul class="related">' + "".join(f'<li><a href="/guides/{x["slug"]}">{html.escape(x["title"])}</a></li>' for x in others) + "</ul></main>"
    out += FOOT
    return path, out

def hub():
    ld = json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":"GasGuard GG40 and GG20 guides","url":f"https://{D}/guides/",
        "hasPart":[{"@type":"TechArticle","headline":a["title"],"url":f"https://{D}/guides/{a['slug']}"} for a in ARTICLES]}, ensure_ascii=False)
    out = HEAD.format(title="GasGuard GG40 and GG20 Manual and Guides", desc="GasGuard GG40 K15 quick-connect nozzle and autogas hose-kit guides, plus the complete GG20 reference: selection, specifications, part numbers, installation, maintenance, repair and compliance.", D=D, B=B, path="/guides/", ld=ld)
    out += f'<main class="wrap article"><nav class="crumbs"><a href="/">{B}</a> / Guides</nav><h1>GasGuard manual and guides</h1><p class="lede">Everything we have published about the ELAFLEX GasGuard GG40, the hose kits that go with it, and the GG20 it replaces on K15 vehicles. Each guide cites the manufacturer document it comes from.</p>'
    for key, heading, blurb in GROUPS:
        out += f'<h2 id="{key}">{html.escape(heading)}</h2><p class="meta">{html.escape(blurb)}</p><div class="grid">'
        for a in ARTICLES:
            if group_of(a) != key: continue
            out += f'<a class="gcard" href="/guides/{a["slug"]}"><span class="eyebrow">{html.escape(a["nav"])}</span><strong>{html.escape(a["title"])}</strong><small>{html.escape(a["desc"])}</small></a>'
        out += '</div>'
    out += '<p class="meta" style="margin-top:28px">Machine-readable version: <a href="/knowledge/gasguard-kb.md">gasguard-kb.md</a></p></main>' + FOOT
    return out

def kb():
    parts = [f"# ELAFLEX GasGuard knowledge base: GG40 (K15 quick connect) and GG20 (1¾\" ACME)\nSeller: {B} (independent reseller, not affiliated with ELAFLEX). Updated {UPDATED}.\nWhat we sell: the GasGuard GG40 nozzle (latched or unlatched) and matching autogas hose kits (LPG 16 S hose, ARK 19.3 pull-away, whip). We no longer sell the GG20; GG20 guides are reference only.\nQuotes: https://{D}/#quote · Phone {PD} · Email {EM}\n"]
    for a in ARTICLES:
        tag = "Product we sell." if product(a) in SOLD else "Reference only (not sold)."
        parts.append(f"\n# {a['title']}\nURL: https://{D}/guides/{a['slug']}\n{tag}\n\nSummary: {a['summary']}\n\n{strip(a['body'])}\n")
        for q,t in a["faqs"]:  # one section per question so retrieval can match it on its own
            parts.append(f"## Q: {q}\nA: {t}\n")
        parts.append("Sources: " + "; ".join(f"{SRC[s][0]} <{SRC[s][1]}>" for s in a["sources"]) + "\n")
    return "\n".join(parts)

def main():
    paths = ["/", "/gg20/", "/guides/"]
    outputs = {}
    for i,a in enumerate(ARTICLES):
        p, h = page(a, i); paths.append(p)
        outputs[os.path.join(ROOT, p.lstrip("/") + ".html")] = h  # Cloudflare Pages serves foo.html at /foo and redirects /foo.html there
    outputs[os.path.join(ROOT, "guides/index.html")] = hub()
    k = kb()
    outputs[os.path.join(ROOT, "knowledge/gasguard-kb.md")] = k
    outputs[os.path.join(ROOT, "knowledge/gg20-kb.md")] = k  # old filename, kept for existing links and the Retell upload path
    outputs[os.path.join(FN, "_lib/kb.js")] = "// Generated by build/build.py. Do not edit by hand.\nexport const KB = " + json.dumps(k, ensure_ascii=False) + ";\n"
    def lines(key): return "".join(f"- [{a['title']}](https://{D}/guides/{a['slug']}): {a['desc']}\n" for a in ARTICLES if group_of(a) == key)
    outputs[os.path.join(ROOT, "llms.txt")] = (f"# {B}: ELAFLEX GasGuard GG40 K15 propane nozzle and hose kits\n\n> Independent US reseller of the ELAFLEX GasGuard GG40 quick-connect (K15) propane nozzle and matching autogas hose kits. Also hosts the complete GG20 1¾\" ACME nozzle reference (no longer sold). Sourced from ELAFLEX documentation.\n\n## Products\n- [GG40 nozzle and hose kits: product page and quote](https://{D}/)\n- [GG20 reference page](https://{D}/gg20/)\n- [Full knowledge base, plain text](https://{D}/knowledge/gasguard-kb.md)\n\n## GG40 and hose-kit guides\n" + lines("gg40") + "\n## GG20 reference guides\n" + lines("gg20"))
    outputs[os.path.join(ROOT, "sitemap.xml")] = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>https://{D}{p}</loc><lastmod>{UPDATED}</lastmod></url>\n" for p in paths) + "</urlset>\n"
    tbd = sorted({os.path.relpath(f, os.path.join(ROOT, "..")) for f, c in outputs.items() if "TBD" in c and f.endswith(".html")})
    if tbd and not os.environ.get("ALLOW_TBD"):
        sys.exit("refusing to build: TBD placeholders remain in " + ", ".join(tbd) + " (set ALLOW_TBD=1 to build anyway)")
    for f, c in outputs.items():
        open(f, "w").write(c)
    print(f"built {len(ARTICLES)} guides, kb {len(k)} chars (~{len(k)//4} tokens)" + (f"; TBD placeholders in {len(tbd)} pages" if tbd else ""))

if __name__ == "__main__":
    main()
