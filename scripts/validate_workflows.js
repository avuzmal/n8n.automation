const fs = require('fs');
const path = require('path');

const WORKFLOWS_DIR = path.join(__dirname, '..', 'workflows');

function validateWorkflows() {
  console.log('Validating n8n JSON workflows...');
  
  const files = fs.readdirSync(WORKFLOWS_DIR).filter(file => file.endsWith('.json'));
  let hasErrors = false;

  for (const file of files) {
    const filePath = path.join(WORKFLOWS_DIR, file);
    try {
      const data = fs.readFileSync(filePath, 'utf8');
      const workflow = JSON.parse(data);

      const errors = [];

      // Required top-level keys
      if (!workflow.name) errors.push('Missing "name" property');
      if (!Array.isArray(workflow.nodes)) errors.push('Missing or invalid "nodes" array');
      if (typeof workflow.connections !== 'object') errors.push('Missing or invalid "connections" object');

      // Check nodes for hardcoded secrets
      if (Array.isArray(workflow.nodes)) {
        workflow.nodes.forEach(node => {
          const nodeString = JSON.stringify(node);
          
          // Basic heuristic for hardcoded API keys / passwords
          if (nodeString.match(/("password"\s*:\s*"(?!\{\{).*?")/i) && !nodeString.includes('={{\\$credentials')) {
            errors.push(`Node "${node.name}" might contain a hardcoded password.`);
          }
          if (nodeString.match(/("api[_-]?key"\s*:\s*"(?!\{\{).*?")/i) && !nodeString.includes('={{\\$credentials')) {
            errors.push(`Node "${node.name}" might contain a hardcoded API key.`);
          }
        });
      }

      if (errors.length > 0) {
        console.error(`\n❌ [FAIL] ${file}`);
        errors.forEach(err => console.error(`   - ${err}`));
        hasErrors = true;
      } else {
        console.log(`✅ [PASS] ${file}`);
      }
    } catch (e) {
      console.error(`\n❌ [FAIL] ${file}`);
      console.error(`   - JSON Parsing Error: ${e.message}`);
      hasErrors = true;
    }
  }

  if (hasErrors) {
    console.error('\n🚨 Validation failed. Please fix the errors above before committing.');
    process.exit(1);
  } else {
    console.log(`\n🎉 All ${files.length} workflows are structurally valid and contain no plaintext secrets!`);
    process.exit(0);
  }
}

validateWorkflows();
