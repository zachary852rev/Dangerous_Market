import mysql.connector
from mysql.connector import Error

connection = None
try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='p1',
                                         user='root',
                                         password='zp90')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


def SQL_inventory():
    cnx = mysql.connector.connect(user="root", password="zp90", host="127.0.0.1", database="p1")
    cursor = cnx.cursor()
    inv01 = "SELECT * FROM Inventory WHERE itemID = 1;"
    inv02 = "SELECT * FROM Inventory WHERE itemID = 2;"
    inv03 = "SELECT * FROM Inventory WHERE itemID = 3;"
    inv04 = "SELECT * FROM Inventory WHERE itemID = 4;"
    inv05 = "SELECT * FROM Inventory WHERE itemID = 5;"
    cursor.execute(inv01)
    fa = cursor.fetchone()
    print(fa)
    cursor.execute(inv02)
    fa = cursor.fetchone()
    print(fa)
    cursor.execute(inv03)
    fa = cursor.fetchone()
    print(fa)
    cursor.execute(inv04)
    fa = cursor.fetchone()
    print(fa)
    cursor.execute(inv05)
    fa = cursor.fetchone()
    print(fa)
SQL_inventory()

