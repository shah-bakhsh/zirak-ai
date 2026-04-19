<div align="center">

# 🌌 Zirak AI 
### *Your Production-Ready, High-Performance Intelligent Assistant*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Backend-black.svg?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Model-Llama--3-purple.svg?style=for-the-badge&logo=meta&logoColor=white" alt="Model">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Status-Production--Ready-success?style=for-the-badge" alt="Status">
</p>

*Zirak AI represents the next generation of personal AI assistants. Engineered from the ground up, it combines the sheer reasoning capability of LLaMA-3 with lightning-fast, custom-built Retrieval-Augmented Generation (RAG) and an elegant, responsive dark-mode UI.*

[**Explore Features**](#-key-features) •
[**Architecture**](#-system-architecture--tech-stack) •
[**Quick Start**](#-quick-start) •
[**Deployment**](#-deployment-ready)

---

</div>

<br>

## 🎨 Premium User Experience

<div align="center">
  <img src="./static/assets/ui-preview.png" alt="Zirak AI User Interface" style="border-radius:12px; box-shadow: 0 8px 16px rgba(0,0,0,0.3); max-width: 100%;">
  <br>
  <i>Featuring a sleek, neon-accented dark theme with specialized intelligence workspaces.</i>
</div>

<br>

## 🚀 Why Zirak AI? (Developer's Vision)

While many modern AI apps rely entirely on heavy, black-box frameworks like LangChain, **Zirak AI was crafted independently to demonstrate a profound understanding of core Machine Learning and AI engineering concepts.** 

Instead of offloading work to bloated libraries, this project implements a **custom, lightweight Vector Search engine utilizing Numpy** for text embeddings and cosine similarity search. This architectural decision guarantees lightning-fast execution, reduced computational overhead, and absolute control over the data pipeline. Furthermore, the project showcases rigorous software engineering practices, secure session management, and highly efficient RESTful API design.

<br>

## ✨ Key Features

Zirak AI isn't just a chatbot; it's a meticulously engineered, multi-modal productivity suite.

- ⚡ **Real-Time Streaming Generation:** Implemented optimized Server-Sent Events (SSE) for fluid, token-by-token instant responses via the OpenRouter API. Watch the AI generate text identically to human typing speeds.
- 📚 **Custom Document Intelligence (RAG):** Built-in TF-IDF style Vector Database utilizing raw Numpy. Upload PDFs, and Zirak will seamlessly parse, vectorize, chunk, and search your documents to anchor responses to your private data.
- 🎯 **Dynamic Personas:** Advanced context-switching architecture seamlessly maps precise system prompts for specialized tasks:
  - 🧠 **General Chat:** A sharp, precise, and highly capable intelligent conversation logic.
  - 📈 **Goal Planner:** Automatically generates structured, step-by-step actionable plans with milestones.
  - 💼 **Career Coach:** Delivers expert professional strategy and industry insights based on the latest trends.
  - 📄 **Document Analyst:** Intelligently restricts conversational context purely to your uploaded PDF knowledge base.
- 🔒 **Secure Authentication Architecture:** Scalable SQLite backend with SHA-256 salted password hashing, robust Flask user sessions, and completely isolated, persistent chat histories per user.

<br>

## 💻 System Architecture & Tech Stack

Carefully selected modern tools ensure Zirak AI handles complex asynchronous operations smoothly while remaining incredibly lightweight.

| Layer | Technologies Used | Purpose |
| :--- | :--- | :--- |
| **Backend API** | Python, Flask, Werkzeug | REST API, Routing, Secure Session Management |
| **Database** | SQLite3 | Persistent User Authentication & Chat History |
| **AI Engine / LLM** | OpenRouter API, LLaMA-3 (8B) | Core Large Language Model processing logic |
| **Vector DB / NLP** | Numpy, PyPDF2, Pickle | Cosine Similarity Search, Embeddings, PDF Parsing |
| **Frontend UI/UX** | HTML5, CSS3, Vanilla JavaScript | Asynchronous fetch, SSE Streaming Handling, DOM manipulation |

<br>

## 🛠 Quick Start Guide

You can have the full AI suite running locally in your environment in **under 2 minutes.**

### 1. Clone & Prepare
```bash
# Clone the repository
git clone https://github.com/shah-bakhsh/zirak-ai.git
cd zirak-ai

# Create a clean virtual environment
python -m venv venv

# Activate the environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
# Install the core engines needed to run Zirak
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a **`.env`** file precisely in the root directory. This standard practice keeps your API keys secure and fully decoupled from the source code.
```env
# Required API Keys & Secrets
OPENROUTER_API_KEY=sk-or-v1-your-api-key-here
SECRET_KEY=super-secret-zirak-session-key-2024
```

### 4. Launch the Application
```bash
# Ignite the server!
python app.py
```
> *Zirak AI is now running at `http://localhost:5000` ✨. Open your browser, register securely, and experience the interface.*

<br>

## 📁 Repository Structure

```text
📦 Zirak AI
 ┣ 📂 data/               # SQLite Databases & Serialized Vectors (.db, .pkl)
 ┣ 📂 templates/          # Modular Jinja2 HTML Templates (index.html, login.html)
 ┣ 📂 static/             # Custom CSS frameworks & JS operational logic 
 ┃ ┗ 📂 assets/           # UI screenshots and visual assets
 ┣ 📂 uploads/            # Temporary volatile storage for PDF file streams
 ┣ 📜 app.py              # Main Application Entry Point & Route Handlers
 ┣ 📜 requirements.txt    # Frozen Python Dependencies
 ┗ 📜 .env                # Secret Environment Variables (Excluded from Git)
```

<br>

## ☁️ Deployment Ready

This application is structurally prepared for immediate production deployment across major cloud-hosting environments like **Render, Heroku, or PythonAnywhere**.

**WSGI Application Server Run Command:**
```bash
gunicorn app:app
```
*(Ensure `gunicorn` is properly referenced and environmental variables are securely populated into your provider's dashboard settings.)*

<br>

## 🤝 Let's Connect

This project was built to solve real-world problems with completely transparent, optimized, and impactful code. I am always open to exploring new engineering opportunities or exciting technical collaborations.

- **GitHub:** [@shah-bakhsh](https://github.com/shah-bakhsh)
- **LinkedIn:** [Shah Bakhsh](https://www.linkedin.com/in/shah-bakhsh/)
- **Email:** [shahbakhshtech@gmail.com](mailto:shahbakhshtech@gmail.com)

If you found the codebase insightful or if it has helped you, I would deeply appreciate it if you could **⭐️ Star** the repository! It keeps me motivated.

<div align="center">
  <br>
  <i>Designed with passion. Engineered for maximum impact.</i>
</div>
