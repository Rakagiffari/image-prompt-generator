import streamlit as st

from config import (
    APP_NAME,
    is_gemini_configured,
    is_openai_configured
)

st.set_page_config(
    page_title=APP_NAME,
    page_icon="✨",
    layout="wide"
)

st.title("✨ AI Image Prompt Generator")

st.subheader("API Configuration")

if is_gemini_configured():
    st.success("✅ Gemini API Key terdeteksi")
else:
    st.error("❌ Gemini API Key belum dikonfigurasi")

if is_openai_configured():
    st.success("✅ OpenAI API Key terdeteksi")
else:
    st.error("❌ OpenAI API Key belum dikonfigurasi")
