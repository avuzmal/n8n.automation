# 04. Customer Success & Support

> ### 1. Proactive Feature Drop-Off Alerting
> **The Problem:** CSMs are often blindsided by churn because they lack visibility into when a customer stops using a key sticky feature in the product.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_01_proactive_feature_drop_off_alerting.json)
> 
> **How it works:** 
> > *Design a workflow that monitors product usage via Segment webhooks; if a key feature adoption drops by 20% week-over-week, automatically create a "Health Score Drop" task in Gainsight and alert the CSM via Slack.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Segment["Segment"]
>     Segment --> Gainsight["Gainsight"]
>     Gainsight --> Slack["Slack"]
> ```
> 
> **🔗 Core Integrations:** `Segment` • `Gainsight` • `Slack`
> ---

> ### 2. AI-Driven Support Ticket Triage
> **The Problem:** Support queues get clogged with low-priority or repetitive questions, delaying responses to critical P1 issues that impact major clients.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_02_ai_driven_support_ticket_triage.json)
> 
> **How it works:** 
> > *Build an automated ticket triage workflow: ingest Zendesk tickets, use AI to classify intent and sentiment, route P1 issues to PagerDuty, and auto-respond to P3 issues with relevant knowledge base articles.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Zendesk["Zendesk"]
>     Zendesk --> AI["AI"]
>     AI --> PagerDuty["PagerDuty"]
> ```
> 
> **🔗 Core Integrations:** `Zendesk` • `AI` • `PagerDuty`
> ---

> ### 3. Automated QBR Deck Generation
> **The Problem:** CSMs spend hours every quarter manually compiling usage graphs and support metrics to build Quarterly Business Review (QBR) slide decks.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_03_automated_qbr_deck_generation.json)
> 
> **How it works:** 
> > *Create a workflow that automates QBR prep: pull usage metrics from Mixpanel, pull support ticket volume from Intercom, generate a slide deck via Google Slides API, and email it to the CSM.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Mixpanel["Mixpanel"]
>     Mixpanel --> Intercom["Intercom"]
>     Intercom --> GoogleSlidesAPI["Google Slides API"]
>     GoogleSlidesAPI --> Email["Email"]
> ```
> 
> **🔗 Core Integrations:** `Mixpanel` • `Intercom` • `Google Slides API` • `Email`
> ---

> ### 4. Dynamic Churn Deflection
> **The Problem:** When a customer hits 'cancel', relying on them to reach out to support is a lost cause. You need immediate, personalized intervention to save the revenue.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_04_dynamic_churn_deflection.json)
> 
> **How it works:** 
> > *Design a workflow that handles automated churn intervention: when a cancellation request is submitted in Stripe, trigger a workflow that offers a dynamic discount via email, and if accepted, updates the subscription and creates a retention win task in Salesforce.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Stripe["Stripe"]
>     Stripe --> EmailAPI["Email API"]
>     EmailAPI --> Salesforce["Salesforce"]
> ```
> 
> **🔗 Core Integrations:** `Stripe` • `Email API` • `Salesforce`
> ---

> ### 5. Community Forum to Bug Tracker Sync
> **The Problem:** Bugs reported by users in public community forums get lost or ignored, leading to frustrated power users and unresolved software defects.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_05_community_forum_to_bug_tracker_sync.json)
> 
> **How it works:** 
> > *Build a workflow that monitors community forums (Discourse); if a user posts a bug, automatically create a Jira ticket, link it to the forum post, and notify the user when the Jira status changes to "Resolved".*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Discourse["Discourse"]
>     Discourse --> Jira["Jira"]
> ```
> 
> **🔗 Core Integrations:** `Discourse` • `Jira`
> ---

> ### 6. Intent-Based Onboarding Sequences
> **The Problem:** Sending generic, one-size-fits-all onboarding emails results in low engagement. Users only care about the features relevant to their specific use-case.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_06_intent_based_onboarding_sequences.json)
> 
> **How it works:** 
> > *Create an automated onboarding email sequence workflow triggered by a welcome call completion in Chili Piper, dynamically adjusting the email content based on the user's selected use-case during the call.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> ChiliPiper["Chili Piper"]
>     ChiliPiper --> MarketingAutomationegMarketoHubSpot["Marketing Automation (e.g., Marketo/HubSpot)"]
> ```
> 
> **🔗 Core Integrations:** `Chili Piper` • `Marketing Automation (e.g., Marketo/HubSpot)`
> ---

> ### 7. Executive CSAT/NPS Correlation
> **The Problem:** NPS scores exist in a silo. Executives need to know if the unhappy customers are your largest enterprise accounts or your lowest-tier users.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_07_executive_csat_nps_correlation.json)
> 
> **How it works:** 
> > *Design a workflow that aggregates NPS/CSAT scores from Delighted, cross-references them with the customer's ARR in Salesforce, and automatically generates a monthly executive summary report in Notion.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Delighted["Delighted"]
>     Delighted --> Salesforce["Salesforce"]
>     Salesforce --> Notion["Notion"]
> ```
> 
> **🔗 Core Integrations:** `Delighted` • `Salesforce` • `Notion`
> ---

> ### 8. Pre-Breach SLA Escalation
> **The Problem:** By the time a support ticket breaches its SLA, the customer is already angry and contract penalties may apply. You need to act *before* the breach.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_08_pre_breach_sla_escalation.json)
> 
> **How it works:** 
> > *Build a workflow that automates SLA breach prevention: monitor ticket age in Freshdesk, and at 80% of SLA time, automatically escalate the ticket to a Tier 2 agent and notify the Support Manager via SMS.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Freshdesk["Freshdesk"]
>     Freshdesk --> SMSAPITwilio["SMS API (Twilio)"]
> ```
> 
> **🔗 Core Integrations:** `Freshdesk` • `SMS API (Twilio)`
> ---

> ### 9. Account Health Slack Digest
> **The Problem:** The wider company (sales, product, leadership) rarely logs into Customer Success software, creating a blind spot for account risks and expansion opportunities.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_09_account_health_slack_digest.json)
> 
> **How it works:** 
> > *Create a workflow that syncs customer health scores from Totango to Slack, posting a weekly "Wins and Risks" digest in the #customer-success channel, highlighting top expansions and at-risk accounts.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Totango["Totango"]
>     Totango --> Slack["Slack"]
> ```
> 
> **🔗 Core Integrations:** `Totango` • `Slack`
> ---

> ### 10. Macro-Update Propagation
> **The Problem:** When the product team releases a new feature, support agents are often left using outdated macros, providing incorrect information to users.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/04_10_macro_update_propagation.json)
> 
> **How it works:** 
> > *Design a workflow that automates macro-update propagation: when a product update is published in Productboard, automatically update the relevant macros in Zendesk and notify agents via a Slack digest.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Productboard["Productboard"]
>     Productboard --> Zendesk["Zendesk"]
>     Zendesk --> Slack["Slack"]
> ```
> 
> **🔗 Core Integrations:** `Productboard` • `Zendesk` • `Slack`
> ---
