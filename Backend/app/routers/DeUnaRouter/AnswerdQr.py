import requests as request
import pydantic
import os

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

def answerd_qr(data: AnswerdQrRequest):
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
        return response_data
    except Exception as e:
        raise Exception(str(e))
