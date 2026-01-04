from fastapi import FastAPI
from src.feature_engineering import hash_feature
import json

app = FastAPI()


def predict_from_file(user_id: str, file_path: str) -> int:
    with open(file_path, "r") as f:
        users = json.load(f)

    if user_id not in users:
        raise ValueError("User not found")

    return hash_feature(user_id)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/predict/{user_id}")
def predict(user_id: str):
    return {"prediction": hash_feature(user_id)}
