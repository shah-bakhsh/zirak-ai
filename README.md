<div align="center">

# Zirak AI

**The Next Generation of Intelligent Assistants**

[![Render Deployment](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://zirak-ai.onrender.com)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-backend-black?style=for-the-badge)](https://flask.palletsprojects.com/)
[![LLaMA-3](https://img.shields.io/badge/Model-meta%20llama%203-blueviolet?style=for-the-badge)](https://ai.meta.com/llama/)

<br>

<h3>🔴 <a href="https://zirak-ai.onrender.com"><b>CLICK HERE TO TRY THE LIVE APP</b></a> 🔴</h3>

*A high-performance, modular AI suite engineered from scratch. Featuring Real-Time Streaming, Custom Numpy-backed Document RAG, and an intuitive Dark Mode UI.*

---

</div>

<br>

## 🖥️ First Impression: Live UI

We heavily prioritize a premium user experience. Click the image below to jump straight to the live web application!

<div align="center">
  <a href="https://zirak-ai.onrender.com">
    <img src="./static/assets/ui-preview.png" alt="Zirak AI User Interface" width="100%" style="border-radius: 10px; max-width: 900px; box-shadow: 0px 8px 24px rgba(0,0,0,0.6);">
  </a>
</div>

<br>

## ⚡ Engineering Philosophy

Unlike many AI wrappers that rely on heavy, black-box frameworks (like LangChain), **Zirak AI is crafted independently**.

- **Zero-Bloat Architecture:** Custom-built TF-IDF Vector Search engine utilizing raw `numpy`.
- **Maximum Performance:** Lightning-fast token execution with optimized API streaming.
- **Secure By Design:** Session-based authentication handling and isolated conversation states.

This repository demonstrates rigorous full-stack software engineering, focusing on transparency, speed, and fundamental Machine Learning concepts.

<br>

## 🔥 Core Features

<table>
  <tr>
    <td width="50%">
      <h3>🚀 Real-Time Streaming</h3>
      <p>Fluid, token-by-token instant responses powered by OpenRouter API and Server-Sent Events (SSE). Experience AI generation at human typing speeds.</p>
    </td>
    <td width="50%">
      <h3>📚 Private Document RAG</h3>
      <p>Securely upload PDFs. Zirak intelligently parses, chunks, and vectorizes your data internally, enabling semantic search and precise document analysis.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>🎭 Dynamic Personas</h3>
      <p>Instantly switch between a core Chat Assistant, an automated <b>Goal Planner</b>, an expert <b>Career Coach</b>, or a specialized <b>Document Analyst</b>.</p>
    </td>
    <td width="50%">
      <h3>🔐 Secure Local DB</h3>
      <p>Powered by SQLite with SHA-256 password hashing. Every user gets an isolated, persistent chat history and secure login session.</p>
    </td>
  </tr>
</table>

<br>

## 🛠️ Technology Stack

<div align="center">
  
| Architectural Layer | Technologies Used | Micro-Service Purpose |
| :--- | :--- | :--- |
| **Backend API Server** | `Python`, `Flask`, `Werkzeug` | REST Routing, Server Session Logic |
| **Vector Engine (RAG)** | `Numpy`, `PyPDF2`, `Pickle` | Custom Math-based Cosine Similarity Search |
| **Large Language Model** | `OpenRouter API`, `LLaMA-3 (8B)` | Core AI Processing & Reasoning Engine |
| **Database Architecture** | `SQLite3` | Persistent authentication and chat states |
| **Frontend Platform** | `Vanilla JS`, `HTML5`, `CSS3` | Asynchronous SSE Fetching, DOM Manipulation |

</div>

<br>

## 🚀 Quick Start (Run Locally)

Ready to test the source code on your own machine? It takes less than 2 minutes.

<details>
<summary><b>🔥 Click here to expand the installation steps!</b></summary>
<br>

**1. Clone the repository:**
```bash
git clone https://github.com/shah-bakhsh/zirak-ai.git
cd zirak-ai
```

**2. Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Set up Environment Variables:**
Create a `.env` file in the root folder:
```env
OPENROUTER_API_KEY=sk-or-v1-your-api-key-here
SECRET_KEY=super-secret-production-key-2024
```

**5. Launch the Server:**
```bash
python app.py
```
*Visit `http://localhost:5000` in your browser!*
</details>

<br>

## ☁️ Cloud Deployment

Zirak AI is actively hosted on Render. To deploy your own instance to Render, Heroku, or AWS:

1. Connect your repository to your cloud provider.
2. Add your `.env` variables in the provider's secret manager.
3. Configure the **WSGI Server Start Command**:
```bash
gunicorn app:app
```

<br>

## 🤝 Connect With The Developer

Built with passion for clean code and innovative AI solutions. If you appreciate independent, high-performance architecture, let's connect!

- **GitHub:** [@shah-bakhsh](https://github.com/shah-bakhsh)
- **LinkedIn:** [Shah Bakhsh](https://www.linkedin.com/in/shah-bakhsh/)
- **Email:** [shahbakhshtech@gmail.com](mailto:shahbakhshtech@gmail.com)

<div align="center">
  <br>
  <i>If you found this project helpful or inspiring, please consider dropping a ⭐️ to show your support!</i>
</div>
