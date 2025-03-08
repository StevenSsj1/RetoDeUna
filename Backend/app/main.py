from fastapi import FastAPI
from .routers import user  # Importamos el router de usuarios

app = FastAPI(title="My FastAPI App", version="1.0.0")

# Incluir routers (agrupaciones de endpoints)
app.include_router(user.router)

# Endpoint de prueba
@app.get("/")
def read_root():
    return {"Hello": "World"}
