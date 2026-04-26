from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Eventoschema import EventoCrearSchema, EventoRespuestaSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.EventoControlador import crear_evento_controlador, buscar_evento_controlador, buscar_evento_por_fechas_controlador, buscar_evento_por_nombre_controlador, buscar_evento_por_lugar_controlador, eliminar_evento_controlador, actualizar_evento_controlador

router = APIRouter(
    prefix="/eventos",
    tags=["Eventos"],
)


@router.post("/", response_model=EventoRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_evento(
    datos: EventoCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    if usuario_actual.id_rol != 1: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acceso denegado")
    evento = crear_evento_controlador(db, datos)
    if not evento:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return evento

