import json
import os

workflows_data = [
    ("Marketing", "Abandoned Cart Recovery", "High cart abandonment rates on e-commerce store with no follow-up.", "Listen for abandoned cart webhooks, wait 1 hour, check if purchased, send targeted discount email via SendGrid.", ["Webhook", "Wait 1 Hour", "Check Purchase Status (API)", "SendGrid Email"]),
    ("Marketing", "Social Media Cross-Posting", "Manually posting the same content across Twitter, LinkedIn, and Facebook wastes time.", "Trigger on new RSS feed item, format message with OpenAI, post to Buffer API for distribution.", ["RSS Trigger", "OpenAI Formatter", "Buffer API"]),
    ("Marketing", "Lead Enrichment from Forms", "Inbound leads only provide email addresses, making qualification difficult.", "Trigger on form submission, query Clearbit API for company data, update HubSpot CRM.", ["Typeform Webhook", "Clearbit API", "HubSpot Update"]),
    ("Marketing", "Competitor Pricing Alert", "Competitors change prices without us knowing, leading to lost sales.", "Daily cron, scrape competitor pricing page, compare to DB, alert Slack channel if changed.", ["Cron (Daily)", "HTTP Scrape", "Compare Logic", "Slack Alert"]),
    ("Marketing", "Webinar Attendee Follow-up", "No automated follow-up for users who attended but didn't convert.", "Zoom webhook for webinar end, cross-reference CRM for deals, send personalized outreach sequence.", ["Zoom Webhook", "Query CRM", "If No Deal", "ActiveCampaign Sequence"]),
    
    ("Sales", "Contract Expiry Notification", "Sales team misses renewal dates, resulting in churn.", "Daily cron queries Salesforce for contracts expiring in 30 days, creates task for Account Manager, sends email.", ["Cron", "Salesforce Query", "Create Salesforce Task", "Email Account Manager"]),
    ("Sales", "High-Intent Page Visitor Alert", "Sales reps don't know when a hot lead visits the pricing page.", "Listen to segment events, filter for 'pricing' and 'logged in', alert account owner in Slack immediately.", ["Segment Webhook", "Filter Event", "Lookup Owner", "Slack Ping"]),
    ("Sales", "Automated Proposal Generation", "Manually typing proposals takes hours per prospect.", "Trigger when deal reaches 'Proposal' stage, fetch CRM data, populate Google Doc template, generate PDF, email.", ["CRM Webhook", "Fetch Deal Data", "Google Docs Template", "Convert to PDF", "Email PDF"]),
    ("Sales", "Stale Lead Re-engagement", "Thousands of cold leads sit in the database with zero touchpoints.", "Monthly cron queries leads untouched > 90 days, sends re-engagement plain-text email sequence.", ["Monthly Cron", "Query Cold Leads", "Send Re-engagement Email"]),
    ("Sales", "Post-Demo Feedback Loop", "Sales managers have no visibility into how demos went.", "Trigger 1 hr after calendar event 'Demo', send Typeform survey to prospect, push results to Slack channel.", ["Calendar Event End", "Wait 1 Hour", "Send Typeform", "Slack Alert"]),
    
    ("Customer Support", "VIP Ticket Escalation", "High-paying enterprise clients wait in the general support queue.", "Intercom webhook, check customer tier in Stripe, if Enterprise, route to PagerDuty and VIP Slack channel.", ["Intercom Webhook", "Check Stripe Tier", "If Enterprise", "PagerDuty Alert", "Slack VIP Channel"]),
    ("Customer Support", "Automated Refund Processing", "Issuing refunds takes multiple manual steps across Stripe and helpdesk.", "Tag 'Refund Approved' in Zendesk, trigger workflow to issue Stripe refund, update ticket, email customer.", ["Zendesk Tag Trigger", "Stripe Refund API", "Update Zendesk", "Email Customer"]),
    ("Customer Support", "Negative Review Auto-Triage", "1-star reviews go unnoticed for days.", "Monitor Trustpilot RSS/API, if 1 or 2 stars, create urgent Jira ticket, alert Customer Success Manager.", ["Trustpilot API", "Filter <= 2 Stars", "Jira Create Issue", "Email CSM"]),
    ("Customer Support", "Multilingual Support Translation", "Support agents can't read tickets in foreign languages.", "Ticket created webhook, use Google Translate API to detect and translate to English, add internal note to ticket.", ["Ticket Webhook", "Google Translate API", "Add Internal Note"]),
    ("Customer Support", "SLA Breach Auto-Escalation", "Tickets sit unanswered past the 24-hour SLA.", "Hourly cron queries tickets open > 24hrs without response, assigns to Support Manager, increases priority.", ["Hourly Cron", "Query Zendesk", "Update Assignee", "Update Priority"]),

    ("Finance", "Expense Receipt OCR", "Employees submit blurry receipts, slowing down reimbursements.", "Email trigger with attachment, AWS Textract extracts amount/merchant, logs to Google Sheets, alerts approver.", ["Email Trigger", "AWS Textract", "Google Sheets Add Row", "Slack Approver"]),
    ("Finance", "Failed Payment Dunning", "Credit cards fail and subscriptions cancel due to lack of follow-up.", "Stripe 'charge.failed' webhook, wait 2 days, retry, if fail again send reminder email sequence.", ["Stripe Webhook", "Wait 2 Days", "Retry Charge", "If Fail", "Send Reminder"]),
    ("Finance", "Daily Cash Balance Report", "CFO has to manually check 3 bank accounts every morning.", "Daily cron, fetch balances via Plaid API, aggregate data, send SMS to CFO.", ["Daily Cron", "Plaid API (Bank 1)", "Plaid API (Bank 2)", "Aggregate Data", "Twilio SMS"]),
    ("Finance", "New Vendor Onboarding", "Collecting W-9s and payment info is scattered in email.", "Form submission, create vendor in ERP (NetSuite), send DocuSign for W-9, notify Finance when signed.", ["Form Trigger", "NetSuite API", "Send DocuSign", "Wait for Signature", "Slack Alert"]),
    ("Finance", "Crypto Payment Reconciliation", "Crypto invoice payments require manual matching on block explorers.", "Coinbase Commerce webhook, find matching invoice ID in Xero, mark as paid.", ["Coinbase Webhook", "Query Xero Invoice", "Mark Xero Paid"]),

    ("HR", "Employee Offboarding Revocation", "Terminated employees retain access to SaaS apps causing security risks.", "Workday termination webhook, trigger Okta deprovisioning, remove from GitHub, remove from Slack.", ["Workday Webhook", "Okta Deprovision", "GitHub Remove", "Slack Remove"]),
    ("HR", "Candidate Interview Reminders", "Candidates miss interviews due to forgotten calendar invites.", "Cron checks ATS for interviews next day, sends automated SMS and email reminder.", ["Cron (Daily)", "ATS Query", "Twilio SMS", "Email"]),
    ("HR", "New Hire Swag Fulfillment", "HR forgets to send t-shirts to new remote hires.", "When candidate marked 'Hired', send Typeform for shirt size/address, upon completion trigger Printful API.", ["ATS Trigger", "Send Typeform", "Wait for Form", "Printful Order API"]),
    ("HR", "PTO Approval Sync", "Approved PTO in HRIS isn't reflected on Google Calendar/Slack.", "Gusto PTO approved webhook, create 'OOO' event on Google Calendar, set Slack status to '🌴'.", ["Gusto Webhook", "Google Calendar Create", "Slack Set Status"]),
    ("HR", "Employee Birthday Celebrations", "HR misses employee birthdays causing morale dips.", "Daily cron checks HRIS for birthdays matching today, posts congratulatory GIF in general Slack channel.", ["Daily Cron", "Query HRIS", "Filter Today", "Post Slack GIF"]),

    ("IT & Ops", "Server Outage Remediation", "Servers crash in the middle of the night and require manual restart.", "Datadog critical alert webhook, trigger AWS Lambda to reboot EC2 instance, log to Jira.", ["Datadog Webhook", "AWS EC2 Reboot", "Jira Create Incident"]),
    ("IT & Ops", "Shadow IT Detection", "Employees sign up for unauthorized apps using company email.", "Monitor Google Workspace admin logs, if OAuth grant to unapproved app, email IT security and revoke.", ["GSuite Logs Cron", "Check App Whitelist", "If Unauthorized", "Revoke OAuth", "Email Security"]),
    ("IT & Ops", "Database Backup Verification", "Backups run but no one checks if the file size is valid.", "Trigger after backup script finishes, check AWS S3 file size, if < 1GB alert engineering channel.", ["S3 Object Created", "Check File Size", "If < 1GB", "Slack Alert"]),
    ("IT & Ops", "Hardware Lifecycle Replacement", "Laptops expire warranty but IT isn't tracking them.", "Monthly cron queries MDM (Jamf) for devices > 3 years old, auto-creates Jira tickets to replace.", ["Monthly Cron", "Query Jamf", "Filter > 3 Years", "Jira Create Ticket"]),
    ("IT & Ops", "New Domain DNS Setup", "Configuring DNS records for new marketing domains is tedious.", "Form submitted with domain name, call Cloudflare API to provision standard MX/TXT records.", ["Form Webhook", "Cloudflare API (MX)", "Cloudflare API (TXT)"]),

    ("Product", "Jira to GitHub Sync", "Product managers use Jira but devs use GitHub, causing siloes.", "Jira issue created webhook, create matching GitHub issue, paste GitHub link back to Jira.", ["Jira Webhook", "GitHub Create Issue", "Jira Update Issue"]),
    ("Product", "Feature Request Aggregation", "User requests are scattered across Intercom, email, and Twitter.", "Zapier/n8n webhook receives requests from multiple sources, uses AI to extract core feature, adds to Productboard.", ["Multi-Webhook", "OpenAI Extraction", "Productboard Create"]),
    ("Product", "App Store Review Alerts", "New iOS app reviews aren't monitored in real-time.", "App Store RSS feed trigger, if review < 3 stars, translate to English, post to #product-feedback Slack.", ["App Store RSS", "Filter < 3 Stars", "Google Translate", "Slack Post"]),
    ("Product", "Release Notes Generation", "Writing release notes manually takes hours.", "Trigger on GitHub release, fetch merged PR descriptions, use LLM to summarize into user-friendly notes, email users.", ["GitHub Release", "Fetch PRs", "LLM Summarize", "Mailchimp Broadcast"]),
    ("Product", "Beta Tester Invite Automation", "Managing TestFlight invites is a manual spreadsheet process.", "User fills out beta form, add to Airtable, trigger Apple App Store Connect API to invite user.", ["Typeform Webhook", "Airtable Add", "App Store Connect API"]),

    ("Legal", "NDA Counter-Signature", "Sales reps send NDAs but legal forgets to sign their half.", "DocuSign completed by prospect webhook, auto-route to Legal GC for counter-signature, save to Box.", ["DocuSign Webhook", "Route to GC", "Wait for GC Sign", "Box Upload"]),
    ("Legal", "Privacy Request (DSAR) Deletion", "GDPR deletion requests are manual and prone to missing databases.", "Data deletion form submitted, query CRM, Helpdesk, and Mailchimp, delete user from all 3, email confirmation.", ["Form Webhook", "Delete CRM", "Delete Helpdesk", "Delete Mailchimp", "Email Confirmation"]),
    ("Legal", "Contract Clause Flagging", "Non-standard clauses in incoming vendor contracts are missed.", "Email with contract attachment, Document AI extracts text, scans for 'unlimited liability', flags to legal.", ["Email Trigger", "Extract Text", "Scan for Keywords", "Flag to Legal"]),

    ("E-Commerce", "Low Stock Hidden Item", "Items run out of stock but remain visible on Shopify.", "Shopify inventory webhook, if quantity == 0, update product status to draft.", ["Shopify Webhook", "Check Quantity", "If 0", "Update Product Draft"]),
    ("E-Commerce", "Fraudulent Order Cancellation", "High-risk orders slip through and cost chargebacks.", "Stripe radar high-risk webhook, immediately cancel order in Shopify, refund payment, ban customer email.", ["Stripe Radar Webhook", "Cancel Shopify Order", "Stripe Refund", "Ban Customer"]),
    ("E-Commerce", "Post-Purchase Upsell", "Customers buy printers but aren't offered ink.", "Order paid webhook, if items include 'Printer', wait 3 days, send email offering 10% off ink.", ["Order Webhook", "Check Items", "Wait 3 Days", "Send Upsell Email"]),
    ("E-Commerce", "Shipping Delay Notification", "Carriers delay shipments and customers complain.", "Daily cron checks Shippo/Easypost for 'delayed' status, sends proactive apology SMS to customer.", ["Daily Cron", "Query Shipping API", "Filter Delayed", "Twilio SMS"]),
    
    ("Operations", "Facility Temperature Alert", "Server room or warehouse HVAC fails, ruining inventory.", "IoT temp sensor webhook, if > 80F, trigger alarm, call facility manager via Twilio Voice.", ["IoT Webhook", "Check Temp > 80F", "Trigger Alarm API", "Twilio Voice Call"]),
    ("Operations", "Vehicle Fleet Mileage Tracker", "Manual mileage logging for delivery vehicles is inaccurate.", "Geotab/Telematics API daily pull, log daily distance to Google Sheets, if > 10,000 miles, schedule maintenance.", ["Daily Cron", "Telematics API", "Log to Sheets", "Maintenance Logic"]),
    ("Operations", "Franchise Royalty Calculation", "Calculating 5% royalties for 50 franchises is a manual spreadsheet nightmare.", "Monthly cron, fetch gross sales from POS API for all locations, calculate 5%, generate Stripe Invoice.", ["Monthly Cron", "POS API", "Calculate Royalties", "Create Stripe Invoices"]),

    ("Security", "Phishing Link Detonation", "Employees forward suspicious emails to IT, who manually check links.", "Email trigger to security inbox, extract URLs, scan via VirusTotal API, reply with safety status.", ["Email Webhook", "Extract URLs", "VirusTotal Scan", "Reply to User"]),
    ("Security", "Failed Login Lockout Alert", "Brute force attacks go unnoticed until it's too late.", "Okta/Auth0 failed login webhook, if > 10 fails in 5 mins from same IP, block IP in Cloudflare.", ["Okta Webhook", "Check Count", "If > 10", "Cloudflare Block IP"]),
    ("Security", "Public S3 Bucket Detection", "Developers accidentally make AWS S3 buckets public.", "AWS CloudTrail webhook for PutBucketAcl, check if 'PublicRead', if true, revert to private and alert SecOps.", ["CloudTrail Webhook", "Check ACL", "If Public", "Revert to Private", "Slack SecOps"]),

    ("Agency/Freelance", "Client Proposal to Project Sync", "When a client signs a proposal, the project board must be set up manually.", "PandaDoc signature webhook, create Asana Project from template, create Slack channel, invite client.", ["PandaDoc Webhook", "Create Asana Project", "Create Slack Channel", "Invite Client"]),
    ("Agency/Freelance", "Automated Time Tracking Invoicing", "Freelancers forget to bill for logged hours.", "End of month cron, aggregate Toggl hours for client, generate Invoice in QuickBooks, send via email.", ["Monthly Cron", "Toggl API", "QuickBooks Invoice", "Send Email"])
]

