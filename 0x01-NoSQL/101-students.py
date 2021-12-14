#!/usr/bin/env python3
""" 14. Top students
"""


def top_students(mongo_collection):
    """ top_students.
    """
    doc = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return doc