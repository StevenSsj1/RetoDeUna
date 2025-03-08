import os
from supabase import create_client, Client
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Creamos el cliente de Supabase.
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)