from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user  # Importamos el router de usuarios
from .routers.new_ import qr
app = FastAPI(title="HackeMate DeUna", version="1.0.0")

origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://localhost:8000",
    # Agrega aquí otros orígenes permitidos
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluir routers (agrupaciones de endpoints)
app.include_router(user.router)
app.include_router(qr.router)