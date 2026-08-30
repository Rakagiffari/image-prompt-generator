import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "AI Image Prompt Generator"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
