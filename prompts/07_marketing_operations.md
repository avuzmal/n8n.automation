# 07. Marketing & Growth Operations

> ### 1. End-to-End Webinar Operations
> **The Problem:** Hosting a webinar requires manually syncing registrants between Zoom, Marketo, and Salesforce, often resulting in missed follow-ups and lost leads.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_01_end_to_end_webinar_operations.json)
> 
> **How it works:** 
> > *Build an n8n workflow that automates webinar operations: when a user registers in Zoom, add them to a Marketo nurture track, send a reminder sequence, and upon completion, push the attendance data to Salesforce and trigger a sales task.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Zoom["Zoom"]
>     Zoom --> Marketo["Marketo"]
>     Marketo --> Salesforce["Salesforce"]
> ```
> 
> **🔗 Core Integrations:** `Zoom` • `Marketo` • `Salesforce`
> ---

> ### 2. AI-Powered Content Syndication
> **The Problem:** Writing a blog post is only half the battle. Distributing it across Medium, LinkedIn, and Twitter requires custom formatting and takes up valuable marketing time.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_02_ai_powered_content_syndication.json)
> 
> **How it works:** 
> > *Design a workflow that automates content syndication: when a new blog post is published in WordPress, automatically format and push it to Medium, LinkedIn, and Twitter, using AI to generate platform-specific hooks and hashtags.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> WordPress["WordPress"]
>     WordPress --> Medium["Medium"]
>     Medium --> LinkedIn["LinkedIn"]
>     LinkedIn --> Twitter["Twitter"]
>     Twitter --> AI["AI"]
> ```
> 
> **🔗 Core Integrations:** `WordPress` • `Medium` • `LinkedIn` • `Twitter` • `AI`
> ---

> ### 3. Automated Ad Spend Pacing & Pause
> **The Problem:** Marketing agencies and internal teams frequently overspend their budgets on Meta or Google Ads because daily pacing is tracked in manual spreadsheets.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_03_automated_ad_spend_pacing_pause.json)
> 
> **How it works:** 
> > *Create an automated ad spend reconciliation workflow: pull daily spend from Meta Ads, Google Ads, and LinkedIn, compare it against the budget in a master sheet, and automatically pause campaigns in the ad platforms if pacing exceeds 110%.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> MetaAds["Meta Ads"]
>     MetaAds --> GoogleAds["Google Ads"]
>     GoogleAds --> LinkedInAds["LinkedIn Ads"]
>     LinkedInAds --> GoogleSheets["Google Sheets"]
> ```
> 
> **🔗 Core Integrations:** `Meta Ads` • `Google Ads` • `LinkedIn Ads` • `Google Sheets`
> ---

> ### 4. Frictionless Influencer & Affiliate Payouts
> **The Problem:** Managing an affiliate program is great until month-end, when you have to calculate hundreds of micro-commissions and pay them out across different countries.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_04_frictionless_influencer_affiliate_payouts.json)
> 
> **How it works:** 
> > *Build a workflow that automates influencer payouts: track affiliate link clicks and conversions via PartnerStack, calculate commissions, generate invoices via Xero, and trigger payouts via Stripe Connect.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> PartnerStack["PartnerStack"]
>     PartnerStack --> Xero["Xero"]
>     Xero --> StripeConnect["Stripe Connect"]
> ```
> 
> **🔗 Core Integrations:** `PartnerStack` • `Xero` • `Stripe Connect`
> ---

