from database import DatabaseConnection

class Usuario:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    @staticmethod
    def crear_usuario(nombre, email, contraseña):
        conexion = DatabaseConnection().get_connection()
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (nombre, email, contraseña) VALUES (%s, %s, %s)"
        valores = (nombre, email, contraseña)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Usuario creado exitosamente")
        cursor.close()
        conexion.close()

    @staticmethod
    def leer_usuarios():
        conexion = DatabaseConnection().get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        for usuario in usuarios:
            print(usuario)
        cursor.close()
        conexion.close()

    @staticmethod
    def actualizar_usuario(id_usuario, nuevo_nombre, nuevo_email):
        conexion = DatabaseConnection().get_connection()
        cursor = conexion.cursor()
        sql = "UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s"
        valores = (nuevo_nombre, nuevo_email, id_usuario)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Usuario actualizado exitosamente")
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar_usuario(id_usuario):
        conexion = DatabaseConnection().get_connection()
        cursor = conexion.cursor()
        sql = "DELETE FROM usuarios WHERE id=%s"
        cursor.execute(sql, (id_usuario,))
        conexion.commit()
        print("Usuario eliminado exitosamente")
        cursor.close()
        conexion.close()
