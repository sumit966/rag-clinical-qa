"""Streamlit UI for RAG Clinical QA."""

import streamlit as st
from src.generator import generate_answer

st.set_page_config(page_title="Clinical QA (RAG)", page_icon="brain", layout="wide")

st.title("RAG-Based Clinical Question Answering")
st.caption("Hybrid search (BM25 + Dense) with RRF fusion - Powered by OpenAI")

question = st.text_input("Ask a clinical question:", placeholder="What are the symptoms of diabetes?")

if st.button("Get Answer") and question:
    with st.spinner("Retrieving and generating..."):
        result = generate_answer(question)

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Sources")
    for s in result["sources"]:
        st.markdown(f"- **{s['doc']}** (page {s['page']}) - score `{s['score']:.4f}`")
