\# 🛡️ AI Security Arsenal



Production-grade offensive \& defensive tools for LLM, Agentic AI, and MCP security testing. Built to address \*\*OWASP LLM Top 10\*\*, \*\*OWASP Agentic AI Top 10\*\*, and \*\*OWASP MCP Top 10\*\* vulnerabilities.



!\[Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)

!\[License](https://img.shields.io/badge/License-MIT-green)



\---



\## 🎯 Tools Overview



| Tool | Type | Purpose |

| :--- | :--- | :--- |

| 🔴 \*\*Agent-Spy\*\* | Offensive | Detects Tool Abuse (ASI02) and data exfiltration via SSE stream parsing |

| 🟢 \*\*AI-Guard\*\* | Defensive | Semantic firewall - blocks Prompt Injection, deobfuscates attacks, redacts PII |

| 🟡 \*\*Auto-AI-Fuzzer\*\* | Automation | Parses Swagger specs to auto-discover AI endpoints and fire payloads |



\---



\## 🚀 Quick Start



```bash

git clone https://github.com/bugshunter95-blip/ai-security-portfolio.git

cd ai-security-arsenal

pip install -r requirements.txt



Agent-Spy

python agent\_spy.py --url http://localhost:8000/api/chat --cookie "session=abc" --payloads payloads.txt



AI-Guard

python ai\_guard.py



Auto-AI-Fuzzer

python auto\_fuzzer.py --swagger swagger.json --payloads payloads.txt



🛡️ Features

Agent-Spy:

Real-time SSE stream parsing

Regex-based leak detection (Email, API Keys, Credentials)

Refusal keyword detection

Auto-save detected leaks

AI-Guard:

Multi-turn context tracking (goal drift detection)

Base64/ROT13 deobfuscation engine

Markdown image exfiltration blocking

System prompt leak prevention

Risk scoring (0-100)

Auto-AI-Fuzzer:

Auto AI endpoint discovery from Swagger

Keyword-based detection (chat, agent, prompt, llm)

Anomaly detection in responses

Built-in WAF bypass delays

⚠️ Disclaimer

These tools are for authorized security testing and educational purposes only. Always obtain proper authorization before testing any system.

📄 License

MIT License

