"""Pipeline"""
import query
import os
import pymongo
import sqlite3

user = os.environ.get("MONGO_USER")
password = os.environ.get("MONGO_PASSWORD")
dbname = os.environ.get("MONGO_DBNAME")

def sqlite_connect(db_path="rpg_db.sqlite3"):
    """Create SQLite connection and cursor object"""
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    return conn, curs


def mongo_connect():
    """Creates mongoDB Client and returns DB"""
    client = pymongo.MongoClient(
        "mongodb+srv://{}:{}@cluster0.uxfef.mongodb.net/{}?retryWrites=true&w=majority"
        .format(user, password, dbname)
        )

    return client.test


"""Print out the total number of records in the test collection"""
def mongo_collection_test():
    db = mongo_connect()
    collection = db.test

    print(
        "Total number of documents in the test collection are {}"
        .format(collection.count_documents({}))
        )


"""Print out the records in the test collection"""
def mongo_collection():
    db = mongo_connect()
    characters = db.test

    for character in characters.find(): 
        print(character)


"""Delete the records in the character collection"""
def mongo_delete_collection():
    db = mongo_connect()
    db.characters.delete_many({})
    print("Deleted all documents from the characters collection")


def main():
    # MongoClient -> Database -> Cluster -> Document
    # Connection methods
    db = mongo_connect()
    sl_conn, sl_curs = sqlite_connect()

    # Getting rpg characters document collection
    collection = db.characters

    # if characters collection already exists then delete them
    if collection.count_documents({}) > 0:
        mongo_delete_collection()

    # character_docs_list = [] <- another way
    # getting characters
    characters = sl_curs.execute(query.GET_charactercreator_characters)

    for character in characters:
        # character = (1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1)
        mongo_document = {
            "name": character[1],  # name = character[1]
            "level": character[2],  # level = character[2]
            "exp": character[3],  # exp = character[3]
            "hp": character[4],  # hp = character[4]
            "strength": character[5],  # strength = character[5]
            "intelligence": character[6],  # intelligence = character[6]
            "dexterity": character[7],  # dexterity = character[7]
            "wisdom": character[8]  # wisdom = character[8]
        }
        # character_docs_list.append(mongo_document) <- another way
        collection.insert_one(mongo_document)
    # collection.insert_many(mongo_documents) <- another way

    # close the sqlite cursor
    sl_curs.close()
    # close sqlite connection
    sl_conn.close()
    print("Yay! Saved data successfully.")



if __name__ == "__main__":
    main()
    mongo_collection_test()
    # mongo_collection()

