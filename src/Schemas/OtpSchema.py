from pydantic import BaseModel, EmailStr

class OTPEnviarSchema(BaseModel):
    correo: EmailStr

class OTPVerificarSchema(BaseModel):
    correo: EmailStr
    codigo: str