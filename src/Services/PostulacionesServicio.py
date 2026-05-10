from sqlalchemy import exists
from sqlalchemy.orm import Session
from fastapi import HTTPException
from Schemas.PostulacionesSchema import PostulacionesCrearSchema, PostulacionesActualizarSchema
from Models.PostulacionesModelo import PostulacionesModelo
from Utils.Mapeadorutilidades import auto_mapear

def buscarPostulacion(db: Session, id_postulacion: str):
    return db.query(PostulacionesModelo).filter(PostulacionesModelo.id_postulacion == int(id_postulacion)).first()

def obtenerPostulacionesPorConvocatoria(db: Session, id_convocatoria: str):
    return db.query(PostulacionesModelo).filter(PostulacionesModelo.id_convocatoria == int(id_convocatoria)).all()

def obtenerPostulacionesPorProyecto(db: Session, id_proyecto: str):
    return db.query(PostulacionesModelo).filter(PostulacionesModelo.id_proyecto == int(id_proyecto)).all()

def obtenerPostulacionesPorPlanNegocio(db: Session, id_plan_negocio: str):
    return db.query(PostulacionesModelo).filter(PostulacionesModelo.id_plan_negocio == int(id_plan_negocio)).all()

def obtenerPostulaciones(db: Session):
    return db.query(PostulacionesModelo).all()