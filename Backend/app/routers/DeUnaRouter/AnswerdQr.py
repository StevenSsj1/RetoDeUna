import requests as request
import pydantic

DE_UNA_QR = "https://apis-merchant.qa.deunalab.com/merchant/v1/payment/info"
API_SECRET = "70aa3a0caa6341f88b67ebb167ef7a50"
API_KEY = "9fd4ac9c11b6455fa7270dba42a135ff"

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
