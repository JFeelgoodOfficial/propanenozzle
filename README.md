# Propane Nozzle site: setup and deployment

Products: the ELAFLEX GasGuard **GG40** K15 quick-connect nozzle and matching autogas hose kits are sold; the **GG20** ACME nozzle is kept as reference only (`/gg20/` and its guides). ELAFLEX hoses, pull-aways, boots, guards and ZVG 2 nozzles are covered as reference from ELAFLEX catalogue pages. GG40 figures ELAFLEX hasn't published are worded "not yet published"; `build/build.py` refuses to build while any `TBD` remains unless you set `ALLOW_TBD=1`.

This folder is the whole business front end:

- **`site.json`**: brand, domain, email and phone. The only place contact details live.
- **`build/`**: the source of the site. `content.py` (GG40, hose-kit and GG20 guides) and `content_elaflex.py` (ELAFLEX reference: LPG 16 hoses, ARK 19 pull-away, boots, sleeves and guards, ZVG 2 nozzles, document library) hold every guide, the chat's knowledge and the phone agent's knowledge. `templates/` holds the two product pages, the chat widget and the stylesheets. `build.py` turns all of it into `public/`.
- **`public/`**: the generated website. Don't edit `index.html`, `gg20/index.html`, `guides/`, `assets/site.css` or `assets/chat.js` by hand; edit the source under `build/` and run `python3 build/build.py`. Images, fonts, `docs/` PDFs, `_headers` and `assets/theme.js` are plain files.
- **`functions/`**: the server side. `/api/lead` (quote form), `/api/chat` (product Q&A) and `/api/call-webhook` (phone agent). All three save to Firestore. Lead and chat requests must come from the site itself (same-origin check), and the form drops submissions sent within 3 seconds of page load.
- **`receptionist/`**: setup steps and the prompt for the Retell AI phone agent.
- **`scripts/`**: `configure.py` updates `site.json` and rebuilds; `export-leads.mjs` dumps leads to CSV; `test-retrieval.mjs` checks the chat finds the right section for 58 common questions.

## 1. Fill in your details

```
python3 scripts/configure.py --brand "Your Company" --domain yourdomain.com --email sales@yourdomain.com
python3 scripts/configure.py --phone "(512) 555-0100"     # once you have a number
```

**No phone number yet.** `site.json` ships with the phone empty. While it is empty the site shows no call links or Call buttons, the schema markup has no telephone, and the chat is told never to give a number. Run the second command when the number exists and everything comes back. The build fails if a `555-` placeholder or a `tel:` link appears while no number is set.

Product photos (`public/gg40.webp`, `public/img/gg40-*.webp`, `public/img/ark19-pull-away.webp`) are cropped from the ELAFLEX PACIFIC GG40 brochure. The brochure and three ELAFLEX catalogue PDFs are served from `/docs/`; they are ELAFLEX's copyright, so confirm with ELAFLEX that hosting them is acceptable. The share image is `public/og.jpg`. To swap a photo, replace the file and update the `width`/`height` on its `<img>` in `build/templates/`.

### Adding another ELAFLEX document

1. Put the PDF in `public/docs/`.
2. Add it to `ELAFLEX_SRC` and `LIBRARY` in `build/content_elaflex.py`, and write a guide `dict(...)` with the figures typed out as tables. Only publish figures you have read in the document; mark numbers taken from a printed chart as approximate.
3. Run `python3 build/build.py`, then `node scripts/test-retrieval.mjs`.

## 2. Domain and email

1. **Domain:** register a .com at Porkbun (about $11/yr) or Cloudflare Registrar (sold at cost).
2. **Add the site to Cloudflare** (free plan) so its DNS is managed there.
3. **Email, free:**
   - Turn on Cloudflare Email Routing and forward `sales@yourdomain.com` to your Gmail.
   - In Gmail, add "Send mail as" so replies come from your domain. You'll need an SMTP relay for that (Gmail's own or Zoho's).
   - Alternative: Zoho Mail Forever Free (up to 5 users, web and app only, no IMAP).
4. **Email, paid but sturdier:** Google Workspace Business Starter, about $8.40/user/month on the flexible plan. Sending is properly authenticated (DKIM), so your quote emails are less likely to land in spam.

## 3. Hosting: Cloudflare Pages (free, commercial use allowed)

