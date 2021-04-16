import sqlite3


""" SQL STATEMENTS """
DEMO_DATA_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS demo (
        s VARCHAR(1),
        x INT,
        y INT
    );
    """

DEMO_DATA_INSERT_DATA = """
    INSERT INTO demo (s, x, y)
    VALUES 
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);
"""

DEMO_DATA_LENGTH = """
    SELECT COUNT(*) FROM demo
"""

DEMO_DATA_X_Y_ATLEAST_5 = """
    SELECT COUNT(*) FROM demo
    WHERE x >= 5
    AND y>=5
"""

DEMO_DATA_DISTINCT_Y = """
    SELECT COUNT(DISTINCT y) FROM demo
"""

def sqlite_connect(db_path="demo_data.sqlite3"):
    """Create SQLite connection and cursor object"""
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    return conn, curs


if __name__ == "__main__":
    
    # Making and populating a Database
    print("Creating demo table if it doesnt exist...")
    demo_conn, demo_curs = sqlite_connect()
    demo_conn.execute(DEMO_DATA_CREATE_TABLE)
    demo_conn.execute(DEMO_DATA_INSERT_DATA)

    # Running queries on the demo table
    demo_conn, demo_curs = sqlite_connect()
    row_count = demo_conn.execute(DEMO_DATA_LENGTH).fetchall()[0][0]
    xy_at_least_5 = demo_conn.execute(DEMO_DATA_X_Y_ATLEAST_5).fetchall()[0][0]
    unique_y = demo_conn.execute(DEMO_DATA_DISTINCT_Y).fetchall()[0][0]

    print("#######################################################")
    print("We have {} rows in the demo table"
        .format(row_count))
    print("There are {} rows in the demo table where both x and y are at least 5"
        .format(xy_at_least_5))
    print("There are {} distinct values of y in the demo table"
        .format(unique_y))
    print("#######################################################")

    demo_conn.commit()
    demo_conn.close()
    print("Closed the cursor and connection...")
