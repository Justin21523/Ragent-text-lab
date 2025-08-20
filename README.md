# ragent-text-lab — Chinese-first RAG & Agentic LLM Lab (Text-only)

**Goal.** A hands-on lab to build *text-only* LLM applications with **RAG, tool use, multi-agent reasoning, a text-adventure demo, Gradio UI, evaluation, and FastAPI deployment**.
The repo follows an **8-stage roadmap** and delivers **runnable Jupyter notebooks** plus reusable Python modules.

---

## Key capabilities

- **LLMAdapter (OSS-first):** unified chat interface for Transformers / llama.cpp / Ollama.
- **Chinese RAG pipeline:** zh-friendly chunking, BGE embeddings, FAISS, reranking, grounded answers with citations.
- **Tools & Function-Calling:** JSON tool schema, web search (DuckDuckGo + trafilatura), calculator, file lookup, ReAct.
- **Multi-Agent Orchestrator:** Researcher → Planner → Writer → Reviewer with a shared blackboard and retries.
- **RAG-driven Text Adventure:** world-knowledge KB, state machine, choices, save/load, style control, moderation.
- **UI & API:** Gradio multi-mode panel and FastAPI (REST + WebSocket, OpenAI-compatible route).
- **Eval & Observability:** Recall@k, nDCG, groundedness, Rouge/chrF++, latency/tokens/VRAM, run reports.

---

## Repository layout

```

ragent-text-lab/
notebooks/1..8/              # 61 notebooks across 8 stages (training-oriented walkthroughs)
shared\_utils/                # adapters/, rag/, agents/, prompts/, metrics/, ui/, utils/
apps/                        # gradio\_app/, api/
configs/                     # rag.yaml, agents.yaml, styles/\*.yaml, ui/api configs
scripts/                     # setup\_env.py, helpers
tests/                       # minimal smoke and component tests
data/ indices/ outs/         # git-ignored artifacts & caches

````

> **Shared model cache only.** Large artifacts (models, indices, outputs) live outside git: `AI_CACHE_ROOT`, `data/`, `indices/`, `outs/`.

---

## Prerequisites (Windows)

- Windows 10/11, **PowerShell**, **Git**, **Conda** (Miniconda/Anaconda), Python 3.11
- Optional CUDA GPU (8–12 GB VRAM recommended). CPU fallback is supported.

---

## Quickstart (Windows)

```powershell
# 1) create the skeleton (PowerShell)
#    -> see "Windows terminal: full bootstrap" in the docs/message

# 2) create env and install deps
conda create -y -n rag-agent python=3.11
conda activate rag-agent
pip install -r requirements-dev.txt
pre-commit install
nbstripout --install

# 3) prepare .env
Copy-Item .env.example .env

# 4) smoke: run FastAPI and Gradio (two terminals)
uvicorn apps.api.main:app --host 0.0.0.0 --port 8000
python apps/gradio_app/app.py
````

---

## Configuration

* **.env**

  * `AI_CACHE_ROOT=/mnt/ai/cache` (shared model/data cache)
  * `MODEL_ID`, `BACKEND=transformers|llama_cpp|ollama`
  * `EMBEDDING_MODEL=BAAI/bge-m3`, `RERANKER_MODEL=BAAI/bge-reranker-base`
  * See `configs/rag.yaml` and `configs/agents.yaml` for RAG/agent settings.

---

## LLMAdapter (usage)

```python
from shared_utils.adapters.llm_adapter import LLMAdapter
adapter = LLMAdapter(model_id="Qwen/Qwen2.5-7B-Instruct")
messages = [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Explain RAG in 3 bullets."}
]
print(adapter.generate(messages, max_new_tokens=200, temperature=0.7))
```

---

## Minimal RAG retrieval with citations

```python
# Load config (rag.yaml), embed with BGE, index with FAISS, retrieve -> rerank -> cite
# See notebooks: 2_rag_basics/nb10..nb15
```

---

## Notebooks roadmap (8 stages, 61 notebooks)

* **Stage 1 — Repo & LLMAdapter (8)**
* **Stage 2 — Chinese RAG Basics (10)**
* **Stage 3 — Tools / Function-Calling (10)**
* **Stage 4 — Multi-Agent Orchestrator (10)**
* **Stage 5 — RAG × Text-Adventure (8)**
* **Stage 6 — Gradio UI (6)**
* **Stage 7 — Eval & Observability (5)**
* **Stage 8 — API & Deploy (4)**

Each notebook includes: goals, prerequisites, **shared-cache bootstrap**, MVP code, low-VRAM settings, smoke test, and a “when to use this” note.

---

## Git workflow

* Branch per notebook/feature: `feature/nb10-rag-index`, `feature/agent-orchestrator`, `feature/ui-gradio`, …
* Merge path: `feature/* → develop → main` (use `--no-ff`; tag releases per stage).
* Conventional Commits examples:

  * `feat(rag): build zh chunk + bge-m3 + FAISS index`
  * `feat(agent): 4-role orchestrator with retries`
  * `feat(ui): gradio modes (chat/rag/agents/game)`
  * `feat(api): openai-compatible /v1/chat/completions)`

---

## Security & Safety

* Never print tokens; store secrets in `.env`.
* Tool calls are whitelisted and schema-validated.
* Input sanitization (HTML/URL) and prompt-injection guards.

---

## Contributing

1. Open an issue with context and a minimal test case.
2. Use a feature branch and **Conventional Commits**.
3. Ensure notebooks have a **smoke cell** and outputs are stripped.
4. Run `pre-commit` and tests before opening a PR.

---

## License

MIT (unless your organization requires a different license). Add your LICENSE file accordingly.

````

### (Optional) Save README from PowerShell
```powershell
@"
<PASTE THE ENTIRE MARKDOWN ABOVE>
"@ | Set-Content -Encoding utf8 README.md
````

---

