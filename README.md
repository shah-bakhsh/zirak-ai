<div align="center">

# Zirak AI

**A production-grade AI assistant with real-time streaming, custom RAG engine, and multi-persona capabilities.**

[![Live Demo](https://img.shields.io/badge/▶_LIVE_DEMO-zirak--ai.onrender.com-9cff93?style=for-the-badge&labelColor=0e0e0e)](https://zirak-ai.onrender.com)

![Python](https://img.shields.io/badge/python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)
![LLaMA 3](https://img.shields.io/badge/LLM-LLaMA%203-7C3AED?style=flat-square&logo=meta&logoColor=white)
![NumPy](https://img.shields.io/badge/RAG-NumPy%20Vectors-013243?style=flat-square&logo=numpy&logoColor=white)
![Render](https://img.shields.io/badge/deploy-render-46E3B7?style=flat-square&logo=render&logoColor=white)

</div>

---

## 📸 Preview

> Click the image to try the live demo!

<div align="center">
<a href="https://zirak-ai.onrender.com">
<img src="./static/assets/ui-preview.png" alt="Zirak AI Interface" width="90%">
</a>
</div>

---

## 💡 About

Zirak AI is a full-stack intelligent assistant built **entirely from scratch** — no LangChain, no heavy abstraction layers.

Instead of relying on bloated frameworks, this project implements:
- A **custom Vector Search Engine** using raw NumPy for cosine similarity
- A **PDF chunking pipeline** for document ingestion and retrieval
- An **SSE streaming frontend** for real-time token-by-token generation
- A **complete auth system** with SHA-256 hashing and isolated user sessions

> *Every component was designed independently to demonstrate deep understanding of how modern AI applications work under the hood.*

---

## ✨ Features

### ⚡ Real-Time Streaming
Fluid token-by-token response generation using Server-Sent Events (SSE). The frontend reads the stream incrementally and renders each token with a typing cursor — identical to ChatGPT.

### 📄 Document Intelligence (RAG)
Upload any PDF. The backend extracts text via PyPDF2, splits it into chunks, generates embeddings using NumPy, and performs cosine similarity search to ground AI responses in your private data.

### 🎭 Multi-Persona Engine
Four specialized AI modes with tuned system prompts:

| Mode | Purpose |
|:-----|:--------|
| 💬 **Chat** | General-purpose sharp assistant |
| 🎯 **Goal Planner** | Step-by-step structured action plans |
| 💼 **Career Coach** | Expert professional strategy advice |
| 📄 **PDF Analyst** | Document-grounded Q&A |

### 🔐 Secure Authentication
Complete user management with SHA-256 password hashing, Flask session middleware, and per-user isolated chat histories in SQLite.

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                      │
│      HTML5 · CSS3 · Vanilla JS · Tailwind · SSE         │
└─────────────────────────┬────────────────────────────────┘
                          │
┌─────────────────────────▼────────────────────────────────┐
│                  FLASK API SERVER                        │
│                                                          │
│  ┌────────────┐  ┌─────────────┐  ┌─────────────────┐   │
│  │ Auth Layer │  │ Chat Router │  │ PDF Processor   │   │
│  │ login/reg  │  │ SSE Stream  │  │ upload/parse    │   │
│  └─────┬──────┘  └──────┬──────┘  └───────┬─────────┘   │
│        │                │                  │             │
│  ┌─────▼──────┐  ┌──────▼──────┐  ┌───────▼─────────┐   │
│  │ SQLite DB  │  │ OpenRouter  │  │ Vector Store    │   │
│  │ users.db   │  │ LLaMA-3 8B │  │ NumPy Cosine    │   │
│  │ memory.db  │  │ (External)  │  │ Similarity      │   │
│  └────────────┘  └─────────────┘  └─────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology | Role |
|:------|:-----------|:-----|
| **Backend** | Python, Flask, Werkzeug | REST API, routing, sessions |
| **Database** | SQLite3 | Users, chat history, memory |
| **AI Engine** | OpenRouter API → LLaMA-3 8B | LLM inference & reasoning |
| **Vector DB** | NumPy, Pickle | Custom embeddings & cosine search |
| **Documents** | PyPDF2 | PDF extraction & chunking |
| **Frontend** | HTML5, CSS3, JavaScript, Tailwind | UI, SSE stream reader |
| **Hosting** | Render, Gunicorn | Production WSGI server |

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/shah-bakhsh/zirak-ai.git
cd zirak-ai
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
```env
OPENROUTER_API_KEY=sk-or-v1-your-key-here
SECRET_KEY=your-secret-session-key
```

**5. Run the app**
```bash
python app.py
```
> Open `http://localhost:5000` in your browser.

---

## ☁️ Deployment

🟢 **Currently live** → [zirak-ai.onrender.com](https://zirak-ai.onrender.com)

Production start command:
```bash
gunicorn app:app
```
Set `OPENROUTER_API_KEY` and `SECRET_KEY` as environment variables in your hosting provider's dashboard.

---

## 📂 Project Structure

```
zirak-ai/
├── app.py                  ← Main app (routes, API, streaming)
├── requirements.txt        ← Python dependencies
├── .env                    ← API keys (git-ignored)
├── .gitignore
├── templates/
│   ├── index.html          ← Chat interface (711 lines)
│   └── login.html          ← Auth page
├── data/
│   ├── users.db            ← User credentials (auto-generated)
│   ├── memory.db           ← Chat history (auto-generated)
│   └── vectors.pkl         ← Vector store (auto-generated)
└── uploads/
    └── pdf_files/          ← Uploaded PDFs
```

---

## 🗺️ Roadmap

| Status | Feature | Description |
|:------:|:--------|:------------|
| ⬜ | **Chat Threads** | Multiple conversations with sidebar navigation |
| ⬜ | **PostgreSQL** | Persistent production database |
| ⬜ | **Markdown Rendering** | Rich text with syntax-highlighted code blocks |
| ⬜ | **Voice Input** | Browser-native speech-to-text |
| ⬜ | **Web Search** | Real-time internet search integration |
| ⬜ | **Multi-Format Upload** | Support for `.docx`, `.csv`, `.txt` |
| ⬜ | **Semantic Embeddings** | HuggingFace transformer-based vectors |

---

## 🤝 Connect

[![GitHub](https://img.shields.io/badge/GitHub-shah--bakhsh-181717?style=for-the-badge&logo=github)](https://github.com/shah-bakhsh)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Shah%20Bakhsh-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shah-bakhsh/)
[![Email](https://img.shields.io/badge/Email-shahbakhshtech-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shahbakhshtech@gmail.com)

---

<div align="center">

*If this project was useful or interesting, a ⭐ on the repo means a lot!*

</div>
