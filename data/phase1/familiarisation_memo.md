# Familiarisation Memo — Phase 1 Week 2

**Researcher:** Leon Kamau Kiunga (201759400)
**Date:** 2026-05-13
**Dataset version:** Anthropic AEI Feb 2026 + OpenAI NBER WP 34255 + OpenRouter 100T Token Study
**Total task instances reviewed:** 131

---

## Initial Impressions

The combined task corpus of 131 instances draws from three empirically grounded sources spanning two major AI platforms (Claude and ChatGPT) and a broad cross-platform aggregator (OpenRouter). Reviewing all instances together reveals several salient patterns.

**Dominance of technical and software tasks.** The Anthropic AEI data (103 tasks, Feb 2026) positions software-related tasks — website development, business software, debugging, ML systems, DevOps, mobile apps, SQL, APIs, security — as collectively the largest cluster. Academic coursework assistance is the single most frequent individual task (5.19%), but code-adjacent tasks collectively represent roughly 35–40% of usage. This broadly replicates the November 2025 distribution, though task labels have been consolidated into broader O*NET groupings in the updated dataset.

**Writing and business communication are substantial and distinct.** Professional email drafting, marketing content, business strategy documents, social media content, and document conversion appear as high-frequency tasks separate from purely technical work. The OpenAI data reinforces this: Writing was 23.9% of ChatGPT messages, with the majority being requests to revise existing text rather than create from scratch. This underscores that editing and review behaviours sit within a broader content generation cluster but warrant sub-categorical distinction.

**Information retrieval, research, and advisory tasks are pervasive across all sources.** Consumer product research, medical information, civic guidance, career advice, and factual Q&A appear consistently across Anthropic, OpenAI (24.4% Seeking Information), and OpenRouter (General Q&A). These tasks are primarily one-shot information requests with a distinct character from multi-turn tutoring or deeper analysis.

**Learning and education form a clear, coherent cluster.** Academic assignment help, STEM tutoring, concept explanation, and educational material creation cluster naturally. The OpenAI data identifies tutoring as 10.2% of all messages — a striking figure that elevates education relative to the Anthropic distribution where coursework tasks appear at various academic levels.

**Creative, expressive, and roleplay tasks are meaningful.** OpenRouter reports roleplay as approximately 50% of open-source token usage. OpenAI identifies 5.3% self-expression messages including chitchat and roleplay. Anthropic includes creative fiction, religious and spiritual content, and gaming scenarios. These tasks are qualitatively distinct from productive output-oriented tasks and constitute a recognisable capability.

**Agentic and multi-step reasoning is an emerging modality rather than a distinct user capability.** OpenRouter notes that reasoning models now represent approximately 50% of all usage, and tool-calling reached approximately 15% of token volume at peak. Tasks involving these behaviours (AI system development, automation, DevOps) will be coded under their functional domains rather than as a separate capability, as the user-facing intent remains within existing categories.

**Translation appears consistently across all sources but at moderate volume.** Explicit translation tasks appear in Anthropic (language learning and translation at 1.51%, document translation at 1.20%) and in both OpenAI and OpenRouter. Sufficient to retain as a distinct capability given its qualitatively different nature (cross-lingual conversion rather than monolingual generation or retrieval).

Overall, the data points towards 7–8 distinguishable capability areas. The primary analytical challenge is cleanly separating Content Generation from Review and Feedback, and Information Retrieval from Learning and Education, as these pairs share surface features but differ in the nature of the user's request and the required model output.

---

*Word count: approximately 450 words*
