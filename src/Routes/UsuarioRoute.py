from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from Schemas.Usuarioschema import UsuarioCrearSchema, UsuarioRespuestaSchema, LoginSchema
from Configs.bd import get_db
from Core.Configuracion import settings

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
)

esquema_oauth2 = OAuth2PasswordBearer(tokenUrl="/usuarios/login")


def obtener_usuario_actual(
    token: str = Depends(esquema_oauth2),
    db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id_usuario = int(payload.get("sub"))
    except (JWTError, TypeError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

    usuario = None  # UsuarioController.obtener_por_id(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.post("/", response_model=UsuarioRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_usuario(datos: UsuarioCrearSchema, db: Session = Depends(get_db)):
    usuario = None  # UsuarioController.crear(db, datos)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return usuario


@router.get("/yo", response_model=UsuarioRespuestaSchema)
async def obtener_yo(usuario_actual=Depends(obtener_usuario_actual)):
    return usuario_actual


@router.post("/login")
async def login(datos: LoginSchema, db: Session = Depends(get_db)):
    token = None  # UsuarioController.login(db, datos)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return token


@router.get("/", response_model=list[UsuarioRespuestaSchema])
async def listar_usuarios(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuarios = []  # UsuarioController.listar_todos(db)
    return usuarios


@router.put("/yo", response_model=UsuarioRespuestaSchema)
async def actualizar_yo(
    datos: UsuarioCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuario = None  # UsuarioController.actualizar(db, usuario_actual.id_usuario, datos)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.delete("/yo", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_yo(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = None  # UsuarioController.eliminar(db, usuario_actual.id_usuario)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return eliminado