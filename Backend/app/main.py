from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.user_endpoints import user  # Importamos el router de usuarios
from .routers.qr_endpoints import qr
from .routers.transactions_endpoints import transactions_count_month
from .routers.user_goal import businessman_goals

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

app.include_router(user.router)
app.include_router(qr.router)
app.include_router(transactions_count_month.router)
app.include_router(businessman_goals.router)