from sqlalchemy.orm import Session
from Schemas.ConvocatoriasSchema import ConvocatoriasActualizarSchema, ConvocatoriasCrearSchema
from Models.ConvocatoriasModelo import ConvocatoriasModelo
from fastapi import HTTPException, status
from Services.ProyectoServicio import buscarEmprendimiento
from datetime import date
from Utils.Mapeadorutilidades import auto_mapear
from Schemas.EstadosSchema import CambiarEstado
from typing import Final

ESTADO_ELIMINADO: Final = 6
ESTADO_ACTIVO: Final = 8

def crear_convocatoria(db: Session, convocatoria: ConvocatoriasCrearSchema):
    proyecto = buscarEmprendimiento(db, convocatoria.id_proyecto)
    
    if not proyecto or proyecto.id_estado != ESTADO_ELIMINADO:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El proyecto especificado no existe.")
    
    convocatoria_nueva = ConvocatoriasModelo(
        titulo_convocatoria = convocatoria.titulo_convocatoria,
        descripcion_convocatoria = convocatoria.descripcion_convocatoria,
        tipo_convocatoria = convocatoria.tipo_convocatoria,
        fecha_inicio = convocatoria.fecha_inicio,
        fecha_cierre = convocatoria.fecha_cierre,
        estado_convocatoria = convocatoria.estado_convocatoria,
        id_proyecto = convocatoria.id_proyecto,
        fecha_registro = date.today(),
        url_convocatoria = convocatoria.url_convocatoria,
        id_estado = ESTADO_ACTIVO
    )
    
    db.add(convocatoria_nueva)
    db.commit()
    db.refresh(convocatoria_nueva)
    return convocatoria_nueva

def buscar_convocatoria_titulo(db: Session, titulo_convocatoria: str):
    existente = db.query(ConvocatoriasModelo).filter(
        ConvocatoriasModelo.titulo_convocatoria == titulo_convocatoria,
        ConvocatoriasModelo.id_estado != ESTADO_ELIMINADO
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La convocatoria especificada no existe.")
    
    return existente

def buscar_convocatoria(db: Session, id_convocatoria: int):
    existente = db.query(ConvocatoriasModelo).filter(
        ConvocatoriasModelo.id_convocatoria == id_convocatoria,
        ConvocatoriasModelo.id_estado != ESTADO_ELIMINADO
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La convocatoria especificada no existe.")
    
    return existente

def listar_convocatorias_por_tipo(db:Session, tipo_convocatoria: str):
    existentes = db.query(ConvocatoriasModelo).filter(
        ConvocatoriasModelo.tipo_convocatoria == tipo_convocatoria,
        ConvocatoriasModelo.id_estado != ESTADO_ELIMINADO
    ).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen convocatorias.")
    
    return existentes

def listar_convocatorias_por_estado(db:Session, estado_convocatoria: str):
    existentes = db.query(ConvocatoriasModelo).filter(
        ConvocatoriasModelo.estado_convocatoria == estado_convocatoria,
        ConvocatoriasModelo.id_estado != ESTADO_ELIMINADO
    ).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen convocatorias.")
    
    return existentes

def actualizar_convocatoria(db: Session, id_convocatoria: int, convocatoria: ConvocatoriasActualizarSchema):
    existente = buscar_convocatoria(db, id_convocatoria)
    
    auto_mapear(existente, convocatoria, excluir=["id_convocatoria", "id_estado"])
    
    db.commit()
    db.refresh(existente)
    return existente

def eliminar_convocatoria(db: Session, id_convocatoria: int):
    existente = buscar_convocatoria(db, id_convocatoria)

    existente.id_estado = ESTADO_ELIMINADO
    
    db.commit()
    db.refresh(existente)
    return {"detail": "Participacion evento eliminado"}


def cambiar_estado(db: Session, id_convocatoria: int, estado: CambiarEstado):
    existente = db.query(ConvocatoriasModelo).filter(
        ConvocatoriasModelo.id_convocatoria == id_convocatoria
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La convocatoria especificada no existe.")
    
    existente.id_estado = estado.id_estado_cambiar
    
    db.commit()
    db.refresh(existente)
    return existente