# 02. HR & Talent Acquisition

> ### 1. Seamless Zero-Touch Employee Onboarding
> **The Problem:** Onboarding requires coordinating accounts, hardware, and meetings across multiple disconnected systems, often leaving new hires waiting days for full access.
> 
> **The Prompt:** 
> > *Design an automated onboarding workflow triggered by a DocuSign completion: create accounts in Okta, assign hardware in SnipeIT, provision Slack channels, schedule intro meetings via Calendly, and trigger a 30-60-90 day check-in sequence in Lattice.*
> 
> **🔗 Core Integrations:** `DocuSign` • `Okta` • `SnipeIT` • `Slack` • `Calendly` • `Lattice`
> ---

> ### 2. Secure Offboarding & Data Leakage Prevention
> **The Problem:** Missed offboarding steps result in ex-employees retaining access to sensitive corporate data, creating severe security and compliance risks.
> 
> **The Prompt:** 
> > *Build an offboarding automation that revokes Okta access, triggers a secure data wipe request to IT via Jira, calculates final PTO payout in Gusto, and sends a secure offboarding survey via Typeform, ensuring zero data leakage.*
> 
> **🔗 Core Integrations:** `Okta` • `Jira` • `Gusto` • `Typeform`
> ---

> ### 3. Automated LinkedIn Talent Sourcing & Screening
> **The Problem:** Recruiters spend too much time manually sourcing candidates, researching profiles, and coordinating initial calls, slowing down the hiring pipeline.
> 
> **The Prompt:** 
> > *Create a workflow that scrapes LinkedIn for specific skill sets, enriches candidate profiles via Clearbit, scores them using a custom AI prompt, and automatically schedules initial screening calls via Calendly for top 10% matches.*
> 
> **🔗 Core Integrations:** `LinkedIn` • `Clearbit` • `AI` • `Calendly`
> ---

> ### 4. 360-Degree Performance Review Aggregation
> **The Problem:** Performance reviews require managers to hunt down data across HR systems and chat apps, making the process biased and incredibly time-consuming.
> 
> **The Prompt:** 
> > *Design a performance review automation that pulls OKR completion data from Lattice, aggregates peer feedback from Slack (using sentiment analysis), and generates a draft performance summary for managers in Notion.*
> 
> **🔗 Core Integrations:** `Lattice` • `Slack` • `Notion` • `Sentiment Analysis AI`
> ---

> ### 5. Proactive Employee Sentiment & Churn Risk Alerting
> **The Problem:** HR often finds out about low team morale or cultural issues too late, resulting in costly employee turnover that could have been prevented.
> 
> **The Prompt:** 
> > *Build a workflow that monitors employee sentiment via weekly Culture Amp pulses; if sentiment drops below a threshold in a specific department, automatically alert the HRBP and schedule a focus group via Outlook.*
> 
> **🔗 Core Integrations:** `Culture Amp` • `Outlook` • `Slack/Teams`
> ---

> ### 6. Automated Visa & Relocation Compliance
> **The Problem:** Missing a visa or passport expiration date can result in illegal working statuses or halted relocations, exposing the company to massive legal fines.
> 
> **The Prompt:** 
> > *Create an automated visa/relocation workflow that tracks passport expiration dates in BambooHR, triggers alerts 90 days out, generates required legal documents via PDFMonkey, and creates a tracking board in Asana.*
> 
> **🔗 Core Integrations:** `BambooHR` • `PDFMonkey` • `Asana`
> ---

> ### 7. Frictionless Internal Mobility & Transfers
> **The Problem:** Internal job applications often bypass current managers or ignore historical performance data, causing internal friction and misaligned expectations.
> 
> **The Prompt:** 
> > *Design a workflow that automates internal mobility: when an employee applies for an internal role via Workday, check their tenure and performance ratings, and automatically notify the hiring manager and current manager.*
> 
> **🔗 Core Integrations:** `Workday` • `Email/Slack`
> ---

> ### 8. Mandatory Compliance Training Enforcement
> **The Problem:** Ensuring 100% compliance on mandatory training (like security or harassment) is difficult, and manual chasing by HR is ineffective.
> 
> **The Prompt:** 
> > *Build an automated learning & development workflow that assigns mandatory compliance training in Docebo based on the employee's department and role, tracking completion and escalating to HR via Slack if overdue.*
> 
> **🔗 Core Integrations:** `Docebo` • `Slack` • `HRIS (e.g., BambooHR)`
> ---

> ### 9. Intelligent Interview Scheduling & Prep
> **The Problem:** Interview coordination is the biggest bottleneck in hiring. Candidates drop off when scheduling takes too long, and interviewers often show up unprepared.
> 
> **The Prompt:** 
> > *Create a workflow that integrates Greenhouse with Slack to automate interview scheduling: parse interviewer availability from Google Calendar, send custom booking links to candidates, and prep interviewers with candidate resumes.*
> 
> **🔗 Core Integrations:** `Greenhouse` • `Slack` • `Google Calendar`
> ---

> ### 10. Pre-Processing Payroll Anomaly Detection
> **The Problem:** Payroll mistakes (incorrect raises, wrong bank details) are catastrophic for employee trust and very difficult to reverse once processed.
> 
> **The Prompt:** 
> > *Design a payroll anomaly detection workflow that compares current month payroll draft in ADP against the previous month, flagging any salary changes >5% or new bank accounts for manual HR review before processing.*
> 
> **🔗 Core Integrations:** `ADP` • `Approval System (Jira/Email)`
> ---
