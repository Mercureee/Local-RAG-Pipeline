# Local RAG Pipeline (From Scratch)

<!-- TODO: one-sentence tagline. e.g. "A local Retrieval-Augmented Generation
pipeline built from first principles in Python — no orchestration frameworks." -->

A local Retrieval-Augmented Generation (RAG) pipeline built as a set of small,
single-responsibility scripts. The goal is to understand the data engineering
behind RAG — loading, chunking, embedding, vector storage, and retrieval —
rather than to abstract it away.

## Design Decision: No Framework

This pipeline is deliberately built **without LangChain or LlamaIndex**. Each
stage is an isolated, importable module so the data flow and the trade-offs at
every step (chunk sizing, embedding model choice, distance metric, prompt
construction) are explicit and inspectable. This is a learning/portfolio
project focused on systems and data-engineering fundamentals.

## Architecture

The pipeline is split into five distinct stages, each a standalone script that
exposes a function for import by the next stage:

| Stage | Script          | Responsibility                                              |
|-------|-----------------|-------------------------------------------------------------|
| 1     | `load_01.py`    | Read a raw text file, return a clean string.                |
| 2     | `chunk_02.py`   | Slice text into overlapping fixed-size chunks.              |
| 3     | `embed_03.py`   | Convert chunks into dense vector embeddings (local).        |
| 4     | `store_04.py`   | Persist vectors + text to a local vector DB (ChromaDB).     |
| 5     | `query_05.py`   | Retrieve nearest chunks and prompt a local LLM via Ollama.  |

<!-- NOTE: scripts use a `name_NN.py` convention (not `NN_name.py`) so that
each stage is importable as a Python module — identifiers can't start with a
digit. -->

## Requirements

- Python 3.10+  <!-- TODO: confirm the version you're actually targeting -->
- [Ollama](https://ollama.com/) running locally for Stage 5 generation
- Dependencies in `requirements.txt`

## Setup

```bash
# Clone
git clone <your-repo-url>
cd <repo-name>

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

<!-- TODO: document any Ollama model pulls the project needs, e.g.:
    ollama pull llama3
-->

## Usage

Each stage can be run directly for inspection, or imported by the next stage.

```bash
python load_01.py      # Stage 1: print the loaded document
python chunk_02.py     # Stage 2: print the generated chunks
# TODO: fill in remaining stages as they are built
```

<!-- TODO: once the pipeline is wired end-to-end, describe the full run here:
what input goes in, what the user sees come out. -->

## Configuration

<!-- TODO: document the key tunable parameters and why they matter, e.g.:
- chunk_size / overlap (chunk_02.py)
- embedding model name + dimensionality (embed_03.py)
- distance metric: cosine / l2 / ip (store_04.py) — must match normalization choice
- retrieval top-k and the prompt template (query_05.py)
-->

## Project Status

- [x] Stage 1 — Document loading
- [x] Stage 2 — Chunking with overlap
- [ ] Stage 3 — Local embeddings
- [ ] Stage 4 — Vector storage
- [ ] Stage 5 — Retrieval + local LLM generation

## Notes & Known Limitations

<!-- TODO: be honest here — this section reads as senior, not weak. Examples:
- Chunking is character-based, not token-based; a model with a smaller token
  window could silently truncate chunks.
- overlap must be < chunk_size or the chunker will not advance.
- Loader currently expects a single UTF-8 text file.
-->

## License

<!-- TODO: add a license if you want this public (MIT is common for portfolios). -->
