# GG20 site: setup and deployment

This folder is the whole business front end:

- **`public/`**: the website. Product page, 12 guides, a knowledge base file, `llms.txt`, sitemap and robots.txt.
- **`functions/`**: the server side. `/api/lead` (quote form), `/api/chat` (product Q&A) and `/api/call-webhook` (phone agent). All three save to Firestore.
- **`receptionist/`**: setup steps and the prompt for the Retell AI phone agent.
- **`build/content.py`**: the single source for every guide, the chat's knowledge and the phone agent's knowledge. Edit it, then run `python3 build/build.py`.
- **`scripts/`**: `configure.py` fills in your business details everywhere; `export-leads.mjs` dumps leads to CSV.

## 1. Fill in your details

```
python3 scripts/configure.py --brand "Your Company" --domain yourdomain.com \
  --phone "(512) 555-0100" --email sales@yourdomain.com \
  --transfer-name "Your Name" --hours "Mon-Fri 8am-5pm Central"
```

Then add your own GG20 photo as `public/gg20.jpg` (1200x630 works for link previews), and swap the schematic in the hero of `public/index.html` for it.

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
2. Each question sends only the knowledge-base sections that match it (about 1,500 tokens, picked by `functions/_lib/retrieve.js`), not the whole 10,000-token knowledge base. That keeps requests under the free plan's tokens-per-minute cap.
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
