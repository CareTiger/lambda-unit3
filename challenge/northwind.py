import sqlite3

expensive_items = """
    SELECT  ProductName FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
"""
""" 
--- OUTPUT OF ABOVE QUERY ---
Côte de Blaye
Thüringer Rostbratwurst
Mishi Kobe Niku
Sir Rodney's Marmalade
Carnarvon Tigers
Raclette Courdavault
Manjimup Dried Apples
Tarte au sucre
Ipoh Coffee
Rössle Sauerkraut
"""

avg_hire_age = """
    SELECT  AVG (HireDate-BirthDate) FROM Employee
"""
""" 
--- OUTPUT OF ABOVE QUERY ---
37.2222222222222
"""



ten_most_expensive = """
    SELECT  P.ProductName, S.CompanyName
    FROM Product as P
    INNER JOIN  Supplier as S
    ON S.Id=P.SupplierId
    ORDER BY P.UnitPrice DESC
    LIMIT 10
"""
""" 
--- OUTPUT OF ABOVE QUERY ---
Côte de Blaye	Aux joyeux ecclésiastiques
Thüringer Rostbratwurst	Plutzer Lebensmittelgroßmärkte AG
Mishi Kobe Niku	Tokyo Traders
Sir Rodney's Marmalade	Specialty Biscuits, Ltd.
Carnarvon Tigers	Pavlova, Ltd.
Raclette Courdavault	Gai pâturage
Manjimup Dried Apples	G'day, Mate
Tarte au sucre	Forêts d'érables
Ipoh Coffee	Leka Trading
Rössle Sauerkraut	Plutzer Lebensmittelgroßmärkte AG
"""


largest_category = """
    SELECT CategoryName
    FROM Product
    INNER JOIN Category
    ON Category.Id = Product.CategoryId
	GROUP BY CategoryId
	ORDER BY COUNT(Product.Id) DESC
	LIMIT 1
"""

""" 
--- OUTPUT OF ABOVE QUERY ---
Confections
"""


def sqlite_connect(db_path="northwind_small.sqlite3"):
    """Create SQLite connection and cursor object"""
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    return conn, curs


if __name__ == "__main__":

    # Making and populating a Database
    print("Creating a connection to the Northwind database")
    conn, curs = sqlite_connect()

    # Expensive items list
    expensive_items_list = conn.execute(expensive_items).fetchall()
    for item in expensive_items_list:
        print("Item name: {} ".format(item[0]))

    # Average age of hire
    avg_age = conn.execute(avg_hire_age).fetchall()[0][0]
    print("Average age of hire at the time of hiring is {}".format(avg_age))

    # Ten most expensive items with their supplier names
    expensive_items_suppliers = conn.execute(ten_most_expensive).fetchall()
    for item in expensive_items_suppliers:
        print("Item name: {}; Item Supplier: {} ".format(item[0], item[1]))

    # largest category
    large_cat = conn.execute(largest_category).fetchall()[0][0]
    print("The largest category by number of distinct products is {}".format(large_cat))

    # close sqlite connection
    conn.close()

