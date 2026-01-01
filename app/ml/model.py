import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "decision_model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)

def predict_growth(model, data):
    if model is None:
        return [0]
    return model.predict(data)
