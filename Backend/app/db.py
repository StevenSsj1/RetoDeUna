# Ejemplo de un archivo para manejar la conexión a la base de datos
# Aquí podrías usar SQLAlchemy, Pydantic, etc.

# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# metadata = MetaData()
#
# # Ejemplo de conexión:
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
