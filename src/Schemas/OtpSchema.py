from pydantic import BaseModel, EmailStr

class EnviarOTPSchema(BaseModel):
    correo: EmailStr

class VerificarOTPSchema(BaseModel):
    correo: EmailStr
    token: str