import base64
from fastapi import UploadFile
from langchain_core.messages import SystemMessage, HumanMessage
from models.car_model import Car
from llms.llm import model  # Must point to your structured LangChain-compatible model
from utils.utils import encode_image_as_data_url

async def analyze_car_image(image: UploadFile) -> Car:
    image_bytes = await image.read()
    image_data_url = encode_image_as_data_url(image_bytes)

    messages = [
        SystemMessage(
            content=(
                "You are an expert car analyst. Describe the car in the image. "
                "Specifically extract: brand, color, type (SUV, sedan, etc), and other visible details. "
                "If you don't know the value of an attribute asked to be extracted, return null for the attribute value."
            )
        ),
        HumanMessage(
            content=[
                {
                    "type": "image_url",
                    "image_url": {"url": image_data_url}
                }
            ]
        )
    ]

    model_with_structure = model.with_structured_output(Car)
    return model_with_structure.invoke(messages)
