import gradio as gr
import requests

API_URL = "http://localhost:8000/analyze-car"  # your actual API

def send_image_to_api(image_path):
    if image_path is None:
        return "", "", "", ""

    try:
        with open(image_path, "rb") as img_file:
            files = {
                "image": ("uploaded.png", img_file, "image/png")
            }
            response = requests.post(API_URL, files=files)
            if response.ok:
                data = response.json()
                return data.get("brand", ""), data.get("color", ""), data.get("type", ""), data.get("other_details", "")
            else:
                return "Error", "", "", response.text
    except Exception as e:
        return "Exception", "", "", str(e)

with gr.Blocks() as demo:
    gr.Markdown("## 🚗 Upload a Car Image to Analyze")

    image_input = gr.Image(type="filepath", label="Upload Car Image")
    btn = gr.Button("Analyze")

    brand = gr.Textbox(label="Brand", interactive=False)
    color = gr.Textbox(label="Color", interactive=False)
    car_type = gr.Textbox(label="Type", interactive=False)
    other_details = gr.Textbox(label="Other Details", lines=4, interactive=False)

    btn.click(send_image_to_api, inputs=image_input, outputs=[brand, color, car_type, other_details])

demo.launch(share=True)
