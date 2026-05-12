from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from Configs.bd import get_db
from Schemas.ParticipacionEventoSchema import ParticipacionActualizarSchema, ParticipacionEventoCrearSchema, ParticipacionEventoRespuestaSchema
from Controllers.ParticipacionEventoControlador import cambiar_estado_controlador, actualizar_participacion_evento_controlador, buscar_participacion_evento_controlador, buscar_usuario_participacion_evento_controlador, buscar_usuarios_participaciones_eventos_controlador, eliminar_participacion_proyecto_controlador, crear_participacion_evento_controlador, listar_participaciones_en_evento_controlador
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.EstadosSchema import CambiarEstado

router = APIRouter(
    prefix="/participacion-evento",
    tags=["Participacion Evento"],
)

@router.post("/", response_model=ParticipacionEventoCrearSchema, status_code=status.HTTP_201_CREATED)
async def crear_participacion_evento(
    datos: ParticipacionEventoCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual),
):
    participacion_evento = crear_participacion_evento_controlador(db, datos)
    if not participacion_evento:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controlador pendiente")
    return participacion_evento

@router.get("/participaciones/usuario/{id_usuario}", response_model=list[ParticipacionEventoRespuestaSchema], status_code=status.HTTP_200_OK)
async def obtener_usuarios_participaciones_eventos(
    id_usuario: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    participacion_evento = buscar_usuarios_participaciones_eventos_controlador(db, id_usuario)
    return participacion_evento

@router.get("/participaciones/evento/{id_evento}", response_model=list[ParticipacionEventoRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_participaciones_en_evento(
    id_evento: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    participacion_evento = listar_participaciones_en_evento_controlador(db, id_evento)
    return participacion_evento

@router.get("/usuario/{id_usuario}/{id_evento}", response_model=ParticipacionEventoRespuestaSchema, status_code=status.HTTP_200_OK)
async def obtener_usuario_participacion_evento(
    id_usuario: int,
    id_evento: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    participacion_evento = buscar_usuario_participacion_evento_controlador(db, id_usuario, id_evento)
    return participacion_evento

@router.get("/{id_participacion_evento}", response_model=ParticipacionEventoRespuestaSchema, status_code=status.HTTP_200_OK)
async def obtener_participacion_evento(
    id_participacion_evento: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    participacion_evento = buscar_participacion_evento_controlador(db, id_participacion_evento)
    return participacion_evento

@router.put("/cambiar-estado/{id_participacion_evento}", response_model=ParticipacionEventoRespuestaSchema, status_code=status.HTTP_200_OK)
async def cambiar_estado_participacion_evento(
    id_participacion_evento: int,
    datos: CambiarEstado,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    participacion_evento = cambiar_estado_controlador(db, id_participacion_evento, datos)
    return participacion_evento

@router.put("/{id_participacion_evento}", response_model=ParticipacionActualizarSchema, status_code=status.HTTP_200_OK)
async def actualizar_participacion_evento(
    id_participacion_evento: int,
    datos: ParticipacionActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    participacion_evento = actualizar_participacion_evento_controlador(db, id_participacion_evento, datos)
    return participacion_evento

@router.delete("/{id_participacion_evento}", status_code=status.HTTP_200_OK)
async def eliminar_participacion_evento(
    id_participacion_evento: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    participacion_evento = eliminar_participacion_proyecto_controlador(db, id_participacion_evento)
    return participacion_evento