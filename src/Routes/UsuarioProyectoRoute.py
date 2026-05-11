from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.UsuarioProyectoSchema import UsuarioProyectoCrearSchema, UsuarioProyectoRespuestaSchema, UsuarioProyectoActualizarSchema
from Controllers.UsuarioProyectoControlador import crear_usuario_proyecto_controlador, listar_usuarios_proyectos_controlador, buscar_usuario_proyecto_controlador, eliminar_usuario_proyecto_controlador, actualizar_usuario_proyecto_controlador, listar_usuarios_proyectos_por_proyecto_controlador, listar_proyectos_por_usuario_controlador, listar_proyectos_por_usuario_propietario_controlador, listar_proyectos_por_usuario_empleado_controlador

router = APIRouter(
    prefix="/usuario-proyecto",
    tags=["Usuario Proyecto"],
)

@router.post("/", response_model=UsuarioProyectoRespuestaSchema, status_code=status.HTTP_201_CREATED)
def crear_usuario_proyecto_endpoint(
    usuario_proyecto: UsuarioProyectoCrearSchema, 
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuario_proyecto_creado = crear_usuario_proyecto_controlador(db, usuario_proyecto)
    if not usuario_proyecto_creado:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return usuario_proyecto_creado

@router.get("/", response_model=list[UsuarioProyectoRespuestaSchema])
async def listar_usuarios_proyectos(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuarios_proyectos = listar_usuarios_proyectos_controlador(db)
    return usuarios_proyectos

@router.get("/proyecto/{id_proyecto}", response_model=list[UsuarioProyectoRespuestaSchema])
async def listar_usuarios_proyectos_por_proyecto(
    id_proyecto: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuarios_proyectos = listar_usuarios_proyectos_por_proyecto_controlador(db, id_proyecto)
    return usuarios_proyectos

@router.get("/usuario/{id_usuario}", response_model=list[UsuarioProyectoRespuestaSchema])
async def listar_proyectos_por_usuario(
    id_usuario: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    proyectos_usuario = listar_proyectos_por_usuario_controlador(db, id_usuario)
    return proyectos_usuario

@router.get("/usuario/propietario/{id_usuario}", response_model=list[UsuarioProyectoRespuestaSchema])
async def listar_proyectos_por_usuario_propietario(
    id_usuario: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    proyectos_propietario = listar_proyectos_por_usuario_propietario_controlador(db, id_usuario)
    return proyectos_propietario

@router.get("/usuario/empleado/{id_usuario}", response_model=list[UsuarioProyectoRespuestaSchema])
async def listar_proyectos_por_usuario_empleado(
    id_usuario: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    proyectos_empleado = listar_proyectos_por_usuario_empleado_controlador(db, id_usuario)
    return proyectos_empleado

@router.get("/{id_usuario_proyecto}", response_model=UsuarioProyectoRespuestaSchema)
async def obtener_usuario_proyecto(
    id_usuario_proyecto: str, 
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuario_proyecto = buscar_usuario_proyecto_controlador(db, id_usuario_proyecto)
    if not usuario_proyecto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="usuario proyecto no encontrado")
    return usuario_proyecto

@router.put("/{id_usuario_proyecto}", response_model=UsuarioProyectoRespuestaSchema)
async def actualizar_usuario_proyecto(
    id_usuario_proyecto: str,
    datos: UsuarioProyectoActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    usuario_proyecto = actualizar_usuario_proyecto_controlador(db, datos, id_usuario_proyecto)
    if not usuario_proyecto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario proyecto no encontrado")
    return usuario_proyecto


@router.delete("/{id_usuario_proyecto}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_usuario_proyecto(
    id_usuario_proyecto: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = eliminar_usuario_proyecto_controlador(db, id_usuario_proyecto)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario proyecto no encontrada")
    return eliminado
