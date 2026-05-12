from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
eliminado = 6

from Schemas.Usuarioschema import (
    UsuarioCrearSchema,
    UsuarioRespuestaSchema,
    LoginSchema,
    UsuarioActualizarSchema,
    UsuarioCambiarContrasena
)

from Schemas.EstadosSchema import CambiarEstado
from Schemas.Autenticacionschema import Token
from Schemas.UsuarioProyectoSchema import UsuarioProyectoRespuestaSchema

from Configs.bd import get_db

from Controllers.UsuarioControlador import (
    ObtenerUsuariosControlador,
    ActualizarUsuarioIdControlador,
    ActualizarUsuarioDocumentoControlador,
    EliminarUsuarioControlador,
    BuscarUsuarioControlador,
    CambiarEstadoControlador,
    BuscarUsuarioPorDocumentoControlador,
    BuscarUsuarioPorCorreoControlador
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
    if not usuario or usuario.id_estado  == eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario especificado no existe.")
    return usuario

@router.get("/buscar-usuario-documento/{numero_documento}", response_model=UsuarioRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_usuario_por_documento(
    numero_documento: int,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual)
):
    usuario = BuscarUsuarioPorDocumentoControlador(db, numero_documento)
    if not usuario or usuario.id_estado  == eliminado:
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


@router.get("/yo", response_model=UsuarioRespuestaSchema)
async def obtener_mi_cuenta(usuario_actual=Depends(obtener_usuario_actual)):
    return usuario_actual


@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login(datos: LoginSchema, db: Session = Depends(get_db)):
    token = IniciarSesionControlador(db, datos)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    usuario = BuscarUsuarioPorCorreoControlador(db, datos.correo)
    if(usuario.id_estado == eliminado):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La cuenta no existe...por favor crea tu cuenta.")
    return token


@router.get("/", response_model=list[UsuarioRespuestaSchema])
async def listar_usuarios(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    existentes = ObtenerUsuariosControlador(db)
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen usuarios.")
    return existentes

@router.put("/cambiar-estado/{numero_documento}", response_model=UsuarioRespuestaSchema)
async def cambiar_estado(
    numero_documento: int,
    datos: CambiarEstado,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    
    nuevo_valor = CambiarEstadoControlador(db, numero_documento, datos)
    
    if not nuevo_valor:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error al cambiar el estado")
    return nuevo_valor


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
async def actualizar_mi_cuenta(
    datos: UsuarioActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuario = ActualizarUsuarioIdControlador(db, datos, usuario_actual.id_usuario)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario

@router.put("/actualizar-usuario/{numero_documento}", response_model=UsuarioRespuestaSchema)
async def actualizar_usuario(
    numero_documento: int,
    datos: UsuarioActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuario = ActualizarUsuarioDocumentoControlador(db, datos, numero_documento)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario

@router.delete("/yo", status_code=status.HTTP_200_OK)
async def eliminar_mi_cuenta(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = EliminarUsuarioControlador(db, usuario_actual.numero_documento)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return eliminado

@router.delete("/eliminar-usuario/{numero_documento}", status_code=status.HTTP_200_OK)
async def eliminar_usuario(
    numero_documento: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    eliminado = EliminarUsuarioControlador(db, numero_documento)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return eliminado