# Day 03 — LLM Fundamentals

Today I learned some basic concepts that are important for understanding how LLMs work and how they can be tested from a security perspective.

## 1. Tokenization

LLMs do not directly process normal human sentences. Text is first converted into tokens, which are then represented as numbers/IDs that the model can process.

A token is not always equal to one complete word. Depending on the tokenizer, a word can be split into multiple tokens.

This is important in AI Security because attackers can sometimes use unusual token patterns, encoding or obfuscation to bypass filters. This is something I will explore later during token smuggling and red teaming.

## 2. Context Window

The context is the information that is available to the model while generating a response.

It can include things such as:

* System instructions
* User messages
* Previous conversation
* Retrieved information
* Tool results

The context window is the maximum amount of tokenized information that a model can handle as context.

It is important to understand that context is not the same as permanent memory.

From a security perspective, if sensitive information is placed inside the model's accessible context, an attacker may try to manipulate the model into revealing it.

## 3. Next Token Prediction

LLMs generate text by predicting the next token based on the context available to them.

For example:

"The cat is sitting on the..."

The model predicts what token is likely to come next.

It repeats this process to generate the complete response.

This is one reason why manipulating the input or context can influence the final output.

## 4. Embeddings

An embedding represents text as a numerical vector.

Texts with similar meanings can have similar representations in embedding space.

Embeddings are especially important in RAG systems.

Basic RAG flow:

Text/Documents
↓
Embeddings
↓
Vector Database
↓
User Query
↓
Similarity Search
↓
Relevant Documents
↓
LLM Context
↓
Answer

From a security perspective, this becomes important because malicious or manipulated documents can potentially enter the retrieved context.

I will study RAG security in much more detail later in the roadmap.

## 5. Inference

Inference means using an already trained model to generate an output.

When I send a prompt to my local Llama model through Ollama and receive a response, the model is performing inference.

Training and inference are different:

* Training → model learns patterns
* Inference → trained model is used to generate output

## 6. Temperature

Temperature affects how predictable or varied the model's output can be.

Lower temperature generally produces more consistent output.

Higher temperature generally produces more variation.

Temperature does not mean that the model becomes more intelligent.

From a security testing perspective, reproducibility matters. If an attack works once, I should test it multiple times to see whether the result is consistent.

## Main Security Takeaway

The important connection from today's topics is:

Attacker-controlled input
↓
Context
↓
LLM processing
↓
Output

If an attacker can influence information that reaches the model's context, they may be able to influence its behaviour.

I don't need to memorize all the technical details yet. The main goal is to understand how tokens, context, inference and embeddings fit into an AI application.
