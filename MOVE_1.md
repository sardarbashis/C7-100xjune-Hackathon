# Move 1 — Real User Sessions

## Objective

Observe real learners attempting to explain systems-thinking concepts and identify where understanding becomes memorized knowledge rather than first-principles reasoning.

---

# Participant 1

## Name

Vikrant Negi

## Evidence

Interview Recording:
https://drive.google.com/file/d/1bHyVY-h7mqobTfF8Z5rGtcZ558MEHpvb/view?usp=sharing

Interview Notes:
evidence/vikrant-negi.pdf

## Concept

Why does a backend exist?

## Original Explanation

The participant explained that a backend exists to support the frontend through storage, authentication, secret management, and other system-level operations. He described the backend as the place where application data is stored and where sensitive information can be managed securely.

## Follow-up Questions

1. Why can't we put everything in the frontend/browser?
2. What specifically breaks if we remove the backend entirely?
3. Suppose you are building Instagram with no backend. How would users log in, upload photos, and see posts from other users?
4. Where would user passwords be stored?
5. If browsers can run JavaScript, what can a backend do that a browser cannot?

## Key Responses

The participant reasoned that:

- Data would be lost if everything stayed only on the client device.
- Users would not be able to synchronize data across devices.
- Authentication would become difficult and insecure.
- Sensitive information should not be exposed to users.
- Social applications such as Instagram require a shared system where users can access each other's content.

## Sentence Where Understanding Became a Label

No significant breakdown was observed.

Although the participant used terms such as "storage" and "authentication," he was able to explain them with concrete examples and consequences when challenged.

## Could They Derive the Concept?

Yes.

## Observation

The participant demonstrated strong first-principles reasoning and was able to explain not only what a backend does but why it exists.

---

# Participant 2

## Name

Pramudu

## Evidence

Interview Recording:
https://drive.google.com/file/d/15xckB24vJeAiZBYs7P2fWlrJR8JauMUA/view?usp=sharing

Interview Notes:
evidence/pramudu_interview.pdf

## Concept

Why do APIs exist?

## Original Explanation

The participant initially described APIs as a way for information to move between frontend, backend, and servers.

## Follow-up Questions

1. What problem was the API invented to solve?
2. What breaks if APIs disappear tomorrow?
3. How would a frontend get data without APIs?
4. Can two systems communicate without an API?
5. Why not connect the frontend directly to the database?
6. Why does ChatGPT need an API?

## Key Responses

The participant initially described APIs using communication and bridge analogies.

As questioning continued, the participant began reasoning about:

- Request and response cycles.
- System-to-system communication.
- Server-side processing.
- Security concerns.
- Database access restrictions.
- The need for compute resources outside client devices.

The participant used a restaurant analogy to explain why users should not directly access the database and why an intermediate layer is needed.

## Sentence Where Understanding Became a Label

"API is a bridge between systems."

This explanation described the API through a common analogy but did not explain the underlying problem that APIs solve.

## Could They Derive the Concept?

Partially at first.

Yes after guided questioning.

## Observation

The participant initially relied on memorized explanations and common analogies. However, after several follow-up questions, the participant started reasoning about APIs from a systems perspective and demonstrated improved understanding.

---

# Key Patterns

## Pattern 1

Some learners can immediately reason from first principles when discussing systems concepts.

## Pattern 2

Other learners rely on memorized labels such as:

- "API is a bridge."
- "Backend stores data."

but struggle to explain the underlying problem being solved.

## Pattern 3

Targeted follow-up questions often transform memorized explanations into causal reasoning.

## Pattern 4

The gap is not always a lack of knowledge.

The gap is often between:

- Recognizing a concept.
- Deriving a concept from first principles.

---

# Preliminary Finding

The interviews provide partial support for the hypothesis.

Out of two participants:

- One participant demonstrated first-principles reasoning from the beginning.
- One participant initially relied on memorized labels but improved significantly after structured follow-up questioning.

This suggests that conceptual understanding exists on a spectrum and that guided Socratic questioning may help learners move from recognition to genuine understanding.

---

# Supporting Design Evidence

## Move 3 — System Boundary Diagram

See:
evidence/boundary Diagram.pdf

This diagram defines the boundary between deterministic system behavior and LLM judgment.

## Move 4 — Data Shape Diagram

See:
evidence/Data shape diagram.pdf

This diagram defines how features, golden cases, rubrics, and runs combine to produce pass/fail grading outcomes.
