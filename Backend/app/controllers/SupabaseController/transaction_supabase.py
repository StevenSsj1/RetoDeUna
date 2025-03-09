from supabase import create_client, Client
import os
from datetime import datetime

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

class SupabaseController:
    def __init__(self):
        self.client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def save_transaction(self, amount: float, detail: str, transaction_id: str, user_id: int):
        data = {
            "amount": amount,
            "detail": detail,
            "transaction_id": transaction_id,
            "user_id": user_id,
            "date": datetime.utcnow().isoformat()
        }
        response = self.client.table("transactions").insert(data).execute()
        return response

    def get_transactions_by_user(self, user_id: int):
        response = self.client.table("transactions").select("*").eq("user_id", user_id).execute()
        return response.data