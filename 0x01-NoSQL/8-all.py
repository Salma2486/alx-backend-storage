#!/usr/bin/env python3
""" eadg tsr htt"""


def list_all(mongo_collection):
    """ etsr """
    return [doc for doc in mongo_collection.find()]
