# 06. ITSM & DevOps

> ### 1. Zero-Touch Incident War Room Creation
> **The Problem:** When an outage occurs, engineers waste the first 15 critical minutes manually creating Jira tickets, spinning up Slack channels, and digging through PagerDuty schedules to find who is on-call.
> 
> **The Prompt:** 
> > *Design an n8n workflow that automates incident response: when a PagerDuty alert fires, automatically create a Jira incident, spin up a dedicated Slack war room, page the on-call engineer, and start a timer for SLA tracking.*
> 
> **🔗 Core Integrations:** `PagerDuty` • `Jira` • `Slack`
> ---

> ### 2. Automated Role-Based Access Provisioning
> **The Problem:** IT helpdesks get bogged down manually granting software licenses based on ServiceNow tickets, slowing down employee productivity and risking over-provisioning.
> 
> **The Prompt:** 
> > *Build a workflow that automates employee access requests: ingest requests from ServiceNow, check the user's role in Okta, automatically provision standard access, and route non-standard access to the data owner for approval.*
> 
> **🔗 Core Integrations:** `ServiceNow` • `Okta` • `Software APIs`
> ---

> ### 3. AI-Assisted CI/CD Failure Triage
> **The Problem:** When a build fails in CI/CD, developers spend hours digging through massive error logs just to find a simple missing dependency or syntax error.
> 
> **The Prompt:** 
> > *Create an automated CI/CD notification workflow: when a GitHub Actions build fails, parse the error logs, use AI to suggest a fix, post the summary to the #dev-ops Slack channel, and assign a Jira bug to the commit author.*
> 
> **🔗 Core Integrations:** `GitHub Actions` • `AI` • `Slack` • `Jira`
> ---

> ### 4. Proactive SSL Expiration Prevention
> **The Problem:** Expired SSL certificates cause immediate customer-facing outages and security warnings, yet they are often tracked poorly in manual spreadsheets.
> 
> **The Prompt:** 
> > *Design a workflow that monitors SSL certificates via API; if a certificate expires in <14 days, automatically create a high-priority Jira ticket, alert the DevOps team via PagerDuty, and update the status in Confluence.*
> 
> **🔗 Core Integrations:** `SSL Checker API` • `Jira` • `PagerDuty` • `Confluence`
> ---

> ### 5. Self-Healing Database Backup Verification
> **The Problem:** Backups are scheduled, but rarely tested. A corrupted backup is useless during a ransomware attack or data loss event.
> 
> **The Prompt:** 
> > *Build a workflow that automates database backup verification: trigger a daily backup in AWS RDS, run a checksum validation script, and if it fails, automatically restore from the last known good backup and alert the DBA.*
> 
> **🔗 Core Integrations:** `AWS RDS` • `Checksum Script` • `Alerting (Slack/Email)`
> ---

> ### 6. CMDB-Aware Vulnerability Routing
> **The Problem:** Security scanners (like Qualys) dump thousands of vulnerabilities, but security teams don't know who owns the vulnerable asset to route the fix to.
> 
> **The Prompt:** 
> > *Create an automated vulnerability management workflow: ingest scan results from Qualys, cross-reference with the CMDB in ServiceNow to identify the asset owner, and automatically create remediation tickets based on CVSS severity.*
> 
> **🔗 Core Integrations:** `Qualys` • `ServiceNow CMDB` • `Ticketing System`
> ---

> ### 7. Automated Non-Prod Cloud Cost Optimization
> **The Problem:** Developers leave expensive dev/test environments running 24/7 over the weekend, driving up AWS/Azure bills unnecessarily.
> 
> **The Prompt:** 
> > *Design a workflow that automates cloud cost optimization: pull AWS Compute Optimizer recommendations, automatically downsize dev/test instances during non-working hours via Lambda, and report savings in a weekly Slack digest.*
> 
> **🔗 Core Integrations:** `AWS Compute Optimizer` • `AWS Lambda` • `Slack`
> ---

> ### 8. Secure Slackbot Password Resets
> **The Problem:** "I forgot my password" is the #1 IT support ticket, consuming massive amounts of Level 1 helpdesk time.
> 
> **The Prompt:** 
> > *Build a workflow that handles automated password resets: ingest requests via Slackbot, verify identity via Okta MFA prompt, reset the password in Active Directory, and send the temporary password via secure email.*
> 
> **🔗 Core Integrations:** `Slackbot` • `Okta MFA` • `Active Directory` • `Email`
> ---

> ### 9. Digital Signature Release Approvals
> **The Problem:** CAB (Change Advisory Board) approvals are often a rubber-stamp process delayed by waiting for managers to log into the ITSM tool to hit "Approve".
> 
> **The Prompt:** 
> > *Create a workflow that automates software deployment approvals: when a release is staged in Jenkins, automatically notify the change advisory board (CAB) via email with a link to the release notes, and proceed only upon digital signature.*
> 
> **🔗 Core Integrations:** `Jenkins` • `Email` • `Digital Signature API`
> ---

> ### 10. Zero-Touch MDM Hardware Provisioning
> **The Problem:** Setting up a new laptop manually with corporate software takes hours of IT time per employee, delaying their Day 1 productivity.
> 
> **The Prompt:** 
> > *Design a workflow that syncs hardware inventory: when a new laptop is scanned into SnipeIT, automatically create a user profile in Jamf, generate a pre-stage enrollment profile, and email the setup instructions to the employee.*
> 
> **🔗 Core Integrations:** `SnipeIT` • `Jamf` • `Email`
> ---
