import mysql.connector

# __cnx is a global variable that will store the connection object.
# This is done so that we can reuse the connection object instead of creating a new one every time we need to connect to the database.
__cnx = None

def get_sql_connection():
    print("Opening mysql connection...")
    global __cnx
    
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='2036', database='GS')
    if __cnx.is_connected():
        print("MySQL connection established.")

    return __cnx

def close_sql_connection():
    global __cnx

    if __cnx is not None and __cnx.is_connected():
        print("Closing MySQL connection...")
        __cnx.close()
        __cnx = None
        print("MySQL connection closed.")