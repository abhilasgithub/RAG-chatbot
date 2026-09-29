# AI-Powered RAG Chatbot

An AI-powered **RAG (Retrieval-Augmented Generation)** chatbot built with **Python and FastAPI** that allows users to upload medical PDF documents and ask questions based on their content.

The application extracts text from PDFs, splits the text into smaller chunks, converts the chunks into vector embeddings, stores them in ChromaDB, retrieves the most relevant chunks for a user question, and uses a Google AI Studio LLM to generate a context-grounded response.

---

## 🚀 Features

* Upload PDF documents through a FastAPI API
* Extract text from PDF documents
* Split documents into smaller text chunks
* Generate vector embeddings using Hugging Face
* Store embeddings in ChromaDB
* Perform semantic similarity search
* Retrieve the top 3 relevant document chunks
* Generate answers using Google AI Studio LLM
* Store application data using PostgreSQL
* REST API implementation using FastAPI
* Logging and exception handling
* Docker support for containerization
* Ready for cloud deployment

---

## 🏗️ Architecture

```text
                    PDF Upload
                        │
                        ▼
                FastAPI Application
                        │
                        ▼
                  PDF Extraction
                        │
                        ▼
                     Chunking
                        │
                        ▼
              Hugging Face Embeddings
                        │
                        ▼
                    ChromaDB
                 Vector Storage
                        │
                        │
        ┌───────────────┘
        │
        ▼
    User Question
        │
        ▼
   Query Embedding
        │
        ▼
  ChromaDB Similarity Search
        │
        ▼
   Top 3 Relevant Chunks
        │
        ▼
 Google AI Studio LLM
        │
        ▼
   Context-Grounded Answer
        │
        ▼
      User
```

---

## 🛠️ Technologies Used

| Technology       | Purpose                                      |
| ---------------- | -------------------------------------------- |
| Python           | Application development                      |
| FastAPI          | REST API and application backend             |
| Hugging Face     | Text embedding generation                    |
| ChromaDB         | Vector database and similarity search        |
| Google AI Studio | Large Language Model for response generation |
| PostgreSQL       | Persistent application data                  |
| PyPDF            | PDF text extraction                          |
| Docker           | Application containerization                 |
| Git/GitHub       | Version control                              |

---

## 📂 Project Structure

```text
RAG-application/
│
├── upload.py
├── requirements.txt
├── Dockerfile
├── .env
│
├── data/
│
├── chroma_db/
│
└── README.md
```

> The exact structure may vary depending on your implementation.

---

## ⚙️ How the RAG Pipeline Works

### 1. Document Upload

The user uploads a PDF document through the FastAPI application.

```text
PDF
 ↓
FastAPI Upload Endpoint
```

### 2. Text Extraction

Text is extracted from the uploaded PDF using a PDF processing library.

```text
PDF
 ↓
Extracted Text
```

### 3. Text Chunking

The extracted text is divided into smaller chunks so that relevant sections can be retrieved efficiently.

```text
Document
 ↓
Text Chunks
```

### 4. Embedding Generation

Each chunk is converted into a numerical vector using a Hugging Face embedding model.

```text
Text Chunk
 ↓
Embedding Model
 ↓
Vector Embedding
```

### 5. Vector Storage

The generated embeddings and their corresponding text chunks are stored in ChromaDB.

```text
Text + Embedding
       ↓
    ChromaDB
```

### 6. User Question

When the user asks a question, the question is also converted into an embedding.

```text
User Question
      ↓
Embedding Model
      ↓
Query Vector
```

### 7. Semantic Search

The query vector is compared with the stored document vectors.

ChromaDB retrieves the **top 3 most relevant chunks**.

```text
Query Vector
     ↓
ChromaDB
     ↓
Top 3 Relevant Chunks
```

### 8. Response Generation

The retrieved chunks and the user's question are provided to the Google AI Studio LLM.

```text
User Question
      +
Retrieved Context
      ↓
Google AI Studio LLM
      ↓
Generated Answer
```

This allows the chatbot to generate responses based on the uploaded documents.

---

## 🔑 Environment Variables

Create a `.env` file and configure the required environment variables.

```env
GOOGLE_API_KEY=your_google_ai_studio_api_key

POSTGRES_HOST=your_database_host
POSTGRES_PORT=5432
POSTGRES_DB=your_database
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
```

**Do not commit your `.env` file or API keys to GitHub.**

Add it to `.gitignore`:

```text
.env
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

```bash
cd RAG-application
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
python -m uvicorn upload:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

Open the FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger UI to test the API endpoints.

---

## 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t rag-app .
```

Run the container:

```bash
docker run -p 8000:8000 rag-app
```

The API can then be accessed at:

```text
http://localhost:8000/docs
```

---

## 🔄 Docker Deployment Flow

The application can be deployed using Docker and AWS.

```text
RAG Application
      ↓
Dockerfile
      ↓
Docker Image
      ↓
Amazon ECR
      ↓
Amazon EC2
      ↓
Docker Container
      ↓
FastAPI
      ↓
RAG Chatbot
```

Where:

* **ECR (Elastic Container Registry)** stores the Docker image.
* **EC2 (Elastic Compute Cloud)** provides the server where the container runs.

---

## 🧪 Example RAG Flow

Example question:

```text
What are common symptoms of asthma?
```

The application:

```text
Question
   ↓
Create Query Embedding
   ↓
Search ChromaDB
   ↓
Retrieve Top 3 Relevant Chunks
   ↓
Send Question + Context to LLM
   ↓
Generate Answer
```

The chatbot therefore uses the retrieved document content as context when generating its response.

---

## 🔮 Future Improvements

* Add authentication and authorization
* Add automated unit and API testing
* Add CI/CD using GitHub Actions
* Add production monitoring and logging
* Use persistent cloud storage for vector data
* Add a production-grade vector database
* Deploy behind HTTPS
* Add a frontend chatbot interface
* Add conversation history and session management
* Improve RAG evaluation and retrieval quality

---

## 📌 Learning Outcomes

Through this project, I gained hands-on experience with:

* RAG application development
* Document processing
* Text chunking
* Vector embeddings
* Semantic search
* Vector databases
* LLM integration
* FastAPI REST APIs
* PostgreSQL
* Docker containerization
* API testing
* Cloud deployment concepts
* Production-oriented AI application development

---

## 👨‍💻 Author

**Abhilash Akasam**

GitHub: `https://github.com/abhilasgithub`
