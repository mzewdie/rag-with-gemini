# Project Summary – Building a RAG System with Gemini from Scratch

## Project Goal

The goal of this project was not simply to build a Retrieval-Augmented Generation (RAG) application, but to understand every component involved in a modern RAG architecture by implementing it ourselves instead of relying on frameworks such as LangChain.

The philosophy throughout the project has been:

> **Understand first, automate later.**

After understanding every component, the next phase of the project will be to rebuild the same architecture using LangChain and compare both approaches.

---

# Overall Architecture

The application consists of two independent pipelines.

## 1. Indexing Pipeline

```
PDF
 │
 ▼
PDFLoader
 │
 ▼
Chunker
 │
 ▼
EmbeddingService
 │
 ▼
VectorStore (ChromaDB)
```

Purpose:

Convert documents into embeddings and store them in the vector database.

---

## 2. Retrieval Pipeline

```
User Question
      │
      ▼
EmbeddingService
      │
      ▼
Retriever
      │
      ▼
VectorStore
      │
      ▼
Relevant Chunks
      │
      ▼
RAGService
      │
      ▼
GeminiClient
      │
      ▼
Gemini Response
```

Purpose:

Retrieve semantically similar document chunks and provide them as context to Gemini.

---

# Components Implemented

## GeminiClient

Responsibilities:

* Communicates with the Gemini API.
* Uses `generate_content()`.
* Returns `response.text`.
* Uses an instance method (`self`) rather than a static function.

Lessons learned:

* Importance of the `self` parameter.
* Importance of returning values.
* Difference between `response` and `response.text`.

---

## EmbeddingService

Responsibilities:

* Generates embeddings using Gemini's embedding model.
* Uses `gemini-embedding-001`.

Important findings:

* Every embedding contains **3072 floating-point numbers**.
* The same text always produces the same embedding.
* Similar texts produce nearby vectors in semantic space.

Examples used:

"The cat is sleeping on the sofa."

"A kitten is taking a nap on the couch."

We learned that semantic similarity is encoded in the vector representation.

---

## VectorStore

Technology:

ChromaDB

Responsibilities:

* Store embeddings.
* Store original chunks.
* Store metadata.

Stored metadata currently includes:

* page number
* source document

Implemented methods:

* add()
* search()

Lessons learned:

* ChromaDB stores both vectors and original text.
* Querying returns similar chunks together with metadata and similarity scores.

---

## Retriever

Responsibilities:

* Convert the user's question into an embedding.
* Search ChromaDB.
* Return relevant chunks.

Design decision:

Retriever should not communicate with Gemini.

Its only responsibility is retrieval.

---

## RAGService

Responsibilities:

* Receive the user question.
* Call Retriever.
* Build the prompt.
* Call GeminiClient.
* Return Gemini's answer.

Design decision:

Prompt construction belongs inside RAGService.

Retriever should not know how Gemini expects its prompts.

---

# PDF Processing

Implemented:

PDFLoader

Uses:

pypdf

Design:

```
PDFLoader
    ↓
list[PDFPage]
```

Implemented dataclass:

```
PDFPage
    page_number
    text
```

Design decisions:

* Extract text page by page.
* Preserve page numbers.
* Keep PDF loading independent of chunking.

Lessons learned:

PDF extraction is imperfect.

Problems observed:

* page numbers become text
* headers
* footers
* tables lose their structure
* images are ignored
* scanned PDFs require OCR

---

# Chunking

Implemented:

Chunk dataclass

```
Chunk
    text
    page_number
    chunk_number
```

Implemented:

Character-based chunking.

Algorithm:

For every page

Split text into fixed-size character chunks.

Lessons learned:

Advantages:

* Simple.
* Easy to understand.
* Preserves page metadata.

Disadvantages:

* Words may be split.
* Sentences may be split.
* Context may be lost.

Future improvements discussed:

* Word-aware chunking.
* Overlapping chunks.
* Sentence-aware chunking.
* Semantic chunking.

---

# Testing

Implemented integration tests.

Tests verify:

* Embedding generation.
* Storage in ChromaDB.
* Retrieval using identical text.
* Retrieval using semantically similar text.

Example:

Stored:

"The cat is sleeping on the sofa."

Queried:

"Where is the kitten sleeping?"

Retrieval succeeded.

This demonstrated semantic search.

---

# Software Engineering Lessons

Throughout the project we emphasized clean architecture.

Important principles:

## Single Responsibility Principle

Every class has one responsibility.

Examples:

GeminiClient

↓

Talks only to Gemini.

EmbeddingService

↓

Creates embeddings only.

Retriever

↓

Retrieves documents only.

VectorStore

↓

Stores and searches vectors only.

---

## Separation of Concerns

Avoid combining responsibilities.

Examples discussed:

PDFLoader should not perform chunking.

EmbeddingService should not store vectors.

Retriever should not build prompts.

RAGService coordinates components rather than implementing their logic.

---

# Python Lessons

Topics covered:

* dataclasses
* enumerate()
* pathlib.Path
* package imports
* `__init__.py`
* project structure
* unittest
* return values
* instance methods
* the `self` parameter

Several debugging sessions included:

* forgetting `return`
* forgetting `self`
* incorrect slicing during chunking
* import path issues
* Gemini SDK autocompletion
* Pylance configuration

---

# Important AI Concepts Learned

* What is RAG?
* What are embeddings?
* Why embeddings are deterministic.
* Why vectors represent semantic meaning.
* Why similar texts are located close together.
* Difference between embeddings and text generation.
* Difference between keyword search and semantic search.
* Why chunk quality strongly influences retrieval quality.

---

# Discussion About Libraries

We intentionally avoided LangChain.

Reason:

We wanted to understand every component first.

Now we understand:

* PDFLoader
* Chunker
* EmbeddingService
* VectorStore
* Retriever
* Prompt Builder
* RAGService

Therefore LangChain will no longer appear as "magic."

Instead we will recognize each abstraction immediately.

---

# Next Phase

The next phase of the project will rebuild the same RAG application using LangChain.

Objectives:

* Replace our custom PDFLoader with LangChain document loaders.
* Replace our Chunker with RecursiveCharacterTextSplitter.
* Replace our VectorStore wrapper with LangChain integrations.
* Use LangChain retrievers.
* Compare our implementation with the framework.

The goal is not merely to use LangChain, but to understand what problems it solves, which abstractions it provides, and where a custom implementation is still preferable.

---

# Final Reflection

The most valuable aspect of this project has been the emphasis on software engineering rather than simply obtaining a working RAG application.

Instead of treating frameworks as black boxes, every architectural decision was discussed, implemented, tested, and reviewed.

As a result, the next phase—using LangChain—will be an exercise in recognizing familiar concepts behind a higher-level API rather than learning an entirely new system.
