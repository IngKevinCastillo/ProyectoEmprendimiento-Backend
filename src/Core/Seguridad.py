from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Security
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from Core.Configuracion import settings , Settings
from Services.UsuarioServicio import buscar_usuario_por_correo
from Configs.bd import get_db
from Controllers.UsuarioControlador import BuscarUsuarioControlador
from fastapi import status
from typing import Final

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

esquema_oauth2 = HTTPBearer()
USUARIO_ADMIN: Final = 2

def HashearContrasena(contrasena: str) -> str:
    return pwd_context.hash(contrasena)

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

    usuario = buscar_usuario_por_correo(db, usuario_id)
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

def obtener_usuario_actual(
    credentials: HTTPAuthorizationCredentials = Security(esquema_oauth2),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id_usuario = int(payload.get("sub"))
    except (JWTError, TypeError):
        raise HTTPException(status_code=401, detail="Token inválido")

    usuario = BuscarUsuarioControlador(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


def verificar_usuario_admin(usuario_actual):
    if usuario_actual.id_rol != USUARIO_ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acceso denegado")
