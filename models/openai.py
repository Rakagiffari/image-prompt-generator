from openai import OpenAI

from config import OPENAI_API_KEY


def analyze_image(image_bytes, mime_type, instruction):

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY belum dikonfigurasi."
        )

    client = OpenAI(
        api_key=OPENAI_API_KEY
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": instruction
                    },
                    {
                        "type": "input_image",
                        "image_url": (
                            f"data:{mime_type};base64,"
                            + __import__("base64")
                            .b64encode(image_bytes)
                            .decode("utf-8")
                        )
                    }
                ]
            }
        ]
    )

    return response.output_text
