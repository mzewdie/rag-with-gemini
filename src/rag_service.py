from .retriever import Retriever
from .gemini_client import GeminiClient
from .embedding_service import EmbeddingService
from .vector_store import VectorStore



class RAGService:

    def __init__(
        self,
        retriever: Retriever,
        gemini_client: GeminiClient
    ):
        self.retriever = retriever
        self.gemini_client = gemini_client
    
        
    def ask(self, chunks: list[str]):
        build_prompt = "\n\n".join(chunks)
        #print(f"Type of BuildPrompt: {type(build_prompt)}")
        #print(f"Buildprompt als string is: {str(build_prompt)}")
        
        response=self.gemini_client.ask(question=str(build_prompt))
        return response
      
        
          