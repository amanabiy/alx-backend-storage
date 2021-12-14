#!/usr/bin/env python3
"""

"""


def insert_school(mongo_collection, **kwargs):
    """ insert into the collection """
    docs = mongo_collection.insert_one(kwargs)
    return docs