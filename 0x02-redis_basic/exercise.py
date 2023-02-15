#!/usr/bin/env python3
""" Redis """

import redis
import uuid


class Cache:
    def __init__(self) -> None:
        """create instance of Redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """method that takes a data argument and returns a string"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
