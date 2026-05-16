from fastapi import APIRouter, HTTPException, status
from Schemas.OtpSchema import EnviarOTPSchema, VerificarOTPSchema
from Controllers.OtpControlador import EnviarOTPControlador, VerificarOTPControlador

router = APIRouter(prefix="/otp", tags=["OTP"])

@router.post("/enviar-otp", status_code=status.HTTP_200_OK)
async def enviar_otp(datos: EnviarOTPSchema):
    try:
        EnviarOTPControlador(datos.correo)
        return {"mensaje": "Código enviado al correo"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/verificar-otp", status_code=status.HTTP_200_OK)
async def verificar_otp(datos: VerificarOTPSchema):
    verificado = VerificarOTPControlador(datos.correo, datos.token)
    return {"verificado": verificado}