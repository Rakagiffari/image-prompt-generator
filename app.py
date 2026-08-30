import streamlit as st

from config import (
    APP_NAME,
    is_gemini_configured,
    is_openai_configured
)


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="✨",
    layout="wide"
)


# ==========================================
# HEADER
# ==========================================

st.title("✨ AI Image Prompt Generator")

st.write(
    "Konfigurasi API untuk Gemini dan OpenAI."
)

st.divider()


# ==========================================
# API STATUS
# ==========================================

st.subheader("🔑 API Configuration")


# Gemini
if is_gemini_configured():
    st.success("✅ Gemini API Key terdeteksi")
else:
    st.error("❌ Gemini API Key belum dikonfigurasi")


# OpenAI
if is_openai_configured():
    st.success("✅ OpenAI API Key terdeteksi")
else:
    st.error("❌ OpenAI API Key belum dikonfigurasi")


st.divider()


# ==========================================
# STATUS SUMMARY
# ==========================================

gemini_status = is_gemini_configured()
openai_status = is_openai_configured()

if gemini_status and openai_status:
    st.success(
        "🎉 Gemini dan OpenAI sudah siap digunakan."
    )

elif gemini_status:
    st.warning(
        "⚠️ Gemini sudah siap, tetapi OpenAI belum dikonfigurasi."
    )

elif openai_status:
    st.warning(
        "⚠️ OpenAI sudah siap, tetapi Gemini belum dikonfigurasi."
    )

else:
    st.warning(
        "⚠️ Belum ada API yang dikonfigurasi."
    )
