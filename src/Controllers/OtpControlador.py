from sqlalchemy.orm import Session
from Services.OtpServicio import enviar_otp_servicio, verificar_otp_servicio

async def enviar_otp_controlador(correo: str, db: Session):
    return await enviar_otp_servicio(correo, db)

def verificar_otp_controlador(correo: str, codigo: str, db: Session):
    return verificar_otp_servicio(correo, codigo, db)