from fastapi import APIRouter

router = APIRouter(
    prefix="/users",      # Prefijo del endpoint, por ejemplo /users/
    tags=["Users"]        # Etiqueta para la documentación
)

@router.get("/")
def get_users():
    """
    Retorna la lista de usuarios.
    """
    return [{"id": 1, "name": "Juan"}, {"id": 2, "name": "María"}]

@router.post("/")
def create_user(user: dict):
    """
    Crea un usuario. Como ejemplo, recibe un diccionario con los datos.
    """
    return {"message": "Usuario creado satisfactoriamente", "data": user}

"""
from fastapi import APIRouter, HTTPException
from ..supabase_client import supabase

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users():

    Retorna la lista de usuarios.
    Supongamos que en Supabase tenemos una tabla llamada 'users'.

    try:
        response = supabase.table("users").select("*").execute()
        return response.data  # La propiedad 'data' contiene las filas resultantes
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/")
def create_user(user: dict):

    Crea un usuario en la tabla 'users'.

    try:
        response = supabase.table("users").insert(user).execute()
        return {
            "message": "Usuario creado satisfactoriamente",
            "data": response.data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
"""