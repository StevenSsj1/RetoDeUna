from fastapi import APIRouter, HTTPException
from ..DeUnaRouter import GenerationQr

# Crear un router de FastAPI
router = APIRouter(
    prefix="/hackemate",      # Prefijo del endpoint, por ejemplo /users/
    tags=["QR"]        # Etiqueta para la documentación
)

@router.post("/generate-qr")
def generate_qr_endpoint(data: GenerationQr.GenerateQrRequest):
    try:
        return GenerationQr.generate_qr(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))