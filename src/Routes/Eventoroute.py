from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from Schemas.Eventoschema import EventoCrearSchema, EventoRespuestaSchema, EventoActualizarSchema, ConsultarFechas
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from datetime import datetime
from Controllers.EventoControlador import cambiar_estado_controlador, buscar_evento_por_rango_fechas_controlador, buscar_eventos_por_estados, crear_evento_controlador, buscar_evento_controlador, buscar_evento_por_fecha_controlador, buscar_evento_por_nombre_controlador, buscar_evento_por_lugar_controlador, eliminar_evento_controlador, actualizar_evento_controlador, listar_eventos_controlador
from Schemas.EstadosSchema import CambiarEstado
from Controllers import StotageControlador
import json

router = APIRouter(
    prefix="/eventos",
    tags=["Eventos"],
)


@router.post("/", response_model=EventoRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_evento(
    datos: str = Form(...),
    foto: UploadFile = File(...),
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)

    try:
        evento_data = EventoCrearSchema(**json.loads(datos))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=f"Datos inválidos: {str(e)}")

    if foto:
        contenido = await foto.read()
        foto_url = StotageControlador.subir_foto_controlador(contenido, foto.filename)
        evento_data.foto_url = foto_url 
        
    evento = crear_evento_controlador(db, evento_data)
    if not evento:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return evento

@router.get("/", response_model=list[EventoRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_eventos(
    db: Session = Depends(get_db),
):
    eventos = listar_eventos_controlador(db)
    return eventos

@router.get("/estados/{id_estado}", response_model=list[EventoRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_eventos_por_estado(
    id_estado: int,
    db: Session = Depends(get_db),
):
    eventos = buscar_eventos_por_estados(db, id_estado)
    return eventos

@router.get("/{id_evento}", response_model=EventoRespuestaSchema, status_code=status.HTTP_200_OK)
async def obtener_evento(
    id_evento: int,
    db: Session = Depends(get_db),
):
    evento = buscar_evento_controlador(db, id_evento)
    return evento

@router.get("/fecha/{fecha}", response_model=list[EventoRespuestaSchema], status_code=status.HTTP_200_OK)
async def obtener_evento_fecha(
    fecha: datetime,
    db: Session = Depends(get_db),
):
    eventos = buscar_evento_por_fecha_controlador(db, fecha)
    return eventos

@router.get("/fechas}", response_model=list[EventoRespuestaSchema], status_code=status.HTTP_200_OK)
async def obtener_evento_fecha(
    datos: ConsultarFechas,
    db: Session = Depends(get_db),
):
    eventos = buscar_evento_por_rango_fechas_controlador(db, datos.fecha_inicio, datos.fecha_fin)
    return eventos

@router.get("/nombre/{nombre}", response_model=EventoRespuestaSchema, status_code=status.HTTP_200_OK)
async def obtener_evento_nombre(
    nombre: str,
    db: Session = Depends(get_db),
):
    evento = buscar_evento_por_nombre_controlador(db, nombre)
    return evento

@router.get("/lugar/{lugar}", response_model=list[EventoRespuestaSchema], status_code=status.HTTP_200_OK)
async def obtener_evento_lugar(
    lugar: str,
    db: Session = Depends(get_db),
):
    evento = buscar_evento_por_lugar_controlador(db, lugar)
    return evento

@router.put("/{id_evento}", response_model=EventoRespuestaSchema, status_code=status.HTTP_200_OK)
async def actualizar_evento(
    id_evento: int,
    datos: str = Form(...),
    foto: UploadFile = File(None),
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    
    try:
        evento_data =  EventoActualizarSchema(**json.loads(datos))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=f"Datos inválidos: {str(e)}")
    
    if foto:
        existente = buscar_evento_controlador(db, id_evento)
        contenido = await foto.read()
        
        if(existente.foto_url != None):
            StotageControlador.eliminar_foto_controlador(existente.foto_url)
            
        foto_url = StotageControlador.subir_foto_controlador(contenido, foto.filename)
        evento_data.foto_url = foto_url
    
    evento = actualizar_evento_controlador(db, id_evento , evento_data)
    return evento

@router.put("/cambiar-estado/{id_evento}", response_model=EventoRespuestaSchema, status_code=status.HTTP_200_OK)
async def cambiar_estado(
    id_evento: int,
    datos: CambiarEstado,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    evento = cambiar_estado_controlador(db, id_evento, datos)
    return evento


@router.delete("/{id_evento}", status_code=status.HTTP_200_OK)
async def eliminar_evento(
    id_evento: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    eliminado = eliminar_evento_controlador(db, id_evento)
    return eliminado