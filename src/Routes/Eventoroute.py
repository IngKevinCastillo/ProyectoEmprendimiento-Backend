from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Eventoschema import EventoCrearSchema, EventoRespuestaSchema, EventoActualizarSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from datetime import datetime
from Controllers.EventoControlador import buscar_eventos_por_estados, crear_evento_controlador, buscar_evento_controlador, buscar_evento_por_fechas_controlador, buscar_evento_por_nombre_controlador, buscar_evento_por_lugar_controlador, eliminar_evento_controlador, actualizar_evento_controlador, listar_eventos_controlador

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
    verificar_usuario_admin(usuario_actual)
    evento = crear_evento_controlador(db, datos)
    if not evento:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return evento

@router.get("/", response_model=list[EventoRespuestaSchema])
async def listar_eventos(
    db: Session = Depends(get_db),
):
    eventos = listar_eventos_controlador(db)
    return eventos

@router.get("/estados/{id_estado}", response_model=list[EventoRespuestaSchema])
async def listar_eventos_por_estado(
    id_estado: int,
    db: Session = Depends(get_db),
):
    eventos = buscar_eventos_por_estados(db, id_estado)
    return eventos

@router.get("/{id_evento}", response_model=EventoRespuestaSchema)
async def obtener_evento(
    id_evento: str,
    db: Session = Depends(get_db),
):
    evento = buscar_evento_controlador(db, id_evento)
    if not evento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento no encontrado")
    return evento

@router.get("/fecha/{fecha}", response_model=list[EventoRespuestaSchema])
async def obtener_evento_fecha(
    fecha: datetime,
    db: Session = Depends(get_db),
):
    evento = buscar_evento_por_fechas_controlador(db, fecha)
    if not evento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento no encontrado")
    return evento

@router.get("/nombre/{nombre}", response_model=EventoRespuestaSchema)
async def obtener_evento_nombre(
    nombre: str,
    db: Session = Depends(get_db),
):
    evento = buscar_evento_por_nombre_controlador(db, nombre)
    if not evento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento no encontrado")
    return evento

@router.get("/lugar/{lugar}", response_model=list[EventoRespuestaSchema])
async def obtener_evento_lugar(
    lugar: str,
    db: Session = Depends(get_db),
):
    evento = buscar_evento_por_lugar_controlador(db, lugar)
    if not evento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento no encontrado")
    return evento

@router.put("/{id_evento}", response_model=EventoRespuestaSchema)
async def actualizar_evento(
    id_evento: str,
    datos: EventoActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    evento = actualizar_evento_controlador(db, id_evento , datos)
    if not evento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento no encontrado")
    return evento


@router.delete("/{id_evento}", status_code=status.HTTP_200_OK)
async def eliminar_evento(
    id_evento: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    eliminado = eliminar_evento_controlador(db, id_evento)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento no encontrada")
    return eliminado