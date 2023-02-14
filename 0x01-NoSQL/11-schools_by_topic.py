#!/usr/bin/env python3
"""find by"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """find by topic"""
    if not mongo_collection:
        return None
    
    return [i for i in mongo_collection.find({"topics":topic})]