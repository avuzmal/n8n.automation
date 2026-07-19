import json
import os

domains = [
    "Sales & CRM",
    "HR & Recruiting",
    "Finance & Accounting",
    "IT & Ops",
    "Customer Support"
]

# 20 Architectural Patterns
architectures = [
    {
        "pattern": "Intelligent Triage & Routing",
        "nodes": ["Incoming Webhook", "AI Sentiment/Category Parser", "Switch/Router", "Create Ticket", "Notify Team", "Assign Owner"],
        "connections": {
            "Incoming Webhook": ["AI Sentiment/Category Parser"],
            "AI Sentiment/Category Parser": ["Switch/Router"],
            "Switch/Router": ["Create Ticket", "Notify Team"],
            "Create Ticket": ["Assign Owner"]
        },
        "domain_flavors": {
            "Sales & CRM": "Inbound Lead Intelligent Triage & CRM Routing",
            "HR & Recruiting": "Employee Request Intelligent Triage to HRBPs",
            "Finance & Accounting": "Expense Report Discrepancy Triage & Routing",
            "IT & Ops": "IT Helpdesk Intelligent Ticket Triage & Escalation",
            "Customer Support": "High-Priority Customer Issue Sentiment Triage"
        }
    },
    {
        "pattern": "Automated Document Extraction",
        "nodes": ["Email Trigger (Attachment)", "OCR / Document AI", "Validate Data Logic", "Update Database", "Upload to Cloud Storage", "Send Confirmation"],
        "connections": {
            "Email Trigger (Attachment)": ["OCR / Document AI"],
            "OCR / Document AI": ["Validate Data Logic"],
            "Validate Data Logic": ["Update Database"],
            "Update Database": ["Upload to Cloud Storage", "Send Confirmation"]
        },
        "domain_flavors": {
            "Sales & CRM": "Automated Purchase Order Extraction & CRM Entry",
            "HR & Recruiting": "Resume Parsing & Applicant Tracking System Entry",
            "Finance & Accounting": "Automated Invoice OCR & ERP Entry",
            "IT & Ops": "Vendor Contract Extraction & Metadata Tagging",
            "Customer Support": "Customer Warranty Claim Document Processing"
        }
    },
    {
        "pattern": "Scheduled Health/Status Report",
        "nodes": ["Cron Trigger (Weekly)", "Aggregate Data via API", "Data Aggregation/Math", "Generate PDF/HTML", "Email Stakeholders", "Log to Slack"],
        "connections": {
            "Cron Trigger (Weekly)": ["Aggregate Data via API"],
            "Aggregate Data via API": ["Data Aggregation/Math"],
            "Data Aggregation/Math": ["Generate PDF/HTML"],
            "Generate PDF/HTML": ["Email Stakeholders", "Log to Slack"]
        },
        "domain_flavors": {
            "Sales & CRM": "Weekly Sales Pipeline & Forecasting Report Generator",
            "HR & Recruiting": "Weekly Department Headcount & Attrition Report",
            "Finance & Accounting": "Automated Cash Flow & Burn Rate Weekly Report",
            "IT & Ops": "Infrastructure Uptime & Incident Weekly Summary",
            "Customer Support": "CSAT & Ticket Resolution Weekly Health Report"
        }
    },
    {
        "pattern": "Multi-Step Approval Workflow",
        "nodes": ["Form Trigger", "Check Threshold Limit", "Manager Approval Wait", "If Approved", "Execute Action", "Notify Requester"],
        "connections": {
            "Form Trigger": ["Check Threshold Limit"],
            "Check Threshold Limit": ["Manager Approval Wait"],
            "Manager Approval Wait": ["If Approved"],
            "If Approved": ["Execute Action", "Notify Requester"]
        },
        "domain_flavors": {
            "Sales & CRM": "Enterprise Deal Discount Multi-Step Approval",
            "HR & Recruiting": "New Hire Offer Letter & Comp Band Approval",
            "Finance & Accounting": "High-Value Capital Expenditure (CapEx) Approval",
            "IT & Ops": "Production Database Access / Privilege Approval",
            "Customer Support": "Customer Refund / Credit Limit Approval Workflow"
        }
    },
    {
        "pattern": "Data Synchronization Engine",
        "nodes": ["Schedule Trigger", "Fetch Source Data", "Fetch Target Data", "Compare & Diff (Python)", "Bulk Create/Update", "Log Sync Results"],
        "connections": {
            "Schedule Trigger": ["Fetch Source Data", "Fetch Target Data"],
            "Fetch Source Data": ["Compare & Diff (Python)"],
            "Fetch Target Data": ["Compare & Diff (Python)"],
            "Compare & Diff (Python)": ["Bulk Create/Update"],
            "Bulk Create/Update": ["Log Sync Results"]
        },
        "domain_flavors": {
            "Sales & CRM": "CRM to Marketing Automation Tool Sync Engine",
            "HR & Recruiting": "HRIS to Active Directory / Identity Sync",
            "Finance & Accounting": "Stripe to ERP / Ledger Data Sync Engine",
            "IT & Ops": "Asset Management Tool to MDM Sync Engine",
            "Customer Support": "Support Desk to CRM Contact Data Sync"
        }
    },
    {
        "pattern": "Proactive Anomaly Detection",
        "nodes": ["Data Stream Trigger", "Calculate Rolling Average", "Anomaly Detection AI", "Is Anomaly?", "Trigger PagerDuty", "Quarantine/Hold Action"],
        "connections": {
            "Data Stream Trigger": ["Calculate Rolling Average"],
            "Calculate Rolling Average": ["Anomaly Detection AI"],
            "Anomaly Detection AI": ["Is Anomaly?"],
            "Is Anomaly?": ["Trigger PagerDuty", "Quarantine/Hold Action"]
        },
        "domain_flavors": {
            "Sales & CRM": "Sudden Drop in E-commerce Conversion Rate Alert",
            "HR & Recruiting": "Abnormal Mass Login / Access Attempts Detection",
            "Finance & Accounting": "Fraudulent Expense / Twin Invoice Detection",
            "IT & Ops": "Server CPU/RAM Spikes Proactive Anomaly Alert",
            "Customer Support": "Sudden Spike in Specific Bug Reports Detection"
        }
    },
    {
        "pattern": "Onboarding/Offboarding Orchestrator",
        "nodes": ["Status Change Webhook", "Delay / Timer", "Provisioning APIs", "Send Welcome/Exit Email", "Schedule Follow-up", "Update Directory"],
        "connections": {
            "Status Change Webhook": ["Delay / Timer", "Provisioning APIs"],
            "Provisioning APIs": ["Send Welcome/Exit Email", "Update Directory"],
            "Delay / Timer": ["Schedule Follow-up"]
        },
        "domain_flavors": {
            "Sales & CRM": "New Client Automated Onboarding & Welcome Sequence",
            "HR & Recruiting": "Employee Day 1 Account Provisioning Orchestrator",
            "Finance & Accounting": "New Vendor Payment Setup & Verification Orchestrator",
            "IT & Ops": "Developer Workstation & Software Provisioning",
            "Customer Support": "Enterprise Customer VIP Support Onboarding"
        }
    },
    {
        "pattern": "Feedback Loop & Auto-Responder",
        "nodes": ["Survey Response Webhook", "Extract Keyword/Score", "NPS Switch", "Auto-Reply Email", "Alert Account Manager", "Add to Retargeting"],
        "connections": {
            "Survey Response Webhook": ["Extract Keyword/Score"],
            "Extract Keyword/Score": ["NPS Switch"],
            "NPS Switch": ["Auto-Reply Email", "Alert Account Manager", "Add to Retargeting"]
        },
        "domain_flavors": {
            "Sales & CRM": "Post-Sale NPS Survey Loop & Cross-Sell Trigger",
            "HR & Recruiting": "Candidate Interview Experience Survey Auto-Responder",
            "Finance & Accounting": "Invoice Payment Friction Survey Loop",
            "IT & Ops": "Internal IT Helpdesk Satisfaction Loop & Alert",
            "Customer Support": "Ticket Resolution CSAT Auto-Responder & Escalation"
        }
    },
    {
        "pattern": "Predictive Scoring & Tagging",
        "nodes": ["Entity Created Webhook", "Fetch Historic Data", "Scoring Algorithm (Code)", "Apply Tags in System", "If High Score", "Alert Specialist"],
        "connections": {
            "Entity Created Webhook": ["Fetch Historic Data"],
            "Fetch Historic Data": ["Scoring Algorithm (Code)"],
            "Scoring Algorithm (Code)": ["Apply Tags in System", "If High Score"],
            "If High Score": ["Alert Specialist"]
        },
        "domain_flavors": {
            "Sales & CRM": "Predictive Lead Scoring & High-Intent Tagging",
            "HR & Recruiting": "Applicant Flight Risk / Culture Fit Predictive Scoring",
            "Finance & Accounting": "Client Default / Churn Risk Predictive Scoring",
            "IT & Ops": "Hardware Failure Predictive Scoring & Maintenance Alert",
            "Customer Support": "Customer Churn Risk Predictive Scoring & Tagging"
        }
    },
    {
        "pattern": "Chatbot Escalation Handoff",
        "nodes": ["Chatbot Webhook", "Determine Intent via NLP", "Can Auto-Resolve?", "Provide Knowledgebase Link", "Create Human Ticket", "Send Chat History Context"],
        "connections": {
            "Chatbot Webhook": ["Determine Intent via NLP"],
            "Determine Intent via NLP": ["Can Auto-Resolve?"],
            "Can Auto-Resolve?": ["Provide Knowledgebase Link", "Create Human Ticket"],
            "Create Human Ticket": ["Send Chat History Context"]
        },
        "domain_flavors": {
            "Sales & CRM": "Sales Chatbot to Human SDR Handoff with Context",
            "HR & Recruiting": "HR Benefits Chatbot to Benefits Specialist Handoff",
            "Finance & Accounting": "Payroll FAQ Chatbot to Payroll Admin Handoff",
            "IT & Ops": "IT Password Reset Chatbot to L2 Tech Escalation",
            "Customer Support": "Support Chatbot to Live Agent Escalation with Context"
        }
    },
    {
        "pattern": "Multi-Channel Broadcast Engine",
        "nodes": ["Database Polling (Daily)", "Filter Audience Segment", "Format Message", "Send Email", "Send SMS", "Send Slack/Teams Push"],
        "connections": {
            "Database Polling (Daily)": ["Filter Audience Segment"],
            "Filter Audience Segment": ["Format Message"],
            "Format Message": ["Send Email", "Send SMS", "Send Slack/Teams Push"]
        },
        "domain_flavors": {
            "Sales & CRM": "Omnichannel Webinar Reminder Broadcast Engine",
            "HR & Recruiting": "Urgent Company-Wide Policy Update Broadcast",
            "Finance & Accounting": "End of Quarter Expense Submission Broadcast",
            "IT & Ops": "Critical System Outage Multi-Channel Broadcast",
            "Customer Support": "Known Issue / Bug Status Multi-Channel Update"
        }
    },
    {
        "pattern": "Contract & Document Generation",
        "nodes": ["Trigger (Deal/Status Won)", "Fetch Variables", "Populate Document Template", "Generate PDF", "Send via eSignature API", "Update Status to 'Sent'"],
        "connections": {
            "Trigger (Deal/Status Won)": ["Fetch Variables"],
            "Fetch Variables": ["Populate Document Template"],
            "Populate Document Template": ["Generate PDF"],
            "Generate PDF": ["Send via eSignature API"],
            "Send via eSignature API": ["Update Status to 'Sent'"]
        },
        "domain_flavors": {
            "Sales & CRM": "Automated Sales Contract & MSA Generation",
            "HR & Recruiting": "Automated Employment Agreement Generation",
            "Finance & Accounting": "Automated Vendor NDA & W-9 Packet Generation",
            "IT & Ops": "IT Asset Liability Waiver Generation & eSign",
            "Customer Support": "SLA Upgrade Custom Contract Generation"
        }
    },
    {
        "pattern": "SLA Breach Monitor & Escalation",
        "nodes": ["Cron Trigger (Every 15m)", "Query Open/Pending Items", "Check Time Elapsed", "Is SLA Breached?", "Escalate to Manager", "Apply 'Urgent' Tag"],
        "connections": {
            "Cron Trigger (Every 15m)": ["Query Open/Pending Items"],
            "Query Open/Pending Items": ["Check Time Elapsed"],
            "Check Time Elapsed": ["Is SLA Breached?"],
            "Is SLA Breached?": ["Escalate to Manager", "Apply 'Urgent' Tag"]
        },
        "domain_flavors": {
            "Sales & CRM": "Inbound Lead Response Time SLA Breach Monitor",
            "HR & Recruiting": "Candidate Interview Feedback SLA Escalation",
            "Finance & Accounting": "Month-End Close Task SLA Breach Monitor",
            "IT & Ops": "Critical Server Incident Resolution SLA Monitor",
            "Customer Support": "VIP Customer Ticket First-Response SLA Monitor"
        }
    },
    {
        "pattern": "Competitive Intelligence / Scraper",
        "nodes": ["Daily Schedule", "Scrape Target URL", "Extract Price/Features", "Compare vs Own Database", "If Change Detected", "Alert Pricing Team"],
        "connections": {
            "Daily Schedule": ["Scrape Target URL"],
            "Scrape Target URL": ["Extract Price/Features"],
            "Extract Price/Features": ["Compare vs Own Database"],
            "Compare vs Own Database": ["If Change Detected"],
            "If Change Detected": ["Alert Pricing Team"]
        },
        "domain_flavors": {
            "Sales & CRM": "Competitor Pricing Change Detection & Sales Alert",
            "HR & Recruiting": "Competitor Job Board Scraper for Salary Intel",
            "Finance & Accounting": "Market Exchange Rate / Commodity Scraper & Alert",
            "IT & Ops": "Cloud Provider Instance Pricing Scraper & Optimizer",
            "Customer Support": "Competitor Trustpilot Review Scraper & Sentiment Analysis"
        }
    },
    {
        "pattern": "Social Media Listening & Action",
        "nodes": ["Twitter/LinkedIn Webhook", "Filter Mentions/Keywords", "LLM Sentiment Analysis", "Is Negative?", "Create PR Ticket", "Auto-Reply / Like"],
        "connections": {
            "Twitter/LinkedIn Webhook": ["Filter Mentions/Keywords"],
            "Filter Mentions/Keywords": ["LLM Sentiment Analysis"],
            "LLM Sentiment Analysis": ["Is Negative?", "Auto-Reply / Like"],
            "Is Negative?": ["Create PR Ticket"]
        },
        "domain_flavors": {
            "Sales & CRM": "Social Selling Trigger on 'Looking for Recommendations'",
            "HR & Recruiting": "Employer Brand Listening (Glassdoor/Twitter) Alerts",
            "Finance & Accounting": "Investor Relations Sentiment Listening on FinTwit",
            "IT & Ops": "Shadow IT / Security Leak Detection on GitHub/Pastebin",
            "Customer Support": "Angry Customer Social Mention Immediate Triage"
        }
    },
    {
        "pattern": "Inventory / Resource Restock",
        "nodes": ["Inventory Level Webhook", "Check Reorder Threshold", "If Below Threshold", "Generate Purchase Order", "Send to Supplier API", "Log Expected Delivery"],
        "connections": {
            "Inventory Level Webhook": ["Check Reorder Threshold"],
            "Check Reorder Threshold": ["If Below Threshold"],
            "If Below Threshold": ["Generate Purchase Order"],
            "Generate Purchase Order": ["Send to Supplier API"],
            "Send to Supplier API": ["Log Expected Delivery"]
        },
        "domain_flavors": {
            "Sales & CRM": "Marketing Swag & Brochure Auto-Restock",
            "HR & Recruiting": "New Hire Welcome Kit Inventory Auto-Restock",
            "Finance & Accounting": "Office Supplies & Procurement Auto-Reordering",
            "IT & Ops": "Server Rack Parts & Cables Inventory Restock",
            "Customer Support": "Replacement Parts Auto-Ordering for RMA fulfillment"
        }
    },
    {
        "pattern": "Knowledge Base Auto-Updater",
        "nodes": ["Issue Resolved Webhook", "Extract Resolution Text", "Check if KB Exists", "If No", "Draft KB Article via LLM", "Submit for Review"],
        "connections": {
            "Issue Resolved Webhook": ["Extract Resolution Text"],
            "Extract Resolution Text": ["Check if KB Exists"],
            "Check if KB Exists": ["If No"],
            "If No": ["Draft KB Article via LLM"],
            "Draft KB Article via LLM": ["Submit for Review"]
        },
        "domain_flavors": {
            "Sales & CRM": "Win/Loss Analysis Auto-Draft to Sales Enablement Wiki",
            "HR & Recruiting": "New Policy Exception Auto-Draft to Employee Handbook",
            "Finance & Accounting": "Tax Compliance Edge-Case Auto-Draft to FinWiki",
            "IT & Ops": "IT Outage Post-Mortem Auto-Draft to Confluence",
            "Customer Support": "Resolved Ticket Auto-Draft to Public Help Center"
        }
    },
    {
        "pattern": "Subscription Dunning & Recovery",
        "nodes": ["Payment Failed Webhook", "Check Failure Reason", "Retry Logic (Days 1, 3, 5)", "Send Reminder Email", "If Hard Fail", "Downgrade Account"],
        "connections": {
            "Payment Failed Webhook": ["Check Failure Reason"],
            "Check Failure Reason": ["Retry Logic (Days 1, 3, 5)"],
            "Retry Logic (Days 1, 3, 5)": ["Send Reminder Email", "If Hard Fail"],
            "If Hard Fail": ["Downgrade Account"]
        },
        "domain_flavors": {
            "Sales & CRM": "SaaS Subscription Dunning & Sales Win-Back Alert",
            "HR & Recruiting": "External Recruiter Retainer Payment Follow-up",
            "Finance & Accounting": "B2B Invoice Net-30 Overdue Dunning Engine",
            "IT & Ops": "SaaS License Renewal Failure & Access Revocation",
            "Customer Support": "Premium Support Tier Payment Failure Downgrade"
        }
    },
    {
        "pattern": "Location-Based Dispatch & Routing",
        "nodes": ["Request Webhook", "Get Coordinates", "Query Available Staff GPS", "Calculate Distance/Traffic", "Dispatch Nearest Person", "Send ETA to Requester"],
        "connections": {
            "Request Webhook": ["Get Coordinates"],
            "Get Coordinates": ["Query Available Staff GPS"],
            "Query Available Staff GPS": ["Calculate Distance/Traffic"],
            "Calculate Distance/Traffic": ["Dispatch Nearest Person"],
            "Dispatch Nearest Person": ["Send ETA to Requester"]
        },
        "domain_flavors": {
            "Sales & CRM": "Field Sales Rep Nearest Lead Dispatch System",
            "HR & Recruiting": "Campus Recruiting Rep to Nearest Career Fair Dispatch",
            "Finance & Accounting": "Physical Audit / Inventory Checker Nearest Dispatch",
            "IT & Ops": "Field IT Technician Nearest Office Dispatch",
            "Customer Support": "On-Site Repair Technician Intelligent Dispatch"
        }
    },
    {
        "pattern": "Data Masking & Privacy Compliance",
        "nodes": ["Database Entry Trigger", "Detect PII via regex/AI", "Mask / Encrypt Fields", "Move to Secure Vault", "Leave Reference ID", "Log Compliance Audit"],
        "connections": {
            "Database Entry Trigger": ["Detect PII via regex/AI"],
            "Detect PII via regex/AI": ["Mask / Encrypt Fields"],
            "Mask / Encrypt Fields": ["Move to Secure Vault", "Leave Reference ID"],
            "Leave Reference ID": ["Log Compliance Audit"]
        },
        "domain_flavors": {
            "Sales & CRM": "Sales Call Transcript PII Masking (GDPR/CCPA)",
            "HR & Recruiting": "Candidate Background Check Secure Vaulting",
            "Finance & Accounting": "Credit Card / Bank Detail Auto-Redaction System",
            "IT & Ops": "Application Log PII Scrubbing & Redaction",
            "Customer Support": "Support Ticket Attachment Health Data (HIPAA) Masking"
        }
    }
]

