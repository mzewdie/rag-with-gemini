from google import genai
import config
#from config import GEMINI_API_KEY
#from config import GEMINI_MODEL


client=genai.Client(api_key=config.GEMINI_API_KEY)


def ask_gemini(question: str)->str:
    try:
        response=client.models.generate_content(model=config.GEMINI_MODEL,
                                            contents=question)
        return response.text
    except Exception as e:
        return f"Gemini Api Error: {e}"