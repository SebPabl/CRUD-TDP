import mysql.connector


class Conexion:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', database='CRUD', user='root', password='')
