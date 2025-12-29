import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA

# -----------------------------
# CONFIG
# -----------------------------
PDF_PATH = "book.pdf"
MODEL_PATH = "models/ggml-model-q4_0.bin"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

st.set_page_config(page_title="Local RAG Chatbot", layout="centered")

# -----------------------------
# VECTOR DB CREATION
# -----------------------------
@st.cache_resource(show_spinner=True)
def create_vector_db(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL
    )

    db = FAISS.from_documents(chunks, embeddings)
    return db

# -----------------------------
# LOAD LOCAL LLM
# -----------------------------
@st.cache_resource(show_spinner=True)
def load_llm(model_path):
    return LlamaCpp(
        model_path=model_path,
        n_ctx=2048,
        temperature=0,
        verbose=False
    )

# -----------------------------
# APP START
# -----------------------------
st.title("📄 Local PDF Chatbot (100% Free & Offline)")
st.caption("HuggingFace Embeddings + FAISS + Local LLaMA")

if "initialized" not in st.session_state:
    with st.spinner("Loading vector database..."):
        st.session_state.vector_db = create_vector_db(PDF_PATH)

    with st.spinner("Loading local LLaMA model..."):
        st.session_state.llm = load_llm(MODEL_PATH)

    st.session_state.initialized = True

# -----------------------------
# RAG Chain
# -----------------------------
qa_chain = RetrievalQA.from_chain_type(
    llm=st.session_state.llm,
    retriever=st.session_state.vector_db.as_retriever(search_kwargs={"k": 3}),
    chain_type="stuff",
    return_source_documents=False
)

# -----------------------------
# UI
# -----------------------------
query = st.text_input("Ask a question from your PDF:")

if query:
    with st.spinner("Thinking..."):
        answer = qa_chain.run(query)

    st.markdown("### ✅ Answer")
    st.write(answer)
