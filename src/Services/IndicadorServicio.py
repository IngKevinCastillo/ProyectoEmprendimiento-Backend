from sqlalchemy.orm import Session
from fastapi import HTTPException
from Schemas.IndicadorSchema import IndicadorCrearSchema, IndicadorActualizarSchema
from Models.IndicadorModelo import IndicadorModelo
from Utils.Mapeadorutilidades import auto_mapear

def buscarIndicador(db: Session, id: str):
    return db.query(IndicadorModelo).filter(IndicadorModelo.id_indicador == int(id)).first()

def buscarIndicadorPorNombre(db: Session, nombre: str):
    return db.query(IndicadorModelo).filter(IndicadorModelo.nombre_indicador == nombre).first()

def obtenerIndicadores(db: Session):
    return db.query(IndicadorModelo).all()

def obtenerIndicadoresPorProyecto(db: Session, id_proyecto: str):
    return db.query(IndicadorModelo).filter(IndicadorModelo.id_proyecto == int(id_proyecto)).all()

def crearIndicador(db: Session, indicador: IndicadorCrearSchema):
    existente = buscarIndicadorPorNombre(db, indicador.nombre_indicador)

    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un indicador con ese nombre")
    
    nuevo_indicador = IndicadorModelo(
        nombre_indicador=indicador.nombre_indicador,
        formula=indicador.formula,
        meta=indicador.meta,
        valor_actual=indicador.valor_actual,
        id_proyecto=indicador.id_proyecto
    )
    db.add(nuevo_indicador)
    db.commit()
    db.refresh(nuevo_indicador)
    return nuevo_indicador

def eliminarIndicador(db: Session, id: int):
    indicador = buscarIndicador(db, id)
    if not indicador:
        raise HTTPException(status_code=404, detail="No se encontró el indicador")

    db.delete(indicador)
    db.commit()
    return {"detail": "Indicador eliminado"}

def actualizarIndicador(db: Session, indicador: IndicadorActualizarSchema, id_indicador: str):
    existente = buscarIndicador(db, int(id_indicador))

    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró el indicador")
    
    if existente.id_proyecto is None:
        raise HTTPException(status_code=400, detail="El indicador debe estar asociado a un proyecto")
    
    auto_mapear(existente, indicador, excluir=["id_indicador"])

    db.commit()
    db.refresh(existente)
    return existente