from google import genai
from src import config




class EmbeddingService:
    """creates embeddings using the Gemini Embedding API."""
    
    def __init__(self):
        #create the client once in the constructor
        self.client = genai.Client(api_key=config.GEMINI_API_KEY)
        
    def embed_document(self, text: str) -> list[float]:
        embedContentResponse=self.client.models.embed_content(
            model=config.EMBEDDING_MODEL,
            contents=text)
        return embedContentResponse.embeddings[0].values

            
   
        
       
        
    
    def embed_query(self, question: str) -> list[float]:
        pass     