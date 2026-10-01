# Day 7 — LLM API Security

## Objective

Understand how LLM-powered applications interact with APIs/tools and learn how an attacker can abuse the LLM as an intermediary to reach sensitive functionality.

---

# 1. How LLM APIs Work

A real LLM application may use this flow:

```text
User
 ↓
Application
 ↓
LLM
 ↓
Function / API
 ↓
External system
 ↓
Result
 ↓
LLM
 ↓
User
```

The important security insight is:

> The LLM may be able to perform actions, not just generate text.

Example:

```text
User:
“Cancel my order.”

LLM
 ↓
cancel_order()
 ↓
Backend
```

---

# 2. Mapping the LLM API Attack Surface

Before attacking an LLM application, identify what the model can access.

Questions:

```text
What APIs exist?
What functions exist?
What tools exist?
What parameters do they accept?
What can each function do?
```

Example:

```text
get_user()
get_order()
cancel_order()
send_email()
```

Security methodology:

```text
Discover
 ↓
Understand
 ↓
Test
```

---

# 3. Excessive Agency

Excessive agency occurs when an LLM has access to powerful or sensitive capabilities and those capabilities can be misused.

Example:

```text
LLM
 ├── get_user()
 ├── cancel_order()
 └── delete_account()
```

If an attacker manipulates the model into performing an unintended sensitive action, the application's agency becomes a security concern.

Important question:

> What capabilities does the model actually need?

---

# 4. Chaining Vulnerabilities in LLM APIs

The LLM does not necessarily need to be the vulnerable component itself.

The chain can look like:

```text
Attacker
 ↓
LLM
 ↓
API
 ↓
Vulnerability in API/backend
 ↓
Impact
```

Example concepts:

```text
LLM → vulnerable file API → path traversal
LLM → vulnerable API → command injection
```

The key idea:

> The LLM can become a gateway to another security vulnerability.

---

# 5. Insecure Output Handling

LLM output should not automatically be considered trusted.

Potential flow:

```text
Attacker input
 ↓
LLM
 ↓
Malicious output
 ↓
Application
 ↓
Another component
 ↓
Vulnerability
```

Example:

```text
LLM output
 ↓
HTML
 ↓
Browser
 ↓
XSS
```

Security question:

> Where does the LLM's output go next?

---

# 6. Practical: Excessive Agency Lab

### Lab

PortSwigger — Exploiting LLM APIs with excessive agency

The lab was completed using the live chat functionality.

### Objective

Understand how an attacker can manipulate an LLM into performing an unintended sensitive action through one of its accessible capabilities.

### Result

The `carlos` account was successfully deleted through prompt-based manipulation.

### Security lesson

The important lesson was not simply:

> “Delete Carlos.”

The deeper lesson:

```text
Attacker input
 ↓
LLM
 ↓
Accessible capability
 ↓
Sensitive action
 ↓
Impact
```

This demonstrated the relationship between:

* prompt manipulation
* LLM capabilities
* API/tool access
* excessive agency
* real-world impact

---

# 7. Practical: Structured Field Injection

### Lab

OWASP AI Vulnerabilities Playground — PI-05 Structured Field Injection

### Scenario

The assistant processed structured data such as:

```json
{
  "name": "...",
  "role": "...",
  "message": "..."
}
```

The objective was to extract a hidden `SECRET`.

### Key observation

Structured fields were being interpreted in the model context.

By manipulating the structured input and influencing how the model interpreted the fields, the hidden secret was successfully extracted.

### Security lesson

> Structured data is not automatically safe just because it is JSON/YAML.

The model may still interpret attacker-controlled values as instructions.

---

# 8. Manual Attack-Surface Exercise

Scenario:

```text
Customer Support AI

User
 ↓
LLM
 ├── get_user()
 ├── get_order()
 ├── cancel_order()
 └── send_email()
 ↓
Backend
 ↓
Database / Email system
```

We identified:

### Asset

Account access

### Attacker-controlled input

User prompt/message

### Sensitive capability

`cancel_order()`

### Trust boundary

LLM → trusted backend action

### Attack

Attempting:

```text
cancel_order(102)
```

where order `102` belongs to another user.

### Impact

Potential unauthorized control over another user's order.

### Lesson

A single AI system can involve:

```text
Prompt Injection
+
Tool/Function abuse
+
Authorization failures
+
Impact
```

These must be analyzed separately.

---

# 9. Day 7 Security Thinking

The main mental model developed:

```text
Asset
 ↓
Attacker-controlled input
 ↓
Trust boundary
 ↓
LLM
 ↓
API / Tool
 ↓
Potential abuse
 ↓
Impact
 ↓
Root cause
 ↓
Defense
```

---

# 10. Key Takeaways

✅ LLMs can call tools/APIs

✅ LLM capabilities create an additional attack surface

✅ Attack-surface mapping should happen before exploitation

✅ Excessive agency is dangerous when the model has unnecessary power

✅ LLMs can act as gateways to traditional vulnerabilities

✅ LLM outputs should be treated as untrusted data

✅ Structured fields can influence LLM behavior

✅ Prompt injection and underlying authorization flaws can coexist

---

## Attacker Mindset

When looking at an AI application, ask:

```text
What is valuable?
What can the attacker control?
What can the LLM access?
Which actions can the LLM perform?
Where are the trust boundaries?
Is authorization enforced outside the model?
Where does the model output go?
What happens if the model is manipulated?
```

---

## Day 7 Result

✅ LLM API flow
✅ Attack-surface mapping
✅ Excessive agency
✅ Vulnerability chaining
✅ Insecure output handling
✅ Excessive Agency lab
✅ PI-05 Structured Field Injection
✅ Manual attack-surface analysis
