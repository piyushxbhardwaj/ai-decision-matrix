# Technical Research Sources & Reference Bibliography

This document lists the technical documentations, API repositories, academic research papers, and industrial benchmarks referenced to compile the **AI Decision Matrix 2026**.

---

## 1. Primary Model Developer Documentation

### OpenAI
*   **API Reference & Model Pricing:** [OpenAI Developer Portal](https://platform.openai.com/docs/models)
    *   *Details sourced:* `o1`, `o3-mini`, `gpt-4o`, `gpt-4o-mini` pricing, input/output structures, and context token parameters.
*   **Reasoning Mechanics & Guidelines:** [OpenAI Reasoning Models Guide](https://platform.openai.com/docs/guides/reasoning)
    *   *Details sourced:* Definition of hidden reasoning tokens, test-time compute modifiers, and STEM bench performance.

### Anthropic
*   **Claude Documentation Hub:** [Anthropic Developer Docs](https://docs.anthropic.com/en/docs/welcome)
    *   *Details sourced:* Claude 3.7 Sonnet thinking mode configurations, Claude 3.5 Haiku tooling structures.
*   **System Prompt & Safety Guidelines:** [Anthropic Model Card Directory](https://www.anthropic.com/news/claude-3-family)
    *   *Details sourced:* Character limits, alignment safety principles, and output generation speeds.

### Google Cloud (Vertex AI)
*   **Vertex AI Model Library:** [Google Vertex AI Pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)
    *   *Details sourced:* Gemini 1.5 Pro/Flash tiered pricing (>128k context doubling rules), context caching billing parameters.
*   **Gemini Technical Documentation:** [Google DeepMind Gemini 1.5 Technical Report](https://arxiv.org/abs/2403.05530)
    *   *Details sourced:* Retrieval needle-in-a-haystack metrics, native audio/video ingestion details.

### Meta AI (Llama Open-Weights)
*   **Llama Model Directory:** [Meta Llama Github Repository](https://github.com/meta-llama/llama-models)
    *   *Details sourced:* Llama 3.1 405B base architecture, Llama 3.2 edge execution profiles.
*   **Meta Llama 3.1 Paper:** *The Llama 3 Herd of Models* (AI at Meta, 2024).
    *   *Details sourced:* Distillation permissibility, license agreements for commercial use.

### Mistral AI
*   **Mistral Model Specifications:** [Mistral AI Platform Docs](https://docs.mistral.ai/)
    *   *Details sourced:* Codestral fill-in-the-middle context parsing, Mistral Large multilingual optimization indices.

### xAI
*   **xAI Developer Console:** [xAI API Documentation](https://docs.x.ai/)
    *   *Details sourced:* Grok 2/Grok 3 API endpoints, image generation integration parameters.

---

## 2. Code & Agentic Framework Documents
*   **GitHub Copilot Business Compliance:** [GitHub Trust Center](https://resources.github.com/learn/pathways/copilot-trust-center/)
    *   *Details sourced:* IP indemnification clauses, telemetry exclusion rules for commercial contracts.
*   **Amazon Q Developer Security:** [AWS Q Security Profile](https://aws.amazon.com/q/developer/)
    *   *Details sourced:* Security vulnerability scanning protocols, legacy Java translation workflows.
*   **LangGraph Documentation:** [LangChain LangGraph Docs](https://langchain-ai.github.io/langgraph/)
    *   *Details sourced:* Stateful DAG architectures, human-in-the-loop callback structures.
*   **CrewAI Orchestration:** [CrewAI Developer Guide](https://docs.crewai.com/)
    *   *Details sourced:* Role-playing prompts, task-based collaborative loops.

---

## 3. Academic Foundations & Research Papers
*   **Retrieval-Augmented Generation (RAG):** *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (Lewis et al., 2020).
*   **Matryoshka Representation Learning (MRL):** *Matryoshka Representation Learning* (Kusupati et al., 2022).
    *   *Details sourced:* Logic behind `text-embedding-3` dimension truncation.
*   **Test-Time Compute Scaling:** *Scaling Laws for Test-Time Compute in Decision-Making* (OpenAI Research / DeepMind, 2024-2025).
    *   *Details sourced:* Theoretical foundations of reinforcement-learning-based chain-of-thought loops.

---

## 4. Benchmark Registries & Repositories
*   **LMSYS Chatbot Arena:** [LMSYS Org Leaderboard](https://chat.lmsys.org/)
    *   *Details sourced:* Crowdsourced human preferences and Elo ratings for open-weights vs. closed models.
*   **SWE-bench:** [Software Engineering Benchmark Registry](https://www.swebench.com/)
    *   *Details sourced:* Code resolving metrics across complex software repositories.
*   **MMLU (Massive Multitask Language Understanding):** [Hugging Face Benchmarks](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
    *   *Details sourced:* Zero-shot accuracy scores across academic subjects.
