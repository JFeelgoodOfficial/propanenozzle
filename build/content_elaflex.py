# ELAFLEX reference guides: hoses, pull-aways, boots, sleeves, nozzle guards and the ZVG 2 nozzles.
# Reference only: Propane Nozzle sells the GG40 and GG40 hose kits, not these parts on their own.
# Every figure below was read from the ELAFLEX catalogue pages hosted under /docs/. Numbers described as
# "read from the chart" are approximations taken off a printed curve, not tabulated values.
# content.py imports ELAFLEX_SRC and ELAFLEX_ARTICLES from here.

ELAFLEX_UPDATED = "2026-11-11"

D116 = "/docs/ELAFLEX_CatPage116_LPG16_Autogas_Hoses.pdf"
D561 = "/docs/ELAFLEX_CatPage561-564_ZVG2_ARK19.pdf"
D567 = "/docs/ELAFLEX_CatPage567-574_GasGuard_ZVG2_EURO_UL_K.pdf"

ELAFLEX_SRC = {
 "cat116": ("ELAFLEX catalogue page 116: LPG 16 S / LPG 16 autogas hoses (hose marking example dated 4Q-21)", "https://propanenozzle.com" + D116),
 "cat561": ("ELAFLEX catalogue pages 561-562: LPG nozzle ZVG 2 and spare parts, rev. 7.2025", "https://propanenozzle.com" + D561),
 "cat563": ("ELAFLEX catalogue pages 563-564: safety break ARK 19, LPG 16 hose and couplings, rev. 11.2022", "https://propanenozzle.com" + D561),
 "cat567": ("ELAFLEX catalogue pages 567-574: GasGuard GG1, GG20, GG30, ZVG 2 EURO UL and ZVG 2 K, rev. 11.2022", "https://propanenozzle.com" + D567),
}

# Documents listed on the library page: (title, what it answers, link, converted guide slug or None, hosted here?)
LIBRARY = [
 ("GasGuard GG40 brochure", "ELAFLEX PACIFIC, 2025. Features and technical information for the K15 quick-connect nozzle; the hanging-hardware set with ARK 19.3 and LPG 16 S hose.", "/docs/ELAFLEX_Pacific_GG40.pdf", "gg40-k15-quick-connect-nozzle", True),
 ("Catalogue page 116: LPG 16 S / LPG 16 autogas hoses", "ELAFLEX. Hose dimensions, pressures, bend radius, construction, markings, pressure-drop chart and the complete dispenser kit drawing.", D116, "elaflex-lpg-16-autogas-hoses", True),
 ("Catalogue pages 561-564: LPG nozzle ZVG 2 and safety break ARK 19", "ELAFLEX, rev. 7.2025 (page 561) and 11.2022 (page 563). ZVG 2 ACME, DISH and EURO part numbers, spare-parts drawing, ARK 19 specification and part numbers, hose couplings, pressure-drop chart.", D561, "elaflex-ark-19-safety-break-pull-away", True),
 ("Catalogue pages 567-574: GasGuard nozzles, ZVG 2 EURO UL and ZVG 2 K", "ELAFLEX, rev. 11.2022. GG1, GG20 and GG30 specifications and options, the UL-listed ZVG 2 EURO UL and the ZVG 2 K, pressure-drop chart, accessory drawings.", D567, "gasguard-family-gg1-gg20-gg30-gg40", True),
 ("GasGuard Information 2.15: GG20 nozzle range", "ELAFLEX, October 2015. The GG20, GG20H and GG20DN.", "https://elaflex.com.au/dokumente/subsidiaries/au/Information/GasGuard_Information_2.15.pdf", "gg20-vs-gg20h-vs-gg20dn", False),
 ("GasGuard Information 6.15: part number breakdown", "ELAFLEX. How GasGuard order codes are built.", "https://elaflex.com.au/dokumente/subsidiaries/au/Information/GasGuard_Information_6.15.pdf", "gg20-part-numbers-and-options", False),
 ("Installation and Operating Manual, GG1 and GG20 series", "ELAFLEX PACIFIC, 5/2016. Installation, thread sealing, operation.", "https://elaflex.com.au/dokumente/subsidiaries/au/Manuals/GasGuard_Manual_GG1_GG20_Installation_Operation_EN.pdf", "gg20-installation-and-hose-assembly", False),
 ("GG20 Repair and Maintenance Manual", "ELAFLEX PACIFIC / L.G. Equipment. Seal kits, strip-down, testing.", "https://elaflex.com.au/dokumente/subsidiaries/au/Manuals/GG20-RM.pdf", "gg20-repair-and-testing", False),
 ("ELAFLEX US Information 1.19: LPG-UL hose assemblies", "ELAFLEX US. The UL 21 / CSA 8.1 hose assemblies for the US and Canada.", "https://elaflexus.com/downloads/lpg-refueling/lpg-hose-assemblies/ELAFLEX_US_Information_1.19.pdf", "autogas-hose-kits", False),
 ("ARK 19 / ARK 19 SS safety break manual", "ELAFLEX. Installation and operation of the pull-away.", "https://elaflex.de/dokumente/download/Manual/Manual_ARK19_ARK19SS.pdf", "elaflex-ark-19-safety-break-pull-away", False),
]

