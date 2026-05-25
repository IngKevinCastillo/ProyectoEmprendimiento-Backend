from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.BeneficioModelo import BeneficioModelo
from Schemas.BeneficioSchema import BeneficioCrearSchema, BeneficioActualizarSchema

def ObtenerBeneficios(db: Session):
    return db.query(BeneficioModelo).all()

def BuscarBeneficio(db: Session, id_beneficio: int):
    return db.query(BeneficioModelo).filter(
        BeneficioModelo.id_beneficio == id_beneficio
    ).first()

def CrearBeneficio(db: Session, datos: BeneficioCrearSchema):
    existe = db.query(BeneficioModelo).filter(
        BeneficioModelo.nombre == datos.nombre
    ).first()
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un beneficio con ese nombre"
        )
    nuevo = BeneficioModelo(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def ActualizarBeneficio(db: Session, id_beneficio: int, datos: BeneficioActualizarSchema):
    beneficio = BuscarBeneficio(db, id_beneficio)
    if not beneficio:
        return None
    if datos.nombre:
        existe = db.query(BeneficioModelo).filter(
            BeneficioModelo.nombre == datos.nombre,
            BeneficioModelo.id_beneficio != id_beneficio
        ).first()
        if existe:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un beneficio con ese nombre"
            )
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(beneficio, campo, valor)
    db.commit()
    db.refresh(beneficio)
    return beneficio

def EliminarBeneficio(db: Session, id_beneficio: int):
    beneficio = BuscarBeneficio(db, id_beneficio)
    if not beneficio:
        return None
    if beneficio.asignaciones:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede eliminar un beneficio que ya ha sido asignado"
        )
    db.delete(beneficio)
    db.commit()
    return True