Don't use Vercel's free Hobby plan; its terms prohibit commercial sites.

1. Put this folder in a GitHub repo.
2. In Cloudflare, go to Workers & Pages → Create → Pages → connect the repo.
   - Framework: none
   - Build command: leave empty
   - Output directory: `public`
   - Cloudflare picks up the `functions/` folder automatically.
3. Add your custom domain.
4. Set these environment variables (Settings → Variables, all marked as secrets):

| Variable | Value |
|---|---|
| FIREBASE_PROJECT_ID | from step 4 |
| FIREBASE_CLIENT_EMAIL | from the service-account JSON |
| FIREBASE_PRIVATE_KEY | the `private_key` value from the JSON, pasted as-is |
| GROQ_API_KEY | from console.groq.com → API Keys, for the chat (free, no card) |
| CALL_WEBHOOK_TOKEN | any long random string; reuse it in the Retell webhook URL |
| NOTIFY_WEBHOOK_URL | optional: a Slack or Discord incoming-webhook URL, so every new lead pings your phone |

## 4. Lead storage: Firebase Firestore (free Spark plan)

The free plan allows 1 GiB of storage and 20,000 writes per day, far more than you need.

1. Create a project at console.firebase.google.com and create a Firestore database in production mode.
2. Paste `firestore.rules` into the Rules tab and publish. This blocks all browser access; only your server functions can write.
3. In Google Cloud console → IAM → Service Accounts:
   - Create an account and give it the **Cloud Datastore User** role.
   - Create a JSON key for it and copy its values into the Cloudflare variables above.
   - Keep the key file private.
4. Leads arrive in three collections:
   - `leads`: the website form.
   - `chat_leads`: anyone who types an email into the chat.
   - `call_leads`: the phone agent.
5. To get a spreadsheet: `node scripts/export-leads.mjs leads > leads.csv` (Node 20+, same three FIREBASE_* variables in your shell).

You don't need Cloud Functions, so you never need the paid Blaze plan.

## 5. Chat

1. The chat uses `openai/gpt-oss-20b` on Groq's free plan. Set `CHAT_MODEL` to use a different Groq model.
2. Each question sends only the knowledge-base sections that match it (about 1,500 tokens, picked by `functions/_lib/retrieve.js`), not the whole 10,000-token knowledge base. That keeps requests under the free plan's tokens-per-minute cap. After editing `build/content.py` or `retrieve.js`, run `node scripts/test-retrieval.mjs` to check that 58 common questions still reach the right section.
3. The free plan's limits, not money, are the ceiling. Check the current numbers at console.groq.com/docs/rate-limits. When a limit is hit, the chat tells the visitor to try again in a minute or use the phone or quote form.
4. Add a Cloudflare rate-limiting rule on `/api/chat` if your plan includes one, so bots can't use up the daily allowance.
5. If `GROQ_API_KEY` isn't set, the chat politely points people to the quote form instead.

## 6. Phone number and AI receptionist

See `receptionist/README.md`. Short version:

- Retell AI number: $2/month.
- About $0.15 per call-minute, so roughly $17 a month at 100 minutes.
- It transfers calls to your cell when needed.
- Google Voice can't be the front door, because Google doesn't support forwarding to an automated system.

## 7. After launch

1. Submit `https://yourdomain.com/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
2. Submit one test lead through each channel (form, chat, phone) and confirm all three land in Firestore.
3. Visit counts: the pages push `dataLayer` events but no analytics script is installed. Cloudflare Web Analytics is free and cookieless; turn it on for the Pages project in the Cloudflare dashboard.
4. Fonts are self-hosted (IBM Plex, SIL Open Font License, `public/assets/fonts/`); the site makes no third-party requests.

## Monthly cost, cheapest setup

| Item | Cost |
|---|---|
| Hosting, Cloudflare Pages | $0 |
| Firestore | $0 |
| Email, routing to Gmail or Zoho free | $0 |
| Domain | ≈ $0.92 |
| Phone agent, Retell at 100 minutes | ≈ $17 |
| Chat API | pennies to a few dollars at low traffic; capped by your spend limit |
| **Total** | **≈ $18 to $25** |

Pricing was checked 2026-10-07; confirm it on each provider's pricing page before you sign up.
