import json
from src.feature_engineering import hash_feature


def load_users(file_path: str):
    with open(file_path, "r") as f:
        return json.load(f)


def predict(user_id: str, data_file: str) -> int:
    users = load_users(data_file)
    if user_id not in users:
        raise ValueError("User not found")
    return hash_feature(user_id)