def generate_100_workflows():
    workflows = []
    counter = 1
    for arch in architectures:
        for domain in domains:
            title = arch["domain_flavors"][domain]
            
            nodes_out = []
            y_pos = 200
            x_pos = 250
            node_map = {}

            for i, node_name in enumerate(arch["nodes"]):
                # Assign dummy node types based on names
                node_type = "n8n-nodes-base.httpRequest"
                if "Webhook" in node_name or "Trigger" in node_name:
                    node_type = "n8n-nodes-base.webhook"
                elif "AI" in node_name or "LLM" in node_name or "NLP" in node_name:
                    node_type = "n8n-nodes-base.openAi"
                elif "Switch" in node_name or "If" in node_name:
                    node_type = "n8n-nodes-base.switch"
                elif "Email" in node_name:
                    node_type = "n8n-nodes-base.emailSend"
                elif "Slack" in node_name or "Notify" in node_name or "Alert" in node_name:
                    node_type = "n8n-nodes-base.slack"
                elif "Database" in node_name or "Log" in node_name:
                    node_type = "n8n-nodes-base.postgres"
                elif "Code" in node_name or "Math" in node_name or "Python" in node_name or "Logic" in node_name:
                    node_type = "n8n-nodes-base.code"
                elif "Schedule" in node_name or "Cron" in node_name or "Daily" in node_name:
                    node_type = "n8n-nodes-base.cron"
                
                nodes_out.append({
                    "parameters": {},
                    "id": f"node-{i}",
                    "name": node_name,
                    "type": node_type,
                    "typeVersion": 1,
                    "position": [x_pos, y_pos]
                })
                node_map[node_name] = node_name
                x_pos += 200
                if x_pos > 850:
                    x_pos = 250
                    y_pos += 200

            connections_out = {}
            for src, targets in arch["connections"].items():
                if src not in connections_out:
                    connections_out[src] = {"main": [[]]}
                for target in targets:
                    connections_out[src]["main"][0].append({
                        "node": node_map[target],
                        "type": "main",
                        "index": 0
                    })

            workflow = {
                "name": f"{counter:03d} - {title}",
                "nodes": nodes_out,
                "connections": connections_out,
                "active": False,
                "settings": {}
            }
            workflows.append((counter, title, workflow, domain))
            counter += 1
            
    return workflows

if __name__ == "__main__":
    out_dir = r"C:\Users\laptopzone\.gemini\antigravity\scratch\n8n-business-problems\templates"
    
    workflows = generate_100_workflows()
    for counter, title, wf_data, domain in workflows:
        safe_title = title.lower().replace(' ', '-').replace('&', 'and').replace('/', '-')
        filename = f"{counter:03d}-{safe_title}.json"
        filepath = os.path.join(out_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(wf_data, f, indent=2)
        print(f"Generated {filename}")
