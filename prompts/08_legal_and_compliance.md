# 08. Legal, Compliance & Risk

> ### 1. Zero-Friction Mutual NDA Generation
> **The Problem:** Sales reps lose momentum when they have to wait days for the legal team to draft, review, and send a standard non-disclosure agreement.
> 
> **The Prompt:** 
> > *Design an n8n workflow that automates NDA processing: when a request is submitted via a portal, generate a mutual NDA via PandaDoc, route for internal legal review, send to the counterparty, and upon signature, store in Contractify and alert the sales rep.*
> 
> **🔗 Core Integrations:** `Internal Portal` • `PandaDoc` • `Contractify`
> ---

> ### 2. Automated Regulatory Tracking & Alerting
> **The Problem:** Compliance officers struggle to keep up with changing global data privacy laws (GDPR, CCPA), risking non-compliance fines.
> 
> **The Prompt:** 
> > *Build a workflow that monitors regulatory changes via an API (e.g., Ascent); if a new GDPR directive is published, automatically create a compliance task in Jira, assign it to the DPO, and link relevant internal policies.*
> 
> **🔗 Core Integrations:** `Ascent (or similar Regulatory API)` • `Jira`
> ---

> ### 3. Omni-System DSAR Data Extraction
> **The Problem:** Executing a Data Subject Access Request (DSAR) requires IT to manually query databases, CRMs, and payment gateways, taking weeks to compile.
> 
> **The Prompt:** 
> > *Create an automated data subject access request (DSAR) workflow: ingest requests via a secure form, verify identity, trigger data extraction scripts across Salesforce, Stripe, and AWS, compile into a secure ZIP, and deliver to the user.*
> 
> **🔗 Core Integrations:** `Secure Form` • `Salesforce` • `Stripe` • `AWS`
> ---

> ### 4. Third-Party Vendor Risk Assessment
> **The Problem:** Onboarding a new vendor without a proper security review exposes the company to supply-chain cyber attacks. Doing it manually slows down procurement.
> 
> **The Prompt:** 
> > *Design a workflow that automates vendor risk assessments: when a new vendor is added to the ERP, trigger a Security Questionnaire via Teams; upon completion, score the risk, and if high, block the vendor in the ERP until remediated.*
> 
> **🔗 Core Integrations:** `ERP` • `MS Teams / Forms` • `Risk Scoring Logic`
> ---

> ### 5. Insider Threat Detection & Lockout
> **The Problem:** Disgruntled employees downloading gigabytes of proprietary data before leaving the company often goes unnoticed until the damage is done.
> 
> **The Prompt:** 
> > *Build a workflow that monitors insider threat indicators: aggregate login anomalies from Okta and large data downloads from the DLP system; if a threshold is crossed, automatically lock the account and alert the CISO via PagerDuty.*
> 
> **🔗 Core Integrations:** `Okta` • `DLP System` • `PagerDuty`
> ---

> ### 6. Proactive Contract Renewal Management
> **The Problem:** Contracts auto-renew without renegotiation, or worse, expire without notice, leaving the business legally exposed or paying for unused software.
> 
> **The Prompt:** 
> > *Create an automated contract renewal workflow: monitor contract end dates in Ironclad; at 90 days out, automatically notify the account owner, generate a renewal quote, and route for legal review.*
> 
> **🔗 Core Integrations:** `Ironclad` • `Quote Generator` • `Email/Slack`
> ---

> ### 7. Continuous SOC2 Evidence Collection
> **The Problem:** Preparing for a SOC2 audit involves scrambling for weeks to manually pull access logs and system screenshots for auditors.
> 
> **The Prompt:** 
> > *Design a workflow that automates SOC2 evidence collection: weekly, pull access logs from Okta, change logs from GitHub, and backup logs from AWS, compile them into a standardized folder structure, and upload to the audit portal (Vanta).*
> 
> **🔗 Core Integrations:** `Okta` • `GitHub` • `AWS` • `Vanta (or similar)`
> ---

> ### 8. Automated IP Infringement Takedowns
> **The Problem:** Brand pirates steal trademarked images and logos across the web. Hunting them down and manually filing DMCA notices is an endless game of whack-a-mole.
> 
> **The Prompt:** 
> > *Build a workflow that handles automated IP infringement takedowns: monitor the web for unauthorized use of trademarks via a brand protection API, automatically generate DMCA notices, and submit them to the hosting providers.*
> 
> **🔗 Core Integrations:** `Brand Protection API` • `DMCA Generator` • `Email API`
> ---

> ### 9. Background Conflict of Interest Checks
> **The Problem:** Employees may accidentally have side-gigs or previous employment with a direct competitor or active vendor, creating severe conflicts of interest.
> 
> **The Prompt:** 
> > *Create a workflow that automates conflict of interest checks: when a new hire is onboarded, cross-reference their name and previous employers against a database of current clients and partners, flagging any overlaps for HR/Legal review.*
> 
> **🔗 Core Integrations:** `HRIS` • `CRM (Client Database)` • `Approval System`
> ---

> ### 10. Mandatory Policy Acknowledgment Tracking
> **The Problem:** When an employee handbook is updated, proving that all 1,000 employees actually read and signed the new policy is a logistical nightmare.
> 
> **The Prompt:** 
> > *Design a workflow that automates policy acknowledgment: when an HR policy is updated in Gusto, automatically push it to all employees via Slack/Email, track acknowledgments, and escalate to managers for those who haven't signed in 7 days.*
> 
> **🔗 Core Integrations:** `Gusto` • `Slack/Email` • `Tracking Database`
> ---
