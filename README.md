<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 🧠 RAG-Based Clinical QA — Advanced Animated README 2026 -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24,30&height=220&section=header&text=🧠%20RAG-Based%20Clinical%20QA&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Hybrid%20Retrieval%20(BM25%20+%20Dense)%20with%20Reciprocal%20Rank%20Fusion&descAlignY=58&descSize=17" />
</div>

<!-- TYPING SVG — FIXED URL -->
<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=24&duration=3000&pause=800&color=A78BFA&center=true&vCenter=true&multiline=true&width=700&height=100&lines=🧠+RAG+Pipeline+for+Clinical+QA;⚡+92%25+Answer+Relevance;🎯+Hybrid+Search+(BM25+%2B+Dense);🚀+Sub-500ms+Latency" alt="Typing SVG" />
  </a>
</div>

<br/>

<!-- LIVE BADGES WITH GLOW -->
<div align="center">
  <a href="https://github.com/sumit966/rag-clinical-qa/stargazers">
    <img src="https://img.shields.io/github/stars/sumit966/rag-clinical-qa?style=for-the-badge&color=8b5cf6&labelColor=0d1117&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966/rag-clinical-qa/network/members">
    <img src="https://img.shields.io/github/forks/sumit966/rag-clinical-qa?style=for-the-badge&color=3b82f6&labelColor=0d1117&logo=git&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966/rag-clinical-qa/issues">
    <img src="https://img.shields.io/github/issues/sumit966/rag-clinical-qa?style=for-the-badge&color=ec4899&labelColor=0d1117&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966/rag-clinical-qa/commits/main">
    <img src="https://img.shields.io/github/last-commit/sumit966/rag-clinical-qa?style=for-the-badge&color=10b981&labelColor=0d1117&logo=git&logoColor=white" />
  </a>
  <img src="https://img.shields.io/github/license/sumit966/rag-clinical-qa?style=for-the-badge&color=f59e0b&labelColor=0d1117" />
</div>

<br/>

<!-- TECH STACK — ANIMATED MARQUEE STYLE -->
<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-0.1-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/ChromaDB-Vector_DB-FF6B6B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-1.30-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-GPT--3.5%2F4-412991?style=for-the-badge&logo=openai&logoColor=white" />
</div>

<br/>

<!-- METRIC BADGES -->
<div align="center">
  <img src="https://img.shields.io/badge/Answer_Relevance-92%25-10b981?style=for-the-badge&logo=target&logoColor=white" />
  <img src="https://img.shields.io/badge/Latency-<500ms-3b82f6?style=for-the-badge&logo=speedtest&logoColor=white" />
  <img src="https://img.shields.io/badge/Citation_Accuracy-94%25-8b5cf6?style=for-the-badge&logo=bookstack&logoColor=white" />
  <img src="https://img.shields.io/badge/Benchmark-100_Q%26A-ec4899?style=for-the-badge&logo=checkmarx&logoColor=white" />
</div>

<br/>

<div align="center">
  <i>🧬 Generative AI Project · Author: <b>Sumit Raj</b> · M.Tech VNIT Nagpur</i>
</div>

<br/>

<!-- ANIMATED DIVIDER -->
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

---

## 🎯 Overview

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="400" alt="AI animation"/>
</div>

<br/>

Clinical documents (guidelines, research papers, patient records) are **lengthy and hard to search**. This system lets doctors and researchers ask **natural-language questions** and get **accurate, source-cited answers** in seconds.

> **🎯 Core Idea:** Combine keyword search (BM25) with semantic search (dense embeddings) for best retrieval, then feed top results to an LLM for grounded answer generation.

> **📈 Result:** **92% answer relevance** on a 100-question clinical benchmark.

<br/>

<!-- PROBLEM VS SOLUTION — ANIMATED CARDS -->
<table align="center">
<tr>
<td width="50%" valign="top">

### 🔴 The Problem

<div align="center">
  <img src="https://img.shields.io/badge/❌_Clinical_PDFs-100%2B_pages-D14836?style=for-the-badge" /><br/>
  <img src="https://img.shields.io/badge/❌_Keyword_Search-Misses_Semantics-D14836?style=for-the-badge" /><br/>
  <img src="https://img.shields.io/badge/❌_LLMs-Hallucinate-D14836?style=for-the-badge" /><br/>
  <img src="https://img.shields.io/badge/❌_Manual_Search-Wastes_Time-D14836?style=for-the-badge" />
