#import gemini_client as gc
from .gemini_client import ask_gemini
from .embedding_service import EmbeddingService
from .vector_store import VectorStore
from .retriever import Retriever



#question="Explain Retrieval-Augmented Generation in one sentence."

while True:
    question=input("Your Question for Gemini (Press quit to exit): ")
    if(question.lower()=="quit"):
        break
    response=ask_gemini(question)
    print(response)
    
    embService=EmbeddingService()
    text="The saved paragraph is"
    response=embService.embed_document(text)
    #print(f"The embed vector for the text {text} is {response} and length of the response is {len(response)}")

    text1="The cat is sleeping on the sofa."
    text2="A kitten is taking a nap on the couch."
    text3="The Eiffel Tower is in Paris."
    response1=embService.embed_document(text1)
    response2=embService.embed_document(text2)
    response3=embService.embed_document(text3)
    print(f"The length of the response for the text {text1} is  {len(response1)}")
    print(f"The length of the response for the text {text2} is  {len(response2)}")
    print(f"The length of the response for the text {text3} is  {len(response3)}")
    
    #compare 
    response1=embService.embed_document(text)
    response2=embService.embed_document(text)
    print(response1==response2)
    
    embedding=[0.1] * 3072
    metadata={"page":36, "source": "test.pdf"}
    chunk = "Python is an interpreted language."
    vector_store=VectorStore()
    vector_store.add(chunk,embedding=embedding,metadata=metadata)
    print("Document chunk added successfully!")
    
    results=vector_store.search(embeddings=embedding)
    print(results)
    print(2*"\n")
    
    #Testing the Retriever
    textRetr="Python is an interpreted programming language."
    embed_service=EmbeddingService()
    vector_store=VectorStore()
    embedding=embed_service.embed_document(textRetr)
    meta_data = {"page":23}
    vector_store.add(chunk=textRetr,embedding=embedding,metadata=meta_data)
    
    retriever=Retriever(embedding_service=embed_service,vector_store=vector_store)
    print(f"Retriver returns: {retriever.retrieve(textRetr)}")
    
    
    