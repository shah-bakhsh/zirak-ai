from flask import Flask, render_template, request, jsonify, session, redirect, url_for, Response, stream_with_context
import os, json, requests, sqlite3, hashlib, pickle, numpy as np
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "zirak-ai-secret-2024")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
MODEL = "meta-llama/llama-3-8b-instruct"
DB_PATH = "data/users.db"
MEMORY_DB = "data/memory.db"
VECTOR_PATH = "data/vectors.pkl"
UPLOAD_FOLDER = "uploads/pdf_files"
ALLOWED_EXTENSIONS = {"pdf"}

os.makedirs("data", exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def init_db():
    with sqlite3.connect(DB_PATH) as c:
        c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
    with sqlite3.connect(MEMORY_DB) as c:
        c.execute("CREATE TABLE IF NOT EXISTS memory (user TEXT, role TEXT, content TEXT, ts DATETIME DEFAULT CURRENT_TIMESTAMP)")

init_db()

def hash_pw(p): return hashlib.sha256(p.encode()).hexdigest()

def get_user(u, p):
    with sqlite3.connect(DB_PATH) as c:
        row = c.execute("SELECT id FROM users WHERE username=? AND password=?", (u, hash_pw(p))).fetchone()
    return row

def create_user(u, p):
    try:
        with sqlite3.connect(DB_PATH) as c:
            c.execute("INSERT INTO users (username, password) VALUES (?,?)", (u, hash_pw(p)))
        return True
    except sqlite3.IntegrityError:
        return False

def save_message(user, role, content):
    with sqlite3.connect(MEMORY_DB) as c:
        c.execute("INSERT INTO memory (user, role, content) VALUES (?,?,?)", (user, role, content))

def get_history(user, limit=20):
    with sqlite3.connect(MEMORY_DB) as c:
        rows = c.execute("SELECT role, content FROM memory WHERE user=? ORDER BY ts DESC LIMIT ?", (user, limit)).fetchall()
    return [{"role": r, "content": c} for r, c in reversed(rows)]

def clear_history(user):
    with sqlite3.connect(MEMORY_DB) as c:
        c.execute("DELETE FROM memory WHERE user=?", (user,))


def load_vectors():
    if os.path.exists(VECTOR_PATH):
        with open(VECTOR_PATH, "rb") as f:
            return pickle.load(f)
    return {"texts": [], "embeddings": []}

def save_vectors(store):
    with open(VECTOR_PATH, "wb") as f:
        pickle.dump(store, f)

def simple_embed(text):
    words = text.lower().split()
    vec = np.zeros(512)
    for i, w in enumerate(words[:512]):
        vec[hash(w) % 512] += 1
    norm = np.linalg.norm(vec)
    return (vec / norm).tolist() if norm > 0 else vec.tolist()

def add_chunks(chunks):
    store = load_vectors()
    for chunk in chunks:
        store["texts"].append(chunk)
        store["embeddings"].append(simple_embed(chunk))
    save_vectors(store)

def search_chunks(query, top_k=5):
    store = load_vectors()
    if not store["texts"]: return []
    q_vec = np.array(simple_embed(query))
    scores = []
    for i, emb in enumerate(store["embeddings"]):
        e = np.array(emb)
        score = float(np.dot(q_vec, e) / (np.linalg.norm(q_vec) * np.linalg.norm(e) + 1e-9))
        scores.append((score, store["texts"][i]))
    scores.sort(reverse=True)
    return [t for _, t in scores[:top_k]]


def process_pdf_file(filepath):
    try:
        import PyPDF2
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                t = page.extract_text()
                if t: text += t + "\n"
        words = text.split()
        chunks = [" ".join(words[i:i+400]) for i in range(0, len(words), 400)]
        add_chunks([c for c in chunks if c.strip()])
        return len(chunks)
    except Exception as e:
        return 0


def stream_openrouter(messages):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": True,
        "max_tokens": 1024
    }
    try:
        with requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers, json=payload, stream=True, timeout=60
        ) as r:
            for line in r.iter_lines():
                if line:
                    line = line.decode("utf-8")
                    if line.startswith("data: "):
                        line = line[6:]
                    if line == "[DONE]": break
                    try:
                        token = json.loads(line)["choices"][0]["delta"].get("content", "")
                        if token: yield token
                    except: continue
    except Exception as e:
        yield f"Error: {e}"


@app.route("/")
def index():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", user=session["user"])

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        action = data.get("action")
        u = data.get("username", "").strip()
        p = data.get("password", "")
        if not u or not p:
            return jsonify({"ok": False, "error": "Fill in all fields."})
        if action == "login":
            if get_user(u, p):
                session["user"] = u
                return jsonify({"ok": True})
            return jsonify({"ok": False, "error": "Invalid username or password."})
        elif action == "register":
            if create_user(u, p):
                session["user"] = u
                return jsonify({"ok": True})
            return jsonify({"ok": False, "error": "Username already taken."})
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/api/chat", methods=["POST"])
def chat():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json()
    prompt = data.get("prompt", "").strip()
    mode = data.get("mode", "chat")
    if not prompt:
        return jsonify({"error": "Empty prompt"}), 400

    history = get_history(session["user"])

    system_map = {
        "chat": "You are Zirak AI, a sharp, precise, and intelligent assistant. Be direct and thorough.",
        "goal": "You are Zirak AI Goal Planner. Create detailed, actionable step-by-step plans with timelines and milestones.",
        "career": "You are Zirak AI Career Coach. Give sharp, specific, expert career advice with concrete next steps.",
        "pdf": "You are Zirak AI Document Analyst. Answer questions using only the provided document context."
    }
    system = system_map.get(mode, system_map["chat"])

    if mode == "pdf":
        context_chunks = search_chunks(prompt, top_k=5)
        if context_chunks:
            context = "\n\n".join(context_chunks)
            messages = [
                {"role": "system", "content": system},
                {"role": "user", "content": f"Document context:\n{context}\n\nQuestion: {prompt}"}
            ]
        else:
            messages = [
                {"role": "system", "content": system},
                {"role": "user", "content": f"No document uploaded yet. User asked: {prompt}. Politely ask them to upload a PDF first."}
            ]
    else:
        messages = [{"role": "system", "content": system}] + history[-10:] + [{"role": "user", "content": prompt}]

    save_message(session["user"], "user", prompt)

    def generate():
        full = ""
        for token in stream_openrouter(messages):
            full += token
            yield f"data: {json.dumps({'token': token})}\n\n"
        save_message(session["user"], "assistant", full)
        yield f"data: {json.dumps({'done': True})}\n\n"

    return Response(stream_with_context(generate()), mimetype="text/event-stream")

@app.route("/api/upload-pdf", methods=["POST"])
def upload_pdf():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    if "file" not in request.files:
        return jsonify({"ok": False, "error": "No file uploaded."})
    f = request.files["file"]
    if f.filename == "" or not f.filename.lower().endswith(".pdf"):
        return jsonify({"ok": False, "error": "Please upload a PDF file."})
    filename = secure_filename(f.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    f.save(path)
    count = process_pdf_file(path)
    return jsonify({"ok": True, "chunks": count, "filename": filename})

@app.route("/api/clear-chat", methods=["POST"])
def clear_chat():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    clear_history(session["user"])
    return jsonify({"ok": True})

@app.route("/api/history")
def history():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(get_history(session["user"], 50))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
