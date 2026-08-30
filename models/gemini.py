from google import genai
from google.genai import types

from config import GEMINI_API_KEY


def analyze_image(image_bytes, mime_type, instruction):
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY belum dikonfigurasi.")

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type
            ),
            instruction
        ]
    )

    return response.text
