                     User
                       │
                       ▼
                  Retriever
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
 EmbeddingService              VectorStore
         │                           ▲
         ▼                           │
  Gemini Embedding Model        ChromaDB
                       │
                       ▼
                 Relevant Chunks
                       │
                       ▼
                 GeminiClient
                       │
                       ▼
                  Final Answer

###########################################
Hint for import problems:
Once a team chooses a project structure, you rarely think about it again.

For example, if we decide that in our project:

modules inside src use relative imports,
tests use from src...,
everything is run with python -m ...,

then you can mostly forget about the import machinery and focus on writing your application.
############################################

#End Summary:

# RAG with Gemini

A Retrieval-Augmented Generation (RAG) application implemented from scratch in Python.

## Goals

- Understand every RAG component
- Implement the architecture without frameworks
- Compare the implementation with LangChain
- Learn software architecture and clean design principles

## Current Components

- PDFLoader
- Chunker
- EmbeddingService
- VectorStore (ChromaDB)
- Retriever
- RAGService
- GeminiClient

## Next Steps

- Improve chunking
- Build Indexer
- Compare with LangChain
- Build a web interface

## Organisation:
RAG-With-Gemini/
│
├── README.md
├── ProjectSummary.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── gemini_client.py
│   ├── embedding_service.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── rag_service.py
│   ├── pdf_loader.py
│   ├── chunker.py
│   └── ...
│
├── tests/
│
├── data/
│
├── chroma_db/
│
└── docs/

##Then, as we continue, you can add:
docs/
│
├── architecture.md
├── lessons_learned.md
├── rag-book/
│     ├── chapter01.md
│     ├── chapter02.md
│     ├── ...
