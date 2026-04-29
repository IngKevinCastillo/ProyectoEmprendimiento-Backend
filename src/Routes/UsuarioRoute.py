from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from Schemas.Usuarioschema import UsuarioCrearSchema, UsuarioRespuestaSchema, LoginSchema
from Schemas.Autenticacionschema import Token
from Configs.bd import get_db
from Core.Configuracion import settings
from Controllers.UsuarioControlador import BuscarUsuarioControlador, ObtenerUsuariosControlador, ActualizarUsuarioControlador, EliminarUsuarioControlador, BuscarUsuarioPorDocumentoControlador, EmprendimientosUsuarioControlador
from Controllers.AutenticacionControlador import CrearUsuarioControlador, IniciarSesionControlador
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.UsuarioProyectoSchema import UsuarioProyectoRespuestaSchema
from Schemas.Usuarioschema import UsuarioActualizarSchema

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
)

@router.post("/", response_model=UsuarioRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_usuario(
    datos: UsuarioCrearSchema, 
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    usuario = CrearUsuarioControlador(db,datos)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return usuario

@router.get("/emprendimientos", response_model=list[UsuarioProyectoRespuestaSchema])
async def obtener_emprendimientos_usuario(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return EmprendimientosUsuarioControlador(db, usuario_actual.id_usuario)

@router.get("/yo", response_model=UsuarioRespuestaSchema)
async def obtener_yo(usuario_actual=Depends(obtener_usuario_actual)):
    return usuario_actual


@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login(datos: LoginSchema, db: Session = Depends(get_db)):
    token = IniciarSesionControlador(db,datos)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return token


@router.get("/", response_model=list[UsuarioRespuestaSchema])
async def listar_usuarios(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    usuarios = ObtenerUsuariosControlador(db)
    return usuarios


@router.put("/yo", response_model=UsuarioRespuestaSchema)
async def actualizar_yo(
    datos: UsuarioActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuario = ActualizarUsuarioControlador(db, datos, usuario_actual.id_usuario)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.delete("/yo", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_yo(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = EliminarUsuarioControlador(db,usuario_actual.id_usuario)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return eliminado