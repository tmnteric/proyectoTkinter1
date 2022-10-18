import mysql.connector

def conectar():
    

    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'productos',
        port = '3308'
    )
    return db
