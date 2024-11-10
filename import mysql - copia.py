import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='tu_host_en_la_nube',        # Por ejemplo: 'db4free.net'
                database='nombre_de_tu_base_de_datos',
                user='tu_usuario',
                password='tu_contraseña'
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
    
    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")
