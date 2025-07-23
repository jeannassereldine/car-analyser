
````markdown
# 🚗 Car Analyzer API

This project provides a REST API to analyze car images using a vision-capable LLM (e.g., GPT-4 Vision, LLaVA, etc.).  
It extracts structured information from car images such as:

- Brand
- Color
- Type (e.g., SUV, sedan)
- Other visible details

---

## 📁 Project Structure

```text
car_analyzer/
│
├── main.py             # FastAPI app entry point
├── api.py              # API routes
├── models.py           # Pydantic model for car information
├── services.py         # LLM inference logic
├── utils.py            # Helper functions (e.g., base64 encoder)
└── llm.py              # Model configuration (OpenAI, Claude, or HuggingFace)
````

---

## ⚙️ Requirements

* Python >= 3.11
* [uv](https://github.com/astral-sh/uv) — ultra-fast package manager (recommended)
* Model Configuration

---

## 🧠 Model Configuration

This project requires a **vision-language (VL) model** that can process images and generate structured text output.

### Using a Local Ollama VL Model (Mandatory)

- You **must use a VL model** that supports image inputs.  
- For example, this project uses the Ollama model `qwen2.5vl:7b`.

#### Install Ollama

If you haven’t installed Ollama yet:

```bash
# macOS example, adjust for your OS
brew install ollama
ollama pull qwen2.5vl:7b
````


## 📦 Installation

Make sure Python 3.11+ is installed.

### 1. Install `uv`

```bash
pip install uv
```

### 2. Start the FastAPI Backend 

```bash
uv run fastapi dev
```
Visit: [http://localhost:8000/docs](http://localhost:8000/docs) to use the Swagger UI.

This will install all required packages listed in `pyproject.toml`.

---

## 🚀  Start the Gradio UI

Start the gradio UI locally:

```bash
uv run gradio/upload_ui.py
```

Visit: [http://localhost:7860](http://localhost:7860) to use the gradio UI.

---

## 📤 Example Request

You can send a POST request to `/analyze-car` with an image file.

### Using `curl`:

```bash
curl -X POST http://localhost:8000/analyze-car \
  -F "image=@/path/to/car.jpg"
```

### Response:

```json
{
  "brand": "Toyota",
  "color": "White",
  "type": "SUV",
  "other_details": "5-door, modern design, front grille visible"
}
```

---


## 📄 License

MIT License. You are free to use, modify, and distribute.

---

## 🙌 Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 🔗 Useful Links

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [LangChain](https://www.langchain.com/)
* [uv Package Manager](https://github.com/astral-sh/uv)
````