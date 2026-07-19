# 🚀 n8n.automation | Enterprise-Grade Automation Prompts & Templates

Welcome to **n8n.automation**, a curated repository of 100 super-complex, enterprise-level automation prompts designed to be fed into AI to generate high-value n8n workflows. This repo is built to help automation agencies, freelancers, and enterprise architects attract high-ticket clients by solving complex business problems.

---

## 📂 Directory of Automations

Each of the 10 categories below contains 10 expertly crafted automation briefs. Click on any category to view the business problems, the prompts to build the workflows, and the core integrations used.

| Category | Description | Link |
| :--- | :--- | :--- |
| **01. FinOps & Revenue** | Multi-currency revenue recognition, AP workflows, subscription dunning, tax syncing. | [View Prompts](./prompts/01_finops_and_revenue.md) |
| **02. HR & Talent** | Automated onboarding, offboarding, performance reviews, internal mobility. | [View Prompts](./prompts/02_hr_and_talent.md) |
| **03. Supply Chain** | Inventory POs, freight tracking, supplier scorecards, demand planning. | [View Prompts](./prompts/03_supply_chain_and_logistics.md) |
| **04. Customer Success** | Product usage monitoring, ticket triage, QBR prep, churn intervention. | [View Prompts](./prompts/04_customer_success.md) |
| **05. Sales & CRM** | Lead routing, CPQ, deal desk approvals, competitor pricing alerts. | [View Prompts](./prompts/05_sales_and_crm.md) |
| **06. ITSM & DevOps** | Incident response, cloud cost optimization, vulnerability management. | [View Prompts](./prompts/06_itsm_and_devops.md) |
| **07. Marketing Ops** | Webinar operations, ad spend reconciliation, content syndication. | [View Prompts](./prompts/07_marketing_operations.md) |
| **08. Legal & Compliance** | NDA processing, DSAR workflows, vendor risk assessments, SOC2 prep. | [View Prompts](./prompts/08_legal_and_compliance.md) |
| **09. Data Engineering** | ETL pipeline monitoring, data dictionary updates, schema evolution. | [View Prompts](./prompts/09_data_engineering.md) |
| **10. Executive Ops** | Board deck creation, M&A data rooms, cap table management. | [View Prompts](./prompts/10_executive_operations.md) |

---

## 📖 How to Use This Repo

1. **The Prompts:** Navigate to the `/prompts` directory. Copy any prompt and feed it to an AI (like ChatGPT, Claude, or Qwen) to generate the exact n8n JSON, node configurations, and architectural logic.
2. **The Meta-Prompt:** Use the prompt in `/meta-prompts` to generate standardized documentation templates for your clients.
3. **The Workflows:** As you build these, export the JSON from n8n and push them to the `/workflows` directory to build your portfolio.

## 🏗 Repository Structure

- **`/prompts`**: 100 complex prompts categorized by enterprise domain.
- **`/meta-prompts`**: AI prompts to generate business problem-solving templates.
- **`/workflows`**: Actual n8n workflow JSON exports (coming soon).

## 🤝 Contributing

Found a complex edge case? Open a PR to add more enterprise prompts!

---
*Built for automation architects who build for the enterprise.*

💡 **Tips for Using This Repo to Attract Clients**
- **Don't just sell the workflow, sell the outcome**: When pitching a client, use the [Meta-Prompt](./meta-prompts/business-problem-template-generator.md) to generate a beautiful business case document. Show them the ROI, not just the n8n nodes.
- **Build a "Proof of Concept" (POC) Library**: Pick 5 of the most common prompts (e.g., #31 for Customer Success, #41 for Sales). Build them, export the JSON, and put them in the `/workflows` folder. Offer these as free/low-cost entry points to get your foot in the door.
- **Customize the Prompts**: Before feeding a prompt to the AI, replace the generic tools (e.g., "Salesforce") with the specific tools your prospect uses (e.g., "HubSpot" or "Pipedrive").
