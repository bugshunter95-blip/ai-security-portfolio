# Day 6 — Authorization, BOLA & BFLA

## What I learned

Today I focused on authorization.

One thing that became clear to me was:

**Authentication and authorization are different.**

Authentication asks:

> “Who are you?”

Authorization asks:

> “What are you allowed to access or do?”

---

## BOLA

BOLA means **Broken Object Level Authorization**.

The basic idea is that a user is able to access another user's object just by changing an identifier.

For example:

```http
GET /api/orders/101
```

Suppose order `101` belongs to me.

If I change it to:

```http
GET /api/orders/102
```

and order `102` belongs to another user, the backend should reject it.

If it doesn't, that can be a BOLA vulnerability.

### My understanding

The important thing is not just changing the ID.

The real question is:

> **Does the backend actually verify whether I am allowed to access this object?**

---

## BFLA

BFLA means **Broken Function Level Authorization**.

This is more about accessing a function/action that my role should not be able to use.

Example:

```text
Normal user
    ↓
Normal functions

Admin
    ↓
Admin-only functions
```

If a normal user can directly call an admin-only function through the API, that can be BFLA.

### Simple difference

```text
BOLA → Which object can I access?

BFLA → Which function can I use?
```

That distinction is important for me to remember.

---

## Attacker thinking

I started asking:

> Can I change the object ID?

> Can I access someone else's object?

> Can I call a function meant for another role?

> Is the backend actually checking my permissions?

One important lesson was that **hiding a button from the UI is not authorization**.

The backend still needs to enforce the permission.

---

## Connection with AI Security

I also started seeing how this connects to AI applications.

For example:

```text
User
 ↓
LLM
 ↓
get_order(102)
 ↓
Backend
```

Even if the LLM is manipulated into asking for order `102`, the backend should still check whether the user is allowed to access it.

So AI does not replace normal authorization.

## My takeaway

Today I understood that a request can look completely valid, but still be unauthorized.

The backend should always independently enforce:

**“Is this user allowed to perform this action on this object?”**
