from google import genai
#import config
from .config import GEMINI_API_KEY
from .config import GEMINI_MODEL


client=genai.Client(api_key=GEMINI_API_KEY)

class GeminiClient:
    def __init__(self):
        self.client=client

    def ask(self,question: str)->str:
        try:
            response=self.client.models.generate_content(model=GEMINI_MODEL,
                                            contents=question)
             #print(f"Client Type: {type(client)}")
             #print(f"Dir client: {dir(client)}")
            return response.text
        except Exception as e:
            return f"Gemini Api Error: {e}"