from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os
from src.logger import logger
import time
from src.validation import validate_order
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.predict import load_config, load_artifacts, predict_single

app = FastAPI(title="Late Delivery Prediction API")

config = load_config()
model, scaler, features = load_artifacts(config)

class OrderInput(BaseModel):
    n_items: float
    total_price: float
    total_freight: float
    n_payments: float
    total_payment: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/model-info")
def model_info():
    return {"model_type": type(model).__name__, "features": features}
@app.post("/predict")
def predict(order: OrderInput):
    global prediction_count, error_count
    is_valid, error_msg = validate_order(order.dict())
    if not is_valid:
        error_count += 1
        logger.warning(f"rejected input: {order.dict()} | reason: {error_msg}")
        return {"error": error_msg}, 400
    
    start = time.time()
    result = predict_single(order.dict(), model, scaler, features)
    result["model_version"] = "v1"
    latency = round(time.time() - start, 4)
    prediction_count += 1
    
    logger.info(f"input={order.dict()} | output={result} | latency={latency}s")
    
    return result
prediction_count = 0
error_count = 0

@app.get("/metrics")
def metrics():
    return {
        "total_predictions": prediction_count,
        "total_errors": error_count
    }