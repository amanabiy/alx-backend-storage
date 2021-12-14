#!/usr/bin/env python3
"""
filter school by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    update_topics using update_many
    """
    mongo_collection.find({"topics": topic})
