import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sandhiyab@12",  
        database="cafeteria"
    )
    return connection
