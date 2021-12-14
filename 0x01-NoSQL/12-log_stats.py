#!/usr/bin/env python3
"""
number of docs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    print("{} logs".format(nginx_logs.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(
        nginx_logs.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(
        nginx_logs.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(
        nginx_logs.count_documents(
            {"method": "PUT"})))
    print("\tmethod PATCH: {}".format(
        nginx_logs.count_documents(
            {"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(
        nginx_logs.count_documents(
            {"method": "DELETE"})))
    print("{} status check".format(
        nginx_logs.count_documents(
            {"method": "GET", "path": "/status"})))
