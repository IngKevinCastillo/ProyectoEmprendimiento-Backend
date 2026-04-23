from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from Core.Configuracion import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def HashearContrasena(contraena: str) -> str:
    return pwd_context.hash(contraena)

def VerificarContrasena(contrasena_plana: str, contrasena_hasheada: str) -> bool:
    return pwd_context.verify(contrasena_plana, contrasena_hasheada)

def CrearTokenAcceso(datos: dict):
    a_codificar = datos.copy()

    expirar = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    a_codificar.update({"exp": expirar})

    jwt_codificado = jwt.encode(
        a_codificar,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return jwt_codificado