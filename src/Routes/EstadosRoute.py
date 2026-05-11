from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.EstadosSchema import EstadosRespuestaSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.EstadosControlador import (
    obtener_estados_controlador,
    buscar_estados_controlador,
    obtener_estados_por_nombre_controlador,
)

router = APIRouter(
    prefix="/estados-proyecto",
    tags=["Estados Proyecto"],
)


@router.get("/", response_model=list[EstadosRespuestaSchema])
async def listar_estados(db: Session = Depends(get_db)):
    return obtener_estados_controlador(db)


@router.get("/nombre/{nombre}", response_model=EstadosRespuestaSchema)
async def obtener_estados_por_nombre(
    nombre: str,
    db: Session = Depends(get_db)
):
    estado = obtener_estados_por_nombre_controlador(db, nombre)
    if not estado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado no encontrado")
    return estado


@router.get("/{id_estado}", response_model=EstadosRespuestaSchema)
async def obtener_estado(
    id_estado: str,
    db: Session = Depends(get_db)
):
    estado = buscar_estados_controlador(db, id_estado)
    if not estado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado no encontrado")
    return estado