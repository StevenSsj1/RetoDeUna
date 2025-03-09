from supabase import create_client, Client
import os
from datetime import datetime
from datetime import timedelta

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

class UserGoalsController:
    def __init__(self):
        self.client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def update_user_goals(self, user_id: int, goal: float, frecuency_goal: str, date_goal: str = None):
        
        if date_goal is None:
            date_goal = datetime.utcnow().isoformat()
        
        data = {
            "goal": goal,
            "goal_frecuency": frecuency_goal,
            "date_goal": date_goal
        }
        response = self.client.table("users").update(data).eq("id", user_id).execute()
        return response

    def check_goal_achieved(self, user_id: int):
        response = self.client.table("users").select("*").eq("id", user_id).execute()
        user_data = response.data[0]

        goal = user_data["goal"]
        goal_frecuency = user_data["goal_frecuency"]
        date_goal = datetime.fromisoformat(user_data["date_goal"])

        if goal_frecuency == "1d":
            deadline = date_goal + timedelta(days=1)
        elif goal_frecuency == "1m":
            deadline = date_goal + timedelta(days=30)
        elif goal_frecuency == "1a":
            deadline = date_goal + timedelta(days=365)
        else:
            raise ValueError("Invalid goal_frecuency. Use '1d', '1m', or '1a'.")

        current_date = datetime.utcnow()
        if current_date < deadline:
            return {"goal_status": "pendiente", "message": "Meta en progreso."}
        elif current_date >= deadline and user_data["progress"] >= goal:
            return {"goal_status": "cumplido", "message": "Meta cumplida."}
        else:
            return {"goal_status": "no cumplido", "message": "Meta no cumplida."}