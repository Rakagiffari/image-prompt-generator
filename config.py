import os
import streamlit as st
from dotenv import load_dotenv


# ==========================================
# LOAD ENVIRONMENT
# ==========================================

load_dotenv()


# ==========================================
# APP CONFIGURATION
# ==========================================

APP_NAME = "AI Image Prompt Generator"


# ==========================================
# GET SECRET
# ==========================================

def get_secret(key):
    """
    Mengambil secret dari Streamlit Secrets.
    Jika tidak tersedia, mengambil dari environment variable.
    """

    # Prioritas 1: Streamlit Secrets
    try:
        if key in st.secrets:
            value = st.secrets[key]

            if value:
                return str(value).strip()

    except Exception:
        pass

    # Prioritas 2: Environment Variable / .env
    value = os.getenv(key)

    if value:
        return value.strip()

    return None


# ==========================================
# API KEYS
# ==========================================

GEMINI_API_KEY = get_secret("GEMINI_API_KEY")
OPENAI_API_KEY = get_secret("OPENAI_API_KEY")


# ==========================================
# API STATUS
# ==========================================

def is_gemini_configured():
    return bool(GEMINI_API_KEY)


def is_openai_configured():
    return bool(OPENAI_API_KEY)
