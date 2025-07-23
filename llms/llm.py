import base64
from pathlib import Path
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage


# Load vision-capable model
model = ChatOllama(model="qwen2.5vl:7b")  # or llava, bakllava, etc.