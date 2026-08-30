from PIL import Image
import io


ALLOWED_TYPES = [
    "jpg",
    "jpeg",
    "png",
    "webp"
]


def validate_image(uploaded_file):
    if uploaded_file is None:
        return False, "Tidak ada gambar yang dipilih."

    extension = uploaded_file.name.lower().split(".")[-1]

    if extension not in ALLOWED_TYPES:
        return False, "Format gambar tidak didukung."

    try:
        image = Image.open(uploaded_file)
        image.verify()
    except Exception:
        return False, "File gambar tidak valid."

    return True, "Gambar valid."


def get_image_bytes(uploaded_file):
    uploaded_file.seek(0)
    return uploaded_file.read()


def get_mime_type(uploaded_file):
    extension = uploaded_file.name.lower().split(".")[-1]

    mime_types = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "webp": "image/webp"
    }

    return mime_types[extension]
