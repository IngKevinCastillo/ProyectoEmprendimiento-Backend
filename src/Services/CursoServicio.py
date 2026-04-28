from sqlalchemy.orm import Session
from fastapi import HTTPException
from Utils.Mapeadorutilidades import auto_mapear
from Models.CursoModelo import CursoModelo
from Schemas.CursoSchema import CursoCrearSchema, CursoActualizarSchema

def buscar_curso(db: Session, id_curso: str):
    return db.query(CursoModelo).filter(CursoModelo.id_curso == int(id_curso)).first()

def buscar_curso_por_nombre_curso(db: Session, nombre: str):
    return db.query(CursoModelo).filter(CursoModelo.nombre_curso == nombre).first()

def crear_curso(db: Session, curso: CursoCrearSchema):
    existrente = buscar_curso_por_nombre_curso(db, curso.nombre_curso)
    if existrente:
        raise HTTPException(status_code=400, detail="Ya existe un curso con ese nombre")
    nuevo_curso = CursoModelo(
        nombre_curso=curso.nombre_curso,
        descripcion=curso.descripcion,
        fecha_inicio=curso.fecha_inicio,
        fecha_fin=curso.fecha_fin
    )
    db.add(nuevo_curso)
    db.commit()
    db.refresh(nuevo_curso)
    return nuevo_curso

def listar_cursos(db: Session):
    return db.query(CursoModelo).all()

def eliminar_curso(db:Session, id_curso: str):
    existente = buscar_curso(db, int(id_curso))
    if not existente:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    db.delete(existente)
    db.commit()
    return {"message": "Curso eliminado correctamente"}

def actualizar_curso(db: Session, id_curso: str, curso_actualizado: CursoActualizarSchema):
    existente = buscar_curso(db, int(id_curso))
    if not existente:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    auto_mapear(existente, curso_actualizado, exclude={"id_curso"})
    db.commit()
    db.refresh(existente)
    return existente