""" This code executes:
1) Open and close connection to the database;
"""
# Import flask Modules
from flask import g
# Import python Modules
import sqlite3
# Import project Modules
from settings import DATABASE


def open_connection():
    """
     open_connection open connect to the database
    :return: database
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def close_connection(exception):
    """
     close_connection close connect to the database
    """
    db = getattr(g, '_database', None)

    if db is not None:
        db.cursor().close()
