from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.TipoConvocatoriaModelo import TipoConvocatoriaModelo
from Schemas.TipoConvocatoriaSchema import TipoConvocatoriaCrearSchema, TipoConvocatoriaActualizarSchema

def ObtenerTiposConvocatoria(db: Session):
    return db.query(TipoConvocatoriaModelo).all()

def BuscarTipoConvocatoria(db: Session, id_tipo_convocatoria: int):
    return db.query(TipoConvocatoriaModelo).filter(
        TipoConvocatoriaModelo.id_tipo_convocatoria == id_tipo_convocatoria
    ).first()

def CrearTipoConvocatoria(db: Session, datos: TipoConvocatoriaCrearSchema):
    existe = db.query(TipoConvocatoriaModelo).filter(
        TipoConvocatoriaModelo.nombre == datos.nombre
    ).first()
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un tipo de convocatoria con ese nombre"
        )
    nuevo = TipoConvocatoriaModelo(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def ActualizarTipoConvocatoria(db: Session, id_tipo_convocatoria: int, datos: TipoConvocatoriaActualizarSchema):
    tipo = BuscarTipoConvocatoria(db, id_tipo_convocatoria)
    if not tipo:
        return None
    if datos.nombre:
        existe = db.query(TipoConvocatoriaModelo).filter(
            TipoConvocatoriaModelo.nombre == datos.nombre,
            TipoConvocatoriaModelo.id_tipo_convocatoria != id_tipo_convocatoria
        ).first()
        if existe:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un tipo de convocatoria con ese nombre"
            )
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(tipo, campo, valor)
    db.commit()
    db.refresh(tipo)
    return tipo

def EliminarTipoConvocatoria(db: Session, id_tipo_convocatoria: int):
    tipo = BuscarTipoConvocatoria(db, id_tipo_convocatoria)
    if not tipo:
        return None
    if tipo.convocatorias:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede eliminar un tipo de convocatoria que tiene convocatorias asociadas"
        )
    db.delete(tipo)
    db.commit()
    return True