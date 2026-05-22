from sqlalchemy.orm import Session
from Services.EscalaServicio import buscar_escala, buscar_escala_nombre, obtener_escalas

def obtener_escalas_controlador(db: Session):
    return obtener_escalas(db)

def buscar_escala_controlador(db: Session, escala_id: str):
    return buscar_escala(db, int(escala_id))

def buscar_escala_por_nombre_controlador(db: Session, nombre: str):
    return buscar_escala_nombre(db, nombre)