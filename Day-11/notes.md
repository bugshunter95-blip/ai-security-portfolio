# Day 11 — LLM Red Teaming: Recon and Attack Surface Mapping

## What I learned

Today I started Phase 2 of my roadmap: **LLM Red Teaming**.

The first thing I learned was that red teaming should be systematic. I should not just keep trying random prompts and hope something breaks.

The workflow I want to follow is:

`Recon → Attack Surface → Trust Boundary → Hypothesis → Test → Exploit → Impact → Defense → Retest`

## Attack surface mapping

I started looking at an AI application and identifying the different places where an attacker may have influence:

* User input
* System/developer instructions
* Context
* External/untrusted content
* Tools/functions
* Function parameters
* Authorization
* Sensitive data
* Output/downstream actions

The main question I kept asking was:

> What can the attacker control?

## Hypothesis-driven testing

I learned that a hypothesis is not a confirmed vulnerability.

For example:

> Can attacker-controlled input manipulate the LLM into invoking a privileged tool?

That is only a suspicion.

I need to test it and then decide whether it is confirmed or rejected.

The process becomes:

`Observation → Hypothesis → Test → Result`

## PortSwigger — Indirect Prompt Injection

I completed an indirect prompt injection lab.

The interesting part was that the malicious instruction was not placed directly into the user's prompt. It was placed inside external content that the LLM later processed.

The attack flow was:

`Malicious External Content → LLM Reads It → Instruction Gets Followed → Privileged Action`

This made the trust-boundary problem much clearer to me.

## What I learned

Untrusted content should not automatically become a trusted instruction just because an LLM processed it.

## Excessive Agency Lab

I also completed an Excessive Agency lab.

The main issue was that the AI assistant had access to a high-impact capability such as account deletion.

This helped me clearly separate three concepts:

**Excessive Agency** → the model has unnecessary or overly powerful capabilities.

**BOLA** → the wrong object can be accessed or modified.

**BFLA** → a function/action can be performed without the required authorization.

## Defense

The main defenses I noted were:

* Least privilege
* Server-side authorization
* Object ownership checks
* Function-level authorization
* Confirmation for high-impact actions
* Do not use the LLM itself as the authorization boundary

## Key takeaway

My biggest takeaway from today was:

> Before trying to break an AI system, I need to understand what the system can actually do.

---

