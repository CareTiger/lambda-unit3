import sqlite3
from queries import (TOTAL_CHARACTERS, TOTAL_SUBCLASS, TOTAL_ITEMS, WEAPONS,
    NON_WEAPONS, CHARACTER_ITEMS, CHARACTER_WEAPONS)


""""A function to connect to our database  and open a cursor"""
def connect(db="rpg_db.sqlite3"):
    # CONNECT TO DB
    conn = sqlite3.connect("rpg_db.sqlite3")
    # CREATE A CURSOR
    curs = conn.cursor()
    return conn, curs


""""A function to use our cursor and run a query"""
def execute_query(curs, query):
    curs.execute(query)
    results = curs.fetchall()
    return results


if __name__ == "__main__":
    conn, rpg_curs = connect()

    print("#############################################")
    print("Total Characters are {}".format(execute_query(rpg_curs, TOTAL_CHARACTERS)[0][0]))
    print("Total Subclass are {}".format(execute_query(rpg_curs, TOTAL_SUBCLASS)[0][0]))
    print("Total Items are {}".format(execute_query(rpg_curs, TOTAL_ITEMS)[0][0]))
    print("Total Weapons are {}".format(execute_query(rpg_curs, WEAPONS)[0][0]))
    print("Total Non-Weapons are {}".format(execute_query(rpg_curs, NON_WEAPONS)[0][0]))
    print("#############################################")
    
    rpg_curs.close()
