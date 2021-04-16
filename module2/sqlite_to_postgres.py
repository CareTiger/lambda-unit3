"""Creating a data pipeline - moving data from sqlite to PostgreSQL"""
import os
import sqlite3
import psycopg2
import create_queries as create
import read_queries as read

PG_PASSWORD = os.environ.get("PG_PASSWORD")
PG_HOST = os.environ.get("PG_HOST")
PG_DBNAME = os.environ.get('PG_DBNAME')
PG_USER = os.environ.get("PG_USER")


def initialize(pg_curs):
    """initiliazes postgresql DB"""
    pg_curs.execute(create.CREATE_charactercreator_character)


def sl_connect(sl_db="rpg_db.sqlite3"):
    """Connects to sqlite"""
    sl_conn = sqlite3.connect(sl_db)
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs


def pg_connect(dbname, user, password, host):
    """Connects to postgresql"""
    pg_conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs


# Only executes read queries
def execute_read_query(curs, query):
    """Executes query through passed in cursor"""
    curs.execute(query)
    return curs.fetchall()


def pipeline(pg_curs, sl_curs):
    """Handling migration of charactercreator_character table"""
    # character_list = [(id, name,  ...), (id, name,  ...), (id, name,  ...), ...] andn the len(character_list) is 302
    character_list = execute_read_query(sl_curs, read.GET_CHARACTERS)
    for character in character_list:
        # character = (id, name, ...)
        insert_statement = create.INSERT_charactercreator_character % (
            character[1],  # name
            character[2],  # level
            character[3],  # exp
            character[4],  # hp
            character[5],  # strength
            character[6],  # intelligence
            character[7],  # dexterity
            character[8],  # wisdom
        )
        # print(insert_statement)  # prints values if you want to see
        pg_curs.execute(insert_statement)    
    return "Data Added!"


if __name__ == "__main__":
    sl_conn, sl_curs = sl_connect()
    pg_conn, pg_curs = pg_connect(
        PG_DBNAME,
        PG_USER,
        PG_PASSWORD,
        PG_HOST
    )
    initialize(pg_curs)
    pipeline(pg_curs, sl_curs)
    pg_conn.commit()
    