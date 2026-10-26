# Single source of truth for the GasGuard knowledge base: GG40 (sold, with hose kits) and GG20 (reference only).
# Every guide page, /knowledge/gasguard-kb.md, /llms.txt and the chat/phone-agent context are generated from this file.
# PENDING from ELAFLEX (owner to supply): GG40 weight, nozzle pressure rating, inlet sizes besides 3/4" NPT, magnet option,
# inspection interval and seal-kit number. Each is worded "not yet published" on the site; search that phrase to update.
# Any "TBD" left in content makes build.py refuse to build unless ALLOW_TBD=1.
# Edit here, then run: python3 build/build.py

UPDATED = "2026-10-16"

SRC = {
 "info215": ("GasGuard Information 2.15: GG20 nozzle range (ELAFLEX, Oct 2015)", "https://elaflex.com.au/dokumente/subsidiaries/au/Information/GasGuard_Information_2.15.pdf"),
 "info615": ("GasGuard Information 6.15: part number breakdown (ELAFLEX)", "https://elaflex.com.au/dokumente/subsidiaries/au/Information/GasGuard_Information_6.15.pdf"),
 "manual": ("Installation and Operating Manual, GG1 & GG20 series (ELAFLEX PACIFIC, 5/2016)", "https://elaflex.com.au/dokumente/subsidiaries/au/Manuals/GasGuard_Manual_GG1_GG20_Installation_Operation_EN.pdf"),
 "rm": ("GG20 Repair & Maintenance Manual (ELAFLEX PACIFIC / L.G. Equipment)", "https://elaflex.com.au/dokumente/subsidiaries/au/Manuals/GG20-RM.pdf"),
 "cat": ("ELAFLEX catalogue pages 567-574, rev. 11.2022", "https://elaflex.it/dokumente/download/Catalogue/CatPage567_574.pdf"),
 "range": ("GasGuard product range (ELAFLEX PACIFIC)", "https://elaflex.com.au/products-catalogue/gasguard"),
 "dist": ("GasGuard distributors (ELAFLEX PACIFIC)", "https://elaflex.com.au/contact/distributors-gasguard-products"),
 "r1177": ("South Coast AQMD Rule 1177, LPG transfer and dispensing", "https://www.aqmd.gov/docs/default-source/rule-book/reg-xi/rule-1177.pdf?sfvrsn=4"),
 "bpn": ("The ins and outs of autogas dispensers (Butane-Propane News)", "https://bpnews.com/equipment/ins-outs-autogas-dispensers"),
 "info315": ("GasGuard Information 3.15: GG30 (ELAFLEX)", "https://elaflex.com.au/products-catalogue/gasguard"),
 "rrc": ("Autogas dispensers, Railroad Commission of Texas", "https://rrc.texas.gov/media/5z3b3fux/autogas_dispensers.pdf"),
 "p4150": ("P4-150 Dual Product Dispenser (Parafour)", "https://parafour.com/p4-150-dual-product-dispenser/"),
 "p4150l": ("Parafour P4-150-L listing (GasEquipment.com)", "https://www.gasequipment.com/catalog/shop/Parafour/mfr-1O4?a=1"),
 "infomat": ("Information Material: GasGuard product range (ELAFLEX PACIFIC)", "https://elaflex.com.au/information-material/gasguard-product-range"),
 "p4disp": ("Dispensers (Parafour)", "https://parafour.com/dispensers/"),
 "p4100": ("P4-100 Single Hose Autogas Dispenser (Parafour)", "https://parafour.com/p4-100-single-hose-autogas-dispenser/"),
 "p4200": ("P4-200 Dual Hose Dispenser (Parafour)", "https://parafour.com/p4-200-dual-hose-dispenser/"),
 "p4200l": ("P4-200-L listing (GasEquipment.com)", "https://www.gasequipment.com/buy/product/p4-200-l/36994"),
 "p4kit": ("Hose & Nozzle Kit, Autogas, for Parafour dispensers, HK-0021 (Chimney Cricket listing)", "https://chimneycricket.com/products/hose-nozzle-kit-autogas-for-parafour-dispensers-includes-pull-away-w-lanyard-18-x-3-4-lp-whip-3-4-x-12-lp-delivery-hose-gg20l-nozzle-parafour-hk-0021-ha0021"),
 "gg40br": ("GasGuard GG40 brochure (ELAFLEX PACIFIC, 2025)", "https://propanenozzle.com/docs/ELAFLEX_Pacific_GG40.pdf"),
 "gg40news": ("New ELAFLEX GasGuard GG40 nozzle (ELAFLEX PACIFIC news)", "https://elaflex.com.au/news/news-elaflex-pacific-pty-ltd/new-elaflex-pacific-brochure-gasguard-gg40"),
 "chsgg40": ("Euro K15 Quick Connect Nozzle UL Listed ¾\" NPT w/ Latch, SKU GG40SL (CHS Propane Equipment listing)", "https://chspropaneequipment.com/products/euro-k15-quick-connect-nozzle-ul-listed-3-4npt-w-latch"),
 "aag": ("K15 Quick-Connect NFPA 58 Code Change for 2020 (Alliance AutoGas)", "https://allianceautogas.com/k15-quick-connect-nfpa-58-code-change-for-2020/"),
 "hcck15": ("Updated Nozzle Guidelines for 2020 Propane Autogas Vehicles (Houston-Galveston Clean Cities)", "https://www.houston-cleancities.org/updated-nozzle-guidelines-for-2020-propane-autogas-vehicles/"),
 "lpgul": ("'LPG-UL' Hose Assemblies for LPGas, Information 1.19 (ELAFLEX US)", "https://elaflexus.com/downloads/lpg-refueling/lpg-hose-assemblies/ELAFLEX_US_Information_1.19.pdf"),
 "ark19": ("ARK 19 / ARK 19 SS safety break manual (ELAFLEX)", "https://elaflex.de/dokumente/download/Manual/Manual_ARK19_ARK19SS.pdf"),
 "zvg2cat": ("ELAFLEX US catalogue pages 573-574: ZVG 2 EURO UL (ISO 19825 nozzles)", "https://elaflexus.com/downloads/lpg-refueling/zvg-2-euro-ul/CatPage573_574_US.pdf"),
 "hcc": ("Propane Fuel Information Event (Houston-Galveston Clean Cities, 2016)", "https://houston-cleancities.org/wp-content/uploads/2016/08/Propane-Fuel-Information-Event_combined.pdf"),
}

