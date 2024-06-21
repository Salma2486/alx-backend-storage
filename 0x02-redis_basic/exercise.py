#!/usr/bin/env python3
"""task0"""
import redis
import uuid
from typing import Union, Callable, Optional

class Cache:
    """Cache class"""
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """get method"""
        value = self.redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str):
        """get_str method"""
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str):
        """get_int method"""
        return self.get(key, fn=int)
        