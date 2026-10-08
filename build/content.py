# Single source of truth for the GG20 knowledge base.
# Every guide page, /knowledge/gg20-kb.md, /llms.txt and the chat/phone-agent context are generated from this file.
# Edit here, then run: python3 build/build.py

UPDATED = "2026-10-07"

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
}

ARTICLES = [

dict(
slug="gg20-vs-gg20h-vs-gg20dn",
title="GG20 vs GG20H vs GG20DN: Which GasGuard Nozzle to Buy",
nav="GG20 vs GG20H vs GG20DN",
desc="How the three GasGuard GG20 nozzles differ: single, hybrid and dual nose pieces, flow, lever force, release volume and who each one is for.",
summary="All three GG20 nozzles share the same body, 160 mm reach and 1¾\" ACME coupling. The nose piece is the only difference. GG20 (single nose) flows the most, 63 L/min, and costs least; it suits trained operators. GG20H (hybrid nose) cuts lever force at 60 L/min for operators who fill all day. GG20DN (patented dual nose) seals even when the nozzle isn't fully tightened, so it is the one to use where the public or untrained staff fill.",
body="""
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
<p>Reach (160 mm connector nut), the 1¾" ACME coupling, the 25 bar (362 psi) pressure rating, the −40 °C to +110 °C range, the inlet swivel choice (½" or ¾" NPT female), the standard 300 µm strainer, and the options (magnet, latch, splashguard, brass ACME insert). See <a href="/guides/gg20-specifications.html">full specifications</a> and <a href="/guides/gg20-part-numbers-and-options.html">part numbers</a>.</p>

<h2>Need standard reach instead?</h2>
<p>The same three nose pieces exist on the shorter GG1 series as GG1E, GG1EH and GG1DN, with a 125 mm connector. Choose GG20 only when the fill valve is recessed. See <a href="/guides/gasguard-family-gg1-gg20-gg30-gg40.html">the GasGuard family compared</a>.</p>
""",
faqs=[("Which GG20 version has the highest flow?","The GG20 with the single nose piece, rated 63 L/min at 12 bar. The GG20H and GG20DN are rated 60 L/min."),
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
<p>These numbers come from the GG20 repair and maintenance manual. Availability of individual spares in the US varies; ask before you plan a repair around one.</p>
""",
faqs=[("What does .3 mean in GG20.3?","A ¾\" NPT female inlet swivel. A .2 suffix means ½\" NPT female."),
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
<li>A problem repeats: take the nozzle out of service and have trained personnel inspect it. See <a href="/guides/gg20-troubleshooting.html">troubleshooting</a>.</li>
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
<p>ELAFLEX PACIFIC recommends fitting a new seal kit throughout the nozzle every 24 months to extend service life and cut downtime. The repair manual lists the GG3 seal kit for the GG20 series. Seal replacement is a bench job; see <a href="/guides/gg20-repair-and-testing.html">repair and testing</a>.</p>

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
faqs=[("At what pressure is a repaired GG20 tested?","The static test in the repair manual uses 1200 to 1800 kPa (12 to 18 bar, 174 to 260 psi) under water, with a 27 N·m bending load on the swivel.")],
sources=["rm"],
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
<p>Butane-Propane News reports that NFPA 58 adopted the K15 "Euro" push-to-connect filler as the style vehicle manufacturers must provide on new LPG vehicles from 2020, and that the 2024 edition lets Euro nozzles be used without specific operator training. Forklift cylinders, RVs and many existing vehicles still use 1¾" ACME fill valves, which is the GG20's job. For K15 vehicles, ELAFLEX makes the GG40.</p>

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
<tr><td>GG40</td><td>K15 quick connect (US/Canada)</td><td>n/a</td><td>See ELAFLEX GG40 brochure</td><td></td><td></td></tr>
<tr><td>ZVG 2 EURO UL</td><td>Euro push-on, ISO 19825</td><td>n/a</td><td>Up to 50 L/min</td><td>&lt;1 cm³</td><td>≈1.41 kg</td></tr>
</tbody></table>

<h2>GG1 or GG20?</h2>
<p>Same function, same nose pieces, same ratings. The GG20 adds 35 mm to the connector nut. If a GG1 bottoms out on a bracket, cradle or body panel before the threads engage, you need the GG20. If it doesn't, the GG1 is lighter and shorter to handle.</p>

<h2>Where the others fit</h2>
<p>The GG30 serves bayonet fill points and has a 4-slot front and redesigned nose piece; ELAFLEX states it reduces released gas on closure by 23% versus its predecessor. The GG40 was designed for the US and Canadian K15 quick-connect systems and fits the same NB-GG boot. The ZVG 2 EURO UL is ELAFLEX's push-on nozzle; latched versions are covered by UL 125 and UL 567.</p>
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
