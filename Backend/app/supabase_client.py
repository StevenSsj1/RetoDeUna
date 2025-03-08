import os
from supabase import create_client, Client

# Si usas python-dotenv para cargar variables, descomenta la siguiente línea:
# from dotenv import load_dotenv
# load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

# Creamos el cliente de Supabase.
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)