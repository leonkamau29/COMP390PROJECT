<!-- markdownlint-disable MD013 -->

# Familiarisation Memo: Phase 1 Week 2

I reviewed 131 task instances drawn from the Anthropic Economic Index February 2026 update, OpenAI's NBER working paper 34255, and the OpenRouter 100T token study. Reading these sources together helped me see the dataset less as a set of isolated tasks and more as a pattern of recurring user intentions across Claude, ChatGPT, and cross-platform model usage.

My first impression was that technical and software-related tasks dominate the corpus. The Anthropic AEI data makes this especially clear through website development, debugging, technical troubleshooting, ML systems, DevOps, mobile application work, SQL, APIs, and security-related activity. Academic coursework support is the highest individual task, but the wider group of code-adjacent tasks forms the largest overall cluster. This broadly matches the earlier AEI pattern, although the February 2026 version uses broader O*NET groupings.

I also noticed that writing and business communication form a substantial cluster in their own right. Professional emails, marketing content, strategy documents, social posts, document formatting, and communication tasks appear frequently. The OpenAI data reinforces this because writing accounts for 23.9 percent of ChatGPT messages, with many of those requests involving revision of existing text rather than writing from scratch. This is why I treated content generation and review as related but distinct behaviours.

Information retrieval and advisory tasks appear across all sources. Users ask for product research, medical information, civic guidance, career advice, and factual Q&A. These tasks feel different from tutoring because the user is normally seeking an answer, recommendation, or decision-support summary rather than a learning process.

Learning and education also emerged as a coherent capability. Coursework help, STEM tutoring, concept explanation, and educational material creation group naturally together. OpenAI's tutoring figure of 10.2 percent is important because it raises the significance of education beyond what the Anthropic occupational task list alone might suggest.

Creative, expressive, and roleplay tasks were also meaningful. OpenRouter reports roleplay as a very large share of open-source token use, while OpenAI identifies self-expression messages such as chitchat and roleplay. Anthropic includes creative fiction, religious or spiritual content, and gaming scenarios. These tasks are different from productivity tasks because the interaction itself is often part of the value.

I decided not to treat agentic or multi-step reasoning as a separate user capability at this stage. OpenRouter shows that reasoning models and tool-calling are increasingly important, but these are better understood as interaction modalities that cut across domains. For example, automation or DevOps tasks still belong under technical problem solving because the user's goal is functional technical work.

Translation appeared consistently, although at a lower volume than the largest categories. I kept it as a separate capability because cross-lingual conversion is qualitatively different from monolingual writing, retrieval, or review.

Overall, the data pointed me toward seven or eight distinguishable capability areas. The main analytical challenge was separating pairs that look similar on the surface: content generation from review and feedback, and information retrieval from learning and education. In each case, I used the user's primary intention and the required model output as the deciding features.
