from src.embedding_service import EmbeddingService
from src.vector_store import VectorStore
from src.retriever import Retriever
from src.rag_service import RAGService
from src.gemini_client import GeminiClient
from src.pdf_loader import PDFLoader
from src.pdf_loader import PDFPage
from src.chunker import Chunker


def show_message(message):
    print(message)
    
""" question="Tell me about Python"

embedding_service=EmbeddingService()
vector_store = VectorStore()
retriever= Retriever(embedding_service,vector_store)
show_message(f"Retriving from the database ...")
chunk=retriever.retrieve(question)
show_message(f"chunk retrieved as {chunk}")
gemini_client=GeminiClient()
show_message("Calling GeminiClient ...")
rag_service=RAGService(embedding_service,gemini_client)
answer = rag_service.ask(chunk)
show_message(f"Answer from Gemini is: {answer}") """

pdf_loader=PDFLoader("./data")
pdf_pages=pdf_loader.load("PythonProgramming.pdf")
#print(pdf_pages)

chunker=Chunker()
chunk_list = chunker.chunk(pdf_pages=pdf_pages)
#print(f"chunked list is: {chunk_list}")
