#!/usr/bin/env python3
"""Set your business details in site.json and rebuild the site.
Every page, the chat and the knowledge base read contact details from site.json, so this is the only place to change them.

  python3 scripts/configure.py --phone "(512) 555-0100"          # add the phone number once you have one
  python3 scripts/configure.py --phone ""                        # hide the phone again
  python3 scripts/configure.py --brand "Propane Nozzle" --domain propanenozzle.com --email sales@propanenozzle.com

While the phone is empty the site shows no call links or call buttons and the chat never offers a number."""
import argparse, json, os, re, subprocess, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PATH = os.path.join(ROOT, "site.json")
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--brand"); ap.add_argument("--domain"); ap.add_argument("--email")
ap.add_argument("--phone", help='display form, e.g. "(512) 555-0100"; pass "" to hide the phone')
a = ap.parse_args()

site = json.load(open(PATH, encoding="utf-8"))
if a.brand: site["brand"] = a.brand
if a.domain: site["domain"] = a.domain.replace("https://", "").replace("http://", "").strip("/")
if a.email: site["email"] = a.email
if a.phone is not None:
    digits = re.sub(r"\D", "", a.phone)
    if a.phone.strip() and len(digits) < 10: sys.exit("phone needs at least 10 digits")
    site["phone_display"] = a.phone.strip()
    site["phone_e164"] = ("+" + digits if len(digits) > 10 else "+1" + digits) if digits else ""
json.dump(site, open(PATH, "w", encoding="utf-8"), indent=2, ensure_ascii=False); open(PATH, "a").write("\n")
print("site.json:", site)
sys.exit(subprocess.call([sys.executable, os.path.join(ROOT, "build", "build.py")]))
