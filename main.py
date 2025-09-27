from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PizzaBot API")

class OrderRequest(BaseModel):
    item: str
    size: str
    quantity: int

class OrderResponse(BaseModel):
    message: str
    price: float

PRICES = {
    "margherita": {"small": 199, "medium": 299, "large": 399},
    "farmhouse": {"small": 249, "medium": 349, "large": 499},
}

@app.post("/order", response_model=OrderResponse)
def order_pizza(order: OrderRequest):
    item = order.item.lower()
    size = order.size.lower()
    qty = order.quantity

    if item not in PRICES or size not in PRICES[item]:
        return {"message": "❌ Invalid pizza selection.", "price": 0}

    total = PRICES[item][size] * qty
    return {"message": f"✅ {qty} {size.capitalize()} {item.capitalize()} ordered!", "price": total}
