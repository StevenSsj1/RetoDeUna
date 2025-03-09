from fastapi import FastAPI
from .routers import user  # Importamos el router de usuarios
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HackeMate DeUna", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],    # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],    # Permite todos los headers
)

app.include_router(user.router)