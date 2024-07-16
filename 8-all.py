#!/usr/bin/env python3

"""writes python function lists all documents in a collection
"""

import pymongo

def list_all(mongo_collection):
    """Return list of all docs"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
