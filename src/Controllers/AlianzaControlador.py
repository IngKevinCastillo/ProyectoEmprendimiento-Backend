from sqlalchemy.orm import Session
from Services.AlianzaServicio import crear_alianza, listar_alianzas, buscar_alianza, actualizar_alianza
from Schemas.AlianzaSchema import AlianzaCrearSchema, AlianzaActualizarSchema

def crear_alianza_controlador(db: Session, alianza: AlianzaCrearSchema):
    return crear_alianza(db, alianza)

def listar_alianzas_controlador(db: Session):
    return listar_alianzas(db)

def buscar_alianza_controlador(db: Session, id_alianza: str):
    return buscar_alianza(db, int(id_alianza))

def actualizar_alianza_controlador(db: Session, id_alianza: str, alianza: AlianzaActualizarSchema):
    return actualizar_alianza(db, id_alianza, alianza)