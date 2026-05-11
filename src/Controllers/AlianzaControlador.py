from sqlalchemy.orm import Session
from Services.AlianzaServicio import cambiar_estado_alianza, crear_alianza, listar_alianzas, buscar_alianza, actualizar_alianza
from Schemas.AlianzaSchema import AlianzaCrearSchema, AlianzaActualizarSchema

def crear_alianza_controlador(db: Session, alianza: AlianzaCrearSchema):
    return crear_alianza(db, alianza)

def listar_alianzas_controlador(db: Session, activo: int | None = None):
    return listar_alianzas(db, activo)

def buscar_alianza_controlador(db: Session, id_alianza: str):
    return buscar_alianza(db, int(id_alianza))

def actualizar_alianza_controlador(db: Session, id_alianza: str, alianza: AlianzaActualizarSchema):
    return actualizar_alianza(db, int(id_alianza), alianza)

def cambiar_estado_alianza_controlador(db: Session, id_alianza: str, id_estado: int):
    return cambiar_estado_alianza(db, int(id_alianza), id_estado)
