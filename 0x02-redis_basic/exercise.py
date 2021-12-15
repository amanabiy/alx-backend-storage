#!/usr/bin/env python3
"""
 a Cache class
 generate a random key (e.g. using uuid),
 store the input data in Redis using the random key and return the key.
"""
from typing import Union
import redis
from uuid import uuid4


class Cache:
    """store an instance of the Redis client as a private variable named"""

    def __init__(self) -> None:
        """instantiate the class"""
        _redis = redis.Redis()
        _redis.flushdb()

    def store(data: Union[int, str, bytes, float]) -> str:
        """
        store the input data in Redis using the random key and return the key
        """
        key: str = str(uuid4())
        redis.set(key, data)
        return key
