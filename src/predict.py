import joblib
import yaml
import pandas as pd

def load_config(path="config/config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def load_artifacts(config):
    model = joblib.load(config["model_path"])
    scaler = joblib.load(config["scaler_path"])
    features = joblib.load(config["features_path"])
    return model, scaler, features

def predict_single(order_data: dict, model, scaler, features):
    df = pd.DataFrame([order_data])
    df[features] = df[features].fillna(0)
    X = scaler.transform(df[features])
    prediction = int(model.predict(X)[0])
    probability = float(model.predict_proba(X)[0][1])
    return {"is_late": prediction, "probability": probability}

if __name__ == "__main__":
    config = load_config()
    model, scaler, features = load_artifacts(config)

    sample_order = {
        "n_items": 2,
        "total_price": 150.0,
        "total_freight": 20.0,
        "n_payments": 1,
        "total_payment": 170.0
    }

    result = predict_single(sample_order, model, scaler, features)
    print(result)