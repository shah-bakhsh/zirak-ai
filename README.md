<div align="center">

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/%F0%9F%8C%8C%20ZIRAK%20AI-Intelligent%20Assistant-9cff93?style=for-the-badge&labelColor=0e0e0e">
  <img src="https://img.shields.io/badge/%F0%9F%8C%8C%20ZIRAK%20AI-Intelligent%20Assistant-9cff93?style=for-the-badge&labelColor=0e0e0e" alt="Zirak AI" height="45">
</picture>

<br><br>

<samp>A production-grade AI assistant with real-time streaming, custom RAG document intelligence, and multi-persona capabilities — engineered entirely from scratch.</samp>

<br><br>

<a href="https://zirak-ai.onrender.com"><kbd> <br> &nbsp;&nbsp;🔴 TRY LIVE DEMO&nbsp;&nbsp; <br> <br></kbd></a>&nbsp;&nbsp;
<a href="#-getting-started"><kbd> <br> &nbsp;&nbsp;⚡ QUICK START&nbsp;&nbsp; <br> <br></kbd></a>&nbsp;&nbsp;
<a href="#-features"><kbd> <br> &nbsp;&nbsp;✨ FEATURES&nbsp;&nbsp; <br> <br></kbd></a>

<br><br>

<img src="https://img.shields.io/badge/python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">&nbsp;
<img src="https://img.shields.io/badge/flask-2.x-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">&nbsp;
<img src="https://img.shields.io/badge/LLM-LLaMA%203-7C3AED?style=flat-square&logo=meta&logoColor=white" alt="LLaMA 3">&nbsp;
<img src="https://img.shields.io/badge/RAG-NumPy%20Vectors-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy">&nbsp;
<img src="https://img.shields.io/badge/deploy-render-46E3B7?style=flat-square&logo=render&logoColor=white" alt="Render">&nbsp;
<img src="https://img.shields.io/badge/build-passing-brightgreen?style=flat-square" alt="Build">

<br>

---

</div>

<br>

## <samp>📸 Preview</samp>

<div align="center">
<a href="https://zirak-ai.onrender.com">
<picture>
  <img src="./static/assets/ui-preview.png" alt="Zirak AI — Chat Interface" width="88%">
</picture>
</a>

<br><br>

<kbd>Dark Theme</kbd>&nbsp;&nbsp;<kbd>Neon Green Accents</kbd>&nbsp;&nbsp;<kbd>Multi-Workspace UI</kbd>&nbsp;&nbsp;<kbd>Real-Time Streaming</kbd>

</div>

<br>

## <samp>💡 About</samp>

<table>
<tr>
<td>

**Zirak AI** is a full-stack AI assistant built **entirely from scratch** — no LangChain, no heavy abstraction layers, no black-box frameworks.

The project implements its own:
- 🔢 **Custom Vector Search Engine** using raw NumPy for cosine similarity
- 📄 **PDF Chunking Pipeline** for document ingestion and retrieval
- ⚡ **SSE Streaming Frontend** for real-time token-by-token generation
- 🔐 **Authentication System** with SHA-256 hashing and isolated sessions

> <samp>Every component — from the embedding engine to the auth layer — was designed and written independently to demonstrate deep understanding of how modern AI applications actually work under the hood.</samp>

</td>
</tr>
</table>

<br>

## <samp>✨ Features</samp>

<table>
<tr>
<td width="50%" valign="top">

<h3 align="center">⚡ Real-Time Streaming</h3>

<p align="center">
<kbd>Server-Sent Events</kbd>&nbsp;<kbd>Token-by-Token</kbd>
</p>

Fluid response generation using SSE. The frontend reads the stream incrementally and renders each token with a typing cursor animation — identical to how ChatGPT works.

</td>
<td width="50%" valign="top">

<h3 align="center">📄 Document RAG</h3>

<p align="center">
<kbd>PDF Upload</kbd>&nbsp;<kbd>Vector Search</kbd>
</p>

Upload any PDF. The backend extracts text via PyPDF2, splits it into chunks, generates TF-IDF style embeddings, and performs cosine similarity search to ground AI responses in your private data.

</td>
</tr>
<tr>
<td width="50%" valign="top">

<h3 align="center">🎭 Multi-Persona Engine</h3>

<p align="center">
<kbd>4 AI Modes</kbd>&nbsp;<kbd>Context Switching</kbd>
</p>

Four specialized modes with tuned system prompts:

| Mode | Purpose |
|:-----|:--------|
| <samp>💬 Chat</samp> | General-purpose assistant |
| <samp>🎯 Goal Planner</samp> | Structured action plans |
| <samp>💼 Career Coach</samp> | Professional strategy |
| <samp>📄 PDF Analyst</samp> | Document-grounded Q&A |

</td>
<td width="50%" valign="top">

<h3 align="center">🔐 Secure Auth</h3>

<p align="center">
<kbd>SHA-256</kbd>&nbsp;<kbd>Flask Sessions</kbd>
</p>

Complete user management with password hashing, session middleware, and per-user isolated chat histories stored in SQLite. Every user gets their own persistent conversation memory.

</td>
</tr>
</table>

<br>

## <samp>🏗️ Architecture</samp>

