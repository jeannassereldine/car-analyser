import base64

def encode_image_as_data_url(image_bytes: bytes, mime_type: str = "image/jpeg") -> str:
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:{mime_type};base64,{image_b64}"