ARTICLES = [

dict(
slug='gg40-k15-quick-connect-nozzle',
product='gg40',
title='ELAFLEX GasGuard GG40: the K15 Quick-Connect Propane Nozzle',
nav='GG40 overview',
desc='What the GasGuard GG40 is, how K15 quick-connect propane filling works, who it is for, and the figures ELAFLEX publishes: up to 17 GPM, under 1 cm³ release, UL approved.',
summary="The GG40 is ELAFLEX's push-on nozzle for the K15 quick-connect fill valves that NFPA 58 has required on new US autogas vehicles since 2020. It is designed to EN 13760, UN R 67 and ISO 19825, flows up to 17 GPM, releases less than 1 cm³ of gas on disconnect, has a lighter lever pull than the GasGuard ACME nozzles, and is UL approved in both latched and unlatched versions. It fits the existing NB-GG nozzle boot and is sold with ELAFLEX's ARK 19.3 pull-away and LPG 16 S hose as a complete hanging-hardware set.",
body='<h2>What it is</h2>\n<p>ELAFLEX PACIFIC introduced the GasGuard GG40 for the US and Canadian markets as a straightforward, recognized nozzle for Quick Connect (K15) propane filling. Where the GasGuard GG1 and GG20 screw onto a 1¾" ACME thread, the GG40 pushes onto the K15 receptacle and locks. ELAFLEX built it to carry the GasGuard reputation for reliability and user comfort into the K15 era.</p>\n\n<h2>How K15 filling works</h2>\n<p>The operator pushes the nozzle over the vehicle\'s K15 fill valve until the locking segments engage, then pulls the lever. The GG40 uses larger locking segments for a secure connection. The design gives low effort at the lever, lower than ELAFLEX\'s own ACME nozzles, and releases less than 1 cm³ of propane when the nozzle comes off. ELAFLEX states that personal protective equipment is not necessary for the GG40 unless local codes or regulations require it.</p>\n\n<h2>Published figures</h2>\n<table><tbody>\n<tr><th>Connection</th><td>K15 quick connect (push-on). Designed acc. to EN 13760, UN R 67 and ISO 19825.</td></tr>\n<tr><th>Flow rate</th><td>Up to 17 GPM (about 64 L/min)</td></tr>\n<tr><th>Gas released on disconnect</th><td>Less than 1 cm³</td></tr>\n<tr><th>Lever effort</th><td>Lower than the GasGuard ACME nozzles</td></tr>\n<tr><th>Latch</th><td>Safety hold-open latch available; larger locking segments</td></tr>\n<tr><th>Listing</th><td>Both latched and unlatched versions are UL approved</td></tr>\n<tr><th>Warranty</th><td>18 months, manufacturer\'s</td></tr>\n<tr><th>Boot</th><td>Compatible with the existing NB-GG nozzle boot</td></tr>\n<tr><th>Hose set</th><td>ARK 19.3 pull-away and UL-listed LPG 16 S hose</td></tr>\n<tr><th>Weight</th><td>Not yet published by ELAFLEX; confirm with your quote</td></tr>\n<tr><th>Pressure rating</th><td>Not yet published for the nozzle; confirm with your quote (the LPG 16 S hose is rated 25 bar)</td></tr>\n<tr><th>Inlet thread</th><td>¾" NPT per distributor listings; other sizes not yet published</td></tr>\n</tbody></table>\n\n<h2>Who it is for</h2>\n<ul>\n<li>Fleets and school-bus operators fueling vehicles built or converted since 2020, which carry K15 valves.</li>\n<li>Autogas stations replacing ACME hose ends as their customers\' vehicles turn over.</li>\n<li>Dispenser builders specifying hanging hardware for new US installations.</li>\n</ul>\n<p>If you still fill forklift cylinders, RVs or older ACME vehicles, you need an ACME nozzle such as the GG20 for those. See <a href="/guides/gg40-vs-gg20-acme-vs-k15">GG40 vs GG20</a>.</p>\n<h2>Ordering a GG40</h2>\n<table><thead><tr><th>Choice</th><th>What to pick</th></tr></thead><tbody>\n<tr><td>Latch</td><td>Latched (hold-open) or unlatched. Both versions are UL approved, so the latch is a workflow choice: latched for attended fleet fueling where the operator stays with the nozzle; check your authority having jurisdiction for self-service sites.</td></tr>\n<tr><td>Inlet</td><td>Distributor listings show ¾" NPT. Tell us the thread on your hose kit; we confirm the inlet on the quote. (Other inlet sizes are not yet published.)</td></tr>\n<tr><td>Hose kit</td><td>We can quote a matching ELAFLEX hose kit: LPG 16 S hose, ARK 19.3 pull-away and whip, built for the GG40. See <a href="/guides/autogas-hose-kits">autogas hose kits</a>.</td></tr>\n<tr><td>Nozzle boot</td><td>The GG40 fits the existing NB-GG boot, so dispensers already fitted with one for a GasGuard ACME nozzle don\'t need a new boot.</td></tr>\n</tbody></table>\n<p class="note">GG40 figures on this page come from the ELAFLEX PACIFIC GG40 brochure (2025) and distributor listings. ELAFLEX has not published every number for the GG40 yet; where a figure is missing we say so instead of guessing. Confirm the current data sheet with your quote.</p>\n',
faqs=[('What is the ELAFLEX GasGuard GG40?', "ELAFLEX's push-on propane nozzle for K15 quick-connect fill valves, designed for the US and Canada. It flows up to 17 GPM, releases under 1 cm³ on disconnect, and is UL approved in latched and unlatched versions."), ('Is the GG40 UL listed?', "ELAFLEX states that both the latched and unlatched versions of the GG40 are UL approved, and the nozzle carries the UL Classified mark in ELAFLEX's brochure."), ('What flow rate does the GG40 deliver?', 'Up to 17 GPM, about 64 L/min, per ELAFLEX. Field flow depends on the pump, hose and vehicle valve.')],
sources=['gg40br', 'gg40news', 'chsgg40', 'aag'],
),

dict(
slug='gg40-vs-gg20-acme-vs-k15',
product='gg40',
title='GG40 vs GG20: K15 Quick Connect vs 1¾" ACME, Which Nozzle Your Vehicles Need',
nav='GG40 vs GG20',
desc='K15 push-on (GG40) or 1¾" ACME thread (GG20)? The NFPA 58 rule for 2020-and-later vehicles, what each nozzle fits, and how the two compare on flow, release and lever effort.',
summary='Match the nozzle to the fill valve on the vehicle. Autogas vehicles built or converted after 1 January 2020 must carry a K15 quick-connect valve under NFPA 58, and those take the GG40. Older ACME vehicles, forklift cylinders and RVs take a 1¾" ACME nozzle such as the GG20. The GG40 flows up to 17 GPM and releases under 1 cm³ on disconnect; the GG20 flows 63 L/min (about 16.6 GPM) and releases 1.9 cm³. Adapters between the two are discouraged. Propane Nozzle sells the GG40; the GG20 guides stay online as reference.',
body='<h2>The rule that drives the change</h2>\n<p>NFPA 58, from its 2017 edition, requires the K15 quick-connect refueling valve on autogas vehicles produced or converted after 1 January 2020. The rule is not retroactive: an existing ACME-equipped vehicle keeps its valve until it is converted, bought or brought back into service. Industry groups report the push-on K15 connection releases far less propane per disconnect than the threaded ACME connection; Alliance AutoGas puts the reduction at about 76%, a trade figure rather than an independent test.</p>\n\n<h2>Side by side</h2>\n<table><thead><tr><th></th><th>GG40</th><th>GG20</th></tr></thead><tbody>\n<tr><th>Fill valve</th><td>K15 quick connect, push-on</td><td>1¾" ACME, threaded</td></tr>\n<tr><th>Vehicles</th><td>Autogas vehicles from model year 2020 on, and conversions since 2020</td><td>Pre-2020 autogas vehicles, forklift cylinders, RVs, small tanks</td></tr>\n<tr><th>Flow</th><td>Up to 17 GPM (≈ 64 L/min)</td><td>63 L/min (≈ 16.6 GPM) at 12 bar; 60 L/min for GG20H and GG20DN</td></tr>\n<tr><th>Gas released on disconnect</th><td>Less than 1 cm³</td><td>1.9 cm³ (1.7 cm³ for GG20H and GG20DN)</td></tr>\n<tr><th>Lever effort</th><td>Lower than the GasGuard ACME nozzles</td><td>Standard; GG20H and GG20DN lower it</td></tr>\n<tr><th>Latch and UL</th><td>Latched and unlatched versions both UL approved</td><td>UL 125 listed; the optional latch is not covered by the listing</td></tr>\n<tr><th>Standards</th><td>EN 13760, UN R 67, ISO 19825</td><td>AS/NZS 1596, AS/NZS 1425, EN 12806 coupling dimensions</td></tr>\n<tr><th>Nozzle boot</th><td colspan="2">Both use the NB-GG boot</td></tr>\n<tr><th>Sold by Propane Nozzle</th><td>Yes, with matching hose kits</td><td>No longer; guides kept as reference</td></tr>\n</tbody></table>\n\n<h2>Mixed fleets</h2>\n<p>A station serving both vehicle generations needs both nozzle types, which usually means a dual-hose dispenser with one K15 hose and one ACME hose, or two dispensers. Adapters that let a K15 nozzle fill an ACME valve exist, but NFPA guidance and the trade press treat them as a stopgap, and ELAFLEX advises against fill-point adapters on its ACME nozzles because they raise the gas released on disconnect. Plan the hanging hardware around the valves you actually fill.</p>\n\n<h2>How to tell which valve a vehicle has</h2>\n<p>An ACME valve is a threaded brass fitting about 1¾" across, usually with a plastic dust cap that screws on. A K15 valve is a smooth-bodied receptacle with no external thread, and its cap pushes on. Vehicle build or conversion paperwork dated 2020 or later almost always means K15.</p>\n<p class="note">GG40 figures on this page come from the ELAFLEX PACIFIC GG40 brochure (2025) and distributor listings. ELAFLEX has not published every number for the GG40 yet; where a figure is missing we say so instead of guessing. Confirm the current data sheet with your quote.</p>\n',
faqs=[('Do I need a GG40 or a GG20?', 'Look at the fill valve. K15 quick-connect (vehicles built or converted since 2020): GG40. 1¾" ACME thread (older vehicles, forklift cylinders, RVs): an ACME nozzle such as the GG20.'), ('Can a GG40 fill an ACME valve with an adapter?', 'Adapters exist, but the trade press and NFPA guidance treat them as a stopgap and ELAFLEX advises against fill-point adapters. Fit the nozzle that matches the valve.'), ('Does Propane Nozzle still sell the GG20?', 'No. We sell the GG40 and matching hose kits. The GG20 guides stay online as reference for owners of existing nozzles.')],
sources=['aag', 'hcck15', 'gg40br', 'info215', 'bpn'],
),

dict(
slug='gg40-part-numbers-and-options',
product='gg40',
title='GG40 Part Numbers and Options: Latched, Unlatched and Inlet',
nav='GG40 part numbers',
desc='How GasGuard GG40 nozzles are coded: latched (L) and unlatched versions, strainer (S), inlet thread, and what to confirm in words on every quote.',
summary='GasGuard codes follow a pattern: nozzle style, then options, then inlet. Distributors list the latched GG40 as GG40SL (S for strainer, L for hold-open latch) with a ¾" NPT inlet; the unlatched nozzle drops the L. Both versions are UL approved. ELAFLEX has not published a full GG40 code table yet, so confirm three things in words on every order: latch (yes or no), inlet thread, and whether you need a matching hose kit.',
body='<h2>What the letters mean</h2>\n<table><thead><tr><th>Code</th><th>Meaning</th><th>Notes</th></tr></thead><tbody>\n<tr><td>GG40</td><td>GasGuard K15 quick-connect nozzle</td><td>The base nozzle, unlatched</td></tr>\n<tr><td>S</td><td>Strainer</td><td>GasGuard nozzles ship with a strainer as standard; the S appears in distributor codes</td></tr>\n<tr><td>L</td><td>Safety hold-open latch</td><td>Latched and unlatched versions are both UL approved, unlike the GG20 where the latch sits outside the listing</td></tr>\n<tr><td>¾" NPT</td><td>Inlet thread</td><td>As listed by US distributors (GG40SL). Other inlet sizes not yet published</td></tr>\n</tbody></table>\n<p>Example: a US distributor lists "Euro K15 Quick Connect Nozzle, UL listed, ¾" NPT, with latch" under SKU GG40SL.</p>\n\n<h2>Which version</h2>\n<p>Pick latched where a trained operator stays with the nozzle and fills many vehicles a shift; the hold-open latch takes the strain off the hand. Pick unlatched where your authority having jurisdiction or site policy wants an attended lever. Because both carry UL approval, the choice is operational rather than a compliance question, which is a change from the ACME GasGuards.</p>\n\n<h2>Spares and repair</h2>\n<p>ELAFLEX describes the GG40 as low maintenance and simple to repair, with an 18-month manufacturer\'s warranty. A GG40 spare-parts list has not been published in the material we cite; ask for the service manual with your quote if you plan to repair in-house.</p>\n<h2>Ordering a GG40</h2>\n<table><thead><tr><th>Choice</th><th>What to pick</th></tr></thead><tbody>\n<tr><td>Latch</td><td>Latched (hold-open) or unlatched. Both versions are UL approved, so the latch is a workflow choice: latched for attended fleet fueling where the operator stays with the nozzle; check your authority having jurisdiction for self-service sites.</td></tr>\n<tr><td>Inlet</td><td>Distributor listings show ¾" NPT. Tell us the thread on your hose kit; we confirm the inlet on the quote. (Other inlet sizes are not yet published.)</td></tr>\n<tr><td>Hose kit</td><td>We can quote a matching ELAFLEX hose kit: LPG 16 S hose, ARK 19.3 pull-away and whip, built for the GG40. See <a href="/guides/autogas-hose-kits">autogas hose kits</a>.</td></tr>\n<tr><td>Nozzle boot</td><td>The GG40 fits the existing NB-GG boot, so dispensers already fitted with one for a GasGuard ACME nozzle don\'t need a new boot.</td></tr>\n</tbody></table>\n<p class="note">GG40 figures on this page come from the ELAFLEX PACIFIC GG40 brochure (2025) and distributor listings. ELAFLEX has not published every number for the GG40 yet; where a figure is missing we say so instead of guessing. Confirm the current data sheet with your quote.</p>\n',
faqs=[('What does GG40SL mean?', 'GasGuard GG40 K15 nozzle with strainer (S) and hold-open latch (L), listed by US distributors with a ¾" NPT inlet.'), ('Is the latched GG40 UL listed?', 'Yes. ELAFLEX states both the latched and unlatched GG40 are UL approved.')],
sources=['gg40br', 'chsgg40', 'info615'],
),

dict(
slug='gg40-installation-hose-and-boot',
product='gg40',
title='Installing a GG40: Hose Kit, ARK 19.3 Pull-Away, Thread Sealing and Boot',
nav='GG40 installation',
desc='Fitting a GasGuard GG40 to a dispenser: the ELAFLEX LPG 16 S hose, ARK 19.3 pull-away, thread sealing without PTFE tape, leak testing, and the NB-GG boot.',
summary='ELAFLEX sells the GG40 as part of a hanging-hardware set: GG40 nozzle, ARK 19.3 pull-away (break-away) and UL-listed LPG 16 S hose. A competent installer connects the nozzle to the hose end with a non-permanent liquid thread sealant (ELAFLEX says no PTFE tape on GasGuard nozzles), tightens with spanners, pressurizes and leak-checks every joint, then hangs the nozzle in an NB-GG boot. The ARK 19.3 separates at a set pull and reconnects by hand.',
body='<h2>Who should install it</h2>\n<p>LP-gas dispensing equipment is installed by competent personnel under NFPA 58 as adopted by your state and your authority having jurisdiction. This page summarizes manufacturer guidance; it does not replace the installer or the manual.</p>\n\n<h2>The complete set</h2>\n<table><thead><tr><th>Part</th><th>Role</th></tr></thead><tbody>\n<tr><td>GG40 nozzle</td><td>K15 quick-connect nozzle, latched or unlatched</td></tr>\n<tr><td>ARK 19.3 pull-away</td><td>Reusable break-away coupling mounted between the short connection hose (whip) and the long delivery hose. ELAFLEX\'s ARK 19 separates when the hose is pulled with 200 to 500 N, independent of internal pressure, closes both sides, and reconnects by hand. Its lanyard fixes to the dispenser.</td></tr>\n<tr><td>LPG 16 S hose</td><td>DN 16 (¾") LPG hose, EN 1762, 25 bar, −40 °C; ELAFLEX\'s US and Canadian LPG hose assemblies are certified to UL 21 and CSA 8.1.</td></tr>\n<tr><td>NB-GG nozzle boot</td><td>Enclosed holster. The GG40 fits the existing NB-GG boot, so a dispenser already fitted for a GasGuard ACME nozzle keeps its boot.</td></tr>\n</tbody></table>\n\n<h2>Connecting the nozzle to the hose</h2>\n<ol>\n<li>Match the hose-end thread to the nozzle inlet (¾" NPT on distributor-listed GG40s).</li>\n<li><strong>No PTFE tape.</strong> ELAFLEX\'s GasGuard manual gives two reasons: poor electrical conductivity across the joint, and tape particles breaking loose into the flow path. Use a non-permanent liquid thread sealant.</li>\n<li>Tighten with spanners on the flats, never a pipe wrench on the nozzle body.</li>\n<li>Pressurize and check every joint with a foaming leak-detection agent.</li>\n<li>Run an operational fill on a K15 receptacle and confirm no leaks at the nozzle, the pull-away and the swivel.</li>\n</ol>\n\n<h2>Pull-away placement</h2>\n<p>Mount the ARK 19.3 between the whip and the delivery hose, with its lanyard anchored to the dispenser or a fixing point that can take more than the coupling\'s maximum separation force. After a drive-off, check both halves and the hose before reconnecting.</p>\n\n<h2>Reed-switch dispensers</h2>\n<p>Some dispensers start the pump from a reed switch in the nozzle boot that senses a magnet in the nozzle. ELAFLEX has not yet published whether the GG40 offers a magnet option; tell us when you order if your boot works that way and we\'ll confirm.</p>\n<p class="note">GG40 figures on this page come from the ELAFLEX PACIFIC GG40 brochure (2025) and distributor listings. ELAFLEX has not published every number for the GG40 yet; where a figure is missing we say so instead of guessing. Confirm the current data sheet with your quote.</p>\n',
faqs=[('Does the GG40 fit the NB-GG nozzle boot?', 'Yes. ELAFLEX states the GG40 is compatible with the existing NB-GG nozzle boot.'), ('Can I use Teflon tape on a GG40?', "No. ELAFLEX's GasGuard guidance is to use a non-permanent liquid thread sealant, because PTFE tape conducts poorly and can shed particles into the flow path.")],
sources=['gg40br', 'ark19', 'lpgul', 'manual'],
),

dict(
slug='gg40-dispenser-compatibility',
product='gg40',
title='Will a GG40 Work With My Dispenser? K15 Hose Kits on Parafour and Others',
nav='GG40 dispenser fit',
desc='How to tell whether a GasGuard GG40 fits your propane dispenser: hose-end thread, pull-away, boot and reed switch, with notes on Parafour P4 dispensers.',
summary='A GG40 fits any autogas dispenser whose hose kit ends in the nozzle\'s inlet thread (¾" NPT on distributor-listed GG40s) and whose boot is an NB-GG or similar. The dispenser doesn\'t care which nozzle hangs on it; the vehicles do. Parafour\'s P4-100, P4-150 and P4-200 are documented with the GG20 on a ¾" hose kit, so a K15 kit with a GG40 goes on the same hose connection; ask the dispenser supplier for the K15 version of the kit.',
body='<h2>The three things that decide fit</h2>\n<table><thead><tr><th>Check</th><th>GG40 needs</th></tr></thead><tbody>\n<tr><td>Hose-end thread</td><td>Matches the GG40 inlet: ¾" NPT per distributor listings. Have the hose kit made with the right end rather than adding reducers.</td></tr>\n<tr><td>Pull-away</td><td>An ARK 19.3 or equivalent break-away between whip and delivery hose; the GG40 ships as part of ELAFLEX\'s set with it.</td></tr>\n<tr><td>Boot and pump start</td><td>NB-GG boot fits. If the boot starts the pump with a reed switch, ask us whether your GG40 needs a magnet option (not yet published; we confirm on the quote).</td></tr>\n</tbody></table>\n\n<h2>Parafour</h2>\n<p>Parafour describes its <a href="/guides/gg20-parafour-p4-100">P4-100</a>, <a href="/guides/gg20-parafour-p4-150">P4-150</a> and <a href="/guides/gg20-parafour-p4-200">P4-200</a> as designed for the GasGuard GG20 on a ¾" autogas hose kit sold separately. The hose connection on the dispenser is the same whichever GasGuard nozzle is on the end of it, so a K15 hose kit with a GG40 fits the autogas hose position; the cylinder hose on a P4-150 keeps its cylinder nozzle. Ask Parafour or your distributor for the K15 version of the hose kit, or send us the dispenser model through the <a href="/#quote">quote form</a> and we\'ll quote the GG40 and a matching kit.</p>\n\n<h2>Other dispensers</h2>\n<p>Check the three items above against the dispenser\'s manual or spec sheet, and confirm the hose-end thread with the dispenser maker. Any dispenser built for a GasGuard ACME nozzle can carry a GG40 instead once the vehicles it serves are K15.</p>\n<p class="note">GG40 figures on this page come from the ELAFLEX PACIFIC GG40 brochure (2025) and distributor listings. ELAFLEX has not published every number for the GG40 yet; where a figure is missing we say so instead of guessing. Confirm the current data sheet with your quote.</p>\n',
faqs=[('Will a GG40 work with a Parafour P4-150?', 'Yes, on the autogas hose. Parafour documents the P4-150 with a GasGuard nozzle on a ¾" hose kit; a K15 kit with a GG40 fits the same connection. Ask your distributor for the K15 version of the kit.')],
sources=['gg40br', 'chsgg40', 'p4150', 'p4kit'],
),

dict(
slug='gg40-safety-codes-and-compliance',
product='gg40',
title='GG40 Safety, Codes and Compliance: NFPA 58, K15 and UL',
nav='GG40 safety & codes',
desc="What NFPA 58 requires for K15 refueling, the GG40's UL approval, the latch question, PPE, emissions claims and who has the final say on an installation.",
summary="NFPA 58 requires K15 quick-connect fill valves on autogas vehicles built or converted since 1 January 2020, and the GG40 is ELAFLEX's nozzle for them. Both latched and unlatched GG40s are UL approved. ELAFLEX states PPE is not necessary with the GG40 unless local codes require it. Emissions: the GG40 releases under 1 cm³ per disconnect by ELAFLEX's figure; the broader claim that K15 cuts fugitive emissions by about 76% versus ACME is an industry figure. Your authority having jurisdiction approves the installation.",
body='<h2>NFPA 58 and the K15 valve</h2>\n<p>The K15 requirement entered NFPA 58 in the 2017 edition and applies to vehicles produced or converted after 1 January 2020; older vehicles are not retroactively affected. The 2024 edition, per Butane-Propane News, lets Euro-style push-on nozzles be used without the operator training the ACME connection required. State adoption of NFPA 58 editions varies, so check which edition your state enforces.</p>\n\n<h2>UL approval and the latch</h2>\n<p>ELAFLEX states that both the latched and unlatched GG40 are UL approved. That removes the latch question that follows the ACME GasGuards, where the hold-open latch sits outside the UL 125 listing. A site\'s authority having jurisdiction can still restrict latched nozzles at self-service sites, so ask before specifying latched nozzles for the public.</p>\n\n<h2>PPE</h2>\n<p>ELAFLEX\'s brochure states personal protective equipment is not necessary for the GG40 unless required by local codes or regulations. Many operators keep gloves and eye protection as site policy regardless; follow your site rules.</p>\n\n<h2>Emissions figures</h2>\n<ul>\n<li>ELAFLEX: the GG40 releases less than 1 cm³ of propane on disconnect, which it calls ultra-low emission.</li>\n<li>Trade press (Alliance AutoGas): the average K15 connection releases about 76% less fugitive emissions than ACME. Treat this as an industry claim, not an independent measurement.</li>\n<li>For comparison, ELAFLEX rates its ACME GG20 at 1.9 cm³ per disconnect.</li>\n</ul>\n\n<h2>LPG hazards to train for</h2>\n<p>Propane is heavier than air and pools low; liquid propane causes cold burns on skin. If a leak or uncontrolled release occurs during filling: release the lever, hit the dispenser emergency stop, move people away, and call emergency services. Train everyone who fills on the site\'s emergency procedure before they fill.</p>\n<p class="note">GG40 figures on this page come from the ELAFLEX PACIFIC GG40 brochure (2025) and distributor listings. ELAFLEX has not published every number for the GG40 yet; where a figure is missing we say so instead of guessing. Confirm the current data sheet with your quote.</p>\n',
faqs=[('Is the GG40 required by NFPA 58?', 'NFPA 58 requires the K15 quick-connect valve on autogas vehicles built or converted since 2020; the GG40 is one nozzle that fits it. The code specifies the valve type, not the nozzle brand.'), ('Do I need PPE to use a GG40?', "ELAFLEX says PPE is not necessary with the GG40 unless local codes or regulations require it. Follow your site's own rules.")],
sources=['gg40br', 'aag', 'hcck15', 'bpn', 'rrc'],
),

dict(
slug='autogas-hose-kits',
product='hose',
title='Autogas Hose Kits for the GG40: Hose, Pull-Away and Whip',
nav='Hose kits',
desc='What is in an autogas hose kit for the GasGuard GG40: ELAFLEX LPG 16 S hose, ARK 19.3 pull-away, whip, lengths and threads, and the UL and CSA listings behind them.',
summary="A hose kit is everything between the dispenser outlet and the nozzle: a short whip hose, an ARK 19.3 pull-away (break-away) with lanyard, and the long delivery hose, assembled with the nozzle on the end. Propane Nozzle quotes ELAFLEX-based kits built for the GG40. ELAFLEX's LPG hose assemblies for the US and Canada are certified to UL 21 and CSA 8.1-2015, rated 350 psi working pressure with burst above 1750 psi. Tell us the dispenser, the delivery-hose length and the thread you need.",
body='<h2>What is in the kit</h2>\n<table><thead><tr><th>Part</th><th>What it does</th><th>ELAFLEX part</th></tr></thead><tbody>\n<tr><td>Whip hose</td><td>Short hose from the dispenser outlet to the pull-away; takes the bending at the cabinet.</td><td>LPG 16 S</td></tr>\n<tr><td>Pull-away</td><td>Break-away coupling that separates on a drive-off and seals both ends; reconnectable by hand. Lanyard anchors to the dispenser.</td><td>ARK 19.3</td></tr>\n<tr><td>Delivery hose</td><td>The long hose to the nozzle.</td><td>LPG 16 S</td></tr>\n<tr><td>Nozzle</td><td>K15 quick-connect nozzle, latched or unlatched.</td><td>GG40</td></tr>\n</tbody></table>\n<p>ELAFLEX calls this set its hanging hardware and sells it as a complete solution with the GG40.</p>\n\n<h2>Hose specification</h2>\n<table><tbody>\n<tr><th>Hose</th><td>ELAFLEX LPG 16 S: DN 16 (¾"), EN 1762, marked 25 bar and −40 °C</td></tr>\n<tr><th>Listings</th><td>ELAFLEX\'s LPG-UL hose assemblies are certified by Underwriters Laboratories to UL 21 and CSA 8.1-2015; the hose carries UL Classified and CSA marks</td></tr>\n<tr><th>Working pressure</th><td>350 psi (25 bar) per ELAFLEX US; burst above 1750 psi (120 bar), safety factor 5:1</td></tr>\n<tr><th>Construction</th><td>NBR lining, electrically conductive, diffusion resistant; textile braid with crossed tinned copper strands</td></tr>\n<tr><th>Fittings</th><td>Ferrule-type (non-reusable) couplings, male NPT ends</td></tr>\n<tr><th>Sizes available in the LPG-UL range</th><td>½", ¾", 1", 1¼", 1½", 2"; autogas kits use ¾"</td></tr>\n</tbody></table>\n\n<h2>Lengths and threads</h2>\n<p>Distributor autogas kits for US dispensers are typically an 18" × ¾" whip plus a ¾" × 12\' delivery hose, with the pull-away between them. Other lengths are built to order. Tell us the dispenser model, where the pull-away anchors, the hose length you need and the outlet thread on the dispenser; we confirm the configuration on the quote.</p>\n\n<h2>Pull-away</h2>\n<p>ELAFLEX\'s ARK 19 separates when the hose is pulled with 200 to 500 N regardless of internal pressure, closes valves on both sides, and can be reconnected by hand. The anchor point must withstand more than the maximum separation force. The 19.3 is the current version ELAFLEX pairs with the GG40.</p>\n\n<h2>Replacing an ACME kit</h2>\n<p>If your dispenser has a GG20 on a ¾" kit today, the GG40 kit uses the same hose connection at the dispenser. Swap the whole kit rather than only the nozzle so the pull-away and hose match the new nozzle\'s warranty and listing.</p>\n<p class="note">GG40 figures on this page come from the ELAFLEX PACIFIC GG40 brochure (2025) and distributor listings. ELAFLEX has not published every number for the GG40 yet; where a figure is missing we say so instead of guessing. Confirm the current data sheet with your quote.</p>\n',
faqs=[("What's in an autogas hose kit?", 'A whip hose, an ARK 19.3 pull-away with lanyard, the delivery hose, and the GG40 nozzle on the end, all assembled. ELAFLEX calls it hanging hardware.'), ('Are the hose kits UL listed?', "ELAFLEX's LPG hose assemblies for the US and Canada are certified to UL 21 and CSA 8.1-2015, and the LPG 16 S hose carries UL Classified and CSA marks."), ('What hose length do I need?', 'Most US autogas kits use an 18" whip and a 12\' delivery hose in ¾". Tell us your dispenser model and where the pull-away anchors and we\'ll confirm.')],
sources=['gg40br', 'lpgul', 'ark19', 'p4kit'],
),

dict(
slug='gg40-maintenance-and-warranty',
product='gg40',
title='GG40 Maintenance, Repair and Warranty',
nav='GG40 maintenance',
desc='What ELAFLEX publishes about keeping a GasGuard GG40 in service: low maintenance, simple repair, the 18-month warranty, boot storage and when to call the manufacturer.',
summary="ELAFLEX describes the GG40 as low maintenance and simple to repair, with an 18-month manufacturer's warranty, and says the robust design is built for a longer lifetime. ELAFLEX has not yet published a GG40 inspection schedule or seal-kit number in the material we cite, so follow your site's LP-gas inspection routine, store the nozzle in its NB-GG boot, and ask for the GG40 service manual with your quote if you plan in-house repair.",
body='<h2>What ELAFLEX says</h2>\n<ul>\n<li>Low maintenance, simple to repair, which ELAFLEX summarizes as low running cost.</li>\n<li>Light weight and a robust design for a longer lifetime.</li>\n<li>18-month manufacturer\'s warranty.</li>\n<li>Store in the NB-GG nozzle boot, which encloses the nozzle so residual gas can\'t enter the dispenser housing.</li>\n</ul>\n\n<h2>Daily checks that apply to any LPG nozzle</h2>\n<ul>\n<li>Nozzle nose and locking segments clean and undamaged; no debris in the K15 interface.</li>\n<li>Swivel turns freely; no gas smell at the hose connection or pull-away.</li>\n<li>Lever and latch move freely and return.</li>\n<li>Hose free of cuts, kinks and abrasion; lanyard intact on the pull-away.</li>\n</ul>\n<p>If a nozzle leaks, sticks or won\'t lock onto a valve, take it out of service and have a trained LP-gas technician inspect it. ELAFLEX states it cannot be responsible for the performance of repaired nozzles, so use genuine parts.</p>\n\n<h2>Inspection interval and seal kit</h2>\n<p>ELAFLEX has not yet published a GG40 inspection schedule or seal-kit part number in the documents we cite. For its ACME nozzles ELAFLEX recommends a full inspection every 6 to 12 months and a seal kit every 24 months; treat that as a starting point for your site routine until GG40-specific guidance is available.</p>\n<p class="note">GG40 figures on this page come from the ELAFLEX PACIFIC GG40 brochure (2025) and distributor listings. ELAFLEX has not published every number for the GG40 yet; where a figure is missing we say so instead of guessing. Confirm the current data sheet with your quote.</p>\n',
faqs=[('What warranty does the GG40 have?', "18 months, manufacturer's warranty, per ELAFLEX."), ('How often should a GG40 be inspected?', "ELAFLEX hasn't published a GG40 schedule yet. Its ACME GasGuards get a full inspection every 6 to 12 months and a seal kit every 24 months; use that as a starting point and follow your site routine.")],
sources=['gg40br', 'manual'],
),

dict(
slug="gg20-vs-gg20h-vs-gg20dn",
title="GG20 vs GG20H vs GG20DN: Which GasGuard Nozzle to Buy",
nav="GG20 vs GG20H vs GG20DN",
desc="How the three GasGuard GG20 nozzles differ: single, hybrid and dual nose pieces, flow, lever force, release volume and who each one is for.",
summary="All three GG20 nozzles share the same body, 160 mm reach and 1¾\" ACME coupling. The nose piece is the only difference. GG20 (single nose) flows the most, 63 L/min, and costs least; it suits trained operators. GG20H (hybrid nose) cuts lever force at 60 L/min for operators who fill all day. GG20DN (patented dual nose) seals even when the nozzle isn't fully tightened, so it is the one to use where the public or untrained staff fill.",
body="""
<p class="note">Reference only: Propane Nozzle no longer sells the GG20 range. US autogas vehicles built or converted since 2020 carry K15 valves, which take the <a href="/guides/gg40-k15-quick-connect-nozzle">GasGuard GG40</a>; we sell the GG40 and matching hose kits.</p>

<h2>The short version</h2>
<table>
<thead><tr><th></th><th>GG20</th><th>GG20H</th><th>GG20DN</th></tr></thead>
<tbody>
<tr><th>Nose piece</th><td>Single ('E')</td><td>Hybrid ('H')</td><td>Dual ('DN'), patented</td></tr>
<tr><th>Flow at 12 bar</th><td>63 L/min (≈16.6 gpm)</td><td>60 L/min (≈15.9 gpm)</td><td>60 L/min (≈15.9 gpm)</td></tr>
<tr><th>Gas released on valve closure</th><td>1.9 cm³</td><td>1.7 cm³</td><td>1.7 cm³</td></tr>
<tr><th>Lever hold-open force</th><td>Standard</td><td>Lower than GG20</td><td>Same low force as GG20H</td></tr>
<tr><th>Seals if not screwed fully tight</th><td>No</td><td>No</td><td>Yes</td></tr>
<tr><th>ELAFLEX intended use</th><td>Industrial, attended refueling</td><td>Industrial, attended refueling</td><td>Public, self-service, untrained users</td></tr>
<tr><th>UL 125 listed</th><td>Yes</td><td>Yes</td><td>Yes</td></tr>
</tbody></table>

<h2>GG20: the economy choice for trained operators</h2>
<p>ELAFLEX calls the GG20 the most economic type in the range. It uses the single 'E' nose piece and has the highest flow of the three. Pick it when the person filling is trained, the site is attended, and cost per nozzle matters more than operator comfort.</p>

<h2>GG20H: less hand fatigue</h2>
<p>The hybrid nose piece lowers the force needed to hold the lever open. On a cylinder-exchange dock where one operator fills dozens of forklift cylinders a shift, that adds up. You give up 3 L/min of rated flow and get a slightly smaller release on disconnect (1.7 cm³ instead of 1.9 cm³).</p>

<h2>GG20DN: when you can't control who fills</h2>
<p>The dual nose piece is the safety upgrade. ELAFLEX states it creates a positive seal to the vehicle even if the user hasn't tightly screwed the nozzle onto the fill point, and that it significantly reduces user error. It has the same low lever force as the GG20H. If members of the public, rental customers or rotating staff will use the nozzle, this is the one to buy.</p>

<h2>What doesn't change between them</h2>
<p>Reach (160 mm connector nut), the 1¾" ACME coupling, the 25 bar (362 psi) pressure rating, the −40 °C to +110 °C range, the inlet swivel choice (½" or ¾" NPT female), the standard 300 µm strainer, and the options (magnet, latch, splashguard, brass ACME insert). See <a href="/guides/gg20-specifications">full specifications</a> and <a href="/guides/gg20-part-numbers-and-options">part numbers</a>.</p>

<h2>Need standard reach instead?</h2>
<p>The same three nose pieces exist on the shorter GG1 series as GG1E, GG1EH and GG1DN, with a 125 mm connector. Choose GG20 only when the fill valve is recessed. See <a href="/guides/gasguard-family-gg1-gg20-gg30-gg40">the GasGuard family compared</a>.</p>
""",
faqs=[("Which GG20 version has the highest flow?","The GG20 with the single nose piece, rated 63 L/min at 12 bar. The GG20H and GG20DN are rated 60 L/min."),
      ("How much lever force does the GG20H or GG20DN need?","ELAFLEX says the hybrid and dual nose pieces reduce the force needed to hold the lever open compared with the single-nose GG20, but the documents we cite don't give a figure in newtons or pounds."),
      ("Which GG20 is safest for self-service?","The GG20DN. Its patented dual nose piece seals even if the nozzle isn't fully tightened, and ELAFLEX designates it for public and untrained users.")],
sources=["info215","cat","info615"],
),

dict(
slug="gg20-specifications",
title="GasGuard GG20 Specifications: Complete Technical Data",
nav="Specifications",
desc="Every published spec for the ELAFLEX GasGuard GG20: reach, flow, pressure, temperature, materials, seals, weight, strainer and standards, in metric and US units.",
summary="The GasGuard GG20 is a 1¾\" ACME LPG nozzle with a 160 mm (6.3 in) connector nut. Max working pressure 25 bar (362 psi), burst pressure above 100 bar (1450 psi), temperature range −40 °C to +110 °C (−40 °F to 230 °F), weight about 2.0 kg (4.4 lb). Flow is 63 L/min for the GG20 and 60 L/min for the GG20H and GG20DN at 12 bar. It is UL listed to UL 125 and built to AS/NZS 1596, AS/NZS 1425 and EN 12806 coupling dimensions.",
body="""
<h2>Core ratings</h2>
<table><tbody>
<tr><th>Coupling</th><td>1¾" ACME thread to AS/NZS 1596, AS/NZS 1425, EN 12806</td></tr>
<tr><th>Nozzle reach</th><td>160 mm (6.3 in) connector nut; 35 mm (1.4 in) longer than the GG1</td></tr>
<tr><th>Media</th><td>LPG: propane, butane and their mixtures</td></tr>
<tr><th>Max working pressure</th><td>25 bar / 2500 kPa / 362 psi</td></tr>
<tr><th>Burst pressure</th><td>&gt;100 bar / &gt;1450 psi</td></tr>
<tr><th>Temperature range</th><td>−40 °C to +110 °C (−40 °F to 230 °F)</td></tr>
<tr><th>Flow at 12 bar system pressure</th><td>GG20 63 L/min; GG20H and GG20DN 60 L/min</td></tr>
<tr><th>Release volume on valve closure</th><td>GG20 1.9 cm³; GG20H and GG20DN 1.7 cm³</td></tr>
<tr><th>Weight incl. swivel</th><td>≈2.0 kg (4.4 lb)</td></tr>
<tr><th>Inlet</th><td>Stainless swivel, ½" NPT female (15 mm) or ¾" NPT female (20 mm)</td></tr>
<tr><th>Strainer</th><td>300 µm / 50 mesh, POM, fitted as standard (standard since July 2014)</td></tr>
<tr><th>Listing</th><td>Underwriters Laboratories, UL 125</td></tr>
</tbody></table>
<p class="note">Two small conflicts in ELAFLEX's own documents: the operating manual prints the temperature range as "−40 °F to 131 °F", but +110 °C converts to 230 °F, so the Fahrenheit figure in the manual is a misprint. The GasGuard brochure lists the GG20 at 1.9 kg while the data sheet and catalogue say ≈2.0 kg. The manual also gives a general maximum flow of 50 to 70 L/min across GG1 and GG20 types, depending on configuration.</p>

<h2>Materials</h2>
<table><tbody>
<tr><th>Nozzle body</th><td>Aluminum, with PVC "comfigrip" cold-protection grip</td></tr>
<tr><th>Connector</th><td>High-strength aluminum alloy casting with stainless steel ACME thread insert; coupling nut aluminum/stainless with ratchet safety system</td></tr>
<tr><th>Swivel</th><td>Stainless steel</td></tr>
<tr><th>Valve body</th><td>Zinc-chromated steel</td></tr>
<tr><th>Internal parts</th><td>Stainless steel, acetal resin (POM) and polyamide (PA)</td></tr>
<tr><th>Lever</th><td>Polyamide; optional hold-open latch in aluminum</td></tr>
<tr><th>Seals</th><td>Low-temperature NBR, low-temperature Viton®, polyurethane</td></tr>
</tbody></table>

<h2>Built-in safety functions</h2>
<ul>
<li>Cannot discharge LPG to atmosphere if the lever is pulled while the nozzle is not coupled.</li>
<li>Seals safely even if the fill point gasket is missing.</li>
<li>Guided connector nut with extended thread helps align the nozzle with the fill point.</li>
<li>Strainer stops contaminants from upstream before they reach the vehicle or tank.</li>
</ul>

<h2>Pressure drop</h2>
<p>ELAFLEX publishes a pressure drop curve for the GG20 family, measured at the National Measurement Institute in Sydney using common adapters without check valves. ELAFLEX warns that real vehicle connections and adapters vary and can change the result, so treat rated flow as a lab figure. The curve is on catalogue page 570.</p>
""",
faqs=[("What is the maximum pressure of the GG20?","25 bar (362 psi) working pressure; burst pressure is above 100 bar (1450 psi)."),
      ("How heavy is the GG20?","About 2.0 kg (4.4 lb) including the swivel, per the ELAFLEX data sheet and catalogue.")],
sources=["info215","cat","manual","info615"],
),

dict(
slug="gg20-part-numbers-and-options",
title="GG20 Part Numbers Decoded: Nose Pieces, Inlets and Option Codes",
nav="Part numbers & options",
desc="How to read a GasGuard GG20 part number: GG20/GG20H/GG20DN, .2 and .3 inlets, and the J, S, L, G and B option codes, plus how distributors label them.",
summary="A GasGuard 1¾\" ACME part number is built from nozzle style (GG1 or GG20), nose piece (E, H or DN), then options: J magnet, S strainer, L hold-open latch, followed by inlet size. In the ELAFLEX catalogue the GG20 types are GG20.2 / GG20.3, GG20H.2 / GG20H.3 and GG20DN.2 / GG20DN.3, where .2 is ½\" NPT female and .3 is ¾\" NPT female. Extra suffixes add J (magnet), L (latch), G (splashguard) or B (hard-anodized connector with brass ACME insert). Distributors don't all write these codes the same way, so confirm nose piece, latch and inlet in words before ordering.",
body="""
<h2>How ELAFLEX builds the number</h2>
<p>ELAFLEX's Information 6.15 lays the code out in six positions:</p>
<table><thead><tr><th>#</th><th>Position</th><th>Choices</th></tr></thead><tbody>
<tr><td>1</td><td>Nozzle style</td><td>GG1 (125 mm reach) or GG20 (160 mm reach)</td></tr>
<tr><td>2</td><td>Nose piece</td><td>E (single, attended, highest flow), H (hybrid, lower lever force), DN (dual, unattended/public)</td></tr>
<tr><td>3</td><td>Magnet</td><td>J, only if the dispenser uses a reed switch in the nozzle boot</td></tr>
<tr><td>4</td><td>Strainer</td><td>S, standard since July 2014</td></tr>
<tr><td>5</td><td>Latch</td><td>L, optional hold-open latch</td></tr>
<tr><td>6</td><td>Inlet size</td><td>½" (15 mm) or ¾" (20 mm) NPT female</td></tr>
</tbody></table>

<h2>Catalogue part numbers</h2>
<table><thead><tr><th>Part number</th><th>Nose piece</th><th>Inlet</th></tr></thead><tbody>
<tr><td>GG20.2</td><td>Single</td><td>½" NPT female</td></tr>
<tr><td>GG20.3</td><td>Single</td><td>¾" NPT female</td></tr>
<tr><td>GG20H.2</td><td>Hybrid</td><td>½" NPT female</td></tr>
<tr><td>GG20H.3</td><td>Hybrid</td><td>¾" NPT female</td></tr>
<tr><td>GG20DN.2</td><td>Dual</td><td>½" NPT female</td></tr>
<tr><td>GG20DN.3</td><td>Dual</td><td>¾" NPT female</td></tr>
</tbody></table>
<p>The GG20 has no "E" in its catalogue code even though it uses the E nose piece. Its shorter sibling is written GG1E.</p>

<h2>Option suffixes</h2>
<table><thead><tr><th>Code</th><th>Option</th><th>Notes</th></tr></thead><tbody>
<tr><td>J</td><td>Magnet in the front guard</td><td>For contactless pump activation where the boot has a reed switch. Not needed otherwise.</td></tr>
<tr><td>L</td><td>Hold-open latch (aluminum)</td><td>Not covered by the UL listing, and ELAFLEX notes not every country or LPG authority allows a latch. Check with your authority having jurisdiction.</td></tr>
<tr><td>G</td><td>Splashguard, soft orange PVC</td><td>Shields the hand from gas released after the valve shuts.</td></tr>
<tr><td>B</td><td>Special connector</td><td>Hard-anodized alloy connector with brass (non-guided) ACME insert, instead of the standard guided stainless insert.</td></tr>
<tr><td>S</td><td>Strainer</td><td>300 µm / 50 mesh. Fitted as standard on current production.</td></tr>
</tbody></table>

<h2>How US distributors write it</h2>
<p>Codes drift between catalogues. Examples seen in US distributor listings: "GG20S" (with strainer), "GG20SL" (strainer and latch), "GG20DNS", and a listing titled simply "GG20" that is described as having a locking latch. Because the latch changes the UL status and the nose piece changes who may safely use it, confirm three things in plain words on every quote: nose piece (single, hybrid or dual), latch (yes or no), inlet (½" or ¾").</p>

<h2>Spare assemblies named in the repair manual</h2>
<table><thead><tr><th>Assembly</th><th>Part number</th></tr></thead><tbody>
<tr><td>Connector assembly</td><td>GG27</td></tr>
<tr><td>Lever assembly (with latch)</td><td>GG5 (GG5L)</td></tr>
<tr><td>Valve assembly</td><td>LG24</td></tr>
<tr><td>Inlet swivel assembly</td><td>LG2, 15 mm or 20 mm</td></tr>
<tr><td>Nozzle body assembly</td><td>10-1307-715</td></tr>
<tr><td>Strainer</td><td>EK172.1</td></tr>
<tr><td>Magnet assembly</td><td>GGJ</td></tr>
<tr><td>Seal kit for GG20 series</td><td>GG3</td></tr>
</tbody></table>
<p>These numbers come from the GG20 repair and maintenance manual. Propane Nozzle quotes complete GG20 nozzles only, not individual spares; ask your LP-gas service company about parts availability before you plan a repair around one.</p>
""",
faqs=[("Can I get a GG20H or GG20DN with a latch, magnet or splashguard?","Yes. The option codes apply to all three nose pieces: J magnet, L hold-open latch, G splashguard and B brass ACME insert can be added to a GG20, GG20H or GG20DN, with either the .2 or .3 inlet. The latch isn't covered by the UL listing, so check with your authority having jurisdiction first."),
      ("What does .3 mean in GG20.3?","A ¾\" NPT female inlet swivel. A .2 suffix means ½\" NPT female."),
      ("What does the L suffix mean on a GasGuard nozzle?","A hold-open latch. ELAFLEX notes the latch is not covered by the UL listing and isn't permitted everywhere.")],
sources=["info615","cat","info215","rm"],
),

dict(
slug="gg20-installation-and-hose-assembly",
title="Installing a GG20: Hose, Thread Sealing, Safety Break and Boot",
nav="Installation",
desc="Installation guidance for the GasGuard GG20 from the ELAFLEX manual: thread sealing (no PTFE tape), leak testing, recommended hose, ARK 19 safety break and NB-GG boot.",
summary="The GG20 ships ready to use and must be installed by competent personnel under local codes. ELAFLEX says not to use PTFE tape on the threads, because it doesn't conduct static well and can shed particles; use a non-permanent liquid thread sealant, tighten with spanners, then leak test under pressure with a foaming agent and run an operational test. ELAFLEX recommends its LPG 16 S hose, an ARK 19 Mod.2 safety break and the NB-GG nozzle boot. Fill point adaptors are not recommended.",
body="""
<h2>Who should install it</h2>
<p>ELAFLEX states the nozzle must be installed by competent personnel following applicable laws and codes. In the US that usually means NFPA 58 as adopted by your state, plus your authority having jurisdiction. In Texas, LP-gas activities fall under the Railroad Commission of Texas, which publishes its own guidance on autogas dispensers. This page summarizes the manufacturer's instructions; it does not replace them or your installer.</p>

<h2>Connecting the nozzle to the hose</h2>
<ol>
<li>Choose the inlet that matches your hose end: ½" NPT female (.2) or ¾" NPT female (.3).</li>
<li><strong>Do not use PTFE tape.</strong> ELAFLEX gives two reasons: poor electrical conductivity, and the risk of tape particles breaking loose into the flow path.</li>
<li>Use a non-permanent liquid thread sealant.</li>
<li>Assemble with spanners, not pipe wrenches on the nozzle body.</li>
<li>Pressurize and check every joint with a foaming leak-detection agent.</li>
<li>Run an operational test with the hose assembly and confirm no leaks at the nozzle, the hose connector and the swivel.</li>
</ol>

<h2>Recommended accessories</h2>
<table><thead><tr><th>Item</th><th>What it does</th></tr></thead><tbody>
<tr><td>LPG 16 S dispensing hose</td><td>DN 16 mm, highly flexible, low permeation, meets EN 1762 and AS/NZS 1869:2012. ELAFLEX recommends professionally assembled hose.</td></tr>
<tr><td>ARK 19 Mod.2 safety break</td><td>Protects against drive-off incidents. Reconnectable by hand under pressure.</td></tr>
<tr><td>BS 19 break sleeve</td><td>Companion sleeve for the safety break.</td></tr>
<tr><td>NB-GG nozzle boot</td><td>Fully enclosed holster for GasGuard nozzles, so residual LPG in the nozzle can't enter the dispenser housing. Has provision for a lock.</td></tr>
<tr><td>KS 16 anti-kink sleeve, CS 16 colour sleeve</td><td>Protect the hose at the nozzle end and mark the fuel grade.</td></tr>
</tbody></table>
<p>US installations must use hose, breakaways and boots acceptable under your local code. Ask your installer before substituting.</p>

<h2>Reed switch dispensers</h2>
<p>If your dispenser starts the pump with a reed switch at the back of the nozzle boot, order the nozzle with the J magnet option. Without it, the pump won't sense the nozzle being lifted.</p>

<h2>Avoid fill point adaptors</h2>
<p>ELAFLEX does not recommend adaptors between nozzle and fill point. They increase the volume of gas released on disconnect and can damage worn receptacles. Removing the need for an adaptor on recessed valves is the main reason the GG20 exists.</p>
""",
faqs=[("Can I use PTFE tape on a GG20 inlet thread?","No. ELAFLEX says not to, because PTFE tape conducts static poorly and can shed particles. Use a non-permanent liquid thread sealant."),
      ("Do I need the magnet option?","Only if your dispenser uses a reed switch in the nozzle boot to start the pump.")],
sources=["manual","cat","range","rrc"],
),

dict(
slug="how-to-fill-forklift-cylinders-and-rvs-with-gg20",
title="How to Fill Forklift Cylinders and RVs with a GasGuard GG20",
nav="Operating the GG20",
desc="Step-by-step GG20 operating procedure from the ELAFLEX manual, applied to forklift motor fuel cylinders and recessed RV fill valves, with PPE and stop conditions.",
summary="To use a GG20: shut off the engine, check the fill point and nozzle seals are clean and undamaged, put on gloves and safety glasses, align the nozzle with the fill valve, screw the connector nut clockwise until firm, pull the lever to fill, and release it to stop. When finished, release the lever, unscrew the nut counter-clockwise keeping hands clear of the small gas release, and return the nozzle to its boot. Stop immediately if gas escapes continuously. The nozzle does not control fill level; follow the filling procedure for the container.",
body="""
<h2>Before you start</h2>
<ul>
<li>No open flames, smoking, static sources, mobile phones or other electrical devices in the transfer area.</li>
<li>Engine off.</li>
<li>Gloves and safety glasses on. LPG is extremely cold when it depressurizes and can cause cold burns.</li>
<li>Look at the fill point and the nozzle: clean, no dents, no sharp edges, seals in place, lever moves freely.</li>
</ul>

<h2>Filling: the manufacturer's sequence</h2>
<ol>
<li>Take the nozzle from the dispenser boot.</li>
<li>Line the nozzle up with the fill point. On a recessed forklift or RV valve, keep it square; the long guided connector nut is there to help.</li>
<li>Screw the connector nut clockwise until firm.</li>
<li>If your nozzle has a latch, engage it with your forefinger.</li>
<li>Pull the lever to start. If you see or hear leakage, let go of the lever.</li>
<li>Release the lever when filling is complete. Unlatch first if latched.</li>
<li>Unscrew the connector nut counter-clockwise. Keep hands away from the coupling while the trapped liquid between nozzle and fill valve vents. A small release here is normal.</li>
<li>Return the nozzle to its boot.</li>
</ol>

<h2>Forklift motor fuel cylinders</h2>
<p>Cylinder cradles and brackets often sit around the filler valve, which is why a standard 125 mm nozzle can bottom out before the threads engage. The GG20's extra 35 mm reaches past the cradle. The nozzle only moves fuel; it does not stop at a fill level. Fill the cylinder by the method your site procedure and the cylinder require, such as by weight or by the fixed maximum liquid level gauge, and only if the cylinder is within its requalification date.</p>

<h2>RVs and motorhomes</h2>
<p>RV fill valves are often behind an access door or skirting. Same procedure. Note that South Coast AQMD Rule 1177, which mandates low-emission connectors in its district, exempts cylinders dedicated to and installed on recreational vehicles.</p>

<h2>Stop and isolate if</h2>
<ul>
<li>Gas escapes continuously or uncontrollably: release the lever, press the dispenser emergency stop, clear the area.</li>
<li>The connection doesn't go on smoothly: disconnect and reconnect. Never force it.</li>
<li>A problem repeats: take the nozzle out of service and have trained personnel inspect it. See <a href="/guides/gg20-troubleshooting">troubleshooting</a>.</li>
</ul>
""",
faqs=[("Is a small hiss of gas normal when disconnecting a GG20?","Yes. ELAFLEX states a small release on uncoupling is normal: 1.9 cm³ for the GG20 and 1.7 cm³ for the GG20H and GG20DN. A continuous release is not normal."),
      ("Does the GG20 stop automatically when the tank is full?","No. It is a manual lever nozzle. Fill level is controlled by the filling procedure for the container, not by the nozzle.")],
sources=["manual","info215","r1177"],
),

dict(
slug="gg20-inspection-and-maintenance",
title="GG20 Inspection and Maintenance Schedule: Daily, 6 to 12 Months, 24 Months",
nav="Inspection & maintenance",
desc="The ELAFLEX inspection schedule for GasGuard GG20 nozzles: daily visual checks, the 6 to 12 month inspection list, and the 24-month seal kit replacement.",
summary="ELAFLEX recommends three levels of care for GG1 and GG20 nozzles: a daily visual check by trained personnel (coupling clean and undamaged, swivel turns, nose piece O-ring intact), a full inspection every 6 to 12 months (seals, connector nut and pawl, swivel grub screw, valve movement, leak test with soapy water on a blanked 1¾\" ACME adaptor), and a complete seal kit replacement every 24 months. The GG20 series seal kit is listed as GG3.",
body="""
<h2>Daily, by trained site personnel</h2>
<ul>
<li>Coupling is clean and undamaged: no dents, sharp edges or blocked lever.</li>
<li>Inlet swivel rotates.</li>
<li>White nose piece O-ring is free of dirt and mechanical damage.</li>
</ul>

<h2>Every 6 to 12 months</h2>
<table><thead><tr><th>#</th><th>Check</th></tr></thead><tbody>
<tr><td>1</td><td>Any physical damage to nozzle components</td></tr>
<tr><td>2</td><td>Connector nut and nose piece seals for cuts or excessive wear</td></tr>
<tr><td>3</td><td>Connector nut turns freely; pawl and spring work</td></tr>
<tr><td>4</td><td>Inlet swivel is secured by its grub screw</td></tr>
<tr><td>5</td><td>Valve slides freely in the slide sleeve: work the lever several times</td></tr>
<tr><td>6</td><td>Valve function on a blanked 1¾" ACME adaptor; check nose seal and U-cup seal with soapy water</td></tr>
<tr><td>7</td><td>Soapy water leak check at the inlet swivel, nozzle body and valve assembly</td></tr>
</tbody></table>

<h2>Every 24 months</h2>
<p>ELAFLEX PACIFIC recommends fitting a new seal kit throughout the nozzle every 24 months to extend service life and cut downtime. The repair manual lists the GG3 seal kit for the GG20 series. Seal replacement is a bench job; see <a href="/guides/gg20-repair-and-testing">repair and testing</a>.</p>

<h2>Keep a log</h2>
<p>A simple record per nozzle (serial number, date, who checked, result) makes the 24-month interval easy to track. Where low-emission rules apply, such as South Coast AQMD Rule 1177, facilities must be able to show that connectors meet the rule and are kept vapor- and liquid-tight.</p>

<h2>Warranty</h2>
<p>The ELAFLEX PACIFIC manual gives a 12-month warranty from date of supply against defective materials and manufacture. It excludes normal wear and improper use, and approvals and warranty are void if non-original parts are used or the nozzle is modified.</p>
""",
faqs=[("How often should a GG20 seal kit be replaced?","Every 24 months, per ELAFLEX PACIFIC. The seal kit for the GG20 series is listed as GG3."),
      ("What warranty does a GasGuard nozzle have?","12 months from supply against defective materials and manufacturing, per the ELAFLEX PACIFIC manual. Wear and misuse are excluded.")],
sources=["manual","rm","r1177"],
),

dict(
slug="gg20-repair-and-testing",
title="GG20 Repair and Pressure Testing: What the Service Manual Covers",
nav="Repair & testing",
desc="Overview of the GasGuard GG20 repair and maintenance manual: assemblies, tools, lubricants, rejection criteria, static and dynamic test procedures and test pressures.",
summary="The GG20 repair manual is written for authorized distributors, OEMs and service centres. It breaks the nozzle into the GG27 connector, GG5 lever, LG24 valve, LG2 inlet swivel and body assemblies, specifies three lubricants and Loctite 263, and requires a static test at 12 to 18 bar (174 to 260 psi) under water with a 27 N·m (20 ft·lb) bending load on the swivel, then a dynamic flow test with propane. Nitrogen or compressed air can substitute for LPG in testing. Repairs should be done by a qualified service shop.",
body="""
<p class="note">This is an overview so you know what a proper repair involves. It is not a substitute for the manual or for a trained technician. ELAFLEX states it cannot be held responsible for the performance of repaired nozzles.</p>

<h2>Main assemblies</h2>
<ul>
<li><strong>GG27 connector assembly</strong>: connector nut, slide sleeve, 31 ball bearings, lip seals, split bearing and GG6 nose piece.</li>
<li><strong>LG24 valve assembly</strong>: valve body, U-cup seal and housing, valve seat, ball valve and spring, spring guide and circlip, O-rings.</li>
<li><strong>LG2 inlet swivel</strong>: 13 ball bearings, ball plug, seals and back-up rings; 15 mm or 20 mm.</li>
<li><strong>GG5 lever</strong> (GG5L with latch), <strong>nozzle body</strong> 10-1307-715, <strong>EK172.1 strainer</strong>, <strong>GGJ magnet</strong>.</li>
</ul>

<h2>Tools and consumables</h2>
<p>38 mm adjustable spanner, internal circlip pliers, ball-peen hammer, 3.2 mm drift, screwdrivers, bench vice, 2.5 to 3.0 mm Allen keys, spring clamps, sharp-nose punch, 5 mm drill bit, the special nose piece assembly tool, and Loctite 263. Lubricants: Aeroshell 22 grease on threads and close-fitting parts, Dow Corning Molykote FS3451 fluorosilicone grease on dynamic O-rings, and Nulon L90 anti-seize on rotating parts.</p>

<h2>When to reject a part</h2>
<ul>
<li>Distortion or damage on any sealing surface.</li>
<li>Wear marks, scoring or plating damage on swivel bodies.</li>
<li>Damage to the nose piece tail ramp or bridge.</li>
<li>Worn lever slipper faces; worn latch pivot pin or contact points.</li>
<li>Damaged strainer mesh or ring seal.</li>
</ul>
<p>The manual says age, wear and abuse can make repair uneconomic, and replacing whole assemblies or the nozzle may be the better choice.</p>

<h2>Nose pieces on the GG20, GG20H and GG20DN</h2>
<p>The nose piece is the only part that differs between the three versions, so it's the part to get right on a repair. The repair manual names the <strong>GG6 nose piece</strong> as part of the GG27 connector assembly; that is the single nose piece used on the standard GG20. The manual we cite doesn't list part numbers for the hybrid (GG20H) or dual (GG20DN) nose pieces. ELAFLEX PACIFIC publishes a separate "Replacement Nose Piece" document and a "Nose Piece O-ring information sheet" on its GasGuard information page.</p>
<p>When you source a nose piece or seal kit for a GG20H or GG20DN, give the full model code from the nozzle (for example GG20DN.3) and its serial number, and confirm the part is for that nose piece type. Fitting the nose piece needs the special nose piece assembly tool listed above, and the white nose piece O-ring is one of the parts the 24-month seal kit replaces.</p>

<h2>Static test (before fitting connector and lever)</h2>
<ol>
<li>Connect to a supply hose with an upstream isolating valve.</li>
<li>Pressurize to 1200 to 1800 kPa (12 to 18 bar, 174 to 260 psi).</li>
<li>Immerse in detergent-loaded water with the nozzle closed.</li>
<li>Apply about 27 N·m (20 ft·lb) bending moment to the inlet swivel while rotating it slowly; watch every joint.</li>
<li>Fit connector and lever; couple to an approved vehicle connector or blanked adaptor. Confirm it locks firmly and the lever and latch work.</li>
</ol>

<h2>Dynamic flow test (with propane)</h2>
<ol>
<li>Connect to a vehicle connector on a dispenser vapor return line with a downstream receiving tank.</li>
<li>With the valve closed, check for vapor leaks with detergent spray.</li>
<li>Pull the lever; spray the connector sides again.</li>
<li>Release the lever; confirm only a small amount of gas escapes.</li>
<li>Close the isolating valve, operate the lever to depressurize, remove the nozzle and refit the connector saddle.</li>
</ol>
<p>If LPG isn't available, the manual allows bottled nitrogen at an 1800 kPa regulator setting, or compressed air.</p>
""",
faqs=[("What is the part number for a GG20H or GG20DN nose piece?","The GG20 repair manual names only the GG6 nose piece, the single nose piece on the standard GG20. Part numbers for the hybrid and dual nose pieces aren't in that manual; ELAFLEX PACIFIC publishes a separate replacement nose piece document. Quote the full model code (such as GG20DN.3) and serial number when sourcing one."),
      ("At what pressure is a repaired GG20 tested?","The static test in the repair manual uses 1200 to 1800 kPa (12 to 18 bar, 174 to 260 psi) under water, with a 27 N·m bending load on the swivel.")],
sources=["rm","infomat","manual"],
),

dict(
slug="gg20-troubleshooting",
title="GG20 Troubleshooting: Leaks, Hard Connections, No Flow, Stiff Lever",
nav="Troubleshooting",
desc="Symptoms, likely causes and actions for common GasGuard GG20 problems, based on the ELAFLEX operating and repair manuals.",
summary="A small gas release on disconnect is normal (1.7 to 1.9 cm³). A continuous leak is not: release the lever, hit the emergency stop, clear the area and take the nozzle out of service. If the nozzle won't thread on smoothly, disconnect and retry; never force it, and check for a damaged or worn fill point. Low or no flow usually means the coupling isn't fully engaged, a clogged strainer, or a dispenser issue. A pump that won't start on a reed-switch dispenser points to a missing J magnet.",
body="""
<table><thead><tr><th>Symptom</th><th>Likely cause</th><th>What to do</th></tr></thead><tbody>
<tr><td>Short hiss when unscrewing</td><td>Normal release of trapped liquid between nozzle and fill valve</td><td>Nothing. Keep hands clear of the coupling.</td></tr>
<tr><td>Continuous or uncontrolled gas release</td><td>Damaged seal, worn nose piece, damaged fill valve</td><td>Release the lever, press the emergency stop, clear the area. Trained personnel inspect the nozzle and the receptacle. Isolate the nozzle if it recurs.</td></tr>
<tr><td>Nut won't thread on smoothly</td><td>Misalignment, cross-threading, dirty or damaged ACME thread on the fill point</td><td>Disconnect and reconnect square to the valve. Never force it. Inspect both threads.</td></tr>
<tr><td>Leak at the inlet swivel</td><td>Swivel seals worn, grub screw loose</td><td>Out of service. Swivel seals are part of the 6 to 12 month inspection and the 24-month seal kit.</td></tr>
<tr><td>No flow with lever pulled</td><td>Nozzle not fully coupled (the valve won't open uncoupled), pump not running</td><td>Check the nut is fully tightened and the dispenser is running.</td></tr>
<tr><td>Flow lower than usual</td><td>Clogged strainer, pump or hose restriction, adapter in line</td><td>Have the strainer inspected and cleaned or replaced (EK172.1). Remove adaptors if fitted.</td></tr>
<tr><td>Pump doesn't start when nozzle lifted</td><td>Reed-switch boot but nozzle has no magnet</td><td>Fit the J magnet option (GGJ assembly) or change the dispenser setting.</td></tr>
<tr><td>Lever hard to hold</td><td>Normal for single nose piece; or worn lever/valve parts</td><td>Consider the GG20H or GG20DN, which have lower lever force. If force has increased over time, inspect the valve.</td></tr>
<tr><td>Connector nut won't turn freely</td><td>Dirt, worn pawl or spring</td><td>Clean; have the pawl and spring checked at inspection.</td></tr>
</tbody></table>
<p class="note">Rows on "flow lower than usual" and "lever hard to hold" combine ELAFLEX's component descriptions with common service practice; they are not listed word for word in the manual. Everything involving a leak follows the manual's stop-and-isolate instruction.</p>
""",
faqs=[("My GG20 leaks continuously, what should I do?","Release the lever, press the dispenser emergency stop, clear the area, and take the nozzle out of service for inspection by trained personnel.")],
sources=["manual","rm"],
),

dict(
slug="gg20-safety-codes-and-compliance",
title="GG20 Safety, Codes and Compliance: UL 125, NFPA 58, Latches and Rule 1177",
nav="Safety & codes",
desc="What the GasGuard GG20's UL 125 listing covers, why the latch option matters, how the GG20 compares to the Rule 1177 low-emission limit, and LPG hazards to train for.",
summary="The GG20, GG20H and GG20DN are UL listed to UL 125, and ELAFLEX states the GG1/GG20 series meet NFPA 58 among other standards. The optional hold-open latch is not covered by the UL listing and is not allowed everywhere. Release on disconnect is 1.7 to 1.9 cm³, under the 4 cm³ limit that defines a low-emission connector in South Coast AQMD Rule 1177. Your authority having jurisdiction has the final word on any installation.",
body="""
<h2>Listings and standards</h2>
<ul>
<li><strong>UL 125</strong>: GG20, GG20H and GG20DN are listed by Underwriters Laboratories.</li>
<li>ELAFLEX's manual states GG1 and GG20 nozzles meet AS/NZS 1596, NFPA 58, AS/NZS 1425 and EN 12806.</li>
<li>Check for the UL mark on the nozzle you receive, and keep the documentation.</li>
</ul>

<h2>The latch question</h2>
<p>The hold-open latch (L) lets the operator take their hand off the lever. ELAFLEX's data sheet states the latch is not UL listed, and its part-number guide notes that not every country or LPG authority allows one. If a quote lists a latch, decide deliberately, and ask your authority having jurisdiction first.</p>

<h2>Low-emission rules</h2>
<p>South Coast AQMD Rule 1177 (Southern California) has required, since after December 31, 2013, that covered LPG transfers use low-emission connectors, defined as releasing no more than 4 cm³ of LPG on disconnect. The GG20 releases 1.9 cm³ and the GG20H and GG20DN 1.7 cm³. The rule exempts containers under 4 gallons water capacity and cylinders dedicated to recreational vehicles, among others, and requires facilities to keep documentation proving their connectors comply. Other districts may have their own rules.</p>

<h2>ACME versus K15 on new vehicles</h2>
<p>Butane-Propane News reports that NFPA 58 adopted the K15 "Euro" push-to-connect filler as the style vehicle manufacturers must provide on new LPG vehicles from 2020, and that the 2024 edition lets Euro nozzles be used without specific operator training. Forklift cylinders, RVs and many existing vehicles still use 1¾" ACME fill valves, which is the GG20's job. For K15 vehicles, ELAFLEX makes the <a href="/guides/gg40-k15-quick-connect-nozzle">GG40</a>, which is what Propane Nozzle now sells.</p>

<h2>LPG hazards to train for</h2>
<ul>
<li>Stored as a liquid under pressure and heavier than air: it collects in low spots.</li>
<li>Extremely flammable between about 2% and 10% in air.</li>
<li>Extremely cold when it depressurizes: cold burns to skin and eyes. Wear gloves and safety glasses.</li>
<li>Keep ignition sources out of the transfer area: flames, smoking, static, phones and electrical devices.</li>
</ul>
<p>If there is an uncontrolled release, stop the transfer, use the emergency stop, move people away and call emergency services if needed.</p>
""",
faqs=[("Is the GG20 a low-emission connector?","Its release on disconnect is 1.7 to 1.9 cm³, below the 4 cm³ limit that South Coast AQMD Rule 1177 uses to define a low-emission connector."),
      ("Is the GG20 latch UL listed?","No. ELAFLEX states the optional hold-open latch is not covered by the UL listing.")],
sources=["info215","manual","info615","r1177","bpn"],
),

dict(
slug="gg20-dispenser-compatibility",
title="Will a GG20 Work With My Dispenser? Compatibility Checklist",
nav="Dispenser compatibility",
desc="How to tell whether a GasGuard GG20 fits your propane dispenser, hose and fill valves, plus dispensers known to ship for it, including Parafour's P4-100, P4-150 and P4-200.",
summary="A GG20 fits any LPG dispenser whose hose ends in a ½\" or ¾\" NPT male thread and runs within the nozzle's 25 bar (362 psi) rating, as long as the thing being filled has a 1¾\" ACME fill valve. Parafour designs its P4-100, P4-150 and P4-200 dispensers for the GG20. Check three things: the fill valve style, the hose-end thread, and whether the dispenser starts its pump from a reed switch in the nozzle boot (then order the J magnet option).",
body="""
<h2>The three things that decide fit</h2>
<table><thead><tr><th>Check</th><th>GG20 needs</th><th>If it doesn't match</th></tr></thead><tbody>
<tr><td>Fill valve on the vehicle, cylinder or tank</td><td>1¾" ACME thread. The 160 mm reach is for recessed valves such as forklift cylinders and RVs.</td><td>K15 / Euro quick connect: use the GG40 or ZVG 2 EURO UL. Bayonet (EN 12806): GG30. Don't bridge the gap with an adaptor; ELAFLEX advises against fill point adaptors.</td></tr>
<tr><td>Hose end at the nozzle</td><td>½" NPT or ¾" NPT, matching the swivel you order (.2 = ½", .3 = ¾").</td><td>Order the other inlet size rather than adding a reducer, or have the hose assembly made with the right end.</td></tr>
<tr><td>Pump start signal</td><td>Nothing, unless the dispenser senses the nozzle leaving its boot with a reed switch.</td><td>Order the J magnet option so the reed switch can see the nozzle.</td></tr>
</tbody></table>
<p>The GG20 is rated for 25 bar (362 psi) working pressure and LPG only (propane, butane and mixtures). It is UL 125 listed. Your installer and authority having jurisdiction have the final say on any dispenser installation.</p>

<h2>Dispensers known to ship for the GG20</h2>
<h3>Parafour</h3>
<p>Parafour describes three of its dispensers as built for the GasGuard GG20: the <a href="/guides/gg20-parafour-p4-100">P4-100</a> (one autogas hose), the <a href="/guides/gg20-parafour-p4-150">P4-150</a> (one autogas hose plus a cylinder hose) and the <a href="/guides/gg20-parafour-p4-200">P4-200</a> (two autogas hoses). It also lists a single-hose <a href="/guides/gg20-parafour-p4-075">P4-075</a> without a published nozzle spec. Each guide covers which GG20 to order for that unit.</p>
<h3>Gilbarco-based autogas dispensers</h3>
<p>A 2016 Houston-Galveston Clean Cities propane presentation lists a Gilbarco-based autogas dispenser with the ELAFLEX GasGuard GG20 nozzle as standard equipment. Configurations vary by builder, so check the hose-end thread on yours.</p>

<h2>Other dispensers</h2>
<p>If your dispenser isn't named here, check the three items above against its manual or spec sheet. The dispenser maker can confirm the hose-end thread and whether the boot uses a reed switch. Send us the make and model through the <a href="/#quote">quote form</a> and we'll check before you order.</p>

<h2>Filling cylinders from the same dispenser</h2>
<p>Forklift cylinders with 1¾" ACME fill valves are exactly what the GG20's long reach is for, so on a dual-hose unit like the P4-150 the GG20 can serve both jobs. Follow the cylinder-filling sequence in <a href="/guides/how-to-fill-forklift-cylinders-and-rvs-with-gg20">how to fill forklift cylinders and RVs</a>.</p>
""",
faqs=[("Will a GG20 work with a Parafour P4-150?","Yes. Parafour designs the P4-150 for the GasGuard GG20 on its autogas hose. Match the GG20 inlet (½\" or ¾\" NPT) to the hose kit, and ask whether the boot uses a reed switch, which needs the J magnet option."),
      ("Will a GG20 fit my dispenser?","If the hose ends in ½\" or ¾\" NPT, the system stays within 25 bar (362 psi), and you are filling 1¾\" ACME valves, yes. Reed switch boots need the J magnet option. K15 quick-connect vehicles need a GG40 instead."),
      ("Do I need an adaptor to use a GG20 on my dispenser?","No, and ELAFLEX advises against adaptors at the fill point. Choose the inlet size that matches your hose end instead.")],
sources=["p4disp","p4100","p4150","p4200","hcc","info215","manual","cat","bpn"],
),

dict(
slug='gg20-parafour-p4-075',
title='GG20 on the Parafour P4-075 Dispenser',
nav='Parafour P4-075',
desc="Using a GasGuard GG20 nozzle on the Parafour P4-075 single-hose autogas dispenser: what's published, what to check, and which GG20 to order.",
summary='Parafour lists the P4-075 as a single-hose autogas dispenser (its site menu also calls it a slim-line fleet dispenser). Parafour hasn\'t published which nozzle it ships for, so check the unit before ordering: if the vehicles you fill have 1¾" ACME fill valves and the hose ends in ½" or ¾" NPT, a GG20 fits. Vehicles with K15 quick-connect fill valves need a GG40 instead.',
body='<h2>What Parafour publishes</h2>\n<p>Parafour\'s dispenser lineup lists the P4-075 as a single-hose autogas dispenser, and its site navigation also calls it the P4-075 slim-line fleet dispenser. Parafour states that all of its dispensers are ETL listed to UL 495, 1203, 1238 and 913 and NTEP certified under NCWM Handbook 44. We couldn\'t find a published spec sheet that names the P4-075\'s nozzle, hose size or meter, unlike the P4-100, P4-150 and P4-200, which Parafour describes as built for the GasGuard GG20.</p>\n\n<h2>Checking whether a GG20 fits your P4-075</h2>\n<ol>\n<li><strong>Look at the vehicles\' fill valves.</strong> 1¾" ACME: the GG20 fits, and its 160 mm reach handles recessed valves. K15 / Euro quick connect, which newer US autogas vehicles use: you need a GG40 or ZVG 2 EURO UL instead.</li>\n<li><strong>Look at the hose end.</strong> The GG20 swivel comes in ½" NPT (.2) or ¾" NPT (.3).</li>\n<li><strong>Check the nozzle boot.</strong> If lifting the nozzle starts the pump through a reed switch, order the J magnet option.</li>\n</ol>\n<p>If the dispenser already has a nozzle on it, the part number on the nozzle body tells you what was fitted. Send it to us through the <a href="/#quote">quote form</a> and we\'ll match it.</p>\n<h2>Ordering the right GG20</h2>\n<table><thead><tr><th>Choice</th><th>What to pick</th></tr></thead><tbody>\n<tr><td>Nose piece</td><td>GG20 (single) for trained attendants, GG20H (hybrid) for operators filling all day, GG20DN (dual) where the public or untrained staff fill. See <a href="/guides/gg20-vs-gg20h-vs-gg20dn">GG20 vs GG20H vs GG20DN</a>.</td></tr>\n<tr><td>Inlet</td><td>.2 for a ½" NPT hose end, .3 for ¾" NPT. Check the end of the hose kit fitted to your dispenser.</td></tr>\n<tr><td>Magnet (J)</td><td>Only if the nozzle boot uses a reed switch to start the pump. Ask your dispenser supplier.</td></tr>\n<tr><td>Latch (L)</td><td>ELAFLEX notes the hold-open latch is not covered by the UL listing and isn\'t allowed everywhere. Check with your authority having jurisdiction before ordering one.</td></tr>\n</tbody></table>\n<p class="note">Parafour details on this page come from Parafour\'s product pages and distributor listings. Specs change; confirm the current configuration with Parafour or your distributor before you order.</p>\n',
faqs=[('Does the Parafour P4-075 use a GG20?', 'Parafour hasn\'t published the P4-075\'s nozzle. It\'s a single-hose autogas dispenser, so a GG20 fits if your vehicles have 1¾" ACME fill valves and the hose ends in ½" or ¾" NPT. K15 vehicles need a GG40.')],
sources=['p4disp', 'info215', 'manual', 'bpn'],
),

dict(
slug='gg20-parafour-p4-100',
title='GG20 on the Parafour P4-100 Single Hose Autogas Dispenser',
nav='Parafour P4-100',
desc='The Parafour P4-100 single-hose autogas dispenser is built for the GasGuard GG20. Which GG20 to order, inlet size, magnet option and what ships with the dispenser.',
summary='Yes, the GG20 is the nozzle the P4-100 is designed for. Parafour describes the P4-100 as a single-hose autogas dispenser built for the GasGuard GG20 nozzle. Pick the nose piece for who will be filling (GG20, GG20H or GG20DN), match the inlet to the hose end (½" or ¾" NPT), and add the J magnet only if the boot uses a reed switch.',
body='<h2>What Parafour publishes</h2>\n<p>Parafour describes the P4-100 as a single-hose autogas dispenser designed for the GasGuard GG20 nozzle. Its listed features include:</p>\n<ul>\n<li>Meter options: Liqua-Tech LPM102, Neptune 4DMD or Liquid Controls MA4.</li>\n<li>Electronic calibration and automatic temperature compensation as standard.</li>\n<li>Optional receipt printer and fuel management upgrades.</li>\n<li>NTEP certified for installation with NTEP-approved meters and fuel management systems.</li>\n<li>Designed and built to UL 495 / 1238 and NFPA 58 / 30A.</li>\n</ul>\n<p>Distributors list it as the P4-100-L, described as the basic UL-listed single-hose model.</p>\n\n<h2>Where the P4-100 fits</h2>\n<p>One hose means one product: autogas vehicles with 1¾" ACME fill valves. If you also fill forklift or exchange cylinders from the same unit, look at the <a href="/guides/gg20-parafour-p4-150">P4-150</a>, which adds a cylinder hose on the same meter. For two autogas lanes, see the <a href="/guides/gg20-parafour-p4-200">P4-200</a>.</p>\n<h2>Ordering the right GG20</h2>\n<table><thead><tr><th>Choice</th><th>What to pick</th></tr></thead><tbody>\n<tr><td>Nose piece</td><td>GG20 (single) for trained attendants, GG20H (hybrid) for operators filling all day, GG20DN (dual) where the public or untrained staff fill. See <a href="/guides/gg20-vs-gg20h-vs-gg20dn">GG20 vs GG20H vs GG20DN</a>.</td></tr>\n<tr><td>Inlet</td><td>.2 for a ½" NPT hose end, .3 for ¾" NPT. Check the end of the hose kit fitted to your dispenser.</td></tr>\n<tr><td>Magnet (J)</td><td>Only if the nozzle boot uses a reed switch to start the pump. Ask your dispenser supplier.</td></tr>\n<tr><td>Latch (L)</td><td>ELAFLEX notes the hold-open latch is not covered by the UL listing and isn\'t allowed everywhere. Check with your authority having jurisdiction before ordering one.</td></tr>\n</tbody></table>\n<h2>Hose kits are a separate purchase</h2>\n<p>Distributor listings for Parafour\'s -L dispensers show them shipping without hoses or a nozzle kit. One retailer lists a Parafour autogas hose and nozzle kit (HK-0021) with a pull-away and lanyard, an 18" × ¾" LP whip, a ¾" × 12\' delivery hose and a GG20L nozzle (the L is the hold-open latch option). Your dispenser supplier or LP-gas installer supplies and assembles the hose; Propane Nozzle quotes the GG20 nozzle itself.</p>\n<p class="note">Parafour details on this page come from Parafour\'s product pages and distributor listings. Specs change; confirm the current configuration with Parafour or your distributor before you order.</p>\n',
faqs=[('Does the Parafour P4-100 use a GG20 nozzle?', 'Yes. Parafour designs the P4-100 single-hose autogas dispenser for the GasGuard GG20.'), ('Which GG20 should I put on a P4-100?', 'GG20 for trained attendants, GG20H to reduce lever force, GG20DN for public or untrained users. Choose .2 or .3 to match a ½" or ¾" NPT hose end, and add J only for a reed-switch boot.')],
sources=['p4100', 'p4disp', 'p4150l', 'p4kit', 'info215', 'info615', 'manual'],
),

dict(
slug='gg20-parafour-p4-150',
title='GG20 on the Parafour P4-150 Dual Product Dispenser',
nav='Parafour P4-150',
desc='The Parafour P4-150 runs a GasGuard GG20 on its autogas hose and a cylinder fill nozzle on the second hose. Which GG20 to order and what to check.',
summary='Yes. Parafour designs the P4-150 single-meter, dual-hose dispenser for the GasGuard GG20 on its autogas hose, with a separate cylinder fill nozzle on the other hose. A selector switch picks the hose and the two products can be priced separately. The GG20\'s 160 mm reach is also built for forklift cylinders with recessed 1¾" ACME valves.',
body='<h2>What Parafour publishes</h2>\n<p>Parafour calls the P4-150 its most flexible dispenser for propane resellers: one meter, two hoses, one for autogas vehicles and one for cylinder and RV filling. Its listed features include:</p>\n<ul>\n<li>Designed for the GasGuard GG20 autogas nozzle and various cylinder fill nozzles.</li>\n<li>Selector switch between the two hoses, with dual product pricing.</li>\n<li>Meter options: Liqua-Tech LPM102, Neptune 4DMD or Liquid Controls MA4.</li>\n<li>Electronic totalizer and pre-wiring for card readers; can be upgraded to Parafour\'s ParaFUEL POS.</li>\n<li>Optional automatic cylinder filling for safety and overfill prevention, which Parafour says can\'t be combined with ParaFUEL POS.</li>\n<li>Skid, island or remote mounting, and can be placed within 5 ft of other product dispensers under NFPA 58\'s low-emission dispenser provisions.</li>\n<li>Designed and built to UL 495 / 1238 and NFPA 58 / 30A; NTEP certified.</li>\n</ul>\n\n<h2>Which hose gets the GG20</h2>\n<p>The autogas hose. That\'s the hose Parafour designs around the GG20, for vehicles with 1¾" ACME fill valves. The cylinder hose takes whatever cylinder fill nozzle your operation uses. If your cylinders have deep-set 1¾" ACME valves, the GG20 handles those too; see <a href="/guides/how-to-fill-forklift-cylinders-and-rvs-with-gg20">filling forklift cylinders and RVs</a>.</p>\n<h2>Ordering the right GG20</h2>\n<table><thead><tr><th>Choice</th><th>What to pick</th></tr></thead><tbody>\n<tr><td>Nose piece</td><td>GG20 (single) for trained attendants, GG20H (hybrid) for operators filling all day, GG20DN (dual) where the public or untrained staff fill. See <a href="/guides/gg20-vs-gg20h-vs-gg20dn">GG20 vs GG20H vs GG20DN</a>.</td></tr>\n<tr><td>Inlet</td><td>.2 for a ½" NPT hose end, .3 for ¾" NPT. Check the end of the hose kit fitted to your dispenser.</td></tr>\n<tr><td>Magnet (J)</td><td>Only if the nozzle boot uses a reed switch to start the pump. Ask your dispenser supplier.</td></tr>\n<tr><td>Latch (L)</td><td>ELAFLEX notes the hold-open latch is not covered by the UL listing and isn\'t allowed everywhere. Check with your authority having jurisdiction before ordering one.</td></tr>\n</tbody></table>\n<h2>Hose kits are a separate purchase</h2>\n<p>Distributor listings for Parafour\'s -L dispensers show them shipping without hoses or a nozzle kit. One retailer lists a Parafour autogas hose and nozzle kit (HK-0021) with a pull-away and lanyard, an 18" × ¾" LP whip, a ¾" × 12\' delivery hose and a GG20L nozzle (the L is the hold-open latch option). Your dispenser supplier or LP-gas installer supplies and assembles the hose; Propane Nozzle quotes the GG20 nozzle itself.</p>\n<p class="note">Parafour details on this page come from Parafour\'s product pages and distributor listings. Specs change; confirm the current configuration with Parafour or your distributor before you order.</p>\n',
faqs=[('Will a GG20 work with a Parafour P4-150?', 'Yes. Parafour designs the P4-150 for the GasGuard GG20 on its autogas hose. Match the GG20 inlet (½" or ¾" NPT) to the hose end, and add the J magnet only for a reed-switch boot.'), ('Can the P4-150 fill cylinders and vehicles?', 'Yes. It has one meter and two hoses, autogas and cylinder, with a selector switch and separate pricing for each product.')],
sources=['p4150', 'p4disp', 'p4150l', 'p4kit', 'info215', 'info615', 'manual'],
),

dict(
slug='gg20-parafour-p4-200',
title='GG20 on the Parafour P4-200 Dual Hose Autogas Dispenser',
nav='Parafour P4-200',
desc='The Parafour P4-200 dual-hose autogas dispenser is built for the GasGuard GG20 on both hoses. Which GG20 to order for each lane, inlet size and magnet option.',
summary="Yes. Parafour describes the P4-200 as a dual-hose autogas dispenser designed for the GasGuard GG20 nozzle, so you need two GG20 nozzles, one per hose. It's laid out for two fueling lanes. Match the nose piece to who fills each lane: GG20DN where the public fills, GG20 or GG20H where trained staff fill.",
body='<h2>What Parafour publishes</h2>\n<p>Parafour describes the P4-200 as a dual-hose autogas dispenser designed for the GasGuard GG20 nozzle, with lane orientation. Its listed features include:</p>\n<ul>\n<li>Meter options: Liqua-Tech LPM102, Neptune 4DMD or Liquid Controls MA4.</li>\n<li>Electronic totalizer, automatic electronic temperature compensation and solenoid flow control.</li>\n<li>Optional receipt printers and a fuel management upgrade.</li>\n<li>Skid mounting on most distributor-built or locally produced skids, island mounting, or remote mounting.</li>\n<li>NTEP certified; designed and built to UL 495 / 1238 and NFPA 58 / 30A.</li>\n</ul>\n<p>A distributor listing for the P4-200-L shows it shipping without hoses or a nozzle kit.</p>\n\n<h2>Two hoses, two nozzles</h2>\n<p>Each hose needs its own GG20, and they don\'t have to match. If one lane serves the public and the other serves your own fleet, put a GG20DN on the public side and a GG20 or GG20H on the fleet side. Order the inlet size for each hose\'s end thread.</p>\n<h2>Ordering the right GG20</h2>\n<table><thead><tr><th>Choice</th><th>What to pick</th></tr></thead><tbody>\n<tr><td>Nose piece</td><td>GG20 (single) for trained attendants, GG20H (hybrid) for operators filling all day, GG20DN (dual) where the public or untrained staff fill. See <a href="/guides/gg20-vs-gg20h-vs-gg20dn">GG20 vs GG20H vs GG20DN</a>.</td></tr>\n<tr><td>Inlet</td><td>.2 for a ½" NPT hose end, .3 for ¾" NPT. Check the end of the hose kit fitted to your dispenser.</td></tr>\n<tr><td>Magnet (J)</td><td>Only if the nozzle boot uses a reed switch to start the pump. Ask your dispenser supplier.</td></tr>\n<tr><td>Latch (L)</td><td>ELAFLEX notes the hold-open latch is not covered by the UL listing and isn\'t allowed everywhere. Check with your authority having jurisdiction before ordering one.</td></tr>\n</tbody></table>\n<h2>Hose kits are a separate purchase</h2>\n<p>Distributor listings for Parafour\'s -L dispensers show them shipping without hoses or a nozzle kit. One retailer lists a Parafour autogas hose and nozzle kit (HK-0021) with a pull-away and lanyard, an 18" × ¾" LP whip, a ¾" × 12\' delivery hose and a GG20L nozzle (the L is the hold-open latch option). Your dispenser supplier or LP-gas installer supplies and assembles the hose; Propane Nozzle quotes the GG20 nozzle itself.</p>\n<p class="note">Parafour details on this page come from Parafour\'s product pages and distributor listings. Specs change; confirm the current configuration with Parafour or your distributor before you order.</p>\n',
faqs=[('Does the Parafour P4-200 use the GG20?', 'Yes. Parafour designs the P4-200 dual-hose autogas dispenser for the GasGuard GG20, one nozzle per hose.'), ('Do both hoses on a P4-200 need the same GG20?', 'No. Pick the nose piece per lane: GG20DN where the public fills, GG20 or GG20H where trained staff fill.')],
sources=['p4200', 'p4disp', 'p4200l', 'p4kit', 'info215', 'info615', 'manual'],
),

dict(
slug="gasguard-family-gg1-gg20-gg30-gg40",
title="GasGuard Family Compared: GG1, GG20, GG30, GG40 and ZVG 2",
nav="GasGuard family",
desc="Which ELAFLEX LPG nozzle fits which fill point: GG1 and GG20 (1¾\" ACME), GG30 (bayonet), GG40 (K15 quick connect) and ZVG 2 EURO UL, with key specs.",
summary="Pick the nozzle by the fill valve. 1¾\" ACME: GG1 (125 mm reach) for normal fill points, GG20 (160 mm) for recessed ones like forklift cylinders and RVs. Bayonet (EN 12806): GG30. K15 / Euro quick connect used on new US vehicles: GG40, or the ZVG 2 EURO UL. The ACME nozzles share nose piece options (single, hybrid, dual) and ratings.",
body="""
<table><thead><tr><th>Model</th><th>Fill point</th><th>Reach</th><th>Flow</th><th>Release on closure</th><th>Weight</th></tr></thead><tbody>
<tr><td>GG1E / GG1EH / GG1DN</td><td>1¾" ACME</td><td>125 mm</td><td>Up to 63 L/min</td><td>1.9 / 1.7 / 1.7 cm³</td><td>≈1.8 kg</td></tr>
<tr><td><strong>GG20 / GG20H / GG20DN</strong></td><td>1¾" ACME, recessed</td><td>160 mm</td><td>63 / 60 / 60 L/min</td><td>1.9 / 1.7 / 1.7 cm³</td><td>≈2.0 kg</td></tr>
<tr><td>GG30</td><td>Bayonet, EN 12806</td><td>150 mm</td><td>60 L/min</td><td>2.2 cm³</td><td>≈1.9 kg</td></tr>
<tr><td>GG40</td><td>K15 quick connect (US/Canada), push-on</td><td>Up to 17 GPM (≈ 64 L/min)</td><td>&lt; 1 cm³ released; low-effort lever; latched and unlatched both UL approved; EN 13760, UN R 67, ISO 19825</td><td>Latch</td><td>¾" NPT (per distributor listings)</td></tr>
<tr><td>ZVG 2 EURO UL</td><td>Euro push-on, ISO 19825</td><td>n/a</td><td>Up to 50 L/min</td><td>&lt;1 cm³</td><td>≈1.41 kg</td></tr>
</tbody></table>

<h2>GG1 or GG20?</h2>
<p>Same function, same nose pieces, same ratings. The GG20 adds 35 mm to the connector nut. If a GG1 bottoms out on a bracket, cradle or body panel before the threads engage, you need the GG20. If it doesn't, the GG1 is lighter and shorter to handle.</p>

<h2>Where the others fit</h2>
<p>The GG30 serves bayonet fill points and has a 4-slot front and redesigned nose piece; ELAFLEX states it reduces released gas on closure by 23% versus its predecessor. The GG40 is ELAFLEX's nozzle for the US and Canadian K15 quick-connect systems: up to 17 GPM, under 1 cm³ released on disconnect, lighter lever than the ACME nozzles, UL approved latched or unlatched, and it fits the same NB-GG boot. It is the nozzle Propane Nozzle sells; see the <a href="/guides/gg40-k15-quick-connect-nozzle">GG40 overview</a>. The ZVG 2 EURO UL is ELAFLEX's push-on nozzle; latched versions are covered by UL 125 and UL 567.</p>
""",
faqs=[("What is the difference between GasGuard GG1 and GG20?","Connector reach: 125 mm on the GG1 versus 160 mm on the GG20. Everything else, including flow and nose piece options, is the same.")],
sources=["cat","range","info215"],
),

dict(
slug="lg20-to-gg20-replacement",
title="Replacing a GasGuard LG20 with a GG20",
nav="LG20 replacement",
desc="The GasGuard GG20 range supersedes the LG20. What to check before ordering the replacement: nose piece, inlet size, latch and magnet.",
summary="ELAFLEX states the GG20, GG20H and GG20DN supersede the GasGuard LG20 range. To order the right replacement, match four things from the old nozzle: the nose piece (single, hybrid or dual), the inlet thread (½\" or ¾\" NPT female), whether it had a latch, and whether your dispenser needs a magnet for a reed switch. Current GG20s have the strainer fitted as standard.",
body="""
<h2>What changed</h2>
<p>ELAFLEX describes the GG20 design as having improved operational performance and reduced maintenance compared with what it replaced, with a guided connector nut on an extended thread to help alignment and a strainer fitted as standard. The repair manual for the GG20 still uses several LG-series assembly numbers, such as the LG24 valve and LG2 inlet swivel, which suggests some service parts carried over. Confirm specific spare-part compatibility before relying on it.</p>

<h2>Replacement checklist</h2>
<table><thead><tr><th>Check on the old nozzle</th><th>Choose on the GG20</th></tr></thead><tbody>
<tr><td>Who uses it: trained operators or the public?</td><td>GG20 or GG20H for trained operators; GG20DN for public/self-service</td></tr>
<tr><td>Hose end thread</td><td>.2 for ½" NPT female, .3 for ¾" NPT female</td></tr>
<tr><td>Hold-open latch fitted?</td><td>L option, not UL listed; check your AHJ</td></tr>
<tr><td>Dispenser starts on lifting the nozzle via reed switch?</td><td>J magnet option</td></tr>
<tr><td>Boot</td><td>NB-GG holds GasGuard nozzles</td></tr>
</tbody></table>
<p>Send a photo of the old nozzle's label with your quote request and we'll match it.</p>
""",
faqs=[("What replaced the GasGuard LG20?","The GG20 range: GG20, GG20H and GG20DN.")],
sources=["info215","rm","info615"],
),

dict(
slug="gg20-glossary",
title="LPG Nozzle Glossary: Terms Used in GG20 Documentation",
nav="Glossary",
desc="Plain definitions of the terms in GasGuard GG20 specs and manuals: ACME, nose piece, release volume, reach, swivel, reed switch, safety break, AHJ, UL 125, K15.",
summary="Short definitions of the terms used across GasGuard GG20 documentation, from 1¾\" ACME and nozzle reach to release volume, nose piece types, reed switches, safety breaks and UL 125.",
body="""
<dl>
<dt>1¾" ACME</dt><dd>The threaded LPG fill connection common on North American forklift cylinders, RVs and older autogas vehicles. The GG20's connector nut screws onto it.</dd>
<dt>Nozzle reach</dt><dd>Length of the connector nut. 160 mm on the GG20, 125 mm on the GG1.</dd>
<dt>Nose piece</dt><dd>The sealing front of the valve. Single ('E'), hybrid ('H') or dual ('DN') on GasGuard ACME nozzles.</dd>
<dt>Dual nose piece</dt><dd>ELAFLEX's patented design that seals to the fill point even if the nozzle isn't fully tightened. Used on the GG20DN.</dd>
<dt>Release volume</dt><dd>LPG vented when the nozzle is disconnected: the liquid trapped between nozzle valve and fill valve. 1.7 to 1.9 cm³ on the GG20 range.</dd>
<dt>Low-emission connector</dt><dd>Under South Coast AQMD Rule 1177, a connector releasing no more than 4 cm³ on disconnect.</dd>
<dt>Inlet swivel</dt><dd>The rotating joint where the hose attaches. ½" or ¾" NPT female on the GG20.</dd>
<dt>NPT</dt><dd>National Pipe Taper, the US tapered pipe thread standard.</dd>
<dt>Strainer</dt><dd>300 µm / 50 mesh screen inside the nozzle that stops debris from upstream.</dd>
<dt>Hold-open latch</dt><dd>A catch that holds the lever open. Optional (L) and not UL listed on the GG20.</dd>
<dt>Reed switch / magnet</dt><dd>Some dispensers start the pump when a magnet in the nozzle guard leaves a reed switch in the boot. Order option J for these.</dd>
<dt>Nozzle boot (NB-GG)</dt><dd>The enclosed holster for GasGuard nozzles on the dispenser.</dd>
<dt>Safety break / pull-away (ARK 19)</dt><dd>A coupling in the hose that separates and seals if a vehicle drives off while connected.</dd>
<dt>UL 125</dt><dd>The Underwriters Laboratories standard covering flow control valves for anhydrous ammonia and LP-gas, under which the GG20 is listed.</dd>
<dt>NFPA 58</dt><dd>The Liquefied Petroleum Gas Code published by the National Fire Protection Association, adopted by most US states.</dd>
<dt>AHJ</dt><dd>Authority having jurisdiction: the agency or official who approves an installation.</dd>
<dt>K15 / Euro connector</dt><dd>Push-to-connect LPG filler adopted under NFPA 58 for new vehicles. Served by the GG40 or ZVG 2, not the GG20.</dd>
</dl>
""",
faqs=[],
sources=["info215","info615","r1177","bpn"],
),
]