def generate_50_workflows():
    workflows = []
    
    for i, data in enumerate(workflows_data, start=1):
        domain, name, problem, solution, node_names = data
        
        nodes_out = []
        y_pos = 200
        x_pos = 250
        node_map = {}

        for j, n_name in enumerate(node_names):
            # Assign dummy node types
            node_type = "n8n-nodes-base.httpRequest"
            n_lower = n_name.lower()
            if "webhook" in n_lower or "trigger" in n_lower or "cron" in n_lower:
                node_type = "n8n-nodes-base.webhook"
                if "cron" in n_lower:
                    node_type = "n8n-nodes-base.cron"
            elif "slack" in n_lower or "email" in n_lower or "sms" in n_lower or "call" in n_lower:
                node_type = "n8n-nodes-base.slack"
            elif "if" in n_lower or "filter" in n_lower:
                node_type = "n8n-nodes-base.if"
            elif "wait" in n_lower:
                node_type = "n8n-nodes-base.wait"
            elif "openai" in n_lower or "llm" in n_lower:
                node_type = "n8n-nodes-base.openAi"
            
            nodes_out.append({
                "parameters": {},
                "id": f"node-{j}",
                "name": n_name,
                "type": node_type,
                "typeVersion": 1,
                "position": [x_pos, y_pos]
            })
            node_map[n_name] = n_name
            x_pos += 200
            if x_pos > 850:
                x_pos = 250
                y_pos += 200

        connections_out = {}
        for k in range(len(node_names) - 1):
            src = node_names[k]
            tgt = node_names[k+1]
            if src not in connections_out:
                connections_out[src] = {"main": [[]]}
            connections_out[src]["main"][0].append({
                "node": tgt,
                "type": "main",
                "index": 0
            })

        workflow = {
            "name": f"{i:03d} - {name}",
            "nodes": nodes_out,
            "connections": connections_out,
            "active": False,
            "settings": {}
        }
        workflows.append((i, domain, name, problem, solution, workflow))
            
    return workflows

if __name__ == "__main__":
    out_dir = r"C:\Users\laptopzone\.gemini\antigravity\scratch\n8n-business-problems\templates"
    os.makedirs(out_dir, exist_ok=True)
    
    workflows = generate_50_workflows()
    
    # Save the JSON templates
    for i, domain, name, problem, solution, wf_data in workflows:
        safe_name = name.lower().replace(' ', '-').replace('/', '-')
        filename = f"{i:03d}-{safe_name}.json"
        filepath = os.path.join(out_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(wf_data, f, indent=2)
        print(f"Generated {filename}")
        
    # Also save the metadata for the README generator
    metadata = [{"id": w[0], "domain": w[1], "name": w[2], "problem": w[3], "solution": w[4], "filename": f"{w[0]:03d}-{w[2].lower().replace(' ', '-').replace('/', '-')}.json"} for w in workflows]
    with open("metadata.json", "w") as f:
        json.dump(metadata, f)
