# 📄 Simple RAG Search Application

## 📌 Overview

This project is a simple Retrieval-Augmented Generation (RAG) application developed using Python, Streamlit, LangChain, Sentence Transformers, and Cohere.

The application allows users to upload a PDF or TXT document, ask questions about the document, retrieve the most relevant chunks using semantic search, and generate answers using Cohere's Large Language Model.

---

## 🚀 Features

- Upload PDF or TXT files
- Automatic document chunking
- Generate semantic embeddings
- Retrieve top matching document chunks
- Generate contextual answers using Cohere AI
- Interactive Streamlit interface

---

## 🛠 Technologies Used

- Python
- Streamlit
- LangChain
- Sentence Transformers
- Scikit-Learn
- NumPy
- PyPDF
- Cohere API

---

## 📂 Project Structure

```
rag_assignment/
│── app.py
│── functions.py
│── notebook.ipynb
│── requirements.txt
│── README.md
│── sample.txt
│── screenshots/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone <repository-url>
cd rag_assignment
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

The application will open automatically in your browser at

```
http://localhost:8501
```

---

## 🔑 Cohere API Key

This application requires a Cohere API Key.

Get your free API key from:

https://dashboard.cohere.com/api-keys

Paste the API key into the application before asking questions.

---

## 📖 How to Use

1. Launch the Streamlit application.
2. Enter your Cohere API Key.
3. Upload a PDF or TXT document.
4. Enter your question.
5. Click **Search**.
6. View:
   - Top Matching Chunks
   - AI Generated Answer

---

## 📋 Assignment Tasks Covered

### Task 1
- Load PDF/TXT documents
- Split documents into text chunks

### Task 2
- Generate embeddings using Sentence Transformers

### Task 3
- Perform semantic search using cosine similarity

### Task 4
- Build an interactive Streamlit interface

### Task 5
- Generate answers using Cohere Chat API

---

## 📷 Output

The application displays:

- Uploaded document
- Retrieved relevant chunks
- AI-generated answer

---

## 👨‍💻 Author

Siddharth Yadav

B.Tech CSE (Data Science)

JSS University, Noida

---

## 📄 License

This project is developed for educational and internship assignment purposes.