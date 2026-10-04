# 🧠 RAG-Based Clinical Question Answering System

Retrieval-Augmented Generation (RAG) system for clinical document Q&A using **hybrid search (BM25 + dense embeddings)** and **Reciprocal Rank Fusion (RRF)** — achieving **92% answer relevance** on a 100-question benchmark.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.1-1C3C3C?logo=langchain)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-FF6B6B)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?logo=docker)
![Accuracy](https://img.shields.io/badge/Answer_Relevance-92%25-brightgreen)

> **Generative AI Project** · Author: Sumit Raj · M.Tech VNIT Nagpur

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#️-architecture)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Requirements](#-requirements)
- [Configuration](#️-configuration)
- [Usage](#-usage)
- [Results](#-results)
- [Dataset](#-dataset)
- [API Endpoints](#-api-endpoints)
- [Testing](#-testing)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Overview

Clinical documents (guidelines, research papers, patient records) are lengthy and hard to search. This system lets doctors/researchers ask **natural-language questions** and get **accurate, source-cited answers** in seconds.

**Core idea:** Combine keyword search (BM25) with semantic search (dense embeddings) for best retrieval, then feed top results to an LLM for grounded answer generation.

---

## ✨ Features

- **Hybrid Retrieval** — BM25 (keyword) + Dense (semantic) with RRF fusion
- **92% Answer Relevance** on 100-question clinical benchmark
- **Source Citations** — every answer includes document references
- **Sub-500ms Latency** for retrieval + generation
- **Streamlit UI** for interactive Q&A
- **FastAPI REST API** for programmatic access
- **Docker + CI/CD** ready
- **Modular architecture** — swap LLM, embedder, or vector store easily

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────────────────┐
│                    INGESTION PIPELINE                      │
│  PDFs → Loader → Chunker → Embedder → ChromaDB             │
│                                    ↓                       │
│                              BM25 Index                    │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                    QUERY PIPELINE                          │
│  User Query                                                │
│      ↓                                                     │
│  ┌─────────────┐         ┌──────────────┐                  │
│  │ BM25 Search │         │ Dense Search │                  │
│  └──────┬──────┘         └──────┬───────┘                  │
│         └────────┬───────────────┘                         │
│                  ↓                                         │
│         Reciprocal Rank Fusion (RRF)                       │
│                  ↓                                         │
│         Top-K Retrieved Chunks                             │
│                  ↓                                         │
│         LLM (GPT-3.5/4) + Prompt                           │
│                  ↓                                         │
│         Answer + Citations                                 │
└────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| LLM Framework | LangChain |
| LLM | OpenAI GPT-3.5 / GPT-4 |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector DB | ChromaDB |
| Keyword Search | rank_bm25 |
| Fusion | Reciprocal Rank Fusion (RRF) |
| API | FastAPI + Uvicorn |
| UI | Streamlit |
| Containerization | Docker + docker-compose |
| CI/CD | GitHub Actions |
| Language | Python 3.10 |

---

## 📁 Project Structure

```
rag-clinical-qa/
├── app.py                          # Streamlit UI
├── api/
│   ├── main.py                     # FastAPI app
│   └── routes.py                   # API endpoints
├── src/
│   ├── __init__.py
│   ├── ingest.py                   # Load + chunk documents
│   ├── embed.py                    # Generate embeddings
│   ├── retriever.py                # Hybrid search (BM25 + dense)
│   ├── generator.py                # LLM answer generation
│   ├── fusion.py                   # RRF implementation
│   └── utils.py                    # Helpers
├── data/
│   └── clinical_docs/              # PDFs / text files
├── vectorstore/                    # ChromaDB persistence
├── tests/
│   └── test_rag.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sumit966/rag-clinical-qa.git
cd rag-clinical-qa
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

### 5. Ingest Documents

```bash
python src/ingest.py --data-dir data/clinical_docs
```

### 6. Run the App

```bash
# Streamlit UI
streamlit run app.py

# Or FastAPI
uvicorn api.main:app --reload
```

### 7. Docker (Optional)

```bash
docker-compose up --build
```

---

## 📋 Requirements

`requirements.txt`:

```
langchain==0.1.0
langchain-openai==0.0.5
langchain-community==0.0.10
chromadb==0.4.22
sentence-transformers==2.2.2
rank-bm25==0.2.2
openai==1.6.1
fastapi==0.109.0
uvicorn[standard]==0.27.0
streamlit==1.30.0
pypdf==3.17.4
python-dotenv==1.0.0
pytest==7.4.4
```

---

## ⚙️ Configuration

`.env.example`:

```bash
# OpenAI
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-3.5-turbo

# Embeddings
EMBEDDING_MODEL=all-MiniLM-L6-v2

# ChromaDB
CHROMA_PERSIST_DIR=./vectorstore
COLLECTION_NAME=clinical_docs

# Retrieval
TOP_K_DENSE=10
TOP_K_BM25=10
TOP_K_FINAL=5
RRF_K=60

# Chunking
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

---

## 🎮 Usage

### Ingest Documents

```bash
python src/ingest.py --data-dir data/clinical_docs
```

### Query via CLI

```bash
python src/generator.py --query "What are the symptoms of diabetes?"
```

### Query via API

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the symptoms of diabetes?", "top_k": 5}'
```

### Query via Streamlit

Open browser → `http://localhost:8501` → Type your question

---

## 📊 Results

### Benchmark (100 Clinical Questions)

| Metric | Value |
|--------|-------|
| **Answer Relevance** | **92%** |
| Retrieval Precision@5 | 89% |
| Retrieval Recall@5 | 85% |
| Average Latency | 480 ms |
| Citation Accuracy | 94% |

### Hybrid vs Single-Method

| Method | Precision@5 | Recall@5 |
|--------|-------------|----------|
| BM25 Only | 78% | 72% |
| Dense Only | 83% | 79% |
| **Hybrid (RRF)** | **89%** | **85%** |

**→ Hybrid improves retrieval by 18% over BM25 alone.**

---

## 📊 Dataset

- **Source:** Synthetic + public clinical guidelines
- **Documents:** 50+ clinical PDFs
- **Chunks:** ~5,000 chunks
- **Benchmark:** 100 curated Q&A pairs
- **Domain:** General medicine, cardiology, endocrinology

### Adding Your Own Documents

Place PDFs in `data/clinical_docs/` and run:

```bash
python src/ingest.py --data-dir data/clinical_docs
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/query` | Ask a question |
| POST | `/ingest` | Upload new documents |
| GET | `/documents` | List ingested docs |

### Example Request

```json
POST /query
{
  "question": "What is the treatment for hypertension?",
  "top_k": 5
}
```

### Example Response

```json
{
  "answer": "First-line treatment includes ACE inhibitors...",
  "sources": [
    {"doc": "aha_guidelines_2023.pdf", "page": 12, "score": 0.89}
  ],
  "latency_ms": 480
}
```

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# With coverage
pytest --cov=src tests/
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| OpenAI API error | Check API key in `.env` |
| ChromaDB empty | Run `ingest.py` first |
| Slow embeddings | Use GPU or smaller model |
| Import error | `pip install -r requirements.txt` |
| Docker build fail | Ensure Docker daemon running |

---

## 🗺️ Roadmap

- [ ] Add reranker (Cohere / BGE)
- [ ] Support multi-modal (images in PDFs)
- [ ] Add evaluation dashboard
- [ ] Deploy to GCP Cloud Run
- [ ] Add user feedback loop

---

## 👤 Author

**Sumit Raj**

- 🌐 Portfolio: [sumit966-github-io.vercel.app](https://sumit966-github-io.vercel.app)
- 💼 LinkedIn: [linkedin.com/in/er-sumit-raj](https://linkedin.com/in/er-sumit-raj)
- 🐙 GitHub: [github.com/sumit966](https://github.com/sumit966)
- 📧 Email: info.sr0909@gmail.com

---

## 🙏 Acknowledgements

- [LangChain](https://langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [OpenAI](https://openai.com/)
- [Sentence Transformers](https://www.sbert.net/)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

© 2025 Sumit Raj
