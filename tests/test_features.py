from src.feature_engineering import hash_feature


def test_hash_feature_returns_int():
    result = hash_feature("user_123")
    assert isinstance(result, int)


def test_hash_feature_range():
    num_buckets = 100
    result = hash_feature("user_123", num_buckets)
    assert 0 <= result < num_buckets
