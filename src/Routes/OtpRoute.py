from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Schemas.OtpSchema import OTPEnviarSchema, OTPVerificarSchema
from Controllers.OtpControlador import enviar_otp_controlador, verificar_otp_controlador

router = APIRouter(
    prefix="/otp",
    tags=["OTP"],
)

@router.post("/enviar", status_code=status.HTTP_200_OK)
async def enviar_otp(
    datos: OTPEnviarSchema,
    db: Session = Depends(get_db)
):
    return await enviar_otp_controlador(datos.correo, db)

@router.post("/verificar", status_code=status.HTTP_200_OK)
def verificar_otp(
    datos: OTPVerificarSchema,
    db: Session = Depends(get_db)
):
    return verificar_otp_controlador(datos.correo, datos.codigo, db)