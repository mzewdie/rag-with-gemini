import gemini_client as gc
from embedding_service import EmbeddingService



#question="Explain Retrieval-Augmented Generation in one sentence."

while True:
    question=input("Your Question for Gemini (Press quit to exit): ")
    if(question.lower()=="quit"):
        break
    response=gc.ask_gemini(question)
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
    