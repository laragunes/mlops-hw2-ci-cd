from fastapi import FastAPI
from src.feature_engineering import hash_feature

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/predict/{user_id}")
def predict(user_id: str):
    return {"prediction": hash_feature(user_id)}
