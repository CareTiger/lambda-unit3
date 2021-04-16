# for csv to postgres
CREATE_titanic = """
    CREATE TABLE IF NOT EXISTS titanic (
        id SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(90),
        Sex VARCHAR(10),
        Age INT,
        Siblings_Spouses_aboard INT,
        Parents_Children_aboard INT,
        Fare FLOAT
    );
    """
INSERT_titanic = """
    INSERT INTO titanic (
        Survived, 
        Pclass,
        Name,
        Sex,
        Age,
        Siblings_Spouses_aboard,
        Parents_Children_aboard,
        Fare
        ) VALUES (
        %s,
        %s, 
        '%s',
        '%s',
        %s,
        %s,
        %s,
        %s
        );
    """


# for sqlite_to_postgres.py
CREATE_charactercreator_character = """
    CREATE TABLE IF NOT EXISTS charactercreator_character (
        id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        level INT,
        exp INT,
        hp INT, 
        strength INT,
        intelligence INT, 
        dexterity INT, 
        wisdom INT
    );
    """

INSERT_charactercreator_character = """
    INSERT INTO charactercreator_character (
        name, 
        level,
        exp,
        hp,
        strength,
        intelligence,
        dexterity,
        wisdom
        ) VALUES (
        '%s',
        %s, 
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
        );
    """


# For postgres_example.py
CREATE_TEST = """
    CREATE TABLE test_table(
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        fav_num INT NOT NULL     
        );
    """

INSERT_TEST = """
    INSERT INTO test_table(name, fav_num) VALUES 
    ('Nick', 43), 
    ('Jack', 42), 
    ('Tim', 777)
    """