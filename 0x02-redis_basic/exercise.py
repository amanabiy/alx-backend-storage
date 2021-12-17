#!/usr/bin/env python3
"""
 a Cache class
 generate a random key (e.g. using uuid),
 store the input data in Redis using the random key and return the key.
"""
from typing import Callable, Optional, Union
import redis
import sys
from uuid import uuid4


class Cache:
    """store an instance of the Redis client as a private variable named"""

    def __init__(self) -> None:
        """instantiate the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get_str(self, data: bytes) -> str:
        """ converts byte to str """
        return data.decode('UTF-8')

    def get_int(self, data: bytes) -> int:
        return int.from_bytes(data, "big")

    def store(self, data: Union[int, str, bytes, float]) -> str:
        """
        store the input data in Redis using the random key and return the key
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, func: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Gets  """
        res = self._redis.get(key)
        return func(res) if func else get_str(res)
