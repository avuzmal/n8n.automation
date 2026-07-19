# 05. Sales & CRM Operations

> ### 1. Intelligent Lead Routing & Scoring
> **The Problem:** High-value inbound leads get lost in round-robin queues or are assigned to the wrong reps, killing momentum and decreasing conversion rates.
> 
> **The Prompt:** 
> > *Build an n8n workflow that automates lead routing: ingest form fills from WordPress, enrich via Clearbit, score using a custom algorithm, and route to the correct AE in Salesforce based on territory, industry, and company size.*
> 
> **🔗 Core Integrations:** `WordPress` • `Clearbit` • `Salesforce`
> ---

> ### 2. Stale Deal Detection
> **The Problem:** Sales reps hold onto dead opportunities to pad their pipelines, making revenue forecasting incredibly inaccurate for leadership.
> 
> **The Prompt:** 
> > *Design a workflow that syncs email engagement data from Outreach/Salesloft to Salesforce, updating lead/contact activity timelines and triggering a "Stale Deal" alert if no engagement occurs in 14 days.*
> 
> **🔗 Core Integrations:** `Outreach/Salesloft` • `Salesforce`
> ---

> ### 3. Zero-Touch CPQ & Provisioning
> **The Problem:** Generating quotes manually introduces pricing errors, rogue discounting, and delays in getting the contract to the prospect while they are hot.
> 
> **The Prompt:** 
> > *Create an automated CPQ workflow: when an Opportunity reaches "Negotiation" in Salesforce, automatically generate a quote in PandaDoc using dynamic pricing logic, and upon signature, update the Opportunity to "Closed Won" and trigger provisioning.*
> 
> **🔗 Core Integrations:** `Salesforce` • `PandaDoc` • `Provisioning API`
> ---

> ### 4. Competitor Pricing Web Scraper
> **The Problem:** Competitors change pricing quietly. If sales enablement doesn't know, reps get blindsided on calls and lose deals to cheaper alternatives.
> 
> **The Prompt:** 
> > *Build a workflow that monitors competitor pricing via web scraping; if a competitor changes pricing, automatically update the battle card in Highspot and notify the sales enablement team via Slack.*
> 
> **🔗 Core Integrations:** `Web Scraper` • `Highspot` • `Slack`
> ---

> ### 5. Intent-Based Lead Recycling
> **The Problem:** SDRs discard "Not Right Now" leads, and marketing rarely nurtures them effectively. When those prospects are ready to buy months later, they go to a competitor.
> 
> **The Prompt:** 
> > *Design a workflow that automates lead recycling: if an SDR marks a lead as "Nurture" in Salesforce, move it to a Marketo nurture track, and automatically re-assign it to an SDR if they download a high-intent asset 6 months later.*
> 
> **🔗 Core Integrations:** `Salesforce` • `Marketo`
> ---

> ### 6. Call Intelligence Sync
> **The Problem:** Sales reps hate writing notes in the CRM, resulting in missing context for Account Managers post-sale and poor handoffs.
> 
> **The Prompt:** 
> > *Create a workflow that integrates Gong call recordings with Salesforce: transcribe the call, extract key objections and next steps via AI, and append a summary to the Opportunity notes and the related Account record.*
> 
> **🔗 Core Integrations:** `Gong` • `AI` • `Salesforce`
> ---

> ### 7. Automated Territory Realignment
> **The Problem:** When a new rep is hired or territories are redrawn, Ops spends days manually exporting, mapping, and mass-updating account owners in the CRM.
> 
> **The Prompt:** 
> > *Build an automated territory alignment workflow: when a new AE is hired, automatically reassign existing open opportunities and accounts in Salesforce based on the new geo/industry mapping, notifying affected reps.*
> 
> **🔗 Core Integrations:** `Salesforce` • `Email/Slack`
> ---

> ### 8. Contextual Deal Desk Approvals
> **The Problem:** Discount approvals are requested in chaotic Slack threads. Leadership lacks visibility into how a 15% discount actually impacts the margin of the deal.
> 
> **The Prompt:** 
> > *Design a workflow that automates deal desk approvals: when a discount >15% is applied in Salesforce, automatically route for approval via Slack/Teams, pulling margin data from the ERP to show impact, and updating the Opp upon approval.*
> 
> **🔗 Core Integrations:** `Salesforce` • `Slack/Teams` • `ERP (Margin Data)`
> ---

> ### 9. Bulletproof Activity Logging
> **The Problem:** Sales reps forget to log meetings in the CRM, making it impossible to measure activity metrics or understand what it takes to close a deal.
> 
> **The Prompt:** 
> > *Create a workflow that syncs calendar data from Outlook to Salesforce, automatically logging meetings as "Events" and linking them to the relevant Opportunity and Contacts, ensuring 100% activity logging compliance.*
> 
> **🔗 Core Integrations:** `Outlook` • `Salesforce`
> ---

> ### 10. AI-Driven Win/Loss Analysis
> **The Problem:** "Price" is the default reason reps choose when they lose a deal. True win/loss analysis requires candid feedback from the prospect themselves.
> 
> **The Prompt:** 
> > *Build a workflow that automates win/loss analysis: when an Opp is Closed Lost, trigger a Typeform survey; upon submission, parse the feedback, categorize the loss reason, and update a custom "Loss Reason" object in Salesforce for reporting.*
> 
> **🔗 Core Integrations:** `Salesforce` • `Typeform` • `AI Parser`
> ---
