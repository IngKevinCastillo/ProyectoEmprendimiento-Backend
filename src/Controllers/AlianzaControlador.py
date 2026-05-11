from sqlalchemy.orm import Session
from Services.AlianzaServicio import activar_alianza, crear_alianza, desactivar_alianza, listar_alianzas, buscar_alianza, actualizar_alianza
from Schemas.AlianzaSchema import AlianzaCrearSchema, AlianzaActualizarSchema

def crear_alianza_controlador(db: Session, alianza: AlianzaCrearSchema):
    return crear_alianza(db, alianza)

def listar_alianzas_controlador(db: Session, activo: bool | None = None):
    return listar_alianzas(db, activo)

def buscar_alianza_controlador(db: Session, id_alianza: str):
    return buscar_alianza(db, int(id_alianza))

def actualizar_alianza_controlador(db: Session, id_alianza: str, alianza: AlianzaActualizarSchema):
    return actualizar_alianza(db, id_alianza, alianza)

def activar_alianza_controlador(db: Session, id_alianza: str):
    return activar_alianza(db, int(id_alianza))

def desactivar_alianza_controlador(db: Session, id_alianza: str):
    return desactivar_alianza(db,int(id_alianza))