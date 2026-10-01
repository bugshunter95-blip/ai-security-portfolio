# Day 6 — Authorization, BOLA & BFLA

## Objective

Understand how authorization failures occur in web applications and learn to distinguish between:

* authentication
* object-level authorization
* function-level authorization

The main focus was learning how an attacker thinks about **what they are allowed to access versus what the server actually allows**.

---

## 1. Authentication vs Authorization

### Authentication

Authentication answers:

> “Who are you?”

Example:

```text
Login → Username + Password
```

### Authorization

Authorization answers:

> “What are you allowed to do?”

Example:

```text
User A → own orders
Admin → all orders
```

A user can be correctly authenticated but still have broken authorization.

---

# 2. BOLA

BOLA = Broken Object Level Authorization.

It happens when an application fails to verify whether the current user is allowed to access a specific object.

Example:

```http
GET /api/orders/101
```

User A owns order `101`.

If User A changes:

```http
GET /api/orders/102
```

and order `102` belongs to User B, the server should deny access.

If it returns User B's order:

```text
User A
 ↓
Order 102
 ↓
User B's data
```

→ BOLA.

---

## 3. Why BOLA matters

The attacker is changing the **object identifier**.

The object could be:

```text
order_id
user_id
document_id
invoice_id
profile_id
```

The important question is:

> Does the server verify ownership/authorization for this object?

---

# 4. BFLA

BFLA = Broken Function Level Authorization.

Here the attacker accesses a **function/action** they should not be allowed to use.

Example:

```text
Normal User
 ↓
/api/user/profile
```

But the user tries to access:

```text
/api/admin/delete-user
```

If the server allows it without proper authorization:

→ BFLA.

---

## 5. BOLA vs BFLA

### BOLA

Problem with:

> **Which object can I access?**

Example:

```text
GET /orders/102
```

### BFLA

Problem with:

> **Which function/action can I perform?**

Example:

```text
DELETE /admin/user/102
```

Memory trick:

```text
BOLA → Object
BFLA → Function
```

---

# 6. Attacker Thinking

For every request, ask:

```text
Who am I?
What role do I have?
Which object am I accessing?
Whose object is it?
Which function am I calling?
Am I authorized for it?
Does the backend verify this independently?
```

---

# 7. Important Lesson

The client/browser cannot be trusted.

Even if the UI hides:

```text
Delete User
Admin Panel
Refund
```

an attacker may still manually send the underlying request.

Therefore:

> Authorization must be enforced on the server/backend.

---

# 8. Practical Security Reasoning

Example:

```text
User A
 ↓
GET /api/orders/101
```

Normal behavior:

```text
Order 101 = User A
→ allowed
```

Modified request:

```text
GET /api/orders/102
```

If:

```text
Order 102 = User B
```

then expected behavior:

```text
403 Forbidden
```

If the application instead returns the order:

```text
200 OK
```

that indicates a possible BOLA vulnerability.

---

# 9. Function-Level Example

Suppose a normal user can:

```text
GET /profile
GET /orders
```

But an admin-only function is:

```text
DELETE /users/123
```

If a normal user can execute that function successfully:

→ BFLA.

---

# 10. Root Cause vs Attack Technique

An important lesson from later AI-security work:

A prompt or request may be the **way an attacker reaches** a vulnerability.

But the underlying vulnerability can still be:

```text
Missing authorization
```

For example:

```text
Prompt Injection
      ↓
LLM
      ↓
get_order(102)
      ↓
Backend doesn't verify ownership
      ↓
BOLA
```

The root authorization flaw is still BOLA.

--

---

# 12. Key Takeaways

✅ Authentication ≠ Authorization

✅ BOLA = broken access to an object

✅ BFLA = broken access to a function

✅ Hidden UI controls are not security controls

✅ Server-side authorization is critical

✅ Always test whether the backend independently validates access

---

## Attacker Mindset

> “Can I change the object?”

> “Can I call a function I shouldn't?”

> “Does the server actually verify my permission?”

---

## Day 6 Result

✅ Authentication vs authorization
✅ BOLA
✅ BFLA
✅ Object-level testing
✅ Function-level testing
✅ Authorization-focused attacker mindset