</div>

</td>
<td width="50%" valign="top">

### 🟢 The Solution

<div align="center">
  <img src="https://img.shields.io/badge/✅_Hybrid_Retrieval-Best_of_Both-10b981?style=for-the-badge" /><br/>
  <img src="https://img.shields.io/badge/✅_RRF_Fusion-Accurate_Ranking-10b981?style=for-the-badge" /><br/>
  <img src="https://img.shields.io/badge/✅_Source_Citations-Every_Answer-10b981?style=for-the-badge" /><br/>
  <img src="https://img.shields.io/badge/✅_Sub--500ms-Latency-10b981?style=for-the-badge" />
</div>

</td>
</tr>
</table>

---

## ✨ Features

<table align="center">
<tr>
<td width="50%" valign="top">

### 🚀 Core Features

- 🎯 **Hybrid Retrieval** — BM25 + Dense with RRF fusion
- 📎 **Source Citations** — Every answer includes references
- ⚡ **Sub-500ms Latency** for retrieval + generation
- 🖥️ **Streamlit UI** for interactive Q&A
- 🌐 **FastAPI REST API** for programmatic access

</td>
<td width="50%" valign="top">

### 🛠️ Engineering

- 🐳 **Docker + CI/CD** ready
- 🧩 **Modular architecture** — swap LLM/embedder easily
- 🧪 **Comprehensive test suite** with pytest
- 📊 **Prometheus metrics** for monitoring
- 🔐 **Environment-based config** via `.env`

</td>
</tr>
</table>

---

## 🏗️ Architecture

### 📥 Ingestion Pipeline

```mermaid
flowchart LR
    A[📄 Clinical PDFs] --> B[📖 Loader]
    B --> C[✂️ Chunker]
    C --> D[🧠 Embedder]
    D --> E[(🗄️ ChromaDB)]
    C --> F[📇 BM25 Index]
    
    style A fill:#8b5cf6,stroke:#fff,color:#fff
    style E fill:#ec4899,stroke:#fff,color:#fff
    style F fill:#3b82f6,stroke:#fff,color:#fff
```

### 🔍 Query Pipeline

```mermaid
flowchart TD
    Q[❓ User Query] --> B1[🔤 BM25 Search]
    Q --> D1[🧠 Dense Search]
    B1 --> R[🎯 Reciprocal Rank Fusion]
    D1 --> R
    R --> T[📊 Top-K Chunks]
    T --> L[🤖 LLM Generation]
    L --> A[✅ Answer + Citations]
    
    style Q fill:#f59e0b,stroke:#fff,color:#fff
    style R fill:#8b5cf6,stroke:#fff,color:#fff
    style A fill:#10b981,stroke:#fff,color:#fff
```

### 📊 Full Data Flow

```
PDFs → Loader → Chunker → Embedder → ChromaDB
                              ↓
                         BM25 Index

User Query
    ↓
┌─────────────┐    ┌──────────────┐
│ BM25 Search │    │ Dense Search │
└──────┬──────┘    └──────┬───────┘
       └───────┬──────────┘
               ↓
      Reciprocal Rank Fusion (RRF)
               ↓
      Top-K Retrieved Chunks
               ↓
      LLM (GPT-3.5/4) + Prompt
               ↓
      Answer + Citations
```

---

## 🛠️ Tech Stack

<table align="center">
<tr>
<td><b>Category</b></td>
<td><b>Technology</b></td>
</tr>
<tr>
<td>🧠 LLM Framework</td>
<td><img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" /></td>
</tr>
<tr>
<td>🤖 LLM</td>
<td><img src="https://img.shields.io/badge/OpenAI_GPT--3.5%2F4-412991?style=flat-square&logo=openai&logoColor=white" /></td>
</tr>
<tr>
<td>🧬 Embeddings</td>
<td><img src="https://img.shields.io/badge/all--MiniLM--L6--v2-FF6B6B?style=flat-square" /></td>
</tr>
<tr>
<td>🗄️ Vector DB</td>
<td><img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square" /></td>
</tr>
<tr>
<td>🔤 Keyword Search</td>
<td><img src="https://img.shields.io/badge/rank__bm25-3b82f6?style=flat-square" /></td>
</tr>
<tr>
<td>🎯 Fusion</td>
<td><img src="https://img.shields.io/badge/RRF-Reciprocal_Rank_Fusion-8b5cf6?style=flat-square" /></td>
</tr>
<tr>
<td>🌐 API</td>
<td><img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/Uvicorn-2C2C2C?style=flat-square" /></td>
</tr>
<tr>
<td>🖥️ UI</td>
<td><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" /></td>
</tr>
<tr>
<td>🐳 Container</td>
<td><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/docker--compose-2496ED?style=flat-square&logo=docker&logoColor=white" /></td>
</tr>
<tr>
<td>⚙️ CI/CD</td>
<td><img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" /></td>
</tr>
<tr>
<td>🐍 Language</td>
<td><img src="https://img.shields.io/badge/Python_3.10-3776AB?style=flat-square&logo=python&logoColor=white" /></td>
</tr>
</table>

