import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="helpdesk_user",
        password="123456",
        database="helpdesk_db"
    )