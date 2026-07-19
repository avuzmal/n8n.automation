# 03. Supply Chain & Logistics

> ### 1. Predictive Inventory PO Generation
> **The Problem:** Manual inventory checks fail to account for seasonal sales velocity or supplier lead times, resulting in frequent stockouts or costly overstocking.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_01_predictive_inventory_po_generation.json)
> 
> **How it works:** 
> > *Build an n8n workflow that monitors inventory levels in Shopify, checks lead times in NetSuite, and automatically generates purchase orders in Coupa when stock hits the reorder point, factoring in seasonal velocity adjustments.*
> 
> **🔗 Core Integrations:** `Shopify` • `NetSuite` • `Coupa`
> ---

> ### 2. Ocean Freight Delay & Rerouting Automation
> **The Problem:** Supply chain delays cause downstream production halts. When shipping updates are missed, customer support and manufacturing teams are left in the dark.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_02_ocean_freight_delay_rerouting_automation.json)
> 
> **How it works:** 
> > *Design a workflow that integrates with Flexport API to track ocean freight shipments; if a delay is detected, automatically update the ETA in Salesforce, notify the customer via SMS, and adjust production schedules in MRPeasy.*
> 
> **🔗 Core Integrations:** `Flexport` • `Salesforce` • `SMS API` • `MRPeasy`
> ---

> ### 3. Automated Supplier Quality Scorecarding
> **The Problem:** Evaluating supplier performance manually is time-consuming and subjective, making it difficult to hold vendors accountable for late deliveries or high defect rates.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_03_automated_supplier_quality_scorecarding.json)
> 
> **How it works:** 
> > *Create an automated supplier scorecard workflow that pulls delivery on-time rates from the WMS, quality defect rates from QA logs, and calculates a monthly score, automatically downgrading suppliers in the ERP if score < 80.*
> 
> **🔗 Core Integrations:** `WMS` • `QA Systems` • `ERP (e.g., SAP/Oracle)`
> ---

> ### 4. Zero-Touch Customs Documentation
> **The Problem:** Generating commercial invoices, packing lists, and AES filings by hand delays international shipments and increases the risk of customs holds due to typos.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_04_zero_touch_customs_documentation.json)
> 
> **How it works:** 
> > *Build a workflow that automates customs documentation: when a commercial invoice is created in SAP, automatically generate a packing list, certificate of origin, and AES filing via API, attaching them to the shipment record.*
> 
> **🔗 Core Integrations:** `SAP` • `Document Generation API` • `Customs API`
> ---

> ### 5. Weather Risk Supply Chain Mitigation
> **The Problem:** Severe weather events (hurricanes, snowstorms) disrupt shipping routes, but logistics teams often react only after the disruption has occurred.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_05_weather_risk_supply_chain_mitigation.json)
> 
> **How it works:** 
> > *Design a workflow that monitors weather APIs for severe conditions along key shipping routes; if a risk is detected, automatically trigger a rerouting evaluation workflow and alert the logistics control tower via Teams.*
> 
> **🔗 Core Integrations:** `Weather API` • `Logistics Software` • `MS Teams`
> ---

> ### 6. AI-Powered RMA & Liquidation Routing
> **The Problem:** Processing returns manually is a massive cost center. Inspecting returned items and deciding whether to refurbish or liquidate takes too much warehouse labor.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_06_ai_powered_rma_liquidation_routing.json)
> 
> **How it works:** 
> > *Create an automated returns processing workflow that ingests RMA requests, checks item condition via uploaded photos (AI vision), routes to refurbishment or liquidation in the WMS, and triggers the refund in Stripe.*
> 
> **🔗 Core Integrations:** `Returns Portal` • `AI Vision` • `WMS` • `Stripe`
> ---

> ### 7. Daily 3PL to ERP Inventory Reconciliation
> **The Problem:** Discrepancies between the 3PL warehouse and the central ERP cause accounting nightmare and overselling issues. 
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_07_daily_3pl_to_erp_inventory_reconciliation.json)
> 
> **How it works:** 
> > *Build a workflow that syncs 3PL warehouse data (ShipHero) with the ERP (Microsoft Dynamics), automatically reconciling daily inventory counts and flagging discrepancies >1% for physical cycle counts.*
> 
> **🔗 Core Integrations:** `ShipHero` • `Microsoft Dynamics`
> ---

> ### 8. Automated Freight Audit & Payment
> **The Problem:** Carriers frequently overcharge due to complex rate matrices. Auditing freight bills manually takes hours and companies leave money on the table.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_08_automated_freight_audit_payment.json)
> 
> **How it works:** 
> > *Design a workflow that automates freight audit and pay: ingest carrier invoices via email, parse PDFs, compare rates against the contract matrix in a database, and auto-approve or flag disputes for the logistics team.*
> 
> **🔗 Core Integrations:** `Email` • `PDF Parser` • `Database`
> ---

> ### 9. Tier-1 Supplier Risk Trigger
> **The Problem:** If a critical supplier faces a natural disaster or financial trouble, the business needs to secure alternative stock immediately before competitors do.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_09_tier_1_supplier_risk_trigger.json)
> 
> **How it works:** 
> > *Create a workflow that monitors supplier risk via API (e.g., Resilinc); if a tier-1 supplier reports a disruption, automatically identify affected SKUs in the ERP and trigger safety stock releases.*
> 
> **🔗 Core Integrations:** `Resilinc API` • `ERP`
> ---

> ### 10. AI-Driven Demand Planning
> **The Problem:** Simple rolling averages fail to predict complex demand shifts, resulting in poor production scheduling and wasted manufacturing capacity.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/03_10_ai_driven_demand_planning.json)
> 
> **How it works:** 
> > *Build an automated demand planning workflow that pulls historical sales from the POS, applies a time-series forecasting Python script, and outputs recommended production schedules to the manufacturing execution system (MES).*
> 
> **🔗 Core Integrations:** `POS System` • `Python Scripting` • `MES`
> ---
