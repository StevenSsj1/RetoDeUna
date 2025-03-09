from fastapi import APIRouter, HTTPException
from ..DeUnaRouter import GenerationQr, AnswerdQr

# Crear un router de FastAPI
router = APIRouter(
    prefix="/hackemate",      # Prefijo del endpoint, por ejemplo /users/
    tags=["Qr"]        # Etiqueta para la documentación
)

@router.post("/generate-qr", response_model=GenerationQr.GenerateQrResponse)
def generate_qr_endpoint(data: GenerationQr.GenerateQrRequest):
    try:
        return GenerationQr.generate_qr(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/answerd-qr", response_model=AnswerdQr.AnswerdQrResponse)
def answerd_qr_endpoint(data: AnswerdQr.AnswerdQrRequest):
    try:
        return AnswerdQr.answerd_qr(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))