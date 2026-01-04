import json
import pytest

from src.app import predict_from_file


@pytest.fixture
def sample_data_file(tmp_path):
    data = {
        "user_123": {"age": 30},
        "user_456": {"age": 25}
    }
    file_path = tmp_path / "users.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return str(file_path)


def test_predict_returns_int(sample_data_file):
    result = predict_from_file("user_123", sample_data_file)
    assert isinstance(result, int)


def test_predict_user_not_found(sample_data_file):
    with pytest.raises(ValueError):
        predict_from_file("user_999", sample_data_file)
