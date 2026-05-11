from sqlalchemy.orm import Session
from Schemas.ConvocatoriasSchema import ConvocatoriasActualizarSchema, ConvocatoriasCrearSchema
from Models.ConvocatoriasModelo import ConvocatoriasModelo
from fastapi import HTTPException, status
from Services.ProyectoServicio import buscarEmprendimiento
from datetime import date
from Utils.Mapeadorutilidades import auto_mapear
eliminado = 6

def crear_convocatoria(db: Session, convocatoria: ConvocatoriasCrearSchema):
    existente = buscar_convocatoria_titulo(db, convocatoria.titulo_convocatoria)
    proyecto = buscarEmprendimiento(db, convocatoria.id_proyecto)
    
    if existente:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="La convocatoria especificada ya existe.")
    
    if not proyecto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El proyecto especificado no existe.")
    
    if not existente.id_estado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El estado especificado no existe.")
    
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
        id_estado = convocatoria.id_estado
    )
    
    db.add(convocatoria_nueva)
    db.commit()
    db.refresh(convocatoria_nueva)
    return convocatoria_nueva

def buscar_convocatoria_titulo(db: Session, titulo_convocatoria: str):
    return db.query(ConvocatoriasModelo).filter(ConvocatoriasModelo.titulo_convocatoria == titulo_convocatoria).first()

def buscar_convocatoria(db: Session, id_convocatoria: int):
    return db.query(ConvocatoriasModelo).filter(ConvocatoriasModelo.id_convocatoria == id_convocatoria).first()

def listar_convocatorias_por_tipo(db:Session, tipo_convocatoria: str):
    return db.query(ConvocatoriasModelo).filter(ConvocatoriasModelo.tipo_convocatoria == tipo_convocatoria).all()

def listar_convocatorias_por_estado(db:Session, estado_convocatoria: str):
    return db.query(ConvocatoriasModelo).filter(ConvocatoriasModelo.estado_convocatoria == estado_convocatoria).all()

def actualizar_convocatoria(db: Session, id_convocatoria: int, convocatoria: ConvocatoriasActualizarSchema):
    existente = buscar_convocatoria(db, id_convocatoria)
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La convocatoria especificada no existe.")
    
    auto_mapear(existente, convocatoria, excluir=["id_convocatoria"])
    
    db.commit()
    db.refresh(existente)
    return existente

def eliminar_convocatoria(db: Session, id_convocatoria: int):
    existente = buscar_convocatoria(db, id_convocatoria)
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La convocatoria especificada no existe.")
    
    if(existente.id_estado == eliminado):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La convocatoria no existe")

    existente.id_estado = eliminado
    
    db.commit()
    db.refresh(existente)
    return {"detail": "Participacion evento eliminado"}