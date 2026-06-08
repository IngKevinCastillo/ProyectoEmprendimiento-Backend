from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Utils.Mapeadorutilidades import auto_mapear
from Models.CursoModelo import CursoModelo
from Schemas.EstadosSchema import CambiarEstado
from Schemas.CursoSchema import CursoCrearSchema, CursoActualizarSchema
from typing import Final

ESTADO_ELIMINADO: Final = 6
ESTADO_ACTIVO: Final = 8

def buscar_curso(db: Session, id_curso: int):
    existente = db.query(CursoModelo).filter(
        CursoModelo.id_curso == id_curso,
        CursoModelo.id_estado != ESTADO_ELIMINADO
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El curso especificado no existe.")
    
    return existente

def buscar_curso_por_nombre_curso(db: Session, nombre: str):
    existente = db.query(CursoModelo).filter(
        CursoModelo.nombre_curso == nombre,
        CursoModelo.id_estado != ESTADO_ELIMINADO
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El curso especificado no existe.")
    
    return existente

def crear_curso(db: Session, curso: CursoCrearSchema):
    
    nuevo_curso = CursoModelo(
        nombre_curso=curso.nombre_curso,
        descripcion=curso.descripcion,
        fecha_inicio=curso.fecha_inicio,
        fecha_fin=curso.fecha_fin,
        id_estado=ESTADO_ACTIVO,
        foto_url=curso.foto_url,
        horas=curso.horas
    )
    db.add(nuevo_curso)
    db.commit()
    db.refresh(nuevo_curso)
    return nuevo_curso

def listar_cursos(db: Session):
    existentes = db.query(CursoModelo).filter(
        CursoModelo.id_estado != ESTADO_ELIMINADO
    ).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen cursos.")
    
    return existentes

def eliminar_curso(db:Session, id_curso: int):
    existente = buscar_curso(db, id_curso)

    existente.id_estado = ESTADO_ELIMINADO

    db.commit()
    db.refresh(existente)
    return {"message": "Curso eliminado correctamente"}

def actualizar_curso(db: Session, id_curso: int, curso_actualizado: CursoActualizarSchema):
    existente = buscar_curso(db, id_curso)
    
    auto_mapear(existente, curso_actualizado, excluir={"id_curso", "id_estado"})
    
    db.commit()
    db.refresh(existente)
    return existente

def cambiar_estado(db: Session, id_curso: int, estado: CambiarEstado):
    existente = db.query(CursoModelo).filter(
        CursoModelo.id_curso == id_curso
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El curso especificado no existe.")
    
    existente.id_estado = estado.id_estado_cambiar
    
    db.commit()
    db.refresh(existente)
    return existente