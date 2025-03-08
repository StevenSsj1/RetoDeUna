from fastapi import APIRouter
from fastapi import APIRouter, HTTPException
from ..supabase_client import supabase
import bcrypt

router = APIRouter(
    prefix="/hackemate",      # Prefijo del endpoint, por ejemplo /users/
    tags=["Users"]        # Etiqueta para la documentación
)

@router.get("/users")
def get_users():

    #Retorna la lista de usuarios.
    #Supongamos que en Supabase tenemos una tabla llamada 'users'.

    try:
        response = supabase.table("users").select("*").execute()
        return response.data  # La propiedad 'data' contiene las filas resultantes
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/user_id/{user_id}")
def get_user(user_id: int):
    try:
        # Realizamos una consulta filtrando por el campo "id"
        response = supabase.table("users").select("*").eq("id", user_id).execute()
        user_data = response.data
        
        # Verificamos si se encontró el usuario
        if not user_data:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Retornamos el primer registro (se asume que 'id' es único)
        return user_data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/user/username/{username}")
def get_user(username: str):
    try:
        # Realizamos una consulta filtrando por el campo "id"
        response = supabase.table("users").select("*").eq("username", username).execute()
        user_data = response.data
        
        # Verificamos si se encontró el usuario
        if not user_data:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Retornamos el primer registro (se asume que 'id' es único)
        return user_data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


"""
CREAR USUARIO
"""
@router.post("/user/register")
def create_user(user: dict):

    password = user.get("password")

    # Encripta la contraseña con bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user["password"] = hashed_password.decode('utf-8')

    #Crea un usuario en la tabla 'users'.
    try:
        response = supabase.table("users").insert(user).execute()
        return {
            "message": "Usuario creado satisfactoriamente",
            "data": response.data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

"""
LOGIN Validar Usuario
"""
@router.post("/user/login")
def validate_user(credentials: dict):
    username = credentials.get("username")
    password = credentials.get("password")
    
    if not username or not password:
        raise HTTPException(status_code=400, detail="Se requieren 'username' y 'password'.")

    try:
        # Buscamos el usuario en la tabla "users" filtrando por el campo 'username'
        response = supabase.table("users").select("*").eq("username", username).execute()
        user_data = response.data
        
        if not user_data:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        user = user_data[0]
        stored_hashed_password = user.get("password")
        
        # Validar la contraseña utilizando bcrypt
        if not bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        
        return {"message": "Credenciales válidas", "user": user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))