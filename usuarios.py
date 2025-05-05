import bcrypt
from data_base import get_database

db = get_database()

# Colección de usuarios
usuarios_col = db["usuarios"]


def crear_usuarios():
    if usuarios_col.count_documents({}) == 0:
    
        usuarios = [{"nombre": "Alicia Torres", "rol": "vendedor",
                "password": bcrypt.hashpw("qwert1".encode(), bcrypt.gensalt())
            },
            {   "nombre": "Ricardo Gutierrez", "rol": "administrador",
                "password": bcrypt.hashpw("prueba".encode(), bcrypt.gensalt())
            }]
        
        usuarios_col.insert_many(usuarios)
        print("Usuarios creados.")
    else:
        print(" Usuarios existentes en la base de datos")




    # Insertar nuevo usuario en la colección
    usuarios_col.insert_one(usuarios)

def autenticar_usuario(username, password):
    """Autentica a un usuario y devuelve su rol si es exitoso."""
    usuario = usuarios_col.find_one({"username": username})
    if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario["password"]):
        return usuario["rol"]
    else:
        return None

def cerrar_sesion():
    """Función para manejar el cierre de sesión (puede ser ampliada según sea necesario)."""
    # Aquí puedes implementar la lógica para el cierre de sesión, como limpiar la sesión del usuario.
    pass

def obtener_usuarios():
    """Devuelve una lista de todos los usuarios."""
    return list(usuarios_col.find({}, {"_id": 0, "password": 0}))  # Excluir la contraseña de los resultados

def actualizar_usuario(username, nuevo_rol):
    """Actualiza el rol de un usuario existente."""
    result = usuarios_col.update_one(
        {"username": username},
        {"$set": {"rol": nuevo_rol}}
    )
    return result.modified_count > 0

def eliminar_usuario(username):
    """Elimina un usuario de la base de datos."""
    result = usuarios_col.delete_one({"username": username})
    return result.deleted_count > 0

if __name__ == "__main__":
    crear_usuarios()
