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

Hint for import problems:
Once a team chooses a project structure, you rarely think about it again.

For example, if we decide that in our project:

modules inside src use relative imports,
tests use from src...,
everything is run with python -m ...,

then you can mostly forget about the import machinery and focus on writing your application.