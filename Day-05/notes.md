# Day 5 — API Security & Burp Suite

## Objective

Understand how modern web applications communicate through APIs and learn to inspect and manipulate HTTP requests using Burp Suite.

The main goal was not only to learn Burp Suite, but to develop an attacker mindset around:

* endpoints
* parameters
* request/response flow
* user-controlled input
* authorization
* unexpected behavior

---

## 1. What is an API?

An API allows one component of an application to communicate with another component.

Typical flow:

```text
Browser
   ↓
HTTP Request
   ↓
API / Backend
   ↓
Database / Application Logic
   ↓
HTTP Response
   ↓
Browser
```

Example:

```http
GET /api/orders/123
```

The application receives the request, processes it, and returns the requested data.

---

## 2. HTTP Request Structure

A request can contain:

* HTTP method
* URL/path
* headers
* parameters
* body
* cookies/session information

Example:

```http
GET /api/orders/123 HTTP/1.1
Host: example.com
Cookie: session=...
```

The important security idea is:

> Any attacker-controlled part of a request should be considered untrusted input.

---

## 3. Burp Suite

Burp Suite was used to inspect application traffic.

Important areas:

```text
Proxy
HTTP history
Request
Response
```

The basic workflow:

```text
Browser
   ↓
Burp Proxy
   ↓
Application
   ↓
Response
   ↓
Burp
   ↓
Browser
```

This allows a security tester to understand exactly what the browser is sending.

---

## 4. What to look for in requests

When inspecting a request, ask:

```text
What endpoint is being called?
What parameters are being sent?
Which values are controlled by the user?
What happens if a value is changed?
Is authorization being checked?
Does the server trust the client?
```

Example:

```http
GET /api/orders/101
```

Potential attacker question:

> What happens if `101` is changed?

This becomes especially important when testing authorization.

---

## 5. Attacker mindset developed

Instead of only thinking:

> “The website works.”

Think:

```text
What request made this happen?
Which part can I control?
What happens if I modify it?
Does the server independently validate it?
```

This became the foundation for the authorization work on Day 6.

---

## 6. Practical Work

### Practical: HTTP Request Inspection

The application was tested through Burp Suite to understand:

* request/response flow
* endpoint structure
* parameters
* user-controlled values
* backend behavior

---
## 7. Key Takeaways

* APIs are part of the application's attack surface.
* HTTP requests contain attacker-controlled input.
* Burp Suite makes application behavior visible.
* Parameters should never automatically be trusted.
* Security testing starts by understanding the request before trying to exploit it.

## Security Thinking

> “What does the application trust that the attacker can control?”

---

## Day 5 Result

✅ HTTP/API fundamentals
✅ Burp Suite basics
✅ Request/response inspection
✅ Parameter analysis
✅ Basic attacker mindset
