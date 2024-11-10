from database import DatabaseConnection

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @staticmethod
    def crear_producto(nombre, precio, stock):
        conexion = DatabaseConnection().get_connection()
        cursor = conexion.cursor()
        sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
        valores = (nombre, precio, stock)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Producto creado exitosamente")
        cursor.close()
        conexion.close()

    # Métodos `leer_productos`, `actualizar_producto`, `eliminar_producto` similares a los de Usuario
