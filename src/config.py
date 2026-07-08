from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

GEMINI_MODEL=os.getenv("GEMINI_MODEL")
if not GEMINI_MODEL:
    raise ValueError("GEMINI_MODEL not found")

EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL")
if not EMBEDDING_MODEL:
    raise ValueError("EMBEDDING_MODEL not found")