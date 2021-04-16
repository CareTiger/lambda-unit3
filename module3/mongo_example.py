"""MongoDB example"""
import os
import pymongo
import sqlite3

user = os.environ.get("MONGO_USER")
password = os.environ.get("MONGO_PASSWORD")
dbname = os.environ.get("MONGO_DBNAME")


def sqlite_connect(db="rpg_db.sqlite3"):
    """create sqlite connection and cursor object"""
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    return conn, curs


def mongo_connect():
    client = pymongo.MongoClient("mongodb+srv://user:password@cluster0.uxfef.mongodb.net/dbname?retryWrites=true&w=majority")
    return client.test


if __name__ == "__main__":
    db = mongo_connect()
    collection = db.test