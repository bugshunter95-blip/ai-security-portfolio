# Day 03 — Hands-on Labs

Today I did hands-on experiments related to tokenization, context and temperature using online tools and my local Llama 3.2 model through Ollama.

## 1. Tokenization Experiment

I used a Hugging Face tokenizer playground to see how normal text gets split into tokens.

Test input:

`I love Mumbai and I am learning AI Security.`

The tokenizer showed:

* 45 characters
* 10 tokens

The tokenizer used for this test was a GPT tokenizer, so this was not an exact demonstration of how Llama 3.2 tokenizes the same sentence.

### What I learned

A token is not necessarily the same as a word.

The model processes tokenized representations rather than directly processing normal human text.

This is important for later security topics such as token smuggling and input obfuscation.

---

## 2. Context Experiment

I used Ollama with Llama 3.2 and provided a test secret in one message, followed by a question asking for it.

Test secret:

`BLUE123`

The model responded that it had stored the value and returned the same test secret.

### Observation

The model was able to use information from the previous message because that information was included in the conversation context.

### Security relevance

This shows why applications should be careful about putting sensitive information into an LLM's accessible context.

---

## 3. Temperature Experiment

I tested the same type of request using different temperature values.

### Temperature: 0.1

I ran the experiment three times.

The responses were mostly similar, although there were still small wording differences.

### Temperature: 1.5

I ran the experiment three times again.

The responses showed more variation in wording while remaining generally understandable.

### Observation

Higher temperature resulted in more variation.

Lower temperature resulted in more consistent responses.

### Security relevance

When testing an attack, I should not assume that one successful response is enough. I should repeat the test and check whether the behaviour is reproducible.

---

## Day 03 Security Takeaway

Today's experiments helped me understand:

* Text is converted into tokens.
* The model works with context.
* Information in the conversation can be used by the model.
* Temperature can affect output variation.
* Security testing should check whether behaviour is reproducible.

The main flow I learned today was:

`Input → Tokens → Context → LLM Inference → Output`
