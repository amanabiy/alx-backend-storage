#!/usr/bin/env python3
"""
 a Cache class
 generate a random key (e.g. using uuid),
 store the input data in Redis using the random key and return the key.
"""
from typing import Callable, Optional, Union
from functools import wraps
import redis
import sys
from uuid import uuid4


def count_calls(func: Callable) -> Callable:
    """ a decorator to count how many times a function is called """
    key: str = func.__qualname__

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """ a function to be wrapped """
        self._redis.incr(key, amount=1)
        return func(self, *args, **kwargs)
    return wrapper


class Cache:
    """store an instance of the Redis client as a private variable named"""

    def __init__(self) -> None:
        """instantiate the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get_str(self, key: str) -> str:
        """ converts byte to str """
        data = self._redis.get(key)
        return data.decode('UTF-8')

    def get_int(self, key: str) -> int:
        data = self._redis.get(key)
        try:
            data = int(data.decode('UTF-8'))
        except Exception:
            data = 0
        return data

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the input data in Redis using the random key and return the key
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Gets  """
        res = self._redis.get(key)
        try:
            res = fn(res) if fn else res
        except ValueError as err:
            pass
        return res
