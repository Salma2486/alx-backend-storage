#!/usr/bin/env python3
""" eadg tsr htt"""


def list_all(mongo_collection):
    """ etsr """
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
