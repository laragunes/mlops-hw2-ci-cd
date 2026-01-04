import pytest
from src.feature_engineering import hash_feature


def test_hash_feature_returns_int():
    result = hash_feature("user_123")
    assert isinstance(result, int)


def test_hash_feature_within_bucket_range():
    num_buckets = 100
    result = hash_feature("user_456", num_buckets)
    assert 0 <= result < num_buckets


def test_hash_feature_deterministic():
    value = "same_user"
    assert hash_feature(value) == hash_feature(value)


def test_hash_feature_invalid_input():
    with pytest.raises(ValueError):
        hash_feature(123)