NOTE = '<p class="note">Converted from the ELAFLEX catalogue page linked under Sources. Tables keep ELAFLEX\'s figures and units; where a number is read off a printed chart we say so. Catalogue data describes ELAFLEX\'s international range and is subject to change without notice. Propane Nozzle is an independent reseller and quotes the GG40 and GG40 hose kits; this page is reference.</p>'

ELAFLEX_ARTICLES = [

dict(
slug="elaflex-lpg-16-autogas-hoses",
product="ref",
updated=ELAFLEX_UPDATED,
title="ELAFLEX LPG 16 S and LPG 16 Autogas Hoses: Specifications, Markings and Pressure Drop",
nav="LPG 16 hoses",
desc="ELAFLEX catalogue page 116 as a web page: LPG 16 S and LPG 16 dispenser hose dimensions, 25 bar working pressure, 80 mm bend radius, temperature range, construction, hose markings and pressure drop.",
summary="LPG 16 S and LPG 16 are ELAFLEX's dispenser hoses for propane, butane and their mixtures, built to EN 1762. Both have a 16 mm (5/8\") bore and a 26 mm outside diameter, weigh about 0.5 kg per metre, and are rated 25 bar working pressure, 40 bar test pressure, burst above 100 bar, with an 80 mm bend radius. LPG 16 S is the standard type, rated -30 °C to +70 °C with very low permeation. LPG 16 has a pricked cover and is rated -40 °C to +70 °C, which makes it the cold-region type.",
body="""
<h2>Dimensions and ratings</h2>
<table><thead><tr><th></th><th>LPG 16 S</th><th>LPG 16</th></tr></thead><tbody>
<tr><th>Inside diameter</th><td colspan="2">16 mm (5/8")</td></tr>
<tr><th>Outside diameter</th><td colspan="2">≈ 26 mm</td></tr>
<tr><th>Weight</th><td colspan="2">≈ 0.5 kg/m</td></tr>
<tr><th>Working pressure</th><td colspan="2">25 bar (PN 25)</td></tr>
<tr><th>Test pressure</th><td colspan="2">40 bar</td></tr>
<tr><th>Burst pressure</th><td colspan="2">Above 100 bar</td></tr>
<tr><th>Vacuum</th><td colspan="2">0.5 bar</td></tr>
<tr><th>Bend radius</th><td colspan="2">80 mm</td></tr>
<tr><th>Coil length</th><td colspan="2">≈ 40 m, 80 m maximum</td></tr>
<tr><th>Temperature range</th><td>-30 °C to +70 °C</td><td>-40 °C to +70 °C</td></tr>
<tr><th>Cover</th><td>Smooth</td><td>Pricked</td></tr>
<tr><th>Colours</th><td colspan="2">Black, or orange</td></tr>
<tr><th>Standard and approvals</th><td colspan="2">Meets EN 1762. DVGW approved (No. DG-4621 AU 0049) and AS 1869 approved.</td></tr>
<tr><th>Media</th><td colspan="2">Propane, butane and their mixtures</td></tr>
</tbody></table>
<p>The 5/8" figure is the hose bore. Autogas hose assemblies are usually described by their end thread, which is why a kit built on this hose with ¾" NPT fittings is sold as a ¾" kit.</p>

<h2>Which type</h2>
<dl>
<dt>LPG 16 S</dt><dd>ELAFLEX calls it the new standard dispensing hose for autogas, suitable for most applications. The lining is plasticiser-free and highly flexible, with very low permeation and what ELAFLEX describes as optimal purity of the medium (it refers to its Information 3.16 for detail). This is the hose ELAFLEX pairs with the GasGuard GG40.</dd>
<dt>LPG 16</dt><dd>Also plasticiser-free and highly flexible. ELAFLEX singles out the black version as highly cold flexible and therefore suited to cold regions. It has a pricked cover.</dd>
</dl>

<h2>Construction</h2>
<table><tbody>
<tr><th>Lining</th><td>NBR, black, seamlessly extruded, electrically dissipative, low permeation, plasticiser-free</td></tr>
<tr><th>Reinforcement</th><td>Low-stretch textile braids with crossed tinned copper strands that can be electrically connected</td></tr>
<tr><th>Cover</th><td>CR (chloroprene), black or orange, smooth, abrasion resistant, highly ageing resistant. Type LPG 16 is pricked.</td></tr>
</tbody></table>

<h2>Reading the hose marking</h2>
<p>Both hoses carry a continuous, abrasion-resistant embossed marking. ELAFLEX's examples:</p>
<table><tbody>
<tr><th>LPG 16 S</th><td>ELAFLEX · LPG 16 S · EN 1762 D · AS 1869 · Ω · PN 25 · M · MADE IN GERMANY · 4Q-21</td></tr>
<tr><th>LPG 16</th><td>ELAFLEX · LPG 16 · EN 1762 D · -40 °C · Ω · PN 25 · M · MADE IN GERMANY · 4Q-21</td></tr>
</tbody></table>
<p>The marking names the hose type, the standard (EN 1762, type D), the pressure rating (PN 25 is 25 bar) and ends with a quarter-and-year stamp, 4Q-21 in the example. The -40 °C mark appears on LPG 16 only.</p>

<h2>Pressure drop</h2>
<p>ELAFLEX plots pressure drop for 5 m hose assemblies in DN 13 to DN 19, measured with Isopar. Values below are read from the printed chart and are approximate.</p>
<table><thead><tr><th>Hose</th><th>Pressure drop at 50 L/min, 5 m assembly</th></tr></thead><tbody>
<tr><td>LPG 13</td><td>About 2 bar</td></tr>
<tr><td>LPG 16 S and LPG 16</td><td>About 0.7 bar (the two share one curve)</td></tr>
<tr><td>LPG 19</td><td>About 0.15 bar</td></tr>
</tbody></table>
<p>The step from a 13 mm to a 16 mm bore cuts the loss by roughly two thirds at the same flow, which is the argument for a 16 mm hose on a dispenser filling at autogas rates.</p>

<h2>Where the hose sits in the dispenser kit</h2>
<p>The same catalogue page draws the complete kit for an LPG dispenser: the nozzle, a colour sleeve and an anti-kink sleeve at the nozzle end of the hose, the delivery hose, an ARK 19 safety break, a short connection hose with a reusable or non-reusable coupling, and a nozzle boot on the dispenser. Each part has its own guide: <a href="/guides/elaflex-ark-19-safety-break-pull-away.html">ARK 19 pull-away</a> and <a href="/guides/lpg-dispenser-kit-boots-sleeves-and-nozzle-guards.html">boots, sleeves and nozzle guards</a>. For the kit we quote with the GG40, see <a href="/guides/autogas-hose-kits.html">autogas hose kits</a>.</p>

<h2>US hose assemblies</h2>
<p>Catalogue page 116 describes the hose as ELAFLEX sells it internationally. For the US and Canada ELAFLEX US publishes a separate sheet, Information 1.19, covering its UL 21 / CSA 8.1 hose assemblies; figures from that sheet are quoted on the <a href="/guides/autogas-hose-kits.html">hose kit guide</a>. Where the two differ, the UL sheet governs a US installation.</p>
""" + NOTE,
faqs=[("What size is ELAFLEX LPG 16 hose?", "16 mm (5/8\") inside diameter and about 26 mm outside diameter, weighing about 0.5 kg per metre, per ELAFLEX catalogue page 116."),
      ("What is the pressure rating of LPG 16 S hose?", "25 bar working pressure (PN 25), 40 bar test pressure and burst pressure above 100 bar, per ELAFLEX catalogue page 116."),
      ("What is the difference between LPG 16 and LPG 16 S?", "LPG 16 S is the standard type with very low permeation, rated -30 °C to +70 °C, with a smooth cover. LPG 16 has a pricked cover and is rated -40 °C to +70 °C; ELAFLEX recommends the black version for cold regions."),
      ("What is the minimum bend radius of LPG 16 hose?", "80 mm for both LPG 16 S and LPG 16, per ELAFLEX catalogue page 116."),
      ("What do the markings on an ELAFLEX LPG hose mean?", "Hose type, EN 1762 type D, PN 25 (25 bar), country of manufacture and a quarter-and-year stamp such as 4Q-21. LPG 16 also carries -40 °C.")],
sources=["cat116", "cat563", "lpgul"],
),

dict(
slug="elaflex-ark-19-safety-break-pull-away",
product="ref",
updated=ELAFLEX_UPDATED,
title="ELAFLEX ARK 19 Safety Break (Pull-Away): Specifications, Part Numbers and Hose Couplings",
nav="ARK 19 pull-away",
desc="ELAFLEX catalogue page 563 as a web page: the ARK 19 LPG safety break. 200 to 500 N separation, EN 14678-1, 25 bar, part numbers ARK 19.3, 19.M30 and SS versions, BS 19 break sleeve, hose couplings.",
summary="The ARK 19 is ELAFLEX's DN 19 safety break for LPG dispenser hoses, called a pull-away or break-away in the US. It sits between a short connection hose and the long delivery hose, separates at an axial pull of 200 to 500 N in line with EN 14678-1, closes both halves automatically, and can be pushed back together under pressure without tools. It is rated 25 bar working pressure for propane and butane up to 50 L/min, -25 °C to +70 °C, and weighs about 1.05 kg. The ARK 19.3 is the version with ¾\" NPT female threads.",
body="""
<h2>What it does</h2>
<p>If a vehicle drives off with the nozzle still connected, the hose pulls on the coupling until it parts. Both halves have self-closing check valves, so the dispenser side and the hose side each seal as they separate; ELAFLEX states the escape of gas is minimal. The coupling is not sacrificial: it can be reassembled under pressure, by hand, without tools.</p>

<h2>Specification</h2>
<table><tbody>
<tr><th>Size</th><td>DN 19, for LPG hoses</td></tr>
<tr><th>Media and flow</th><td>Propane and butane, up to 50 L/min</td></tr>
<tr><th>Working pressure</th><td>25 bar maximum</td></tr>
<tr><th>Test pressure</th><td>40 bar</td></tr>
<tr><th>Burst pressure</th><td>Above 100 bar</td></tr>
<tr><th>Temperature range</th><td>-25 °C to +70 °C</td></tr>
<tr><th>Separation force</th><td>Axial pull of 200 N up to 500 N, corresponding to EN 14678-1</td></tr>
<tr><th>Standards</th><td>Self-closing check valves on both ends according to EN 14678-1 and German safety rules (TRG 404)</td></tr>
<tr><th>Certificate</th><td>TÜV.ST. BCD.007-06</td></tr>
<tr><th>Body</th><td>Bronze, or stainless steel on the ARK 19 … SS, with pressurised parts of brass</td></tr>
<tr><th>Internals</th><td>Stainless steel balls, acetal resin poppet assembly, NBR seals</td></tr>
<tr><th>Break sleeve</th><td>BS 19, polyurethane</td></tr>
<tr><th>Lanyard</th><td>Stainless steel, for fastening at the stanchion or pump; cable length ≈ 300 mm, other lengths on request</td></tr>
<tr><th>Weight</th><td>≈ 1.05 kg</td></tr>
<tr><th>Size</th><td>≈ 98 mm long in bronze, ≈ 111 mm in stainless with M 30 thread; 56 mm diameter (68 mm maximum)</td></tr>
</tbody></table>

<h2>Part numbers</h2>
<table><thead><tr><th>Part number</th><th>Thread</th><th>Body</th></tr></thead><tbody>
<tr><td><strong>ARK 19.3</strong></td><td>¾" NPT female</td><td>Bronze</td></tr>
<tr><td>(ARK 19.4)</td><td>G ¾ BSP female</td><td>Bronze</td></tr>
<tr><td>ARK 19.M30</td><td>M 30 × 1.5 L male (L = left-hand thread)</td><td>Bronze</td></tr>
<tr><td>ARK 19.3 SS</td><td>¾" NPT female</td><td>Stainless steel</td></tr>
<tr><td>ARK 19.M30 SS</td><td>M 30 × 1.5 L male (left-hand thread)</td><td>Stainless steel</td></tr>
</tbody></table>
<p>The ¾" NPT version, ARK 19.3, is the one ELAFLEX names in its GG40 brochure as the pull-away for the US and Canadian hanging-hardware set. ELAFLEX prints ARK 19.4 in brackets in the catalogue.</p>

<h2>Where it goes</h2>
<p>ELAFLEX's rule is that the ARK is assembled between a short connection hose and the long LPG hose. The catalogue drawing shows a connection hose of 0.3 to 1.0 m on the dispenser side and a delivery hose of 3 to 5 m on the nozzle side, with the BS 19 break sleeve over the coupling. The lanyard fastens to the stanchion or pump so that the pull lands on the coupling instead of the dispenser pipework.</p>

<h2>Pressure drop</h2>
<p>ELAFLEX's chart, measured with Isopar, puts the ARK 19 at roughly 0.4 bar at 50 L/min (read from the printed curve). The same chart shows the ZVG 2 nozzle at about 1 bar at 30 L/min and about 3 bar near 48 L/min, so the coupling is a small part of the total loss.</p>

<h2>Flow rating and the GG40</h2>
<p>The catalogue page (revision 11.2022) rates the ARK 19 for up to 50 L/min. ELAFLEX's 2025 GG40 brochure pairs the ARK 19.3 with the GG40, which it rates at up to 17 GPM, about 64 L/min. The two documents do not reconcile those figures. If your dispenser is sized near the top of the GG40's range, ask for the current ARK 19.3 data sheet with your quote.</p>

<h2>Hose couplings on the same page</h2>
<p>Page 563 also lists the brass ferrule-type couplings ELAFLEX fits to LPG 16 hose. They are suitable for self-assembly, rated up to 25 bar and meet EN 14424.</p>
<table><thead><tr><th>Part number</th><th>Thread</th><th>Type</th><th>Weight</th></tr></thead><tbody>
<tr><td>V 16-¾" NPT</td><td>¾" NPT male</td><td>Type V: hose tail and ferrule of brass</td><td>≈ 0.16 kg</td></tr>
<tr><td>V 16-1"</td><td>G 1 BSP male</td><td>Type V</td><td>≈ 0.17 kg</td></tr>
<tr><td>M 16-30 LPG</td><td>M 30 × 1.5 L female (left-hand thread)</td><td>Type M: hose tail, union nut and ferrule of brass, captive polyurethane seal</td><td>≈ 0.17 kg</td></tr>
</tbody></table>

<h2>After a drive-off</h2>
<p>The catalogue says the ARK can be reassembled under pressure without tools; it does not give an inspection procedure. Before reconnecting, a qualified LP-gas technician should check both halves, the hose, the nozzle and the dispenser connection for damage, and follow ELAFLEX's ARK 19 manual and your site procedure.</p>
""" + NOTE,
faqs=[("At what force does the ELAFLEX ARK 19 separate?", "At an axial pull of 200 N up to 500 N, corresponding to EN 14678-1, per ELAFLEX catalogue page 563."),
      ("What is the ARK 19.3?", "The ARK 19 safety break with ¾\" NPT female threads and a bronze body. ARK 19.3 SS is the stainless steel version. ELAFLEX names the ARK 19.3 as the pull-away for its GG40 hanging-hardware set."),
      ("Can an ARK 19 be reused after a drive-off?", "Yes. ELAFLEX states it can be reassembled under pressure without tools. Have a qualified technician inspect the coupling, hose and nozzle before reconnecting."),
      ("Where is the pull-away installed on an LPG dispenser hose?", "Between a short connection hose on the dispenser side and the long delivery hose, with the lanyard fastened to the stanchion or pump."),
      ("What is the pressure rating of the ARK 19?", "25 bar maximum working pressure, 40 bar test pressure and burst above 100 bar, for propane and butane up to 50 L/min.")],
sources=["cat563", "gg40br", "ark19"],
),

dict(
slug="lpg-dispenser-kit-boots-sleeves-and-nozzle-guards",
product="ref",
updated=ELAFLEX_UPDATED,
title="LPG Dispenser Kit Parts: NB-GG Nozzle Boot, Sleeves and Nozzle Guards",
nav="Boots, sleeves & guards",
desc="The small parts in ELAFLEX's LPG dispenser kit: NB-GG and NB-ZVG nozzle boots, KS 16 anti-kink sleeve, CS 16 colour sleeve, BS 19 break sleeve, and the guard options: magnet, splashguard and scuffguard.",
summary="ELAFLEX draws the same kit around every LPG nozzle: a nozzle boot on the dispenser (NB-GG for GasGuard nozzles, NB-ZVG for ZVG nozzles), a KS 16 anti-kink sleeve and a CS 16 colour sleeve at the nozzle end of the hose, and a BS 19 break sleeve over the ARK 19 safety break. Three nozzle options are described as guards: a magnet built into the nozzle guard for reed-switch dispensers, a soft PVC splashguard on the GasGuard ACME and bayonet nozzles, and the EA 866 scuffguard on ZVG 2 nozzles. The GG40 fits the existing NB-GG boot.",
body="""
<h2>The kit, part by part</h2>
<table><thead><tr><th>Part</th><th>ELAFLEX name</th><th>What it is for</th><th>Catalogue reference</th></tr></thead><tbody>
<tr><td>Nozzle boot</td><td>NB-GG</td><td>Holster on the dispenser for GasGuard nozzles</td><td>Pages 116, 568</td></tr>
<tr><td>Nozzle boot</td><td>NB-ZVG</td><td>Holster for ZVG 2 and ZVG 1 nozzles, and nozzles of other manufacturers</td><td>Pages 116, 564</td></tr>
<tr><td>Anti-kink sleeve</td><td>KS 16</td><td>Supports the hose where it leaves the nozzle</td><td>Page 211</td></tr>
<tr><td>Colour sleeve</td><td>CS 16 orange</td><td>Coloured sleeve at the nozzle end of the hose</td><td>Page 211</td></tr>
<tr><td>Break sleeve</td><td>BS 19</td><td>Polyurethane sleeve over the ARK 19 safety break</td><td>Page 563</td></tr>
<tr><td>Safety break</td><td>ARK 19</td><td>Pull-away, reconnectable under pressure</td><td>Page 563</td></tr>
<tr><td>Hose couplings</td><td>Type V, Type M</td><td>Reusable or non-reusable hose ends</td><td>Pages 203, 205, 563</td></tr>
<tr><td>Hose</td><td>LPG 16 S / LPG 16</td><td>Dispenser hose</td><td>Page 116</td></tr>
</tbody></table>
<p>Pages 211, 203 and 205 are in sections of the ELAFLEX catalogue we have not converted, so dimensions and order codes for the sleeves and the boots are not given here. Ask for them with a quote if you need them.</p>

<h2>Nozzle boots</h2>
<p>A boot is the enclosed holster the nozzle hangs in between fills. ELAFLEX makes two for LPG: the NB-GG for GasGuard nozzles and the NB-ZVG for the ZVG 2 and ZVG 1, which ELAFLEX says also takes nozzles of other manufacturers. In its GG40 brochure ELAFLEX states the GG40 is compatible with the existing NB-GG boot, so a dispenser already set up for a GasGuard ACME nozzle keeps its boot when it moves to K15.</p>

<h2>Guards: three different things</h2>
<p>ELAFLEX uses the word guard for three unrelated options. All three are factory options on the nozzle, ordered by a suffix on the part number.</p>
<table><thead><tr><th>Option</th><th>Nozzles</th><th>Code</th><th>What ELAFLEX says it does</th></tr></thead><tbody>
<tr><td>Magnet in the nozzle guard</td><td>GasGuard GG1, GG20, GG30</td><td>J</td><td>Contactless activation of dispensers with reed-switch technology. The magnet is built into the lever guard.</td></tr>
<tr><td>Magnet in the nozzle guard</td><td>ZVG 2, ZVG 2 EURO UL, ZVG 2 K</td><td>M</td><td>Contactless activation of the pump by reed contacts</td></tr>
<tr><td>Splashguard</td><td>GasGuard GG1, GG20, GG30</td><td>G</td><td>Soft PVC, orange. Protects the user's hands against any gas release after the nozzle valve has shut.</td></tr>
<tr><td>Scuffguard</td><td>ZVG 2 (ACME, DISH, EURO), ZVG 2 EURO UL, ZVG 2 K</td><td>EA 866 plus colour</td><td>Black or orange cover with fuel grade identification 'LPG' to EN 16942 and a large printing space. Materials PU / PA, weather and deformation resistant.</td></tr>
</tbody></table>
<p>ELAFLEX prints the splashguard code G on the GG30 page; the GG1 and GG20 pages list the same splashguard without repeating the letter there. On the ZVG 2 the scuffguard is EA 866 … AD for ACME and DISH and EA 866 … EK for EURO; on the ZVG 2 EURO UL and ZVG 2 K it is EA 866 E. ELAFLEX points to its Information 4.17 for scuffguard detail.</p>

<h2>Reed-switch dispensers and the GG40</h2>
<p>Some dispensers start the pump when a reed switch in the boot senses a magnet in the nozzle. The catalogue lists a magnet option for every GasGuard ACME and bayonet nozzle and for the ZVG 2 range. ELAFLEX has not yet published whether the GG40 has one. If your boot works that way, say so when you ask for a quote and we will confirm it before you order.</p>

<h2>Other GasGuard options on the same pages</h2>
<ul>
<li><strong>Hold-open latch (L):</strong> assists the user in holding the lever during refuelling. On the GG30 the latch is red anodised aluminium.</li>
<li><strong>Special connector:</strong> a hard anodised alloy connector with a brass, non-guided ACME thread insert, on the GG1 and GG20.</li>
</ul>
""" + NOTE,
faqs=[("What is the ELAFLEX NB-GG?", "The nozzle boot for GasGuard nozzles: the holster the nozzle hangs in on the dispenser. ELAFLEX states the GG40 is compatible with the existing NB-GG boot."),
      ("What is the difference between the NB-GG and NB-ZVG nozzle boots?", "NB-GG is for GasGuard nozzles. NB-ZVG is for the ZVG 2 and ZVG 1, and ELAFLEX says it also takes nozzles of other manufacturers."),
      ("What is the KS 16?", "ELAFLEX's anti-kink sleeve for 16 mm LPG dispenser hose, fitted where the hose leaves the nozzle. It is listed on catalogue page 211."),
      ("What does the magnet in the nozzle guard do?", "It lets a reed switch in the dispenser sense the nozzle and start the pump without contact. The option code is J on GasGuard ACME and bayonet nozzles and M on ZVG 2 nozzles."),
      ("What is a GasGuard splashguard?", "An orange soft PVC guard that protects the user's hands against any gas release after the nozzle valve has shut. It is an option on the GG1, GG20 and GG30."),
      ("What is the EA 866 scuffguard?", "A black or orange PU / PA cover for ZVG 2 nozzles that carries the LPG fuel grade identification to EN 16942 and a printing space.")],
sources=["cat116", "cat563", "cat567", "cat561", "gg40br"],
),

dict(
slug="elaflex-zvg-2-lpg-nozzles",
product="ref",
updated=ELAFLEX_UPDATED,
title="ELAFLEX ZVG 2 LPG Nozzles: ACME, DISH, EURO, EURO UL and K Compared",
nav="ZVG 2 nozzles",
desc="ELAFLEX catalogue pages 561 and 573 as a web page: ZVG 2 ACME, DISH and EURO, the UL-listed ZVG 2 EURO UL and the ZVG 2 K. Ratings, weights, gas release, part numbers, options and pressure drop.",
summary="The ZVG 2 is ELAFLEX's modular LPG vehicle nozzle: one body with interchangeable couplings. ACME (1¾\" thread), DISH (Italian claw) and EURO (push-in, EN 13760) versions flow up to 50 L/min at 25 bar. The ZVG 2 EURO UL is the UL-listed push-in nozzle to ISO 19825, weighing about 1.41 kg and releasing under 1 cm³; latched versions are covered by UL 125 and UL 567. The ZVG 2 K is a second push-in version at about 1.55 kg. Propane Nozzle does not sell the ZVG 2; for K15 vehicles we sell the GasGuard GG40.",
body="""
<h2>The five versions</h2>
<table><thead><tr><th>Version</th><th>Coupling</th><th>Gas release</th><th>Weight</th><th>Temperature</th></tr></thead><tbody>
<tr><td>ZVG 2 ACME</td><td>1¾" ACME threaded coupling, for vehicle connections to EN 12806</td><td>≈ 1.7 cm³</td><td>≈ 1.5 kg</td><td>-25 °C to +70 °C; LT type to -40 °C</td></tr>
<tr><td>ZVG 2 DISH</td><td>'Italian' claw coupling to EN 12806; one-handed operation possible</td><td>&lt; 1 cm³</td><td>≈ 1.2 kg</td><td>-25 °C to +70 °C; LT type to -40 °C</td></tr>
<tr><td>ZVG 2 EURO</td><td>Push-in coupling to EN 13760; one-handed operation possible</td><td>&lt; 1 cm³</td><td>≈ 1.4 kg</td><td>-25 °C to +70 °C; LT type to -40 °C</td></tr>
<tr><td>ZVG 2 EURO UL</td><td>Push-in coupling to ISO 19825; UL listed</td><td>&lt; 1 cm³</td><td>≈ 1.41 kg</td><td>-40 °C to +70 °C</td></tr>
<tr><td>ZVG 2 K</td><td>Push-in coupling with a brass and PA coupling slider</td><td>&lt; 1 cm³</td><td>≈ 1.55 kg</td><td>-40 °C to +70 °C</td></tr>
</tbody></table>
<p>All five share the same ratings: liquefied petroleum gas (propane, butane and mixtures) up to 50 L/min, 25 bar working pressure, 40 bar test pressure, burst above 100 bar.</p>
<p>ELAFLEX groups the EURO UL and the K together as push-in couplings and gives both the mark "Meets EN 13760 / UN R 67 / ISO 19825". The catalogue page does not say which vehicle receptacle the K coupling is cut for, so confirm that with ELAFLEX before assuming it matches a given fill valve. For bayonet couplings ELAFLEX recommends the GasGuard GG30 instead.</p>

<h2>Safety features</h2>
<p>The nozzle only lets gas flow when it is correctly coupled, and it will not open when coupled misaligned or tilted. On uncoupling the discharge volume is minimal and directed away from the user.</p>

<h2>Construction</h2>
<p>ELAFLEX describes the design as modular: the nozzle body, with valve body and operating mechanism, is identical for all coupling types. Body aluminium with a comfigrip PVC cover; easy-rotating swivel EA 820 in stainless steel and brass; coupling nut stainless steel (aluminium on the DISH); inner parts stainless steel, acetal resin and PA; lever and latch PA; seals NBR and PU. The EURO UL and K use low-temperature seals (NBR-LT, PU-LT) and the EA 820 LT swivel as standard.</p>

<h2>Part numbers</h2>
<table><thead><tr><th>Hose inlet</th><th>ACME</th><th>DISH</th><th>EURO</th><th>EURO UL</th><th>K</th></tr></thead><tbody>
<tr><td>G 1 BSP female</td><td>ZVG2 ACME.1</td><td>ZVG2 DISH.1</td><td>ZVG2 EURO.1</td><td></td><td></td></tr>
<tr><td>¾" NPT female</td><td>ZVG2 ACME.3</td><td>ZVG2 DISH.3</td><td>ZVG2 EURO.3</td><td>ZVG2 EURO UL.3</td><td>ZVG2 K.3</td></tr>
<tr><td>M 30 × 1.5 L male (left-hand)</td><td>ZVG2 ACME.M30</td><td>ZVG2 DISH.M30</td><td>ZVG2 EURO.M30</td><td></td><td></td></tr>
</tbody></table>

<h2>Options</h2>
<table><thead><tr><th>Suffix</th><th>Option</th><th>Notes</th></tr></thead><tbody>
<tr><td>… M</td><td>Magnet integrated in the guard</td><td>For contactless activation of the dispenser by reed contacts</td></tr>
<tr><td>… D</td><td>Without hold-open latch</td><td>'Deadman' type, required at some dispensers (ZVG 2 ACME, DISH, EURO)</td></tr>
<tr><td>… LT</td><td>Low-temperature type to -40 °C</td><td>ZVG 2 ACME, DISH, EURO; fitted with LT seals</td></tr>
<tr><td>… EA 866 + colour</td><td>Scuffguard with fuel grade identification 'LPG' to EN 16942</td><td>Black or orange. See <a href="/guides/lpg-dispenser-kit-boots-sleeves-and-nozzle-guards.html">boots, sleeves and guards</a></td></tr>
</tbody></table>
<p>The ZVG 2 EURO UL and ZVG 2 K come with a hold-open latch as standard. ELAFLEX states that ZVG 2 EURO UL latched nozzles are covered by UL 125 and UL 567.</p>

<h2>Approvals</h2>
<ul>
<li>ZVG 2 ACME, DISH, EURO: TÜV-approved according to EN 13760 / ISO 19825, certificate 1321 Z 0040/8/01; fulfils the requirements of VdTÜV sheet 513; ATEX II 1 G Ex h IIA, certificate TPS 19 ATEX 103415 0003 U.</li>
<li>ZVG 2 EURO UL: Underwriters Laboratories listed, file reference MH17142.</li>
</ul>

<h2>Pressure drop</h2>
<p>ELAFLEX's GasGuard chart, from testing with propane at the National Measurement Institute in Sydney, plots the nozzles together. Values are read from the printed curves and are approximate.</p>
<table><thead><tr><th>Nozzle</th><th>At 40 L/min</th><th>At 50 L/min</th></tr></thead><tbody>
<tr><td>ZVG 2 K</td><td>About 3.0 bar</td><td>About 4.6 bar</td></tr>
<tr><td>GG1DN / GG20DN and GG1EH / GG20H / GG30</td><td>About 2.0 bar</td><td>About 3.3 bar</td></tr>
<tr><td>ZVG 2 EURO UL</td><td>About 1.8 bar</td><td>About 2.8 bar</td></tr>
<tr><td>GG1E / GG20</td><td>About 1.3 bar</td><td>About 2.0 bar</td></tr>
</tbody></table>
<p>ELAFLEX notes the tests used common adapters without a check valve and that the variety of vehicle connections in the market can give different values. The GG40 is newer than this chart and is not on it.</p>

<h2>Spare parts</h2>
<p>Catalogue pages 562 and 574 are exploded drawings with a part number against every component. Two points from them that matter when ordering: the nozzle body is not available as a spare part, and the swivel is ordered by inlet thread (EA 820.3 for ¾" NPT female, EA 820.M30 for M 30 × 1.5 L male, EA 820.1 for G 1 BSP female, each with an LT version). Use the drawing in the PDF for anything else; we have not transcribed the full list.</p>

<h2>ZVG 2 or GasGuard GG40</h2>
<p>Both are push-on nozzles from the same manufacturer, and both publish a gas release under 1 cm³. The catalogue rates the ZVG 2 range at up to 50 L/min; ELAFLEX's GG40 brochure gives up to 17 GPM, about 64 L/min, and says the GG40 was designed for the US and Canadian K15 systems with latched and unlatched versions both UL approved. Propane Nozzle sells the GG40; see the <a href="/guides/gg40-k15-quick-connect-nozzle.html">GG40 overview</a>.</p>
""" + NOTE,
faqs=[("What is the ELAFLEX ZVG 2?", "A modular LPG vehicle refuelling nozzle: one body with ACME, DISH (Italian claw), EURO push-in, EURO UL or K couplings, rated up to 50 L/min at 25 bar working pressure."),
      ("Is the ZVG 2 EURO UL UL listed?", "Yes. ELAFLEX's catalogue shows it as Underwriters Laboratories listed, file reference MH17142, and states latched ZVG 2 EURO UL nozzles are covered by UL 125 and UL 567."),
      ("How much does a ZVG 2 weigh?", "About 1.5 kg (ACME), 1.2 kg (DISH), 1.4 kg (EURO), 1.41 kg (EURO UL) and 1.55 kg (K), per ELAFLEX's catalogue."),
      ("What does the D suffix mean on a ZVG 2?", "Without hold-open latch: a 'deadman' type that ELAFLEX says is required at some dispensers."),
      ("Does Propane Nozzle sell the ZVG 2?", "No. We keep this page as reference. For K15 quick-connect vehicles we sell the GasGuard GG40 and matching hose kits.")],
sources=["cat561", "cat567", "gg40br"],
),

]
