import os
from dotenv import load_dotenv

# Load environment variables dari file .env
load_dotenv()

# Nama aplikasi
APP_NAME = "AI Image Prompt Generator"

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def is_gemini_configured():
    """Mengecek apakah Gemini API Key tersedia."""
    return bool(GEMINI_API_KEY)


def is_openai_configured():
    """Mengecek apakah OpenAI API Key tersedia."""
    return bool(OPENAI_API_KEY)
