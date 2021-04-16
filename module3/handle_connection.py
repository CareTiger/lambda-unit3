"""MongoDB simple example for Lambda Students"""
import sqlite3
import pymongo

PASSWORD = "LkDudVAoLvE7dECk"
DBNAME = "test"


def sqlite_connect(db_path="../data/rpg_db.sqlite3"):
    """Create SQLite connection and cursor object"""
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    return conn, curs


def mongo_connect(password, dbname):
    """Creates mongoDB Client and returns DB"""
    client = pymongo.MongoClient(
        "mongodb+srv://MacOS-nwdelafu:{}@cluster0.3oigq.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
    )
    return client.test


# if __name__ == "__main__":
#     # MongoClient -> Database -> Cluster -> Document
#     db = mongo_connect(PASSWORD, DBNAME)
#     collection = db.test