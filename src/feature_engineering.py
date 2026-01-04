def hash_feature(value: str, num_buckets: int = 100) -> int:
    """
    Converts a high-cardinality categorical feature into a fixed-size bucket
    using hashing.

    Args:
        value (str): Input categorical value (e.g., user_id)
        num_buckets (int): Number of hash buckets

    Returns:
        int: Bucket index in range [0, num_buckets)
    """
    if not isinstance(value, str):
        raise ValueError("Input value must be a string")

    return abs(hash(value)) % num_buckets


