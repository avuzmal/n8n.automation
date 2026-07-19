# 01. FinOps & Revenue Operations

> ### 1. Multi-Currency Revenue Recognition & Reporting
> **The Problem:** Finance teams waste hours manually fetching daily FX rates, reconciling discrepancies across global sales, and compiling month-end reports, leading to delayed revenue recognition and compliance risks.
> 
> **The Prompt:** 
> > *Build an n8n workflow connecting SAP ERP, Stripe, and Salesforce to automate multi-currency revenue recognition, including automated daily FX rate fetching via API, discrepancy flagging in Slack, and generating a monthly PDF report via Documint.*
> 
> **🔗 Core Integrations:** `SAP ERP` • `Stripe` • `Salesforce` • `Documint` • `Slack`
> ---

> ### 2. Automated Budget vs. Actuals Cloud Cost Monitoring
> **The Problem:** Cloud spend often spirals out of control before FinOps can catch it. Manual comparison between AWS bills and NetSuite budgets is too slow for agile cost management.
> 
> **The Prompt:** 
> > *Design a workflow that monitors AWS Cost Explorer API, compares actuals vs. budgeted spend in NetSuite, and automatically triggers a Jira ticket for the FinOps team if variance exceeds 5%, including a Slack summary.*
> 
> **🔗 Core Integrations:** `AWS Cost Explorer` • `NetSuite` • `Jira` • `Slack`
> ---

> ### 3. Intelligent Accounts Payable Automation
> **The Problem:** Processing hundreds of inbound invoices manually is prone to human error, missed PO matching, and delayed payment approvals, straining vendor relationships.
> 
> **The Prompt:** 
> > *Create an automated accounts payable workflow that ingests invoices from a dedicated email inbox, uses OCR (via AWS Textract) to extract line items, matches them against POs in Oracle, and routes for multi-tier approval in DocuSign based on amount thresholds.*
> 
> **🔗 Core Integrations:** `Email Inbox` • `AWS Textract` • `Oracle` • `DocuSign`
> ---

> ### 4. Dynamic Subscription Dunning & Retention
> **The Problem:** Failed payments lead to involuntary churn. Handling collections manually is inefficient and results in poor customer experiences when services are cut without proper warning.
> 
> **The Prompt:** 
> > *Build a subscription dunning workflow integrating Stripe, Intercom, and Salesforce: on failed payment, pause service via API, trigger a personalized SMS/Email sequence, update CRM opportunity stage, and create a high-priority support ticket if unresolved in 48 hours.*
> 
> **🔗 Core Integrations:** `Stripe` • `Intercom` • `Salesforce` • `SMS/Email API`
> ---

> ### 5. Omnichannel Sales Aggregation & Data Warehousing
> **The Problem:** Aggregating daily sales data across multiple platforms (Shopify, Amazon, custom portals) for accurate BI analysis is tedious and requires constant data engineering overhead.
> 
> **The Prompt:** 
> > *Design a workflow that aggregates daily sales data from Shopify, Amazon, and custom APIs, transforms it using complex JavaScript nodes, and pushes it to a Snowflake data warehouse via SFTP, triggering a dbt run upon completion.*
> 
> **🔗 Core Integrations:** `Shopify` • `Amazon` • `Snowflake` • `dbt` • `SFTP`
> ---

> ### 6. Corporate Card Expense Reconciliation
> **The Problem:** Employees delay submitting receipts, and finance struggles to match them against corporate card statements, creating massive backlogs at month-end.
> 
> **The Prompt:** 
> > *Create an automated expense reconciliation workflow that pulls corporate card transactions from Brex, matches them against receipts uploaded to a SharePoint folder using AI vision, and posts approved entries to QuickBooks Online.*
> 
> **🔗 Core Integrations:** `Brex` • `SharePoint` • `AI Vision` • `QuickBooks Online`
> ---

> ### 7. Crypto Treasury Real-Time P&L Tracking
> **The Problem:** Managing corporate crypto treasuries requires constant monitoring. Sudden market shifts can cause massive unnotified losses without real-time tracking systems in place.
> 
> **The Prompt:** 
> > *Build a workflow that monitors crypto treasury wallets via Etherscan API, calculates daily P&L based on real-time oracle prices, and updates a Notion dashboard while alerting the CFO via PagerDuty if daily loss exceeds a set threshold.*
> 
> **🔗 Core Integrations:** `Etherscan API` • `Notion` • `PagerDuty`
> ---

> ### 8. Fraud-Resistant Vendor Payment Gateway
> **The Problem:** Vendor bank detail spoofing is a common fraud vector. Verifying payment details and compiling bank transfer files manually exposes the company to massive financial risk.
> 
> **The Prompt:** 
> > *Design a vendor payment automation workflow that pulls approved invoices from Coupa, checks vendor bank details against a sanitized fraud database, formats BACS/ACH files, and uploads them to the banking portal via SFTP.*
> 
> **🔗 Core Integrations:** `Coupa` • `Fraud Database` • `SFTP / Banking Portal`
> ---

> ### 9. Automated Month-End Close & Board Reporting
> **The Problem:** The month-end close process requires aggregating data, running complex variance calculations, and formatting board decks, taking days of manual accounting work.
> 
> **The Prompt:** 
> > *Create a workflow that automates month-end close tasks: pulling trial balances from Xero, running variance analysis via Python script nodes, and generating a comprehensive Excel report distributed to the board via secure email.*
> 
> **🔗 Core Integrations:** `Xero` • `Python` • `Excel generation` • `Secure Email`
> ---

> ### 10. Headless Checkout Tax Liability Sync
> **The Problem:** Global tax compliance (nexus rules, VAT) is notoriously difficult. Syncing e-commerce tax calculations to the ERP often involves messy CSV uploads and data lags.
> 
> **The Prompt:** 
> > *Build an automated tax calculation workflow that integrates Avalara with a custom headless checkout, handling complex nexus rules, and automatically syncing tax liability journals to the general ledger in Workday.*
> 
> **🔗 Core Integrations:** `Avalara` • `Headless Checkout API` • `Workday`
> ---
