from .retrieve import Retriever
from .gemini_client import GeminiClient



class RAGService:

    def __init__(
        self,
        retriever: Retriever,
        gemini_client: GeminiClient
    ):
        self.retriever = retriever
        self.gemini_client = gemini_client