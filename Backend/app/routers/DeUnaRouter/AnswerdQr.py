import requests as request
import pydantic
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

DE_UNA_QR = os.getenv("ANSWER_QR")
API_SECRET = os.getenv("API_SECRET")
API_KEY = os.getenv("API_KEY")

class AnswerdQrRequest(pydantic.BaseModel):
    idTransacionReference: str

class AnswerdQrResponse(pydantic.BaseModel):
    status: str
    internalTransactionReference: str
    amount: int 
    transactionId: str
    transferNumber: str
    date: str
    branchId: str
    posId: str
    currency: str
    description: str
    ordererName: str
    ordererIdentification: str

def answerd_qr(data: AnswerdQrRequest) -> AnswerdQrResponse:
    try:
        headers = {
            "x-api-secret": API_SECRET,
            "x-api-key": API_KEY
        }
        payload = {
            "idTransacionReference": data.idTransacionReference,
            "idType": "0"  # Valor predeterminado
        }
        response = request.post(DE_UNA_QR, json=payload, headers=headers)
        response_data = response.json()
        return AnswerdQrResponse(**response_data)
    except Exception as e:
        raise Exception(str(e))
