# AI phone receptionist setup (Retell AI)

Why Retell: the cheapest option in the pricing research that has all three things you need: a no-code agent builder, a knowledge base, and post-call webhooks with custom extracted fields. It also sells phone numbers directly, so you don't need a separate phone carrier.

Research figures (checked 2026-10-07; verify on retellai.com/pricing before you sign up):
- Roughly $0.15 per call-minute all-in.
- About $17 a month at 100 minutes, about $79 a month at 500 minutes.
- Phone number: $2/month.
- $10 of free credit to start.

## Steps
1. Create a Retell account. Buy a local number in your area code ($2/mo).
2. **Knowledge base:** create one and upload `public/knowledge/gg20-kb.md` from this site, after running scripts/configure.py. Whenever you change `build/content.py`, run the build again and re-upload the file.
3. **Agent:** create a single-prompt agent, paste `agent-prompt.md`, fill in {{TRANSFER_NAME}} and {{BUSINESS_HOURS}}, and attach the knowledge base.
4. **Transfer:** add a "transfer call" tool that points to your cell number. Retell's research figures listed transfer fees as unconfirmed, so check them on retellai.com/pricing.
5. **Post-call analysis:** add these custom fields. The names must match exactly, because the webhook reads them:

| Field | Type | Description to give Retell |
|---|---|---|
| caller_name | text | Caller's full name |
| company | text | Caller's company or organization |
| callback_phone | text | Best callback number the caller gave |
| email | text | Caller's email address |
| product_interest | selector: GG20, GG20H, GG20DN, unsure, other | Which nozzle they want |
| quantity | number | Number of nozzles |
| application | selector: forklift cylinders, RV, autogas fleet, public station, LG20 replacement, other | What they'll use it for |
| ship_to_zip | text | Delivery ZIP code |
| wants_callback | boolean | Caller asked for a call back |
| urgency | selector: today, this week, this month, researching | How soon they need it |

6. **Webhook:** set the agent webhook URL to `https://propanenozzle.com/api/call-webhook?token=<CALL_WEBHOOK_TOKEN>`. Use the same long random token you set in Cloudflare. Leads land in Firestore under `call_leads`. Retell can send the same call more than once, so the call ID is used as the record ID and repeats are stored only once.
7. **Test call:** make one test call and check the record in Firestore. Retell's docs I could reach didn't spell out the exact analysis payload, so the webhook also saves the whole analysis object as `raw_analysis`. If any named field comes through empty, compare its name against `raw_analysis` and fix the mapping in `functions/api/call-webhook.js`.

## Optional hardening
- **IP allowlist:** Retell sends webhooks from 100.20.5.228. You can add a Cloudflare WAF rule that only allows that IP on `/api/call-webhook`.
- **Signature check:** Retell signs requests with an `x-retell-signature` header, keyed with your API key. The token check is enough to start; add the signature check later.

## Use your own number instead
If you already have a number you want to keep, Retell can use a Twilio number you own instead of one of its own (the research put Twilio at $1.15/mo plus about $0.0085/min inbound). Free Google Voice won't work as the front door: Google doesn't support forwarding calls to an automated system.