> ### 5. Instant VIP Brand Mention Triage
> **The Problem:** By the time a PR team notices a high-profile influencer complaining about the brand on Twitter, the tweet has already gone viral.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_05_instant_vip_brand_mention_triage.json)
> 
> **How it works:** 
> > *Design a workflow that monitors brand mentions via Mention API; if a high-profile account mentions the brand, automatically alert the PR team via Slack and draft a response using AI based on brand guidelines.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> MentionAPI["Mention API"]
>     MentionAPI --> Slack["Slack"]
>     Slack --> AI["AI"]
> ```
> 
> **🔗 Core Integrations:** `Mention API` • `Slack` • `AI`
> ---

> ### 6. Automated Technical SEO Monitoring
> **The Problem:** Developers deploy code changes that accidentally drop meta tags or create 404 loops, destroying SEO rankings before marketing even notices.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_06_automated_technical_seo_monitoring.json)
> 
> **How it works:** 
> > *Create an automated SEO audit workflow: trigger a weekly crawl via Screaming Frog API, identify new 404s or dropped meta tags, and automatically create Jira tickets for the dev team to fix them.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> ScreamingFrogAPI["Screaming Frog API"]
>     ScreamingFrogAPI --> Jira["Jira"]
> ```
> 
> **🔗 Core Integrations:** `Screaming Frog API` • `Jira`
> ---

> ### 7. Speed-to-Lead Ad Handoff
> **The Problem:** Leads generated from Facebook or LinkedIn forms sit in a CSV file waiting to be downloaded, growing cold by the minute.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_07_speed_to_lead_ad_handoff.json)
> 
> **How it works:** 
> > *Build a workflow that automates lead handoff from ads: ingest form fills from Facebook Lead Ads, enrich via HubSpot, and if the lead meets the ICP, instantly notify the on-demand sales rep via SMS with a link to call the lead.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> FacebookLeadAds["Facebook Lead Ads"]
>     FacebookLeadAds --> HubSpot["HubSpot"]
>     HubSpot --> SMSAPI["SMS API"]
> ```
> 
> **🔗 Core Integrations:** `Facebook Lead Ads` • `HubSpot` • `SMS API`
> ---

> ### 8. Event Badge Scanner to CRM Sync
> **The Problem:** Sales reps collect hundreds of business cards at trade shows, but rarely enter them into the CRM promptly, killing post-event momentum.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_08_event_badge_scanner_to_crm_sync.json)
> 
> **How it works:** 
> > *Design a workflow that automates event follow-ups: scan business cards via a mobile app (OCR), push contacts to HubSpot, tag them with the event name, and trigger a personalized "Great meeting you" email sequence.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> OCRScannerApp["OCR Scanner App"]
>     OCRScannerApp --> HubSpot["HubSpot"]
>     HubSpot --> EmailSequence["Email Sequence"]
> ```
> 
> **🔗 Core Integrations:** `OCR Scanner App` • `HubSpot` • `Email Sequence`
> ---

> ### 9. Statistical A/B Test Decision Engine
> **The Problem:** Marketers often call an A/B test a "winner" too early without calculating true statistical significance, leading to poor CRO decisions.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_09_statistical_a_b_test_decision_engine.json)
> 
> **How it works:** 
> > *Create a workflow that automates A/B test analysis: pull conversion data from Optimizely, run a statistical significance calculation via a Python node, and automatically declare a winner and push the winning variant to production.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Optimizely["Optimizely"]
>     Optimizely --> PythonScripting["Python Scripting"]
>     PythonScripting --> CMSProductionSystem["CMS/Production System"]
> ```
> 
> **🔗 Core Integrations:** `Optimizely` • `Python Scripting` • `CMS/Production System`
> ---

> ### 10. Voice of Customer Feedback Loop
> **The Problem:** Marketing captures great user feedback in Intercom, but it never makes its way to the Product team's roadmap.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/07_10_voice_of_customer_feedback_loop.json)
> 
> **How it works:** 
> > *Build a workflow that syncs product feedback from Intercom to Productboard: use AI to summarize the feedback, tag the relevant feature, and update the Productboard status, which then syncs back to the user in Intercom.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Intercom["Intercom"]
>     Intercom --> Productboard["Productboard"]
>     Productboard --> AI["AI"]
> ```
> 
> **🔗 Core Integrations:** `Intercom` • `Productboard` • `AI`
> ---
