# 09. Data Engineering & Analytics

> ### 1. Self-Healing ETL Pipeline Monitor
> **The Problem:** When an Airbyte or Fivetran sync fails silently, data engineers only find out days later when executives complain about stale dashboards.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_01_self_healing_etl_pipeline_monitor.json)
> 
> **How it works:** 
> > *Build an n8n workflow that automates ETL pipeline monitoring: listen for webhooks from Fivetran/Airbyte; if a sync fails, parse the error, restart the sync, and if it fails twice, page the data engineer via PagerDuty.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> FivetranAirbyteWebhooks["Fivetran/Airbyte Webhooks"]
>     FivetranAirbyteWebhooks --> PagerDuty["PagerDuty"]
> ```
> 
> **🔗 Core Integrations:** `Fivetran/Airbyte Webhooks` • `PagerDuty`
> ---

> ### 2. Automated Data Quality Circuit Breaker
> **The Problem:** Bad data ingested from upstream systems pollutes downstream BI reports. By the time it's noticed, the data warehouse is already corrupted.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_02_automated_data_quality_circuit_breaker.json)
> 
> **How it works:** 
> > *Design a workflow that automates data quality checks: run a Great Expectations script via a webhook; if data quality drops below 99%, automatically halt downstream dbt models in Snowflake and alert the data team.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> GreatExpectations["Great Expectations"]
>     GreatExpectations --> dbt["dbt"]
>     dbt --> Snowflake["Snowflake"]
>     Snowflake --> AlertingAPI["Alerting API"]
> ```
> 
> **🔗 Core Integrations:** `Great Expectations` • `dbt` • `Snowflake` • `Alerting API`
> ---

> ### 3. Auto-Updating Data Dictionary 
> **The Problem:** Data catalogs (like Atlan or Alation) go out of date instantly because engineers forget to document new schema columns.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_03_auto_updating_data_dictionary.json)
> 
> **How it works:** 
> > *Create an automated data dictionary update workflow: when a new column is added to a Snowflake table, automatically extract the metadata, use AI to generate a description, and push it to the data catalog (Atlan).*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Snowflake["Snowflake"]
>     Snowflake --> AI["AI"]
>     AI --> DataCatalogAtlan["Data Catalog (Atlan)"]
> ```
> 
> **🔗 Core Integrations:** `Snowflake` • `AI` • `Data Catalog (Atlan)`
> ---

> ### 4. Statistical Dashboard Anomaly Detection
> **The Problem:** Business owners don't look at dashboards every day. When a key metric crashes, it goes unnoticed unless a data analyst spots it manually.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_04_statistical_dashboard_anomaly_detection.json)
> 
> **How it works:** 
> > *Build a workflow that automates anomaly detection in dashboards: pull daily metrics from Looker; if a metric deviates >3 standard deviations from the 30-day mean, automatically generate a root-cause analysis prompt and email the data owner.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Looker["Looker"]
>     Looker --> StatisticalScripting["Statistical Scripting"]
>     StatisticalScripting --> EmailSlack["Email/Slack"]
> ```
> 
> **🔗 Core Integrations:** `Looker` • `Statistical Scripting` • `Email/Slack`
> ---

> ### 5. Dynamic PII Masking for Dev Environments
> **The Problem:** Copying production databases to dev environments for testing often accidentally exposes sensitive customer PII to developers, causing massive compliance breaches.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_05_dynamic_pii_masking_for_dev_environments.json)
> 
> **How it works:** 
> > *Design a workflow that handles automated data masking: when a production database clone is requested for dev, automatically trigger a script to mask PII (names, emails, SSNs) before provisioning the database to the developer.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> DatabaseCloningAPI["Database Cloning API"]
>     DatabaseCloningAPI --> MaskingScript["Masking Script"]
> ```
> 
> **🔗 Core Integrations:** `Database Cloning API` • `Masking Script`
> ---

> ### 6. Automated Schema Evolution Handling
> **The Problem:** When an upstream engineering team adds a field to a JSON payload, it breaks downstream Kafka consumers if the schema registry isn't updated.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_06_automated_schema_evolution_handling.json)
> 
> **How it works:** 
> > *Create a workflow that automates schema evolution: when a new JSON field is detected in an incoming Kafka topic, automatically update the Avro schema in the Schema Registry and notify the data engineers via Slack.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Kafka["Kafka"]
>     Kafka --> SchemaRegistry["Schema Registry"]
>     SchemaRegistry --> Slack["Slack"]
> ```
> 
> **🔗 Core Integrations:** `Kafka` • `Schema Registry` • `Slack`
> ---

> ### 7. BI Tool "Data Health" Digest
> **The Problem:** The data team has no idea which dashboards are actually being used by the business, leading to wasted compute costs refreshing abandoned reports.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_07_bi_tool_data_health_digest.json)
> 
> **How it works:** 
> > *Build a workflow that syncs BI tool metadata to Slack: every Monday, pull the most viewed dashboards from Tableau, the slowest running queries from Snowflake, and post a "Data Health & Usage" digest to the #data-team channel.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Tableau["Tableau"]
>     Tableau --> SnowflakeMetadata["Snowflake Metadata"]
>     SnowflakeMetadata --> Slack["Slack"]
> ```
> 
> **🔗 Core Integrations:** `Tableau` • `Snowflake Metadata` • `Slack`
> ---

> ### 8. Automated Data Retention & Archival
> **The Problem:** Keeping years of raw log data in a high-performance Snowflake warehouse costs a fortune. DBA teams rarely have time to clean up old tables manually.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_08_automated_data_retention_archival.json)
> 
> **How it works:** 
> > *Design a workflow that automates data retention policies: monthly, query Snowflake for tables older than X days, generate a drop/alter script, route it for DBA approval via Slack, and execute upon approval.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> Snowflake["Snowflake"]
>     Snowflake --> Slack["Slack"]
> ```
> 
> **🔗 Core Integrations:** `Snowflake` • `Slack`
> ---

> ### 9. Intelligent API Rate Limit Handler
> **The Problem:** Simple ETL scripts often crash because they hit rate limits on external APIs (like Shopify or Zendesk), requiring manual engineering intervention to restart.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_09_intelligent_api_rate_limit_handler.json)
> 
> **How it works:** 
> > *Create a workflow that automates API rate limit handling: when an external API returns a 429 Too Many Requests, automatically parse the Retry-After header, pause the n8n workflow using a Wait node, and resume seamlessly.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> ExternalAPIs["External APIs"]
>     ExternalAPIs --> WaitNodesn8n["Wait Nodes (n8n)"]
> ```
> 
> **🔗 Core Integrations:** `External APIs` • `Wait Nodes (n8n)`
> ---

> ### 10. Automated Data Lineage Mapping
> **The Problem:** When a base table changes, data engineers have no way to know which downstream reports will break because documentation is completely siloed.
> 
> **The Workflow:** 📥 [Download n8n JSON](../workflows/09_10_automated_data_lineage_mapping.json)
> 
> **How it works:** 
> > *Build a workflow that automates data lineage mapping: parse SQL queries from the query warehouse (e.g., Databricks), extract table dependencies, and automatically update the lineage graph in the data catalog.*
> 
> **Visual Pipeline:**
> ```mermaid
> graph LR
>     Trigger[Webhook Trigger] --> DatabricksQueryHistory["Databricks (Query History)"]
>     DatabricksQueryHistory --> SQLParser["SQL Parser"]
>     SQLParser --> DataCatalog["Data Catalog"]
> ```
> 
> **🔗 Core Integrations:** `Databricks (Query History)` • `SQL Parser` • `Data Catalog`
> ---
