from ...controllers.SupabaseController import transaction_supabase
from ...controllers.AnalysisController import analysis_data_month
from fastapi import APIRouter, HTTPException, Query

# Crear un router de FastAPI
router = APIRouter(
    prefix="/hackemate",      # Prefijo del endpoint, por ejemplo /users/
    tags=["Transactions"]        # Etiqueta para la documentación
)

@router.get("/user_transactions/{user_id}")
def get_user_transactions(user_id: int, format: str = Query("month", enum=["month", "date"])):
    supabase_controller = transaction_supabase.SupabaseController()
    transactions = supabase_controller.get_transactions_by_user(user_id)

    analysis_controller = analysis_data_month.AnalysisController(transactions)
    chart_data = analysis_controller.analyze_transactions(format=format)
    
    return chart_data

@router.get("/user_transactions_by_amount/{user_id}")
def get_user_transactions_by_amount(user_id: int):
    supabase_controller = transaction_supabase.SupabaseController()
    transactions = supabase_controller.get_transactions_by_user(user_id)
    
    analysis_controller = analysis_data_month.AnalysisController(transactions)
    chart_data = analysis_controller.analyze_transactions_by_amount()
    
    return chart_data