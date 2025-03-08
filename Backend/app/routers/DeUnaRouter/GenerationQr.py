import requests as request
import pydantic
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

DE_UNA_QR = "https://apis-merchant.qa.deunalab.com/merchant/v1/payment/request"
API_SECRET = "70aa3a0caa6341f88b67ebb167ef7a50"
API_KEY = "9fd4ac9c11b6455fa7270dba42a135ff"

class GenerateQrRequest(pydantic.BaseModel):
    qrType: str
    amount: float
    detail: str


class GenerateQrResponse(pydantic.BaseModel):
    transactionId: str
    status: int
    qr: str


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
        return response_data
    except Exception as e:
        raise Exception(str(e))