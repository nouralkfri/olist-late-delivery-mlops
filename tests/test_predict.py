import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.predict import load_config, load_artifacts, predict_single

def test_predict_returns_valid_output():
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

    assert "is_late" in result
    assert "probability" in result
    assert result["is_late"] in [0, 1]
    assert 0 <= result["probability"] <= 1

def test_predict_handles_missing_values():
    config = load_config()
    model, scaler, features = load_artifacts(config)

    incomplete_order = {"n_items": 1, "total_price": 50.0, "total_freight": None, "n_payments": 1, "total_payment": 50.0}
    result = predict_single(incomplete_order, model, scaler, features)

    assert "is_late" in result