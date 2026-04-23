from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from Core.Configuracion import settings , Settings
from Services.UsuarioServicio import BuscarUsuarioPorCorreo
from Configs.bd import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
esquema_oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login") #aqui pones la ruta de tu endpoint de login, por ejemplo "/auth/login"

def HashearContrasena(contraena: str) -> str:
    return pwd_context.hash(contraena)

def VerificarContrasena(contrasena_plana: str, contrasena_hasheada: str) -> bool:
    return pwd_context.verify(contrasena_plana, contrasena_hasheada)

def obtener_usuario_actual(
    token: str = Depends(esquema_oauth2),
    db: Session = Depends(get_db)
):
    try:
        payload    = jwt.decode(token, Settings.SECRET_KEY, algorithms=[Settings.ALGORITHM])
        usuario_id = int(payload.get("sub"))
    except (JWTError, TypeError):
        raise HTTPException(status_code=401, detail="Token inválido")

    usuario = BuscarUsuarioPorCorreo(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

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