# 📄 Local PDF RAG Chatbot (Offline)

A **100% offline PDF chatbot** built using **Streamlit, LangChain, FAISS, HuggingFace embeddings**, and a **local LLM (LLaMA/Mistral via llama.cpp)**.  
Ask questions from a PDF without any paid APIs.

---

## 🚀 Features

- 📚 Question answering from PDFs
- 🔒 Fully offline (no API keys)
- 🧠 Semantic search using FAISS
- 🦙 Local LLM with llama.cpp
- 🖥️ Simple Streamlit UI

---

## 🏗️ Architecture

User
│
▼
Streamlit UI
│
▼
LangChain RetrievalQA
│
├── FAISS Vector DB
│ └── HuggingFace Embeddings
│
└── Local LLM (LLaMA / Mistral)
via llama.cpp


---

## 🗂️ Project Structure

project/
│── chatbot.py
│── book.pdf
│── README.md
│── models/
│ └── ggml-model-q4_0.bin


> ⚠️ Model files are not committed to GitHub.

---

## 🛠️ Requirements

- Python 3.9 – 3.11
- Minimum 8 GB RAM
- CPU only (no GPU required)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python -m venv venv
venv\Scripts\activate   # Windows
pip install langchain==0.2.14 langchain-core==0.2.38 langchain-community==0.2.12
pip install langchain-text-splitters faiss-cpu llama-cpp-python streamlit
pip install sentence-transformers pypdf

🧠 Download Model

Download a GGML/GGUF model (example):

mistral-7b-instruct-v0.1.Q4_0.bin

Place it here:

models/ggml-model-q4_0.bin

▶️ Run App
streamlit run chatbot.py


Open: http://localhost:8501

📸 Screenshots

Add screenshots here after running the app:

screenshots/
│── home.png
│── answer.png

![Home](screenshots/home.png)
![Answer](screenshots/answer.png)

🧪 Troubleshooting
❌ ModuleNotFoundError

✔️ Ensure correct LangChain versions are installed
✔️ Activate virtual environment

❌ Model not loading / app crashes

✔️ Use Q4 model for low RAM
✔️ Check correct MODEL_PATH

❌ Slow responses

✔️ Reduce chunk_size
✔️ Use smaller model (TinyLLaMA / Phi-2)

❌ GitHub push fails (large file)

✔️ Add to .gitignore:

models/
*.bin
venv/

📌 Notes

Works fully offline after setup

CPU inference is slower than cloud APIs

Ideal for learning RAG fundamentals

📜 License

For educational use.
Follow the license of the downloaded LLM model.


---
