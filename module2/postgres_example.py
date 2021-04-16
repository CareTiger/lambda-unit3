"""Example of a PostgresSQL connection"""
import os
import psycopg2
import create_queries as create

dbname = os.environ.get('PG_DBNAME')
user = os.environ.get("PG_USER")
password = os.environ.get("PG_PASSWORD")
host = os.environ.get("PG_HOST")

# step1 - connect to a database
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
# step2 - make a cursor
pg_curs = pg_conn.cursor()

# step 3 - make a queries.py file

# step 4 - execute query
pg_curs.execute(create.CREATE_TEST)
pg_curs.execute(create.INSERT_TEST)

pg_curs.execute("SELECT * FROM test_table;")

# step 5 - fetch data
results = pg_curs.fetchall()

if __name__ == "__main__":
    print(results)

