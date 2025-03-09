import requests as request
import pydantic
from dotenv import load_dotenv
import os
from ...controllers.SupabaseController import transaction_supabase
DE_UNA_QR = os.getenv("REQUEST_QR")
API_SECRET = os.getenv("API_SECRET")
API_KEY = os.getenv("API_KEY")

class GenerateQrRequest(pydantic.BaseModel):
    qrType: str
    amount: float
    detail: str
    user_id: int 


class GenerateQrResponse(pydantic.BaseModel):
    transactionId: str
    status: int
    qr: str
    deeplink: str


def generate_qr(data: GenerateQrRequest) -> GenerateQrResponse:
    try:
        headers = {
            "x-api-secret": API_SECRET,
            "x-api-key": API_KEY
        }
        payload = {
            "pointOfSale": "4121565",  # Valor predeterminado
            "qrType": data.qrType,
            "amount": data.amount,
            "detail": data.detail,
            "internalTransactionReference": "IXWAHROMYSCEZWQ",  # Valor predeterminado
            "format": "2"  # Valor predeterminado
        }
        response = request.post(DE_UNA_QR, json=payload, headers=headers)
        response_data = response.json()

        supabase_controller = transaction_supabase.SupabaseController()
        supabase_controller.save_transaction(data.amount, data.detail, response_data["transactionId"], data.user_id)

        return GenerateQrResponse(**response_data)
    except Exception as e:
        raise Exception(str(e))