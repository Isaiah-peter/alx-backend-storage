#!/usr/bin/env python3
"""insert"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert function"""
    if not mongo_collection:
        return None
    return mongo_collection.insert(kwargs)
