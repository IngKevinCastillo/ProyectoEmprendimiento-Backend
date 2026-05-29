from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.ParticipacionEventoModelo import ParticipacionEventoModelo
from Schemas.ParticipacionEventoSchema import ParticipacionEventoCrearSchema, ParticipacionActualizarSchema
from Services.RolServicio import BuscarRol
from Services.EventoServicio import buscar_evento
from Services.UsuarioServicio import buscar_usuario
from Utils.Mapeadorutilidades import auto_mapear
from Schemas.EstadosSchema import CambiarEstado
from typing import Final

ESTADO_ELIMINADO: Final = 6
ESTADO_INSCRITO: Final = 25
CONFIRMAR_ESTADO: Final = 26

def crear_participacion_evento(db: Session, participacion_evento: ParticipacionEventoCrearSchema):
    existente = db.query(ParticipacionEventoModelo).filter(
        ParticipacionEventoModelo.id_usuario == participacion_evento.id_usuario,
        ParticipacionEventoModelo.id_evento == participacion_evento.id_evento,
        ParticipacionEventoModelo.id_estado != ESTADO_ELIMINADO
    ).first()
    
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya participa en este evento.")        
    
    if not BuscarRol(db, participacion_evento.id_rol):
        raise HTTPException(status_code=400, detail="El rol especificado no existe")
    
    if not buscar_evento(db, participacion_evento.id_evento):
        raise HTTPException(status_code=400, detail="El evento especificado no existe")
    
    if not buscar_usuario(db, participacion_evento.id_usuario):
        raise HTTPException(status_code=400, detail="El usuario especificado no existe")
    
    nuevo_registro = ParticipacionEventoModelo(
        id_usuario=participacion_evento.id_usuario,
        id_evento=participacion_evento.id_evento,
        id_rol=participacion_evento.id_rol,
        id_estado=ESTADO_INSCRITO
    )
    
    db.add(nuevo_registro)
    db.commit()
    db.refresh(nuevo_registro)
    return nuevo_registro

def buscar_participacion_evento(db: Session, id_participacion_evento: int):
    existente = db.query(ParticipacionEventoModelo).filter(
        ParticipacionEventoModelo.id_participacion_evento == id_participacion_evento,
        ParticipacionEventoModelo.id_estado != ESTADO_ELIMINADO
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La participacion evento no existe.")
    
    return existente

def buscar_usuario_participacion_evento(db: Session, id_usuario: int, id_evento: int):
    existente = db.query(ParticipacionEventoModelo).filter(
        ParticipacionEventoModelo.id_usuario == id_usuario,
        ParticipacionEventoModelo.id_evento == id_evento,
        ParticipacionEventoModelo.id_estado != ESTADO_ELIMINADO
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La participacion evento no existe.")
    
    return existente
    
def buscar_usuario_participaciones_eventos(db: Session, id_usuario: int):
    existentes = db.query(ParticipacionEventoModelo).filter(
        ParticipacionEventoModelo.id_usuario == id_usuario, 
        ParticipacionEventoModelo.id_estado != ESTADO_ELIMINADO
    ).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen participaciones eventos.")
    
    return existentes

def listar_participaciones_en_evento(db: Session, id_evento: int):
    existentes = db.query(ParticipacionEventoModelo).filter(
        ParticipacionEventoModelo.id_evento == id_evento,
        ParticipacionEventoModelo.id_estado != ESTADO_ELIMINADO
    ).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen participaciones eventos.")
    
    return existentes

def listar_asistencia_evento(db: Session, id_evento: int):
    existentes = db.query(ParticipacionEventoModelo).filter(
        ParticipacionEventoModelo.id_evento == id_evento,
        ParticipacionEventoModelo.id_estado == CONFIRMAR_ESTADO
    ).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay asistencias registradas en el evento.")
    
    return existentes

def actualizar_participacion_evento(db: Session, id_participacion_evento: int, participacion_evento: ParticipacionActualizarSchema):
    existente = buscar_participacion_evento(db, id_participacion_evento)
    
    auto_mapear(existente,participacion_evento, excluir=["id_participacion_evento", "id_estado"])
    
    db.commit()
    db.refresh(existente)
    return existente

def eliminar_participacion_proyecto(db: Session, id_participacion_evento: int):
    existente = buscar_participacion_evento(db, id_participacion_evento)
    
    existente.id_estado = ESTADO_ELIMINADO
    
    db.commit()
    db.refresh(existente)
    return {"detail": "Participacion evento eliminado"}

def confirmar_asistencia(db: Session, id_usuario: int, id_evento: int):
    existente = buscar_usuario_participacion_evento(db, id_usuario, id_evento)
    existente.id_estado = CONFIRMAR_ESTADO
    
    db.commit()
    db.refresh(existente)
    return existente