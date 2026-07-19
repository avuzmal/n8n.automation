import json
import os

ideas = [
    {
        "id": 1,
        "name": "Multi-Source Disaster Alert & Resource Routing",
        "description": "Delayed coordination during natural disasters. Triggers via Webhooks from USGS and NOAA. Uses AI Agent to parse severity, queries OpenStreetMap, and routes SMS alerts (Twilio) while updating Airtable.",
        "nodes": [
            {"name": "USGS Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "NOAA Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "Merge Triggers", "type": "n8n-nodes-base.merge"},
            {"name": "AI Severity Parser", "type": "n8n-nodes-base.openAi"},
            {"name": "Query OpenStreetMap", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Route Alerts", "type": "n8n-nodes-base.switch"},
            {"name": "Twilio SMS", "type": "n8n-nodes-base.twilio"},
            {"name": "Update Airtable", "type": "n8n-nodes-base.airtable"}
        ],
        "connections": {
            "USGS Webhook": ["Merge Triggers"],
            "NOAA Webhook": ["Merge Triggers"],
            "Merge Triggers": ["AI Severity Parser"],
            "AI Severity Parser": ["Query OpenStreetMap"],
            "Query OpenStreetMap": ["Route Alerts"],
            "Route Alerts": ["Twilio SMS", "Update Airtable"]
        }
    },
    {
        "id": 2,
        "name": "Post-Disaster Infrastructure Damage Triage",
        "description": "Ingests citizen reports via WhatsApp/Telegram. Uses Vision AI to analyze photos, estimates repair priority (Python), logs into GIS, and creates work orders via HTTP.",
        "nodes": [
            {"name": "Telegram Trigger", "type": "n8n-nodes-base.telegramTrigger"},
            {"name": "WhatsApp Trigger", "type": "n8n-nodes-base.webhook"},
            {"name": "Merge Reports", "type": "n8n-nodes-base.merge"},
            {"name": "Vision AI", "type": "n8n-nodes-base.awsRekognition"},
            {"name": "Estimate Priority", "type": "n8n-nodes-base.code"},
            {"name": "GIS Database", "type": "n8n-nodes-base.postgres"},
            {"name": "Create Work Order", "type": "n8n-nodes-base.httpRequest"}
        ],
        "connections": {
            "Telegram Trigger": ["Merge Reports"],
            "WhatsApp Trigger": ["Merge Reports"],
            "Merge Reports": ["Vision AI"],
            "Vision AI": ["Estimate Priority"],
            "Estimate Priority": ["GIS Database"],
            "GIS Database": ["Create Work Order"]
        }
    },
    {
        "id": 3,
        "name": "Wildfire Evacuation & Pet Rescue Coordination",
        "description": "Monitors NASA FIRMS. Scrapes shelter APIs, cross-references pet owner registries, and auto-generates evacuation routes.",
        "nodes": [
            {"name": "NASA FIRMS API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Cron Trigger", "type": "n8n-nodes-base.cron"},
            {"name": "Check Fire Proximity", "type": "n8n-nodes-base.if"},
            {"name": "Scrape Shelter APIs", "type": "n8n-nodes-base.graphql"},
            {"name": "Query Pet Registry", "type": "n8n-nodes-base.mysql"},
            {"name": "Route Optimization", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Notify Volunteer Drivers", "type": "n8n-nodes-base.slack"}
        ],
        "connections": {
            "Cron Trigger": ["NASA FIRMS API"],
            "NASA FIRMS API": ["Check Fire Proximity"],
            "Check Fire Proximity": ["Scrape Shelter APIs"],
            "Scrape Shelter APIs": ["Query Pet Registry"],
            "Query Pet Registry": ["Route Optimization"],
            "Route Optimization": ["Notify Volunteer Drivers"]
        }
    },
    {
        "id": 4,
        "name": "AI-Driven Mental Health Crisis Triage & Routing",
        "description": "Ingests texts, LLM assesses risk. High-risk -> PagerDuty. Medium-risk -> schedule check-ins and send PDFs via WhatsApp.",
        "nodes": [
            {"name": "Incoming Text (Webhook)", "type": "n8n-nodes-base.webhook"},
            {"name": "LLM Risk Assessment", "type": "n8n-nodes-base.openAi"},
            {"name": "Risk Level Switch", "type": "n8n-nodes-base.switch"},
            {"name": "PagerDuty Alert", "type": "n8n-nodes-base.pagerDuty"},
            {"name": "Schedule Check-in", "type": "n8n-nodes-base.googleCalendar"},
            {"name": "Send Resource PDF", "type": "n8n-nodes-base.whatsapp"}
        ],
        "connections": {
            "Incoming Text (Webhook)": ["LLM Risk Assessment"],
            "LLM Risk Assessment": ["Risk Level Switch"],
            "Risk Level Switch": ["PagerDuty Alert", "Schedule Check-in"],
            "Schedule Check-in": ["Send Resource PDF"]
        }
    },
    {
        "id": 5,
        "name": "Medication Shortage Early Warning & Redistribution",
        "description": "Scrapes FDA shortage lists and local pharmacy APIs. Predicts shortages, alerts health depts, and triggers transfer orders.",
        "nodes": [
            {"name": "Daily Trigger", "type": "n8n-nodes-base.cron"},
            {"name": "Scrape FDA API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Get Pharmacy Inventory", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Predictive Analytics (Python)", "type": "n8n-nodes-base.code"},
            {"name": "Shortage Detected?", "type": "n8n-nodes-base.if"},
            {"name": "Alert Health Dept", "type": "n8n-nodes-base.emailSend"},
            {"name": "Trigger ERP Transfer", "type": "n8n-nodes-base.httpRequest"}
        ],
        "connections": {
            "Daily Trigger": ["Scrape FDA API"],
            "Scrape FDA API": ["Get Pharmacy Inventory"],
            "Get Pharmacy Inventory": ["Predictive Analytics (Python)"],
            "Predictive Analytics (Python)": ["Shortage Detected?"],
            "Shortage Detected?": ["Alert Health Dept", "Trigger ERP Transfer"]
        }
    },
    {
        "id": 6,
        "name": "Elderly Fall Detection & Autonomous Wellness Check",
        "description": "IoT webhook. If no motion, cascading workflow: voice call -> text neighbor -> dispatch EMS & email medical history.",
        "nodes": [
            {"name": "IoT Motion Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "Wait (Until 10 AM)", "type": "n8n-nodes-base.wait"},
            {"name": "Check Motion Status", "type": "n8n-nodes-base.if"},
            {"name": "Twilio Voice Call", "type": "n8n-nodes-base.twilio"},
            {"name": "Wait (Answer)", "type": "n8n-nodes-base.wait"},
            {"name": "Text Neighbor", "type": "n8n-nodes-base.twilio"},
            {"name": "Wait (Neighbor)", "type": "n8n-nodes-base.wait"},
            {"name": "Dispatch EMS", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Email Medical History", "type": "n8n-nodes-base.emailSend"}
        ],
        "connections": {
            "IoT Motion Webhook": ["Wait (Until 10 AM)"],
            "Wait (Until 10 AM)": ["Check Motion Status"],
            "Check Motion Status": ["Twilio Voice Call"],
            "Twilio Voice Call": ["Wait (Answer)"],
            "Wait (Answer)": ["Text Neighbor"],
            "Text Neighbor": ["Wait (Neighbor)"],
            "Wait (Neighbor)": ["Dispatch EMS"],
            "Dispatch EMS": ["Email Medical History"]
        }
    },
    {
        "id": 7,
        "name": "Hyper-Local Food Waste Rescue Network",
        "description": "Connects restaurant POS to food banks. Calculates nutrients, matches banks, dispatches UberDirect, SMS updates.",
        "nodes": [
            {"name": "Restaurant POS Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "Calculate Nutrients", "type": "n8n-nodes-base.code"},
            {"name": "Match Food Bank", "type": "n8n-nodes-base.postgres"},
            {"name": "Dispatch UberDirect", "type": "n8n-nodes-base.httpRequest"},
            {"name": "SMS Notifications", "type": "n8n-nodes-base.twilio"}
        ],
        "connections": {
            "Restaurant POS Webhook": ["Calculate Nutrients"],
            "Calculate Nutrients": ["Match Food Bank"],
            "Match Food Bank": ["Dispatch UberDirect"],
            "Dispatch UberDirect": ["SMS Notifications"]
        }
    },
    {
        "id": 8,
        "name": "Smallholder Farmer Micro-Insurance Payouts",
        "description": "Monitors weather APIs and satellite moisture. Calculates payout and triggers mobile money transfer (M-Pesa).",
        "nodes": [
            {"name": "Cron Trigger", "type": "n8n-nodes-base.cron"},
            {"name": "Weather Station API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Satellite Soil Moisture", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Rainfall Threshold Check", "type": "n8n-nodes-base.if"},
            {"name": "Smart Contract Logic", "type": "n8n-nodes-base.code"},
            {"name": "M-Pesa API Transfer", "type": "n8n-nodes-base.httpRequest"},
            {"name": "SMS Confirmation", "type": "n8n-nodes-base.twilio"}
        ],
        "connections": {
            "Cron Trigger": ["Weather Station API"],
            "Weather Station API": ["Satellite Soil Moisture"],
            "Satellite Soil Moisture": ["Rainfall Threshold Check"],
            "Rainfall Threshold Check": ["Smart Contract Logic"],
            "Smart Contract Logic": ["M-Pesa API Transfer"],
            "M-Pesa API Transfer": ["SMS Confirmation"]
        }
    },
    {
        "id": 9,
        "name": "Community Garden Resource Allocation",
        "description": "Aggregates soil sensor/weather data. AI recommends crops. Orders seeds and publishes weekly forecasts via Webhooks.",
        "nodes": [
            {"name": "Weekly Trigger", "type": "n8n-nodes-base.cron"},
            {"name": "Get Soil Data", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Get Weather Forecast", "type": "n8n-nodes-base.httpRequest"},
            {"name": "AI Crop Recommendation", "type": "n8n-nodes-base.openAi"},
            {"name": "Check Seed Inventory", "type": "n8n-nodes-base.mysql"},
            {"name": "Order Seeds API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Publish Harvest Forecast", "type": "n8n-nodes-base.webhook"}
        ],
        "connections": {
            "Weekly Trigger": ["Get Soil Data"],
            "Get Soil Data": ["Get Weather Forecast"],
            "Get Weather Forecast": ["AI Crop Recommendation"],
            "AI Crop Recommendation": ["Check Seed Inventory"],
            "Check Seed Inventory": ["Order Seeds API", "Publish Harvest Forecast"]
        }
    },
    {
        "id": 10,
        "name": "Illegal Deforestation Acoustic Triangulation",
        "description": "Ingests IoT audio. AI detects chainsaws. Triangulates, checks ranger GPS, dispatches team via encrypted messaging.",
        "nodes": [
            {"name": "Audio IoT Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "AI Audio Classification", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Is Chainsaw/Gunshot?", "type": "n8n-nodes-base.if"},
            {"name": "Triangulate Location", "type": "n8n-nodes-base.code"},
            {"name": "Get Ranger GPS Tracks", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Dispatch Nearest Team", "type": "n8n-nodes-base.telegram"}
        ],
        "connections": {
            "Audio IoT Webhook": ["AI Audio Classification"],
            "AI Audio Classification": ["Is Chainsaw/Gunshot?"],
            "Is Chainsaw/Gunshot?": ["Triangulate Location"],
            "Triangulate Location": ["Get Ranger GPS Tracks"],
            "Get Ranger GPS Tracks": ["Dispatch Nearest Team"]
        }
    },
    {
        "id": 11,
        "name": "Urban Air Quality & Asthma Alert System",
        "description": "Aggregates AQI sensors. AI predicts spikes. Triggers asthma action plans and adjusts smart HVAC in schools.",
        "nodes": [
            {"name": "Hourly Trigger", "type": "n8n-nodes-base.cron"},
            {"name": "Citizen AQI Sensors", "type": "n8n-nodes-base.httpRequest"},
            {"name": "EPA Data API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "AI Pollution Predictor", "type": "n8n-nodes-base.openAi"},
            {"name": "High Pollution?", "type": "n8n-nodes-base.if"},
            {"name": "Alert Vulnerable Users", "type": "n8n-nodes-base.emailSend"},
            {"name": "Adjust School HVAC", "type": "n8n-nodes-base.httpRequest"}
        ],
        "connections": {
            "Hourly Trigger": ["Citizen AQI Sensors"],
            "Citizen AQI Sensors": ["EPA Data API"],
            "EPA Data API": ["AI Pollution Predictor"],
            "AI Pollution Predictor": ["High Pollution?"],
            "High Pollution?": ["Alert Vulnerable Users", "Adjust School HVAC"]
        }
    },
    {
        "id": 12,
        "name": "Corporate ESG Compliance Auto-Trading",
        "description": "Monitors energy/travel. Calculates carbon footprint. Auto-purchases carbon credits and generates ESG report.",
        "nodes": [
            {"name": "Internal Data Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "Calculate Carbon Footprint", "type": "n8n-nodes-base.code"},
            {"name": "Threshold Check", "type": "n8n-nodes-base.if"},
            {"name": "Purchase Carbon Credits", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Generate ESG PDF", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Email Stakeholders", "type": "n8n-nodes-base.emailSend"}
        ],
        "connections": {
            "Internal Data Webhook": ["Calculate Carbon Footprint"],
            "Calculate Carbon Footprint": ["Threshold Check"],
            "Threshold Check": ["Purchase Carbon Credits"],
            "Purchase Carbon Credits": ["Generate ESG PDF"],
            "Generate ESG PDF": ["Email Stakeholders"]
        }
    },
    {
        "id": 13,
        "name": "Legislative Bill Impact Analyzer & Civic Digest",
        "description": "Monitors gov APIs. LLM summarizes and analyzes impact. Translates and distributes personalized digests via email/SMS.",
        "nodes": [
            {"name": "Gov Legislative API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "New Bill Detected", "type": "n8n-nodes-base.if"},
            {"name": "LLM Impact Analysis", "type": "n8n-nodes-base.openAi"},
            {"name": "Translation API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Get Citizen Subscriptions", "type": "n8n-nodes-base.postgres"},
            {"name": "Send Personalized Emails", "type": "n8n-nodes-base.emailSend"},
            {"name": "Send SMS Digest", "type": "n8n-nodes-base.twilio"}
        ],
        "connections": {
            "Gov Legislative API": ["New Bill Detected"],
            "New Bill Detected": ["LLM Impact Analysis"],
            "LLM Impact Analysis": ["Translation API"],
            "Translation API": ["Get Citizen Subscriptions"],
            "Get Citizen Subscriptions": ["Send Personalized Emails", "Send SMS Digest"]
        }
    },
    {
        "id": 14,
        "name": "Pothole Gamified Reporting & Tracking",
        "description": "Ingests app reports. Vision AI verifies issue. Assigns to department, updates citizen, and rewards transit credits.",
        "nodes": [
            {"name": "Citizen App Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "Vision AI Verification", "type": "n8n-nodes-base.awsRekognition"},
            {"name": "Valid Report?", "type": "n8n-nodes-base.if"},
            {"name": "Categorize & Assign", "type": "n8n-nodes-base.code"},
            {"name": "Create Muni Ticket", "type": "n8n-nodes-base.jira"},
            {"name": "Update Citizen", "type": "n8n-nodes-base.emailSend"},
            {"name": "Reward Transit Credits API", "type": "n8n-nodes-base.httpRequest"}
        ],
        "connections": {
            "Citizen App Webhook": ["Vision AI Verification"],
            "Vision AI Verification": ["Valid Report?"],
            "Valid Report?": ["Categorize & Assign"],
            "Categorize & Assign": ["Create Muni Ticket"],
            "Create Muni Ticket": ["Update Citizen", "Reward Transit Credits API"]
        }
    },
    {
        "id": 15,
        "name": "Public Fund Allocation Fraud Detection",
        "description": "Monitors procurement portals. Cross-references bidders with PEPs and shell registries. Flags patterns and alerts NGOs.",
        "nodes": [
            {"name": "Procurement Portal API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Extract Bidders", "type": "n8n-nodes-base.code"},
            {"name": "Check PEP Database", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Check Shell Registries", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Suspicious Pattern Found?", "type": "n8n-nodes-base.if"},
            {"name": "Alert Anti-Corruption NGO", "type": "n8n-nodes-base.emailSend"},
            {"name": "Secure Drop to Journalists", "type": "n8n-nodes-base.httpRequest"}
        ],
        "connections": {
            "Procurement Portal API": ["Extract Bidders"],
            "Extract Bidders": ["Check PEP Database", "Check Shell Registries"],
            "Check PEP Database": ["Suspicious Pattern Found?"],
            "Check Shell Registries": ["Suspicious Pattern Found?"],
            "Suspicious Pattern Found?": ["Alert Anti-Corruption NGO", "Secure Drop to Journalists"]
        }
    },
    {
        "id": 16,
        "name": "AI-Powered Personalized IEP Generator",
        "description": "Ingests student data. LLM drafts compliant IEP. Routes for review and schedules parent-teacher meeting.",
        "nodes": [
            {"name": "SIS Data Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "Fetch Psych Evals", "type": "n8n-nodes-base.googleDrive"},
            {"name": "LLM Drafts IEP", "type": "n8n-nodes-base.openAi"},
            {"name": "Send for Review", "type": "n8n-nodes-base.slack"},
            {"name": "Wait for Approval", "type": "n8n-nodes-base.wait"},
            {"name": "Schedule Meeting", "type": "n8n-nodes-base.googleCalendar"},
            {"name": "Email Parents", "type": "n8n-nodes-base.emailSend"}
        ],
        "connections": {
            "SIS Data Webhook": ["Fetch Psych Evals"],
            "Fetch Psych Evals": ["LLM Drafts IEP"],
            "LLM Drafts IEP": ["Send for Review"],
            "Send for Review": ["Wait for Approval"],
            "Wait for Approval": ["Schedule Meeting"],
            "Schedule Meeting": ["Email Parents"]
        }
    },
    {
        "id": 17,
        "name": "Dropout Prediction & Mentorship Matching",
        "description": "Analyzes SIS records. Predictive modeling flags at-risk students. Matches with mentors and sets up check-ins.",
        "nodes": [
            {"name": "Weekly SIS Extract", "type": "n8n-nodes-base.cron"},
            {"name": "Predictive Model API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Is At-Risk?", "type": "n8n-nodes-base.if"},
            {"name": "Query Mentor Database", "type": "n8n-nodes-base.postgres"},
            {"name": "Match Mentor (Logic)", "type": "n8n-nodes-base.code"},
            {"name": "Email Mentor Intro", "type": "n8n-nodes-base.emailSend"},
            {"name": "Setup Recurring Check-ins", "type": "n8n-nodes-base.googleCalendar"}
        ],
        "connections": {
            "Weekly SIS Extract": ["Predictive Model API"],
            "Predictive Model API": ["Is At-Risk?"],
            "Is At-Risk?": ["Query Mentor Database"],
            "Query Mentor Database": ["Match Mentor (Logic)"],
            "Match Mentor (Logic)": ["Email Mentor Intro"],
            "Email Mentor Intro": ["Setup Recurring Check-ins"]
        }
    },
    {
        "id": 18,
        "name": "Open Educational Resource (OER) Localization",
        "description": "Monitors OER repos. AI translates/adapts. Formats for low-bandwidth and distributes via WhatsApp.",
        "nodes": [
            {"name": "OER RSS Feed", "type": "n8n-nodes-base.rssFeed"},
            {"name": "AI Translation & Adaptation", "type": "n8n-nodes-base.openAi"},
            {"name": "Format for SMS/Micro-lesson", "type": "n8n-nodes-base.code"},
            {"name": "Get Teacher List", "type": "n8n-nodes-base.mysql"},
            {"name": "Distribute via WhatsApp", "type": "n8n-nodes-base.whatsapp"}
        ],
        "connections": {
            "OER RSS Feed": ["AI Translation & Adaptation"],
            "AI Translation & Adaptation": ["Format for SMS/Micro-lesson"],
            "Format for SMS/Micro-lesson": ["Get Teacher List"],
            "Get Teacher List": ["Distribute via WhatsApp"]
        }
    },
    {
        "id": 19,
        "name": "Rapid Rehousing Shelter Bed Matching",
        "description": "Aggregates real-time bed availability. Matches client needs to nearest bed and auto-generates intake paperwork.",
        "nodes": [
            {"name": "Social Worker Intake Form", "type": "n8n-nodes-base.typeform"},
            {"name": "Aggregate Shelter APIs", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Match Algorithm", "type": "n8n-nodes-base.code"},
            {"name": "Bed Found?", "type": "n8n-nodes-base.if"},
            {"name": "Reserve Bed API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Generate PDF Paperwork", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Email Intake Packet", "type": "n8n-nodes-base.emailSend"}
        ],
        "connections": {
            "Social Worker Intake Form": ["Aggregate Shelter APIs"],
            "Aggregate Shelter APIs": ["Match Algorithm"],
            "Match Algorithm": ["Bed Found?"],
            "Bed Found?": ["Reserve Bed API"],
            "Reserve Bed API": ["Generate PDF Paperwork"],
            "Generate PDF Paperwork": ["Email Intake Packet"]
        }
    },
    {
        "id": 20,
        "name": "Benefit Cliff & Social Safety Net Navigator",
        "description": "Ingests financial data. Rules engine determines eligibility. Auto-fills applications via API/RPA and sets reminders.",
        "nodes": [
            {"name": "User Financial Data Form", "type": "n8n-nodes-base.webhook"},
            {"name": "Eligibility Rules Engine", "type": "n8n-nodes-base.code"},
            {"name": "Is Eligible?", "type": "n8n-nodes-base.if"},
            {"name": "Submit API Application", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Trigger RPA Bot", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Set Recertification Reminder", "type": "n8n-nodes-base.cron"}
        ],
        "connections": {
            "User Financial Data Form": ["Eligibility Rules Engine"],
            "Eligibility Rules Engine": ["Is Eligible?"],
            "Is Eligible?": ["Submit API Application", "Trigger RPA Bot"],
            "Submit API Application": ["Set Recertification Reminder"]
        }
    },
    {
        "id": 21,
        "name": "Mobile Health Clinic Route Optimization",
        "description": "Combines public health, traffic, weather data. Optimizes routes and sends SMS reminders to targeted zip codes.",
        "nodes": [
            {"name": "Daily Cron Trigger", "type": "n8n-nodes-base.cron"},
            {"name": "Fetch Public Health Data", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Fetch Traffic & Weather", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Route Optimization Algorithm", "type": "n8n-nodes-base.code"},
            {"name": "Query Residents by Zip", "type": "n8n-nodes-base.postgres"},
            {"name": "Send SMS Reminders", "type": "n8n-nodes-base.twilio"}
        ],
        "connections": {
            "Daily Cron Trigger": ["Fetch Public Health Data"],
            "Fetch Public Health Data": ["Fetch Traffic & Weather"],
            "Fetch Traffic & Weather": ["Route Optimization Algorithm"],
            "Route Optimization Algorithm": ["Query Residents by Zip"],
            "Query Residents by Zip": ["Send SMS Reminders"]
        }
    },
    {
        "id": 22,
        "name": "Real-Time Sign Language Accessibility Event Auditor",
        "description": "Monitors video streams. AI generates captions/avatars/transcripts. Distributes accessibility packages.",
        "nodes": [
            {"name": "Video Stream Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "AI Speech-to-Text", "type": "n8n-nodes-base.awsTranscribe"},
            {"name": "Translate to Sign Avatar API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Generate Transcript PDF", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Get Registered Attendees", "type": "n8n-nodes-base.eventbrite"},
            {"name": "Email Accessibility Package", "type": "n8n-nodes-base.emailSend"}
        ],
        "connections": {
            "Video Stream Webhook": ["AI Speech-to-Text"],
            "AI Speech-to-Text": ["Translate to Sign Avatar API", "Generate Transcript PDF"],
            "Translate to Sign Avatar API": ["Get Registered Attendees"],
            "Generate Transcript PDF": ["Get Registered Attendees"],
            "Get Registered Attendees": ["Email Accessibility Package"]
        }
    },
    {
        "id": 23,
        "name": "Adaptive Technology Repair & Loaner Coordination",
        "description": "Ingests repair requests. Checks loaner inventory. Dispatches volunteer, pings tech, and tracks lifecycle.",
        "nodes": [
            {"name": "Repair Request Form", "type": "n8n-nodes-base.webhook"},
            {"name": "Check Loaner Inventory", "type": "n8n-nodes-base.airtable"},
            {"name": "Is Available?", "type": "n8n-nodes-base.if"},
            {"name": "Dispatch Delivery Volunteer", "type": "n8n-nodes-base.slack"},
            {"name": "Ping Tech Volunteer", "type": "n8n-nodes-base.emailSend"},
            {"name": "Create Tracking Ticket", "type": "n8n-nodes-base.jira"}
        ],
        "connections": {
            "Repair Request Form": ["Check Loaner Inventory"],
            "Check Loaner Inventory": ["Is Available?"],
            "Is Available?": ["Dispatch Delivery Volunteer"],
            "Dispatch Delivery Volunteer": ["Ping Tech Volunteer"],
            "Ping Tech Volunteer": ["Create Tracking Ticket"]
        }
    },
    {
        "id": 24,
        "name": "Human-Wildlife Conflict Early Warning System",
        "description": "Integrates GPS collar data with geofences. Triggers IoT deterrents and sends SMS warnings to village leaders.",
        "nodes": [
            {"name": "GPS Collar Data Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "Check Geofence (Python)", "type": "n8n-nodes-base.code"},
            {"name": "Approaching Village?", "type": "n8n-nodes-base.if"},
            {"name": "Trigger Smart Lights/IoT", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Get Village Leader Contact", "type": "n8n-nodes-base.mysql"},
            {"name": "Send SMS Warning", "type": "n8n-nodes-base.twilio"}
        ],
        "connections": {
            "GPS Collar Data Webhook": ["Check Geofence (Python)"],
            "Check Geofence (Python)": ["Approaching Village?"],
            "Approaching Village?": ["Trigger Smart Lights/IoT", "Get Village Leader Contact"],
            "Trigger Smart Lights/IoT": ["Send SMS Warning"],
            "Get Village Leader Contact": ["Send SMS Warning"]
        }
    },
    {
        "id": 25,
        "name": "Marine Plastic Tracking & Cleanup Fleet Dispatch",
        "description": "Aggregates ocean current/plastic maps. AI predicts accumulation. Dispatches vessels and logs weight for donors.",
        "nodes": [
            {"name": "Weekly Cron Trigger", "type": "n8n-nodes-base.cron"},
            {"name": "Ocean Current Data API", "type": "n8n-nodes-base.httpRequest"},
            {"name": "Satellite Plastic Maps", "type": "n8n-nodes-base.httpRequest"},
            {"name": "AI Accumulation Predictor", "type": "n8n-nodes-base.openAi"},
            {"name": "Dispatch Cleanup Vessels", "type": "n8n-nodes-base.httpRequest"},
            {"name": "IoT Scale Data Webhook", "type": "n8n-nodes-base.webhook"},
            {"name": "Generate Donor Report", "type": "n8n-nodes-base.emailSend"}
        ],
        "connections": {
            "Weekly Cron Trigger": ["Ocean Current Data API"],
            "Ocean Current Data API": ["Satellite Plastic Maps"],
            "Satellite Plastic Maps": ["AI Accumulation Predictor"],
            "AI Accumulation Predictor": ["Dispatch Cleanup Vessels"],
            "Dispatch Cleanup Vessels": ["IoT Scale Data Webhook"],
            "IoT Scale Data Webhook": ["Generate Donor Report"]
        }
    }
]

def generate_n8n_json(idea):
    nodes_out = []
    y_pos = 200
    x_pos = 250
    node_map = {}

    for i, node in enumerate(idea["nodes"]):
        nodes_out.append({
            "parameters": {},
            "id": f"node-{i}",
            "name": node["name"],
            "type": node["type"],
            "typeVersion": 1,
            "position": [x_pos, y_pos]
        })
        node_map[node["name"]] = node["name"]
        x_pos += 200
        if x_pos > 850:
            x_pos = 250
            y_pos += 200

    connections_out = {}
    for src, targets in idea["connections"].items():
        if src not in connections_out:
            connections_out[src] = {"main": [[]]}
        for target in targets:
            connections_out[src]["main"][0].append({
                "node": node_map[target],
                "type": "main",
                "index": 0
            })

    workflow = {
        "name": f"{idea['id']:02d} - {idea['name']}",
        "nodes": nodes_out,
        "connections": connections_out,
        "active": False,
        "settings": {}
    }
    return workflow

if __name__ == "__main__":
    out_dir = r"C:\Users\laptopzone\.gemini\antigravity\scratch\n8n-social-impact\templates"
    for idea in ideas:
        filename = f"{idea['id']:02d}-{idea['name'].lower().replace(' ', '-').replace('&', 'and').replace('/', '-')}.json"
        filepath = os.path.join(out_dir, filename)
        workflow_data = generate_n8n_json(idea)
        with open(filepath, 'w') as f:
            json.dump(workflow_data, f, indent=2)
        print(f"Generated {filename}")
