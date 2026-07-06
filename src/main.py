from google import genai
from config import GEMINI_API_KEY
from gemini_client import ask_gemini

import gemini_client as gc



#question="Explain Retrieval-Augmented Generation in one sentence."

while True:
    question=input("Your Question for Gemini (Press quit to exitThen we mus): ")
    if(question.lower()=="quit"):
        break
    response=gc.ask_gemini(question)
    print(response)

