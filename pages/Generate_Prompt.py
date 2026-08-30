import streamlit as st

from models.gemini import analyze_image as analyze_gemini
from models.openai import analyze_image as analyze_openai

from models.prompt_generator import (
    PROMPT_STYLES,
    build_instruction
)

from utils.image_utils import (
    validate_image,
    get_image_bytes,
    get_mime_type
)


st.set_page_config(
    page_title="Generate Prompt",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Generate Prompt")
st.caption(
    "Upload gambar dan biarkan AI mengubahnya menjadi prompt."
)

st.divider()

col1, col2 = st.columns([1, 1])

with col1:

    st.subheader("Input Image")

    uploaded_file = st.file_uploader(
        "Upload gambar",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if uploaded_file:

        valid, message = validate_image(uploaded_file)

        if not valid:
            st.error(message)
        else:
            uploaded_file.seek(0)

            st.image(
                uploaded_file,
                caption=uploaded_file.name,
                width="stretch"
            )


with col2:

    st.subheader("AI Configuration")

    provider = st.selectbox(
        "AI Provider",
        ["Gemini", "OpenAI"]
    )

    style = st.selectbox(
        "Prompt Style",
        list(PROMPT_STYLES.keys())
    )

    st.write("")

    generate = st.button(
        "✨ Generate Prompt",
        type="primary",
        width="stretch"
    )


if generate:

    if uploaded_file is None:
        st.warning("Silakan upload gambar terlebih dahulu.")

    else:

        valid, message = validate_image(uploaded_file)

        if not valid:
            st.error(message)

        else:

            image_bytes = get_image_bytes(uploaded_file)
            mime_type = get_mime_type(uploaded_file)

            instruction = build_instruction(style)

            with st.spinner(
                f"AI sedang menganalisis gambar menggunakan {provider}..."
            ):

                try:

                    if provider == "Gemini":
                        result = analyze_gemini(
                            image_bytes,
                            mime_type,
                            instruction
                        )

                    else:
                        result = analyze_openai(
                            image_bytes,
                            mime_type,
                            instruction
                        )

                    st.session_state["generated_prompt"] = result

                except Exception as e:
                    st.error(
                        f"Gagal menghasilkan prompt: {str(e)}"
                    )


if "generated_prompt" in st.session_state:

    st.divider()

    st.subheader("✨ Generated Prompt")

    prompt = st.text_area(
        "Prompt",
        value=st.session_state["generated_prompt"],
        height=350
    )

    st.download_button(
        label="⬇️ Download Prompt",
        data=prompt,
        file_name="generated_prompt.txt",
        mime="text/plain",
        width="stretch"
    )
