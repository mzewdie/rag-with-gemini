import unittest
from src.embedding_service import EmbeddingService
from src.vector_store import VectorStore
from src.retriever import Retriever

class TestEmbeddingIntegration(unittest.TestCase):
    
    def test_embeeding(self):
        text="The cat is sleeping on the sofa."
        embService=EmbeddingService()
        embedding=embService.embed_document(text)
        meta_datas = {"page":17}
        vector_store=VectorStore()
        vector_store.add(text,embedding=embedding, metadata=meta_datas)
        
        #search
        search_results=vector_store.search(embeddings=embedding)
        self.assertTrue(text in search_results)
        
    def test_embeeding_semantic_retrieval(self):
        text="The cat is sleeping on the sofa."
        embService=EmbeddingService()
        embedding=embService.embed_document(text)
        meta_datas = {"page":17}
        vector_store=VectorStore()
        vector_store.add(text,embedding=embedding, metadata=meta_datas)
        
        #search with a similar sentence
        question = "Where is the kitten sleeping?"
        embedding=embService.embed_document(question)
        search_results=vector_store.search(embeddings=embedding)
        self.assertTrue(text in search_results)   
        
    def test_retriever(self):
        text="Python is an interpreted programming language."
        embed_service=EmbeddingService()
        embedding=embed_service.embed_document(text)
        meta_datas = {"page":17}
        vector_store=VectorStore()
        vector_store.add(text,embedding=embedding, metadata=meta_datas)
        
        #test retriver
        question = "Tell me about Python.?"
        retriever = Retriever(embedding_service=embed_service,vector_store=vector_store)
        
        search_results=retriever.retrieve(question=question)
        expected_chunks=[text]
        print(f"Search results test retriever: {search_results}")
        print(f"Expected Chuncs: {expected_chunks}")
        self.assertTrue(text in search_results)      
        
        
if __name__ == "__main__":
    unittest.main()        