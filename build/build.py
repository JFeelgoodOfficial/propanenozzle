#!/usr/bin/env python3
"""Generates every page of the site: the product pages (from build/templates), the guide pages, the knowledge
base, llms.txt, sitemap.xml, 404.html, and the modules the chat and phone agent read.
Run from anywhere: python3 build/build.py   (writes into ../public and ../functions/_lib/)
Contact details come from ../site.json. While phone_display is empty, every call link is left out.
Refuses to build while any "TBD" placeholder remains in the content unless ALLOW_TBD=1 is set."""
import hashlib, html, json, os, re, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import ARTICLES, SRC, UPDATED

ROOT = os.path.join(HERE, "..", "public")
FN = os.path.join(HERE, "..", "functions")
TPL = os.path.join(HERE, "templates")
SITE = json.load(open(os.path.join(HERE, "..", "site.json"), encoding="utf-8"))
D = SITE["domain"]; B = SITE["brand"]; EM = SITE["email"]
PD = SITE.get("phone_display", "").strip(); P164 = SITE.get("phone_e164", "").strip()
if bool(PD) != bool(P164): sys.exit("site.json: set both phone_display and phone_e164, or leave both empty")

def tpl(name): return open(os.path.join(TPL, name), encoding="utf-8").read()
SHARED_CSS = tpl("shared.css")
SITE_CSS = tpl("site.css").rstrip() + "\n" + SHARED_CSS
THEME_JS = open(os.path.join(ROOT, "assets/theme.js"), encoding="utf-8").read()
V = hashlib.sha1((SITE_CSS + tpl("chat.js") + THEME_JS + json.dumps(SITE)).encode()).hexdigest()[:8]  # cache-buster for /assets

def render(t):
    """{{#phone}}..{{/phone}} is kept only when a phone number is set, {{^phone}}..{{/phone}} only when it isn't."""
    t = re.sub(r"\{\{#phone\}\}(.*?)\{\{/phone\}\}", lambda m: m.group(1) if PD else "", t, flags=re.S)
    t = re.sub(r"\{\{\^phone\}\}(.*?)\{\{/phone\}\}", lambda m: "" if PD else m.group(1), t, flags=re.S)
    for k, v in {"BRAND": B, "DOMAIN": D, "EMAIL": EM, "PHONE": PD, "PHONE164": P164, "V": V, "SHARED_CSS": SHARED_CSS}.items():
        t = t.replace("{{" + k + "}}", v)
    return t

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
          ("ref", "ELAFLEX hoses, pull-aways, boots and guards", "ELAFLEX catalogue pages rewritten as web pages: LPG 16 hoses, the ARK 19 pull-away, nozzle boots, sleeves and guards, the ZVG 2 nozzles and the GasGuard range. Reference only."),
          ("gg20", "GG20 1¾\" ACME reference", "Kept for owners of existing GG20 nozzles. We no longer sell the GG20; these guides are reference only.")]
def group_of(a):
    p = product(a)
    return "gg40" if p in SOLD else "ref" if p in ("ref", "family") else "gg20"
def updated(a): return a.get("updated", UPDATED)
LATEST = max(updated(a) for a in ARTICLES)

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
<meta property="og:image" content="https://{D}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://{D}/og.jpg">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#d6ebf8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#14213a" media="(prefers-color-scheme: dark)">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<script src="/assets/theme.js?v={V}" defer></script>
<link rel="preload" href="/assets/fonts/plex-sans-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={V}">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
  <a class="brand" href="/">{B}</a>
  <nav class="site" aria-label="Site"><a href="/">GG40 nozzle</a><a href="/#hosekits">Hose kits</a><a href="/guides/">Guides</a><a href="/guides/elaflex-documents.html">ELAFLEX documents</a><a href="/gg20/">GG20 reference</a><details class="mnav"><summary>Menu</summary><div><a href="/">GG40 nozzle</a><a href="/#hosekits">Hose kits</a><a href="/guides/">All guides</a><a href="/guides/#ref">Hoses, pull-aways, boots</a><a href="/guides/elaflex-documents.html">ELAFLEX documents</a><a href="/gg20/">GG20 reference</a></div></details><button type="button" class="theme-toggle" data-theme-toggle aria-label="Theme: Auto (follows your device)."></button><a class="btn btn-primary" href="/#quote">Get a quote</a></nav>
