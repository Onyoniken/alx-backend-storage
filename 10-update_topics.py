#!/usr/bin/env python3
"""python function that changes topics of school documnets based on name:
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
