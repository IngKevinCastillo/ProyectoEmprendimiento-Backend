from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Schemas.Usuarioschema import (
    UsuarioCrearSchema,
    UsuarioRespuestaSchema,
    LoginSchema,
    UsuarioActualizarSchema,
    UsuarioCambiarContrasena
)
from Schemas.Autenticacionschema import Token
from Schemas.UsuarioProyectoSchema import UsuarioProyectoRespuestaSchema

from Configs.bd import get_db

from Controllers.UsuarioControlador import (
    ObtenerUsuariosControlador,
    ActualizarUsuarioControlador,
    EliminarUsuarioControlador,
    EmprendimientosUsuarioControlador,
    BuscarUsuarioControlador
)

from Controllers.AutenticacionControlador import (
    CrearUsuarioControlador,
    IniciarSesionControlador,
    CambiarContrasena
)

from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
)

@router.get("/buscar-usuario/{id_usuario}", response_model=UsuarioRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_usuario(
    id_usuario: int,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual)
):
    usuario = BuscarUsuarioControlador(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario especificado no existe.")
    return usuario


@router.post("/", response_model=UsuarioRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_usuario(
    datos: UsuarioCrearSchema, 
    db: Session = Depends(get_db)
):
    usuario = CrearUsuarioControlador(db, datos)
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
    token = IniciarSesionControlador(db, datos)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return token


@router.get("/", response_model=list[UsuarioRespuestaSchema])
async def listar_usuarios(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return ObtenerUsuariosControlador(db)


@router.put("/cambiarcontrasena", response_model=UsuarioRespuestaSchema)
async def cambiar_contrasena(
    datos: UsuarioCambiarContrasena,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    nuevo_valor = CambiarContrasena(
        db,
        usuario_actual.id_usuario,
        datos.contasena_anterior,
        datos.contrasena_nueva
    )
    if not nuevo_valor:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error al cambiar la contraseña")
    return nuevo_valor


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
    eliminado = EliminarUsuarioControlador(db, usuario_actual.id_usuario)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return eliminado