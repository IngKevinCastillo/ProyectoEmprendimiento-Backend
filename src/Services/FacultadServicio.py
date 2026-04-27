from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.FacultadModelo import FacultadModelo
from Schemas.Facultadschema import FacultadCrearSchema
from Utils.Mapeadorutilidades import auto_mapear

def BuscarFacultad(db: Session, id: str):
    return db.query(FacultadModelo).filter(FacultadModelo.id_facultad == int(id)).first()

def BuscarFacultadPorNombre(db: Session, nombre: str):
    return db.query(FacultadModelo).filter(FacultadModelo.nombre == nombre).first()

def ObtenerFacultades(db: Session):
    return db.query(FacultadModelo).all()

def CrearFacultad(db: Session, facultad: FacultadCrearSchema):
    existente = BuscarFacultadPorNombre(db, facultad.nombre)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe una facultad con ese nombre")

    nueva_facultad = FacultadModelo(
        nombre=facultad.nombre,
        descripcion=facultad.descripcion,
        estado=facultad.estado
    )
    db.add(nueva_facultad)
    db.commit()
    db.refresh(nueva_facultad)
    return nueva_facultad

def EliminarFacultad(db: Session, id: str):
    existente = BuscarFacultad(db, int(id))
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró la facultad")
    
    db.delete(existente)
    db.commit()
    return {"detail": "Facultad eliminada"}

def ActualizarFacultad(db: Session, facultad: any, id_facultad: str):
    existente = BuscarFacultad(db, int(id_facultad))
    if not existente:
        raise HTTPException(status_code=404, detail="No se encontró la facultad")
    
    auto_mapear(existente, facultad, excluir=["id_facultad"])
    
    db.commit()
    db.refresh(existente)
    return existente