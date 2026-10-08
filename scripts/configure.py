#!/usr/bin/env python3
"""Fill in your business details everywhere at once.
Usage:  python3 scripts/configure.py --brand "Propane Nozzle" --domain propanenozzle.com \
          --phone "(512) 555-0100" --email sales@propanenozzle.com \
          --transfer-name "Jordan" --hours "Mon-Fri 8am-5pm Central"
Re-run the build afterwards if you edit build/content.py: python3 build/build.py"""
import argparse, os, re

ap = argparse.ArgumentParser()
ap.add_argument("--brand", required=True); ap.add_argument("--domain", required=True)
ap.add_argument("--phone", required=True, help='display form, e.g. "(512) 555-0100"')
ap.add_argument("--email", required=True)
ap.add_argument("--transfer-name", default="our team"); ap.add_argument("--hours", default="Monday to Friday, 8 am to 5 pm Central")
a = ap.parse_args()

digits = re.sub(r"\D", "", a.phone)
e164 = "+1" + digits[-10:] if len(digits) >= 10 else "+" + digits
domain = a.domain.replace("https://", "").replace("http://", "").strip("/")
MAP = {"{{BRAND_NAME}}": a.brand, "{{DOMAIN}}": domain, "{{PHONE_DISPLAY}}": a.phone, "{{PHONE_E164}}": e164,
       "{{EMAIL}}": a.email, "{{TRANSFER_NAME}}": a.transfer_name, "{{BUSINESS_HOURS}}": a.hours}

root = os.path.join(os.path.dirname(__file__), "..")
n = 0
for d, _, files in os.walk(root):
    if "node_modules" in d or ".git" in d: continue
    for f in files:
        if f == "configure.py" or not f.endswith((".html", ".js", ".md", ".txt", ".xml", ".py", ".json")): continue
        p = os.path.join(d, f); s = open(p, encoding="utf-8").read(); t = s
        for k, v in MAP.items(): t = t.replace(k, v)
        if t != s: open(p, "w", encoding="utf-8").write(t); n += 1
print(f"updated {n} files; phone link {e164}")
left = []
for d, _, files in os.walk(root):
    for f in files:
        if f.endswith((".html", ".js", ".md", ".txt", ".xml")):
            if "{{" in open(os.path.join(d, f), encoding="utf-8").read(): left.append(os.path.join(d, f))
print("files still containing {{tokens}}:", left or "none")
