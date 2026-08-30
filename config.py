import os
import streamlit as st
from dotenv import load_dotenv


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()


# ==========================================
# APP CONFIGURATION
# ==========================================

APP_NAME = "AI Image Prompt Generator"


# ==========================================
# API KEY
# ==========================================

def get_secret(key):
    """
    Mengambil API key dari Streamlit Secrets.
    Jika tidak tersedia, gunakan environment variable.
    """

    try:
        value = st.secrets.get(key)

        if value:
            return value

    except Exception:
        pass

    return os.getenv(key)


GEMINI_API_KEY = get_secret("GEMINI_API_KEY")
OPENAI_API_KEY = get_secret("OPENAI_API_KEY")


# ==========================================
# API STATUS
# ==========================================

def is_gemini_configured():
    return bool(GEMINI_API_KEY)


def is_openai_configured():
    return bool(OPENAI_API_KEY)
