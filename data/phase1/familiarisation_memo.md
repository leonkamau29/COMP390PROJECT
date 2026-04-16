# Familiarisation Memo

**Phase:** Phase 1, Week 2 — Content Familiarisation (Braun & Clarke, 2006, Phase 1)
**Date:** 2026-04-15
**Researcher:** Leon Kamau Kiunga (201759400)
**Sources reviewed:** Handa et al. (2025) Anthropic Economic Index (top 111 tasks); O*NET Detailed Work Activities (AI-relevant subset); task_instances_raw.csv (111 entries)

---

## Initial Impressions

After reading through the full set of 111+ task instances drawn from the Anthropic Economic Index and O*NET occupational data, several strong patterns emerge immediately. The most striking observation is the sheer dominance of **software and code-related tasks**: debugging, building web applications, working with databases, troubleshooting infrastructure, and implementing AI systems together account for well over 30% of documented usage. This is consistent with Handa et al.'s (2025) finding that technical assistance constitutes 65.1% of usage, though the granularity of the task list reveals this is not monolithic — it spans front-end, back-end, DevOps, ML, and embedded systems.

A second prominent cluster is **content generation**: writing academic assignments, professional emails, marketing copy, creative fiction, legal documents, and business plans. This category is exceptionally broad, blurring the line between producing new content and reformatting or improving existing content. This boundary will require explicit decision rules in the taxonomy.

**Information retrieval and advisory tasks** — answering questions on health, law, finance, career, travel — form a third large cluster. These tasks are often conversational in nature, where the model is expected to synthesise and apply domain knowledge rather than produce structured output.

Notably, **reviewing and editing** (proofreading, revising academic documents, responding to peer reviewers, formatting) emerges as a meaningfully distinct cluster despite not always being labelled as such. This aligns directly with Handa et al.'s finding that "reviewing work" is the second most common usage category at 58.9%, yet lacks dedicated evaluation benchmarks — a finding that is central to this project's contribution.

Finally, **teaching and explanation** tasks (explaining algorithms, tutoring mathematics, teaching programming) appear frequently enough to warrant their own capability, distinct from simply retrieving information: the task is not just to provide facts but to structure and scaffold understanding for a learner.

Overall, the data suggest **7–8 core capabilities** will be sufficient to cover the documented task space without excessive overlap.

---

*Braun & Clarke (2006) Phase 1: Familiarising yourself with your data.*
