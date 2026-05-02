from sqlalchemy.orm import Session
from fastapi import HTTPException
from Services.CursoServicio import buscar_curso, crear_curso, listar_cursos, eliminar_curso, actualizar_curso, buscar_curso_por_nombre_curso
from Schemas.CursoSchema import CursoCrearSchema, CursoActualizarSchema

def crear_curso_controlador(db: Session, curso: CursoCrearSchema):
    return crear_curso(db, curso)

def buscar_curso_controlador(db: Session, id_curso: str):
    return buscar_curso(db, int(id_curso))

def buscar_curso_nombre_contolador(db: Session, nombre: str):
    return buscar_curso_por_nombre_curso(db, nombre)

def listar_cursos_contolador(db: Session):
    return listar_cursos(db)

def actualizar_curso_controlador(db: Session, id_curso: str, curso: CursoActualizarSchema):
    return actualizar_curso(db, id_curso, curso)

def eliminar_curso_controlador(db: Session, id_curso: str):
    return eliminar_curso(db, id_curso)