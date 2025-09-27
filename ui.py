import gradio as gr
import requests

API_URL = "http://localhost:8000/order"

def order_pizza_ui(item, size, quantity):
    payload = {"item": item, "size": size, "quantity": quantity}
    response = requests.post(API_URL, json=payload)
    return response.json()["message"], response.json()["price"]

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🍕 Welcome to PizzaBot 🍕\nOrder your pizza easily!")
    
    item = gr.Dropdown(["Margherita", "Farmhouse"], label="Choose Pizza")
    size = gr.Dropdown(["Small", "Medium", "Large"], label="Size")
    quantity = gr.Number(label="Quantity", value=1, precision=0)
    
    order_btn = gr.Button("Place Order")
    message = gr.Textbox(label="Order Status")
    price = gr.Number(label="Total Price (₹)", precision=2)
    
    order_btn.click(order_pizza_ui, inputs=[item, size, quantity], outputs=[message, price])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
