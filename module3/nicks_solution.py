"""Sprint 2 Module 3: Data pipeline - SQLite to MongoDB"""
from os import getenv
import sqlite3  # dont need to install
import pymongo  # make sure its in your pipenv

password = getenv("MONGO_DB_PASSWORD")
dbname = "rpg_data"

def create_mdb_connection(password, dbname):
    # using string formatting to add in my password and dbname
    client = pymongo.MongoClient(
        "mongodb+srv://MacOS-Nick:{}@solutions.r8cfq.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname))
    return client

def create_sl_connection(extraction_db="rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(extraction_db)  # local sqlitedb
    return sl_conn

def execute_query(curs, query):
    return curs.execute(query).fetchall()
    
def doc_creation(db, sl_curs, character_table_query, item_table_query, weapon_table_query):
    # character - (id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    weapons = execute_query(sl_curs, weapon_table_query)
    characters = execute_query(sl_curs, character_table_query)
    for character in characters:
        # item - (item_name)
        item_character_query = item_table_query.format("\'%s\'" % character[1])
        item_names = execute_query(sl_curs, item_character_query)
        weapon_names = []
        for item in item_names:
            if item in weapons:
                weapon_names.append(item[0])
        doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8],
            "items": item_names,
            "weapons": weapon_names
        }
        db.insert_one(doc)
def show_all(db):
    all_docs = list(db.find())
    return all_docs
# SQLite Quiries
GET_CHARACTER_TABLE = """
    SELECT *
    FROM charactercreator_character;
"""
GET_ITEM_TABLE = """
    SELECT ai.name as item_name
    FROM (SELECT *
    FROM charactercreator_character as cc_char
    INNER JOIN charactercreator_character_inventory as cc_ci
    WHERE cc_char.character_id = cc_ci.character_id) as char_ci
    INNER JOIN armory_item as ai
    WHERE ai.item_id = char_ci.item_id
    AND char_ci.name = {};
"""
GET_WEAPON_TABLE = """
    SELECT aw_ai.name
    FROM (SELECT *
    FROM armory_item as ai
    INNER JOIN armory_weapon as aw
    WHERE ai.item_id = aw.item_ptr_id) as aw_ai
    INNER JOIN (SELECT *
    FROM charactercreator_character as cc_char
    INNER JOIN charactercreator_character_inventory as  cc_ci
    WHERE cc_char.character_id = cc_ci.character_id) as char_ci
    WHERE aw_ai.item_id = char_ci.item_id;
"""
if __name__ == "__main__":
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(password, dbname)
    db = client.rpg_data.rpg_data
    db.drop({})
    doc_creation(db, sl_curs, GET_CHARACTER_TABLE,
                 GET_ITEM_TABLE, GET_WEAPON_TABLE)
    print(show_all(db))