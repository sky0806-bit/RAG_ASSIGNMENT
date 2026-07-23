import streamlit as st
import tempfile

from functions import (
    load_and_chunk_document,
    create_embeddings,
    search_chunks,
    generate_answer
)

st.set_page_config(
    page_title="Simple RAG Search",
    page_icon="📄"
)

st.title("📄 Simple RAG Search")

# Cohere API Key
api_key = st.text_input(
    "Enter Cohere API Key",
    type="password"
)

# Upload File
uploaded_file = st.file_uploader(
    "Upload a PDF or TXT file",
    type=["pdf", "txt"]
)

# Question
query = st.text_input("Ask a question")

# Search Button
if st.button("Search"):

    if uploaded_file is None:
        st.warning("Please upload a file.")
        st.stop()

    if query.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    if api_key.strip() == "":
        st.warning("Please enter your Cohere API Key.")
        st.stop()

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix="." + uploaded_file.name.split(".")[-1]
    ) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    try:

        with st.spinner("Processing document..."):

            # Load document
            chunks = load_and_chunk_document(file_path)

            # Create embeddings
            embeddings = create_embeddings(chunks)

            # Retrieve relevant chunks
            results = search_chunks(
                query,
                chunks,
                embeddings,
                k=3
            )

            # Display retrieved chunks
            st.subheader("Top Matching Chunks")

            for i, chunk in enumerate(results, start=1):
                st.markdown(f"### Chunk {i}")
                st.write(chunk)

            # Generate answer using Cohere
            context = "\n\n".join(results)

            answer = generate_answer(
                query=query,
                context=context,
                api_key=api_key
            )

        st.success("Answer Generated Successfully!")

        st.subheader("Generated Answer")

        st.write(answer)

    except Exception as e:
        st.error(f"Error: {e}")