---

## 📁 Project Structure

```
rag-clinical-qa/
├── 📱 app.py                  # Streamlit UI
├── 🌐 api/
│   ├── main.py                # FastAPI app
│   └── routes.py
├── 🧠 src/
│   ├── __init__.py
│   ├── ingest.py              # Load + chunk documents
│   ├── embed.py               # Generate embeddings
│   ├── retriever.py           # Hybrid search
│   ├── generator.py           # LLM answer generation
│   ├── fusion.py              # RRF implementation
│   └── utils.py
├── 📄 data/clinical_docs/     # PDFs
├── 🗄️ vectorstore/            # ChromaDB storage
├── 🧪 tests/
│   └── test_rag.py
├── ⚙️ .github/workflows/
│   └── ci.yml
├── 📋 requirements.txt
├── 🐳 Dockerfile
├── 🐳 docker-compose.yml
├── 🔐 .env.example
├── 🚫 .gitignore
├── 📜 LICENSE
└── 📖 README.md
```

---

## 🚀 Quick Start

<div align="center">
  <img src="https://img.shields.io/badge/⏱️_5_min_setup-3776AB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🐳_Docker_ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</div>

<br/>

### 1️⃣ Clone

```bash
git clone https://github.com/sumit966/rag-clinical-qa.git
cd rag-clinical-qa
```

### 2️⃣ Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

```bash
cp .env.example .env
# Add your OpenAI API key in .env
```

### 5️⃣ Ingest Documents

```bash
python src/ingest.py --data-dir data/clinical_docs
```

### 6️⃣ Run

```bash
# 🖥️ Streamlit UI
streamlit run app.py

# 🌐 Or FastAPI
uvicorn api.main:app --reload
```

### 7️⃣ Docker

```bash
docker-compose up --build
```

---

## 📋 Requirements

```txt
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
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-3.5-turbo
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHROMA_PERSIST_DIR=./vectorstore
COLLECTION_NAME=clinical_docs
TOP_K_DENSE=10
TOP_K_BM25=10
TOP_K_FINAL=5
RRF_K=60
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

---

## 🎮 Usage

```bash
# 📥 Ingest
python src/ingest.py --data-dir data/clinical_docs

# 💬 Query CLI
python src/generator.py --query "What are the symptoms of diabetes?"

