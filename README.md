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