</div></header>
"""
FOOT = """
<footer><div class="wrap">
  <span>© 2026 BRAND · {{#phone}}<a href="tel:{{PHONE164}}">{{PHONE}}</a> · {{/phone}}<a href="mailto:EMAIL">EMAIL</a></span>
  <span>BRAND is an independent reseller, not affiliated with or endorsed by ELAFLEX. ELAFLEX and GasGuard are trademarks of their respective owners. Specifications per ELAFLEX documentation, subject to change.</span>
</div></footer>
<script src="/assets/chat.js?v={{V}}" defer></script>
</body></html>"""
FOOT = render(FOOT.replace("BRAND", B).replace("EMAIL", EM))

CTA_SOLD = '<aside class="cta"><div><strong>Need a GG40 or a hose kit?</strong> Tell us latched or unlatched, the hose length and your dispenser, and we\'ll quote price and lead time.</div><a class="btn btn-primary" href="/#quote">Request a quote</a></aside>'
CTA_ELA = '<aside class="cta"><div><strong>Reference page.</strong> We quote the GasGuard GG40 with a matching ELAFLEX hose kit: LPG 16 S hose, ARK 19.3 pull-away and whip.</div><a class="btn btn-primary" href="/#quote">Request a quote</a></aside>'
CTA_REF = '<aside class="cta"><div><strong>Reference only.</strong> We no longer sell the GG20. For K15 vehicles we sell the GasGuard GG40 and matching hose kits.</div><a class="btn btn-primary" href="/">See the GG40</a></aside>'

def src_href(s):
    """Documents hosted on this site are linked by path so they work on previews as well as the live domain."""
    u = SRC[s][1]
    return u[len(f"https://{D}"):] if u.startswith(f"https://{D}/") else u

def page(a, idx):
    path = f"/guides/{a['slug']}.html"
    about = f"https://{D}/#product" if product(a) in SOLD else f"https://{D}/gg20/#product"
    graph = [
      {"@type":"TechArticle","headline":a["title"],"description":a["desc"],"dateModified":updated(a),
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
    out = HEAD.format(title=html.escape(a["title"]), desc=html.escape(a["desc"]), D=D, B=B, V=V, path=path, ld=ld)
    out += f"""<main class="wrap article" id="main">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">{B}</a> / <a href="/guides/">Guides</a> / {html.escape(a['nav'])}</nav>
<h1>{html.escape(a['title'])}</h1>
<p class="meta">Updated {updated(a)} · Sourced from manufacturer documentation</p>
<div class="answer"><strong>Short answer:</strong> {html.escape(a['summary'])}</div>
{a['body']}
"""
    if a["faqs"]:
        out += "<h2>Quick answers</h2>\n" + "".join(f"<details><summary>{html.escape(q)}</summary><div>{html.escape(t)}</div></details>\n" for q,t in a["faqs"])
    out += "<h2>Sources</h2><ol class=\"sources\">" + "".join(f'<li><a href="{src_href(s)}" rel="noopener" target="_blank">{html.escape(SRC[s][0])}</a></li>' for s in a["sources"]) + "</ol>"
    same = [x for x in ARTICLES if x is not a and group_of(x) == group_of(a)]
    others = same[:6]
    g = group_of(a)
    out += CTA_SOLD if g == "gg40" else CTA_ELA if g == "ref" else CTA_REF
    label = {"gg40": "More GG40 and hose-kit guides", "ref": "More ELAFLEX reference", "gg20": "More GG20 reference guides"}[g]
    out += f'<h2>{label}</h2><ul class="related">' + "".join(f'<li><a href="/guides/{x["slug"]}.html">{html.escape(x["title"])}</a></li>' for x in others) + "</ul></main>"
    out += FOOT
    return path, out

def hub():
    ld = json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":"GasGuard GG40 and GG20 guides","url":f"https://{D}/guides/",
        "hasPart":[{"@type":"TechArticle","headline":a["title"],"url":f"https://{D}/guides/{a['slug']}.html"} for a in ARTICLES]}, ensure_ascii=False)
    out = HEAD.format(title="GasGuard GG40 and GG20 Manual and Guides", desc="GasGuard GG40 K15 nozzle and autogas hose-kit guides, ELAFLEX reference on LPG 16 hoses, the ARK 19 pull-away, nozzle boots and guards, and the complete GG20 reference.", D=D, B=B, V=V, path="/guides/", ld=ld)
    out += f'<main class="wrap article" id="main"><nav class="crumbs"><a href="/">{B}</a> / Guides</nav><h1>GasGuard manual and guides</h1><p class="lede">Everything we have published about the ELAFLEX GasGuard GG40, the hose kits that go with it, the ELAFLEX hoses, pull-aways and boots behind those kits, and the GG20 it replaces on K15 vehicles. Each guide cites the manufacturer document it comes from; the PDFs are in the <a href="/guides/elaflex-documents.html">document library</a>.</p>'
    for key, heading, blurb in GROUPS:
        out += f'<h2 id="{key}">{html.escape(heading)}</h2><p class="meta">{html.escape(blurb)}</p><div class="grid">'
        for a in ARTICLES:
            if group_of(a) != key: continue
            out += f'<a class="gcard" href="/guides/{a["slug"]}.html"><span class="eyebrow">{html.escape(a["nav"])}</span><strong>{html.escape(a["title"])}</strong><small>{html.escape(a["desc"])}</small></a>'
        out += '</div>'
    out += '<p class="meta" style="margin-top:28px">Machine-readable version: <a href="/knowledge/gasguard-kb.md">gasguard-kb.md</a></p></main>' + FOOT
    return out

def kb():
    parts = [f"# ELAFLEX GasGuard knowledge base: GG40 (K15 quick connect) and GG20 (1¾\" ACME)\nSeller: {B} (independent reseller, not affiliated with ELAFLEX). Updated {LATEST}.\nWhat we sell: the GasGuard GG40 nozzle (latched or unlatched) and matching autogas hose kits (LPG 16 S hose, ARK 19.3 pull-away, whip). We no longer sell the GG20; GG20 guides are reference only.\nQuotes: https://{D}/#quote · {('Phone ' + PD + ' · ') if PD else ''}Email {EM}{'' if PD else ' · No phone line yet: do not give out a phone number'}\n"]
    for a in ARTICLES:
        tag = "Product we sell." if product(a) in SOLD else "Reference only (not sold on its own)." if group_of(a) == "ref" else "Reference only (not sold)."
        parts.append(f"\n# {a['title']}\nURL: https://{D}/guides/{a['slug']}.html\n{tag}\n\nSummary: {a['summary']}\n\n{strip(a['body'])}\n")
        for q,t in a["faqs"]:  # one section per question so retrieval can match it on its own
            parts.append(f"## Q: {q}\nA: {t}\n")
        parts.append("Sources: " + "; ".join(f"{SRC[s][0]} <{SRC[s][1]}>" for s in a["sources"]) + "\n")
    return "\n".join(parts)

def notfound():
    out = HEAD.format(title="Page not found", desc="That page doesn't exist. Find the GasGuard GG40, hose kits and ELAFLEX reference guides here.", D=D, B=B, V=V, path="/404.html", ld="{}")
    out = out.replace('<link rel="canonical" href="https://' + D + '/404.html">', '<meta name="robots" content="noindex">')
    out += ('<main class="wrap article" id="main"><h1>Page not found</h1><p class="lede">That address doesn\'t match a page on this site. These do:</p>'
            '<div class="grid"><a class="gcard" href="/"><span class="eyebrow">Product</span><strong>GasGuard GG40 K15 nozzle and hose kits</strong><small>Specifications and quote form</small></a>'
            '<a class="gcard" href="/guides/"><span class="eyebrow">Guides</span><strong>All guides</strong><small>GG40, hose kits, ELAFLEX reference, GG20</small></a>'
            '<a class="gcard" href="/guides/elaflex-documents.html"><span class="eyebrow">Documents</span><strong>ELAFLEX document library</strong><small>Catalogue pages and brochures</small></a>'
            '<a class="gcard" href="/#quote"><span class="eyebrow">Quote</span><strong>Request a quote</strong><small>Price and lead time in writing</small></a></div></main>')
    return out + FOOT

def main():
    paths = [("/", LATEST), ("/gg20/", UPDATED), ("/guides/", LATEST)]
    outputs = {}
    for i,a in enumerate(ARTICLES):
        p, h = page(a, i); paths.append((p, updated(a)))
        outputs[os.path.join(ROOT, p.lstrip("/"))] = h
    outputs[os.path.join(ROOT, "guides/index.html")] = hub()
    outputs[os.path.join(ROOT, "404.html")] = notfound()
    outputs[os.path.join(ROOT, "index.html")] = render(tpl("index.html"))
    outputs[os.path.join(ROOT, "gg20/index.html")] = render(tpl("gg20.html"))
    outputs[os.path.join(ROOT, "assets/chat.js")] = render(tpl("chat.js"))
    outputs[os.path.join(ROOT, "assets/site.css")] = SITE_CSS
    k = kb()
    outputs[os.path.join(ROOT, "knowledge/gasguard-kb.md")] = k
    outputs[os.path.join(ROOT, "knowledge/gg20-kb.md")] = k  # old filename, kept for existing links and the Retell upload path
    gen = "// Generated by build/build.py. Do not edit by hand.\n"
    outputs[os.path.join(FN, "_lib/kb.js")] = gen + "export const KB = " + json.dumps(k, ensure_ascii=False) + ";\n"
    outputs[os.path.join(FN, "_lib/site.js")] = gen + "export const SITE = " + json.dumps({"brand": B, "domain": D, "email": EM, "phone": PD}, ensure_ascii=False) + ";\n"
    def lines(key): return "".join(f"- [{a['title']}](https://{D}/guides/{a['slug']}.html): {a['desc']}\n" for a in ARTICLES if group_of(a) == key)
    outputs[os.path.join(ROOT, "llms.txt")] = (f"# {B}: ELAFLEX GasGuard GG40 K15 propane nozzle and hose kits\n\n> Independent US reseller of the ELAFLEX GasGuard GG40 quick-connect (K15) propane nozzle and matching autogas hose kits. Also hosts ELAFLEX reference material on LPG 16 hoses, the ARK 19 pull-away, nozzle boots and guards and the ZVG 2 nozzles, and the complete GG20 1¾\" ACME nozzle reference (no longer sold). Sourced from ELAFLEX documentation.\n\n## Products\n- [GG40 nozzle and hose kits: product page and quote](https://{D}/)\n- [GG20 reference page](https://{D}/gg20/)\n- [Full knowledge base, plain text](https://{D}/knowledge/gasguard-kb.md)\n\n## GG40 and hose-kit guides\n" + lines("gg40") + "\n## ELAFLEX reference: hoses, pull-aways, boots, guards, ZVG 2\n" + lines("ref") + "\n## GG20 reference guides\n" + lines("gg20"))
    outputs[os.path.join(ROOT, "sitemap.xml")] = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>https://{D}{p}</loc><lastmod>{d}</lastmod></url>\n" for p, d in paths) + "</urlset>\n"
    tbd = sorted({os.path.relpath(f, os.path.join(ROOT, "..")) for f, c in outputs.items() if "TBD" in c and f.endswith(".html")})
    if tbd and not os.environ.get("ALLOW_TBD"):
        sys.exit("refusing to build: TBD placeholders remain in " + ", ".join(tbd) + " (set ALLOW_TBD=1 to build anyway)")
    for f, c in outputs.items():
        rel = os.path.relpath(f, os.path.join(ROOT, ".."))
        if re.search(r"\{\{[#^/]?[A-Za-z_0-9]+\}\}", c): sys.exit(f"unfilled template token in {rel}")
        if "555-" in c or "5556667777" in c: sys.exit(f"placeholder phone number in {rel}")
        if not PD and "tel:" in c: sys.exit(f"call link in {rel} but no phone number is set in site.json")
    for f, c in outputs.items():
        os.makedirs(os.path.dirname(f), exist_ok=True)
        open(f, "w", encoding="utf-8").write(c)
    print(f"built {len(ARTICLES)} guides, kb {len(k)} chars (~{len(k)//4} tokens), phone {'set' if PD else 'hidden (none in site.json)'}" + (f"; TBD placeholders in {len(tbd)} pages" if tbd else ""))

if __name__ == "__main__":
    main()
