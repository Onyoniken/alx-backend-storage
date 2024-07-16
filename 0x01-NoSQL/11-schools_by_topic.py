#!/usr/bin/env python3

"""write a python function thatv return list of school
"""

import pymongo

def schools_by_topic(mongo_collection, topic):
    """return list of school having specific topic"""
    return mongo_collection.find({"topics": topic})
