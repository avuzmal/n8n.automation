# Contributing to n8n.automation

First off, thank you for considering contributing to `n8n.automation`! It's people like you that make this repository such a great resource for enterprise automation architects.

## Adding a New Workflow

1. Fork the repository and create your branch from `main`.
2. Build your workflow in n8n, ensuring no hardcoded credentials or sensitive data are included. Use expressions like `{{$credentials.myApi.key}}`.
3. Export the workflow as a JSON file and place it in the `/workflows` directory. Please follow the naming convention: `XX_XX_workflow_name.json`.
4. Create a matching Markdown brief in the `/prompts` directory describing the business problem and the core integrations.
5. Make sure the Node.js validation script passes (`npm test`).
6. Issue that pull request!

## Code Review Process

The core team looks at Pull Requests on a regular basis. After feedback has been given, we expect responses within two weeks. After two weeks, we may close the pull request if it isn't showing any activity.
