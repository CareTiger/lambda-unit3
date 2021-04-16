import pandas as pd
import sqlite3

NOS_OF_ROWS = """
    SELECT  COUNT(*) FROM review;
    """
NOS_OF_USERS = """
    SELECT  COUNT(*) FROM review
    WHERE Nature > 100 AND Shopping > 100
    ;
    """


""""A function to connect to our database  and open a cursor"""
def connect(db):
    # CREATE A CONNECT TO DB
    conn = sqlite3.connect(db)
    # CREATE A CURSOR
    curs = conn.cursor()
    return conn, curs


""""A function to use our cursor and run a query"""
def execute_query(curs, query):
    curs.execute(query)
    results = curs.fetchall()
    return results


if __name__ == "__main__":
    # create a database called buddymove_holidayiq.sqlite3
    conn, curs = connect("buddymove_holidayiq.sqlite3")


    # Create a dataframe from the csv file
    df = pd.read_csv("buddymove_holidayiq.csv")
    # use created connection to load the dataframe into a SQL table
    df.to_sql(name="review", con=conn, if_exists='replace')


    # Output results of our queries
    print("###############################################")
    print("Number of rows: {}".format(execute_query(curs, NOS_OF_ROWS)[0][0]))
    print("Number users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category: {}".format(execute_query(curs, NOS_OF_USERS)[0][0]))
    print("###############################################")
    
    # CLOSE THE CURSOR TO THE DATABASE
    curs.close()