# 05. Sales & CRM Operations

> ### 1. Intelligent Lead Routing & Scoring
> **The Problem:** High-value inbound leads get lost in round-robin queues or are assigned to the wrong reps, killing momentum and decreasing conversion rates.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_01_intelligent_lead_routing_scoring.json)
> 
> **How it works:** 
> > *Build an n8n workflow that automates lead routing: ingest form fills from WordPress, enrich via Clearbit, score using a custom algorithm, and route to the correct AE in Salesforce based on territory, industry, and company size.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> WordPress["WordPress"]
>     WordPress --> Clearbit["Clearbit"]
>     Clearbit --> Salesforce["Salesforce"]
> ```
> 
> **🔗 Core Integrations:** `WordPress` • `Clearbit` • `Salesforce`
> ---

> ### 2. Stale Deal Detection
> **The Problem:** Sales reps hold onto dead opportunities to pad their pipelines, making revenue forecasting incredibly inaccurate for leadership.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_02_stale_deal_detection.json)
> 
> **How it works:** 
> > *Design a workflow that syncs email engagement data from Outreach/Salesloft to Salesforce, updating lead/contact activity timelines and triggering a "Stale Deal" alert if no engagement occurs in 14 days.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> OutreachSalesloft["Outreach/Salesloft"]
>     OutreachSalesloft --> Salesforce["Salesforce"]
> ```
> 
> **🔗 Core Integrations:** `Outreach/Salesloft` • `Salesforce`
> ---

> ### 3. Zero-Touch CPQ & Provisioning
> **The Problem:** Generating quotes manually introduces pricing errors, rogue discounting, and delays in getting the contract to the prospect while they are hot.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_03_zero_touch_cpq_provisioning.json)
> 
> **How it works:** 
> > *Create an automated CPQ workflow: when an Opportunity reaches "Negotiation" in Salesforce, automatically generate a quote in PandaDoc using dynamic pricing logic, and upon signature, update the Opportunity to "Closed Won" and trigger provisioning.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Salesforce["Salesforce"]
>     Salesforce --> PandaDoc["PandaDoc"]
>     PandaDoc --> ProvisioningAPI["Provisioning API"]
> ```
> 
> **🔗 Core Integrations:** `Salesforce` • `PandaDoc` • `Provisioning API`
> ---

> ### 4. Competitor Pricing Web Scraper
> **The Problem:** Competitors change pricing quietly. If sales enablement doesn't know, reps get blindsided on calls and lose deals to cheaper alternatives.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_04_competitor_pricing_web_scraper.json)
> 
> **How it works:** 
> > *Build a workflow that monitors competitor pricing via web scraping; if a competitor changes pricing, automatically update the battle card in Highspot and notify the sales enablement team via Slack.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> WebScraper["Web Scraper"]
>     WebScraper --> Highspot["Highspot"]
>     Highspot --> Slack["Slack"]
> ```
> 
> **🔗 Core Integrations:** `Web Scraper` • `Highspot` • `Slack`
> ---

> ### 5. Intent-Based Lead Recycling
> **The Problem:** SDRs discard "Not Right Now" leads, and marketing rarely nurtures them effectively. When those prospects are ready to buy months later, they go to a competitor.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_05_intent_based_lead_recycling.json)
> 
> **How it works:** 
> > *Design a workflow that automates lead recycling: if an SDR marks a lead as "Nurture" in Salesforce, move it to a Marketo nurture track, and automatically re-assign it to an SDR if they download a high-intent asset 6 months later.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Salesforce["Salesforce"]
>     Salesforce --> Marketo["Marketo"]
> ```
> 
> **🔗 Core Integrations:** `Salesforce` • `Marketo`
> ---

> ### 6. Call Intelligence Sync
> **The Problem:** Sales reps hate writing notes in the CRM, resulting in missing context for Account Managers post-sale and poor handoffs.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_06_call_intelligence_sync.json)
> 
> **How it works:** 
> > *Create a workflow that integrates Gong call recordings with Salesforce: transcribe the call, extract key objections and next steps via AI, and append a summary to the Opportunity notes and the related Account record.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Gong["Gong"]
>     Gong --> AI["AI"]
>     AI --> Salesforce["Salesforce"]
> ```
> 
> **🔗 Core Integrations:** `Gong` • `AI` • `Salesforce`
> ---

> ### 7. Automated Territory Realignment
> **The Problem:** When a new rep is hired or territories are redrawn, Ops spends days manually exporting, mapping, and mass-updating account owners in the CRM.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_07_automated_territory_realignment.json)
> 
> **How it works:** 
> > *Build an automated territory alignment workflow: when a new AE is hired, automatically reassign existing open opportunities and accounts in Salesforce based on the new geo/industry mapping, notifying affected reps.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Salesforce["Salesforce"]
>     Salesforce --> EmailSlack["Email/Slack"]
> ```
> 
> **🔗 Core Integrations:** `Salesforce` • `Email/Slack`
> ---

> ### 8. Contextual Deal Desk Approvals
> **The Problem:** Discount approvals are requested in chaotic Slack threads. Leadership lacks visibility into how a 15% discount actually impacts the margin of the deal.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_08_contextual_deal_desk_approvals.json)
> 
> **How it works:** 
> > *Design a workflow that automates deal desk approvals: when a discount >15% is applied in Salesforce, automatically route for approval via Slack/Teams, pulling margin data from the ERP to show impact, and updating the Opp upon approval.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Salesforce["Salesforce"]
>     Salesforce --> SlackTeams["Slack/Teams"]
>     SlackTeams --> ERPMarginData["ERP (Margin Data)"]
> ```
> 
> **🔗 Core Integrations:** `Salesforce` • `Slack/Teams` • `ERP (Margin Data)`
> ---

> ### 9. Bulletproof Activity Logging
> **The Problem:** Sales reps forget to log meetings in the CRM, making it impossible to measure activity metrics or understand what it takes to close a deal.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_09_bulletproof_activity_logging.json)
> 
> **How it works:** 
> > *Create a workflow that syncs calendar data from Outlook to Salesforce, automatically logging meetings as "Events" and linking them to the relevant Opportunity and Contacts, ensuring 100% activity logging compliance.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Outlook["Outlook"]
>     Outlook --> Salesforce["Salesforce"]
> ```
> 
> **🔗 Core Integrations:** `Outlook` • `Salesforce`
> ---

> ### 10. AI-Driven Win/Loss Analysis
> **The Problem:** "Price" is the default reason reps choose when they lose a deal. True win/loss analysis requires candid feedback from the prospect themselves.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/05_10_ai_driven_win_loss_analysis.json)
> 
> **How it works:** 
> > *Build a workflow that automates win/loss analysis: when an Opp is Closed Lost, trigger a Typeform survey; upon submission, parse the feedback, categorize the loss reason, and update a custom "Loss Reason" object in Salesforce for reporting.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Salesforce["Salesforce"]
>     Salesforce --> Typeform["Typeform"]
>     Typeform --> AIParser["AI Parser"]
> ```
> 
> **🔗 Core Integrations:** `Salesforce` • `Typeform` • `AI Parser`
> ---
