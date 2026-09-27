# Day 04 — Transformer and Attention

Today I learned the basic idea of Transformers and Attention and connected them with AI Security.

## 1. Transformer

A Transformer is an architecture used by modern language models to process tokens and their relationships with the surrounding context.

A simplified flow is:

Text
↓
Tokens
↓
Transformer
↓
Context and token relationships
↓
Next-token prediction
↓
Output

I don't need to learn the mathematical details of Transformers at this stage.

## 2. Attention

Attention is a mechanism that helps the model process relationships between tokens and determine which parts of the available context are relevant while processing the input.

For example:

"The animal crossed the road because it was tired."

The meaning of "it" depends on the surrounding context.

Another example is the word "bank":

"I deposited money in the bank."

"The boat reached the river bank."

The surrounding context changes the meaning.

### Important point

Attention is not human-like thinking.

It is a mechanism used inside Transformer-based models to process relationships between tokens.

## 3. Encoder and Decoder

Transformers can use encoder and/or decoder components depending on the model architecture.

Basic idea:

* Encoder → processes and represents input information
* Decoder → generates output

There are different Transformer model families:

* Encoder-only
* Decoder-only
* Encoder-decoder

Models such as GPT and Llama are examples of decoder-only language models.

## 4. Causal Language Model

Autoregressive/causal language models generate text by predicting the next token based on the available previous/current context.

Example:

"The cat is sitting on the..."

The model predicts what token could come next.

The model should not use future tokens when making a causal prediction.

## 5. Attention Mask

An attention mask can restrict which tokens the model is allowed to attend to.

For causal language modelling, future tokens are hidden so that the model cannot look ahead while predicting the next token.

Simple idea:

Token 1 → can use Token 1

Token 2 → can use Token 1 and Token 2

Token 3 → can use Token 1, Token 2 and Token 3

But Token 2 cannot use a future Token 3.

## 6. Security Connection

Attention itself is not a vulnerability.

The security concern is what information reaches the model's context and how that information can influence the model's behaviour.

For example:

Attacker-controlled input
↓
Application context
↓
Transformer + Attention
↓
LLM output
↓
Possible security impact

This becomes especially important later when studying indirect prompt injection and RAG security.

If a malicious document is retrieved by a RAG system and added to the model's context, the attacker-controlled content may influence the model's output.

## What I Need To Remember

The main points from Day 4 are:

1. Transformer = architecture used by modern LLMs.
2. Attention = mechanism for processing relationships between tokens/context.
3. Context can influence model behaviour.
4. GPT/Llama are decoder-only models.
5. Causal LM predicts the next token from available previous/current context.
6. Attention masks can restrict access to certain tokens.

I don't need to memorize Q/K/V mathematics or attention equations yet. I need to understand the security implications of context and model behaviour.
