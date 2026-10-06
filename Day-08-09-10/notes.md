# Day 8 — AI Application Attack Surface

## What I learned

Today I continued working on the security foundations required for LLM-based applications.

One thing that became much clearer to me was that an AI application is not just the chatbot or the prompt. There can be multiple components behind it:

* User input
* System/developer instructions
* Context
* LLM
* APIs and tools
* Backend services
* Databases
* External content

I started looking at the complete flow instead of focusing only on the prompt:

`User Input → LLM → Tool/API → Backend → Data/Action`

The main question I kept asking was:

> What can the attacker control, and what does the application trust?

## What I focused on

I worked on the difference between trusted and untrusted input.

An attacker-controlled input can influence the model, and the model may then interact with a component that has much more authority than the attacker.

This creates an important trust boundary:

`Untrusted Input → LLM → Trusted Tool/API`

If the model is allowed to pass attacker-controlled information into a trusted component without enough validation, the impact can be much bigger than the original prompt.

## My initial thinking

At first I was mostly thinking about the prompt itself.

Then I started looking at what happens after the model receives the prompt.

For example:

* Can the model call a function?
* Can it access sensitive data?
* Can it send an email?
* Can it modify something?
* Can it trigger an external action?

This helped me understand why the AI application around the model is just as important as the model itself.

## What I learned

The biggest lesson today was that I need to understand the **whole AI application flow**, not only the LLM.

A prompt may look harmless, but if it can influence a privileged tool or backend action, it can become a real security issue.

---

# Day 9 — Authentication, Authorization and Tool Security

## What I learned

Today I focused more on authorization and how traditional application security problems can appear inside AI applications.

The biggest distinction I worked on was:

**Authentication = Who are you?**

**Authorization = What are you allowed to do?**

A user being authenticated does not mean that the user should be able to access every object or perform every action.

## Example

I used a simple example:

`User A → Order B`

Even if User A is logged in, the backend still has to verify whether User A is actually allowed to access or modify Order B.

This helped me understand why BOLA and BFLA are important when an LLM can interact with APIs and tools.

## Tool and parameter thinking

I also started treating AI tools like normal APIs.

For example:

```text
update_profile(employee_id, field, value)
```

I started breaking the parameters down:

* `employee_id` → whose object?
* `field` → what is being changed?
* `value` → what is the new value?

Instead of only asking what the function does, I started asking:

> Who controls each parameter?

> Can the parameter be manipulated?

> Does the backend validate it?

> What happens if I change it?

## My initial thinking

At first I was mostly thinking about the tool itself.

Then I realized that every parameter can create another attack surface.

For example, changing `employee_id` could potentially target another user's object, while changing `field` could potentially target a more sensitive property.

## What I learned

A useful way to think about an AI tool is:

`Function → Parameters → Authorization → Backend Action`

The LLM does not remove traditional security problems. It can actually become another path through which an attacker reaches APIs and business logic.

---

# Day 10 — AI Security Foundation Consolidation

## What I learned

Today I consolidated the AI Security concepts before starting the LLM Red Teaming phase.

I started connecting vulnerabilities together instead of treating every vulnerability as an isolated topic.

The main workflow I want to remember is:

`Attack Surface → Root Cause → Exploit → Impact → Defense → Retest`

## Questions I want to ask when looking at an AI application

* What can the attacker control?
* What does the LLM trust?
* What tools or functions are available?
* What parameters can be influenced?
* What sensitive data can the model reach?
* Where is authorization enforced?
* What happens if the model is manipulated?
* What is the final security impact?

## What became clearer

Prompt Injection by itself is not always the final impact.

For example:

`Prompt Injection → Tool Call → Backend → Sensitive Action`

The real severity depends on what the model can reach after it is manipulated.

This made concepts like Excessive Agency, BOLA and BFLA much easier to understand.

## Key concepts reinforced

* Prompt Injection
* Sensitive Information Disclosure
* Excessive Agency
* Authentication vs Authorization
* BOLA
* BFLA
* Least Privilege
* Trust Boundaries
* Input Validation

## What I learned

I am starting to move away from simply memorizing vulnerability names.

I want to be able to explain:

**How the attack works → why it works → what the impact is → how to fix it → how to retest it.**

That is the mindset I want to take into LLM Red Teaming.
