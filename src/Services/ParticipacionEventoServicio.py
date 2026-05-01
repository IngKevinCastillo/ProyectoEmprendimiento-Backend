from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.ParticipacionEventoModelo import ParticipacionEventoModelo
from Schemas.ParticipacionEventoSchema import ParticipacionEventoCrearSchema, ParticipacionActualizarSchema
from Services.RolServicio import BuscarRol
from Services.EventoServicio import buscar_evento
from Services.UsuarioServicio import BuscarUsuario

def crear_participacion_evento(db: Session, participacion_evento: ParticipacionEventoCrearSchema):
    existente = 1
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