import json

with open("metadata.json", "r") as f:
    metadata = json.load(f)

# Group by domain
grouped = {}
for item in metadata:
    domain = item["domain"]
    if domain not in grouped:
        grouped[domain] = []
    grouped[domain].append(item)

with open("README.md", "w", encoding="utf-8") as f:
    f.write('''<div align="center">
  <img src="assets/banner.png" alt="n8n Business Automations" width="100%" style="border-radius: 10px;"/>
  <br/><br/>
  
  # 🏢 50 Specific Business Problems Solved with n8n
  
  **Exact Problem & Solution Mappings for Enterprise Automations**
  
  [![n8n.io](https://img.shields.io/badge/Made_for-n8n-FF6D5A?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/)
  [![Open Source](https://img.shields.io/badge/Open_Source-❤️-blue?style=for-the-badge)](https://github.com/avuzmal/business.problems.n8n)
  
</div>

<hr/>

## 📖 The Vision

Instead of generic architectures, this repository outlines **50 highly specific, real-world business bottlenecks** across multiple departments. Each problem is paired with a distinct, ready-to-deploy **n8n automation solution**.

---

## ⚡ Quick Start

1. **Clone this repository**:
   ```bash
   git clone https://github.com/avuzmal/business.problems.n8n.git
   ```
2. **Open your n8n workspace**.
3. In a new or existing workflow, click the **Options** menu (top right) `>` **Import from File...**
4. Select any `.json` file from the `templates/` directory.

---

## 🗂️ Problem & Solution Catalog

''')

    icons = {
        "Marketing": "📈",
        "Sales": "🤝",
        "Customer Support": "🎧",
        "Finance": "💰",
        "HR": "🧑‍💼",
        "IT & Ops": "⚙️",
        "Product": "📦",
        "Legal": "⚖️",
        "E-Commerce": "🛒",
        "Operations": "🏗️",
        "Security": "🔒",
        "Agency/Freelance": "🚀"
    }

    for domain, items in grouped.items():
        icon = icons.get(domain, "🔹")
        f.write(f"### {icon} {domain}\n\n")
        f.write("| Workflow Name | The Problem | The n8n Solution |\n")
        f.write("|:---|:---|:---|\n")
        for item in items:
            name_link = f"**[{item['name']}](templates/{item['filename']})**"
            prob = item['problem']
            sol = item['solution']
            f.write(f"| {name_link} | {prob} | {sol} |\n")
        f.write("\n<br/>\n\n")

    f.write('''---

## 🤝 Contributing

We welcome contributions to expand this library! 

<div align="center">
  <sub>Built with ❤️ by the community. Stop manual work.</sub>
</div>
''')

print("README.md generated successfully!")