# 🌐 Query API
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the symptoms of diabetes?", "top_k": 5}'
```

---

## 📊 Results

<div align="center">
  <img src="https://img.shields.io/badge/Answer_Relevance-92%25-10b981?style=for-the-badge&logo=target&logoColor=white" />
  <img src="https://img.shields.io/badge/Precision@5-89%25-3b82f6?style=for-the-badge&logo=target&logoColor=white" />
  <img src="https://img.shields.io/badge/Recall@5-85%25-8b5cf6?style=for-the-badge&logo=target&logoColor=white" />
  <img src="https://img.shields.io/badge/Latency-480ms-f59e0b?style=for-the-badge&logo=speedtest&logoColor=white" />
  <img src="https://img.shields.io/badge/Citation_Accuracy-94%25-ec4899?style=for-the-badge&logo=bookstack&logoColor=white" />
</div>

<br/>

### 📈 Benchmark Metrics

| Metric | Value |
|--------|-------|
| 🎯 **Answer Relevance** | **92%** |
| 🔍 Retrieval Precision@5 | 89% |
| 📊 Retrieval Recall@5 | 85% |
| ⚡ Average Latency | 480 ms |
| 📎 Citation Accuracy | 94% |

### ⚔️ Hybrid vs Single-Method

| Method | Precision@5 | Recall@5 |
|--------|:-----------:|:--------:|
| 🔤 BM25 Only | 78% | 72% |
| 🧠 Dense Only | 83% | 79% |
| ⭐ **Hybrid (RRF)** | **89%** | **85%** |

> 💡 **Insight:** Hybrid RRF outperforms both methods by **+6% precision** and **+6% recall**.

---

## 📊 Dataset

<table align="center">
<tr>
<td width="50%" valign="top">

- 📚 **Source:** Synthetic + public clinical guidelines
- 📄 **Documents:** 50+ clinical PDFs
- ✂️ **Chunks:** ~5,000 chunks
- 📝 **Benchmark:** 100 curated Q&A pairs
- 🏥 **Domain:** General medicine, cardiology, endocrinology

</td>
<td width="50%" valign="top">

**🔄 Add Your Own Data**

1. Drop PDFs into `data/clinical_docs/`
2. Run the ingestion script:

```bash
python src/ingest.py --data-dir data/clinical_docs
```

3. Query via UI or API — done! ✅

</td>
</tr>
</table>

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|:------:|----------|-------------|
| 🟢 `GET` | `/` | Health check |
| 🔵 `POST` | `/query` | Ask a question |
| 🟣 `POST` | `/ingest` | Upload documents |
| 🟠 `GET` | `/documents` | List docs |

---

## 🧪 Testing

```bash
pytest tests/
pytest --cov=src tests/
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| 🔑 OpenAI API error | Check API key in `.env` |
| 🗄️ ChromaDB empty | Run `ingest.py` first |
| 🐌 Slow embeddings | Use GPU or smaller model |
| 📦 Import error | `pip install -r requirements.txt` |
| 🐳 Docker fails | `docker-compose down -v` then rebuild |

---

## 🗺️ Roadmap

- [x] ✅ Hybrid retrieval (BM25 + Dense)
- [x] ✅ Reciprocal Rank Fusion reranking
- [x] ✅ FastAPI + Streamlit interfaces
- [x] ✅ Docker + CI/CD pipeline
- [ ] 🚧 Streaming responses via SSE
- [ ] 🚧 Multi-turn conversation memory
- [ ] 🚧 Fine-tuned domain-specific embedder
- [ ] 🚧 Multilingual support
- [ ] 🚧 PDF upload via UI

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🎉 Open a Pull Request

---

## 👤 Author

<div align="center">
  <a href="https://sumit966.github.io">
    <img src="https://img.shields.io/badge/🌐_Portfolio-Visit-3b82f6?style=for-the-badge" />
  </a>
  <a href="https://www.linkedin.com/in/er-sumit-raj-/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="mailto:info.sr0909@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
</div>

<br/>

<div align="center">
  <b>Sumit Raj</b> — M.Tech Applied AI & ML @ VNIT Nagpur
</div>

---

<br/>

<div align="center">

<table border="1" cellpadding="20" cellspacing="0" width="80%" style="border-color:#8b5cf6; border-radius:12px; border-collapse:separate;">
<tr>
<td align="center">

<br/>

### <samp>L I C E N S E</samp>

<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=600&size=42&duration=3500&pause=1500&color=A78BFA&center=true&vCenter=true&width=400&height=70&lines=MIT+License" alt="MIT License" />

<br/>

<samp>
Free to use &nbsp;·&nbsp; Modify &nbsp;·&nbsp; Distribute
</samp>

<br/>

<samp>
Built and maintained by <b>Sumit Raj</b>
</samp>

<br/>
<br/>

<table border="0" cellpadding="8">
<tr>
<td align="center">
  <img src="https://img.shields.io/badge/📜-MIT-8b5cf6?style=flat-square&labelColor=0d1117" />
</td>
<td align="center">
  <img src="https://img.shields.io/badge/✅-Open_Source-10b981?style=flat-square&labelColor=0d1117" />
</td>
<td align="center">
  <img src="https://img.shields.io/badge/©-2025_Sumit_Raj-3b82f6?style=flat-square&labelColor=0d1117" />
</td>
</tr>
</table>

<br/>

[<kbd> &nbsp; Read the full license &nbsp; </kbd>](LICENSE)

<br/>

</td>
</tr>
</table>

</div>

<br/>

---

</div>

---


<!-- deployment guide coming soon -->
