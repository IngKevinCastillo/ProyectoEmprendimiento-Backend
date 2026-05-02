from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.ParticipacionEventoModelo import ParticipacionEventoModelo
from Schemas.ParticipacionEventoSchema import ParticipacionEventoCrearSchema, ParticipacionActualizarSchema
from Services.RolServicio import BuscarRol
from Services.EventoServicio import buscar_evento
from Services.UsuarioServicio import BuscarUsuario
from Utils.Mapeadorutilidades import auto_mapear

def crear_participacion_evento(db: Session, participacion_evento: ParticipacionEventoCrearSchema):
    existente = buscar_usuario_participacion_evento(db, participacion_evento.id_usuario, participacion_evento.id_evento)
    
    if existente:
        raise HTTPException(status_code=400, detail="El usuario ya pertenece al proyecto")
    
    if not BuscarRol(db, participacion_evento.Id_rol):
        raise HTTPException(status_code=400, detail="El rol especificado no existe")
    
    if not buscar_evento(db, participacion_evento.id_evento):
        raise HTTPException(status_code=400, detail="El evento especificado no existe")
    
    if not BuscarUsuario(db, participacion_evento.id_usuario):
        raise HTTPException(status_code=400, detail="El usuario especificado no existe")
    
    nuevo_registro = ParticipacionEventoModelo(
        id_usuario=participacion_evento.id_usuario,
        id_evento=participacion_evento.id_evento,
        Id_rol=participacion_evento.Id_rol,
    )
    
    db.add(nuevo_registro)
    db.commit()
    db.refresh(nuevo_registro)
    return nuevo_registro

def buscar_participacion_evento(db: Session, id_participacion_evento: int):
    return db.query(ParticipacionEventoModelo).filter(ParticipacionEventoModelo.id_participacion_evento == id_participacion_evento).first()

def buscar_usuario_participacion_evento(db: Session, id_usuario: int, id_evento: int):
    return db.query(ParticipacionEventoModelo).filter(
        ParticipacionEventoModelo.id_usuario == id_usuario,
        ParticipacionEventoModelo.id_evento == id_evento
    ).first()
    
def buscar_usuario_participaciones_eventos(db: Session, id_usuario: int):
    return db.query(ParticipacionEventoModelo).filter(ParticipacionEventoModelo.id_usuario == id_usuario).all()

def listar_participaciones_en_evento(db: Session, id_evento: int):
    return db.query(ParticipacionEventoModelo).filter(ParticipacionEventoModelo.id_evento == id_evento).all()

def actualizar_participacion_evento(db: Session, id_participacion_evento: int, participacion_evento: ParticipacionActualizarSchema):
    existente = buscar_participacion_evento(db, id_participacion_evento)
    
    if not existente:
        raise HTTPException(status_code=404, detail="El evento especificado no existe")
    
    auto_mapear(existente,participacion_evento, excluir=["id_participacion_evento"])
    
    db.commit()
    db.refresh(existente)
    return existente

def eliminar_participacion_proyecto(db: Session, id_participacion_evento: int):
    existente = buscar_participacion_evento(db, id_participacion_evento)
    
    if not existente:
        raise HTTPException(status_code=404, detail="El usuario especificado no existe")
    
    db.delete(existente)
    db.commit()
    return {"detail": "Participacion evento eliminado"}