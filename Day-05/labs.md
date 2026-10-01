# Day 5 — API Security & Burp Suite

## What I learned

Today I focused on how APIs work and how I can inspect their requests and responses using Burp Suite.

Before this, I mostly looked at an application from the UI side. Today I started looking at what is actually happening in the background.

### Basic API flow I understood

```text
Browser
   ↓
HTTP Request
   ↓
API / Backend
   ↓
Database / Logic
   ↓
HTTP Response
   ↓
Browser
```

I learned that the browser is not the whole application. A lot of important security checks happen at the API/backend level.

## Burp Suite

I used Burp Suite to see the requests sent by the application.

The main things I looked at were:

* endpoint
* HTTP method
* parameters
* headers
* request body
* response

The main thing I realized was that many values in a request can be controlled or modified by an attacker.

For example:

```http
GET /api/orders/123
```

I started thinking about questions like:

> What happens if I change `123`?

> Does the server actually check whether I am allowed to access that object?

## Attacker mindset I started building

Instead of only asking:

> “Does this feature work?”

I started asking:

> “What request makes this feature work?”

> “Which part of this request can I control?”

> “What happens if I change it?”

This became the base for the authorization testing I did on Day 6.

## What I learned from the practical work

* APIs are an important part of the attack surface.
* Client-side restrictions are not enough.
* Request parameters should be treated as untrusted input.
* Burp makes it much easier to understand application behavior.

## My takeaway

The biggest thing I learned today was that **I should understand the request first and then think about how it can be abused.**
