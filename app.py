import streamlit as st

from config import APP_NAME

st.set_page_config(
    page_title=APP_NAME,
    page_icon="✨",
    layout="wide"
)

st.title("✨ AI Image Prompt Generator")

st.markdown(
    """
    ### Ubah gambar menjadi prompt AI

    Upload sebuah gambar, lalu gunakan **Gemini** atau **OpenAI**
    untuk menganalisis gambar dan menghasilkan prompt yang detail.
    """
)

st.info(
    "Gunakan menu di sebelah kiri untuk mulai membuat prompt."
)