```
┌─────────────────────────────────────────────────────────────────┐
│                      CLIENT  (Browser)                          │
│       HTML5 · CSS3 · Vanilla JS · Tailwind · SSE Reader         │
└──────────────────────────┬──────────────────────────────────────┘
                           │  HTTP + Server-Sent Events
┌──────────────────────────▼──────────────────────────────────────┐
│                    FLASK API SERVER (app.py)                     │
│                                                                 │
│   ┌──────────────┐   ┌───────────────┐   ┌──────────────────┐  │
│   │  Auth Layer   │   │  Chat Router  │   │  PDF Processor   │  │
│   │  signup/login │   │  SSE Stream   │   │  upload/parse    │  │
│   └──────┬───────┘   └───────┬───────┘   └────────┬─────────┘  │
│          │                   │                     │            │
│   ┌──────▼───────┐   ┌──────▼───────┐   ┌────────▼─────────┐  │
│   │   SQLite DB   │   │  OpenRouter  │   │  Vector Store     │  │
│   │   users.db    │   │  LLaMA-3 8B  │   │  NumPy Cosine    │  │
│   │   memory.db   │   │  (External)  │   │  Similarity      │  │
│   └──────────────┘   └──────────────┘   └──────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

<br>

## <samp>🛠️ Tech Stack</samp>

<div align="center">

| <samp>Layer</samp> | <samp>Technology</samp> | <samp>Role</samp> |
|:------|:-----------|:-----|
| <kbd>Backend</kbd> | `Python` `Flask` `Werkzeug` | REST API, routing, sessions |
| <kbd>Database</kbd> | `SQLite3` | Users, chat history, memory |
| <kbd>AI Engine</kbd> | `OpenRouter API` → `LLaMA-3 8B` | LLM inference & reasoning |
| <kbd>Vector DB</kbd> | `NumPy` `Pickle` | Custom embeddings & search |
| <kbd>Documents</kbd> | `PyPDF2` | PDF extraction & chunking |
| <kbd>Frontend</kbd> | `HTML5` `CSS3` `JavaScript` `Tailwind` | UI, SSE stream reader |
| <kbd>Hosting</kbd> | `Render` `Gunicorn` | Production WSGI server |

</div>

<br>

## <samp>🚀 Getting Started</samp>

<details>
<summary><kbd> &nbsp;📋 EXPAND — Local Development Setup&nbsp; </kbd></summary>
<br>

**<samp>STEP 1 — Clone</samp>**
```bash
git clone https://github.com/shah-bakhsh/zirak-ai.git
cd zirak-ai
```

**<samp>STEP 2 — Virtual Environment</samp>**
```bash
python -m venv venv

# Activate:
source venv/bin/activate    # Mac / Linux
venv\Scripts\activate       # Windows
```

**<samp>STEP 3 — Dependencies</samp>**
```bash
pip install -r requirements.txt
```

**<samp>STEP 4 — Environment Variables</samp>**

Create a `.env` file in the project root:
```env
OPENROUTER_API_KEY=sk-or-v1-your-key-here
SECRET_KEY=your-secret-session-key
```

**<samp>STEP 5 — Launch</samp>**
```bash
python app.py
```

> Open <kbd>http://localhost:5000</kbd> in your browser.

</details>

<br>

## <samp>☁️ Deployment</samp>

<table>
<tr>
<td>

🟢 **Currently live** at <a href="https://zirak-ai.onrender.com"><kbd>&nbsp;zirak-ai.onrender.com&nbsp;</kbd></a>

**Production server command:**
```bash
gunicorn app:app
```

Set <kbd>OPENROUTER_API_KEY</kbd> and <kbd>SECRET_KEY</kbd> as environment variables in your hosting provider's dashboard.

</td>
</tr>
</table>

<br>

## <samp>📂 Project Structure</samp>

```
zirak-ai/
│
├── app.py                  ← Application entry point (routes, API, streaming)
├── requirements.txt        ← Python dependencies
├── .env                    ← API keys (git-ignored)
├── .gitignore
│
├── templates/
│   ├── index.html          ← Main chat interface (711 lines of UI)
│   └── login.html          ← Authentication page
│
├── data/
│   ├── users.db            ← User credentials    (auto-generated)
│   ├── memory.db           ← Chat history         (auto-generated)
│   └── vectors.pkl         ← Vector embeddings    (auto-generated)
│
└── uploads/
    └── pdf_files/          ← Uploaded documents
```

<br>

## <samp>🗺️ Roadmap</samp>

<table>
<tr><td>

| Status | Feature | Description |
|:------:|:--------|:------------|
| <samp>🔲</samp> | **Chat Threads** | Multiple independent conversations with sidebar |
| <samp>🔲</samp> | **PostgreSQL** | Persistent database for production |
| <samp>🔲</samp> | **Markdown Rendering** | Rich text with syntax-highlighted code blocks |
| <samp>🔲</samp> | **Voice Input** | Browser-native speech-to-text |
| <samp>🔲</samp> | **Web Search** | Real-time internet search integration |
| <samp>🔲</samp> | **Multi-Format Upload** | Support for `.docx`, `.csv`, `.txt` |
| <samp>🔲</samp> | **Semantic Embeddings** | HuggingFace transformer-based vectors |

</td></tr>
</table>

<br>

## <samp>🤝 Connect</samp>

<div align="center">

<a href="https://github.com/shah-bakhsh"><kbd> <br> &nbsp;&nbsp;GitHub: @shah-bakhsh&nbsp;&nbsp; <br> <br></kbd></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/shah-bakhsh/"><kbd> <br> &nbsp;&nbsp;LinkedIn: Shah Bakhsh&nbsp;&nbsp; <br> <br></kbd></a>&nbsp;&nbsp;
<a href="mailto:shahbakhshtech@gmail.com"><kbd> <br> &nbsp;&nbsp;Email: shahbakhshtech&nbsp;&nbsp; <br> <br></kbd></a>

<br><br>

<samp>If this project was useful or interesting, a ⭐ on the repo means a lot.</samp>

</div>
