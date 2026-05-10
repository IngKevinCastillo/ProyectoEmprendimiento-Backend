from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.EstadoProyectoSchema import EstadoProyectoRespuestaSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.EstadoProyectoControlador import (
    obtener_estados_proyectos_controlador,
    buscar_estado_proyecto_controlador,
    obtener_estados_proyectos_por_nombre_controlador,
)

router = APIRouter(
    prefix="/estados-proyecto",
    tags=["Estados Proyecto"],
)


@router.get("/", response_model=list[EstadoProyectoRespuestaSchema])
async def listar_estados_proyecto(db: Session = Depends(get_db)):
    return obtener_estados_proyectos_controlador(db)


@router.get("/nombre/{nombre}", response_model=EstadoProyectoRespuestaSchema)
async def obtener_estado_proyecto_por_nombre(
    nombre: str,
    db: Session = Depends(get_db)
):
    estado = obtener_estados_proyectos_por_nombre_controlador(db, nombre)
    if not estado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado de proyecto no encontrado")
    return estado


@router.get("/{id_estado_proyecto}", response_model=EstadoProyectoRespuestaSchema)
async def obtener_estado_proyecto(
    id_estado_proyecto: str,
    db: Session = Depends(get_db)
):
    estado = buscar_estado_proyecto_controlador(db, id_estado_proyecto)
    if not estado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado de proyecto no encontrado")
    return estado