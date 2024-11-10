from database import DatabaseConnection

class Compra:
    def __init__(self, usuario_id, producto_id, cantidad, fecha):
        self.usuario_id = usuario_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.fecha = fecha

    @staticmethod
    def crear_compra(usuario_id, producto_id, cantidad, fecha):
        conexion = DatabaseConnection().get_connection()
        cursor = conexion.cursor()
        sql = "INSERT INTO compras (usuario_id, producto_id, cantidad, fecha) VALUES (%s, %s, %s, %s)"
        valores = (usuario_id, producto_id, cantidad, fecha)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Compra creada exitosamente")
        cursor.close()
        conexion.close()

    # Métodos `leer_compras`, `leer_compras_por_usuario`, `eliminar_compra` similares
