#!/usr/bin/env python3
"""
List all documents in Python
"""


def list_all(mongo_collection):
    """ list_all documents """
    docs = mongo_collection.find()
    return [x for x in docs]