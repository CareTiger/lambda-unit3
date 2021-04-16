"""Creating a data pipeline - moving data from csv to PostgreSQL"""
import os
import sqlite3
import psycopg2
import create_queries as create
import read_queries as read
import pandas as pd
import csv

PG_PASSWORD = os.environ.get("PG_PASSWORD")
PG_HOST = os.environ.get("PG_HOST")
PG_DBNAME = os.environ.get('PG_DBNAME')
PG_USER = os.environ.get("PG_USER")

def initialize(pg_curs):
    """initiliazes postgresql DB"""
    pg_curs.execute(create.CREATE_titanic)
    print("TITANIC TABLE CREATED")


def pg_connect(dbname, user, password, host):
    """Connects to postgresql"""
    pg_conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs


if __name__ == "__main__":
    pg_conn, pg_curs = pg_connect(
        PG_DBNAME,
        PG_USER,
        PG_PASSWORD,
        PG_HOST
    )
    initialize(pg_curs)
    # read the csv file and
    with open('titanic.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.

        for row in reader:
            insert_statement = create.INSERT_titanic % (
                row[0],  # Survived
                row[1],  # PClass
                row[2].replace("'", " "),  # Name
                row[3],  # Sex
                row[4],  # Age
                row[5],  # Siblings/Spouses aboard
                row[6],  # Parents/Children aboard
                row[7],  # Fare
            )   
            # print(insert_statement)            
            pg_curs.execute(insert_statement)
    pg_conn.commit()
    print("Data uploaded")
