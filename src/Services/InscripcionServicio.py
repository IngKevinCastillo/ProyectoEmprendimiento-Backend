from sqlalchemy.orm import Session
from Schemas.InscripcionSchema import InscripcionCrearSchema, InscripcionActualizarSchema
from Models.InscripcionModelo import InscripcionModelo
from fastapi import HTTPException
from Services.UsuarioServicio import buscar_usuario
from Services.CursoServicio import buscar_curso
from Utils.Mapeadorutilidades import auto_mapear

def crear_inscripcion(db: Session, inscripcion: InscripcionCrearSchema):
    existente = buscar_usuario(db, inscripcion.id_usuario)
    consultado = buscar_curso(db, inscripcion.id_curso)
    registro_existente = verificar_registro(db, inscripcion.id_usuario, inscripcion.id_curso)
    
    if not existente:
        raise HTTPException(status_code=404, detail="El usuario especificado no existe")
    
    if not consultado:
        raise HTTPException(status_code=404, detail="El curso especificado no existe")
    
    if registro_existente:
        raise HTTPException(status_code=409, detail="No se puede crear la inscripcion. Ya estas inscrito en este curso")
    
    nueva_inscripcion = InscripcionModelo(
        id_usuario=inscripcion.id_usuario,
        id_curso=inscripcion.id_curso,
        fecha_inscripcion=inscripcion.fecha_inscripcion
    )
    
    db.add(nueva_inscripcion)
    db.commit()
    db.refresh(nueva_inscripcion)
    return nueva_inscripcion

def listar_inscripciones_curso(db: Session, id_curso: int):
    existente = buscar_curso(db, id_curso)
    
    if not existente:
        raise HTTPException(status_code=404, detail="El curso especificado no existe")
    
    return db.query(InscripcionModelo).filter(InscripcionModelo.id_curso == id_curso).all()

def buscar_inscripcion(db: Session, id_inscripcion: int):
    return db.query(InscripcionModelo).filter(InscripcionModelo.id_inscripcion == id_inscripcion).first()

def listar_inscripciones_usuario(db: Session, id_usuario: int):
    return db.query(InscripcionModelo).filter(InscripcionModelo.id_usuario == id_usuario).all()

def verificar_registro(db: Session, id_usuario: int, id_curso: int):
    return db.query(InscripcionModelo).filter(InscripcionModelo.id_usuario == id_usuario, InscripcionModelo.id_curso == id_curso).first()

def actualizar_inscripcion(db: Session, id_inscripcion: int, inscripcion: InscripcionActualizarSchema):
    existente = buscar_inscripcion(db, id_inscripcion)
    
    if not existente:
        raise HTTPException(status_code=404, detail="La inscricion especificada no existe")
    
    auto_mapear(existente, inscripcion, excluir=["id_inscripcion"])
    
    db.commit()
    db.refresh(existente)
    return existente

def eliminar_inscripcion(db: Session, id_inscripcion: int):
    existente = buscar_inscripcion(db, id_inscripcion)
    
    if not existente:
        raise HTTPException(status_code=404, detail="La inscricion especificada no existe")
    
    db.delete(existente)
    db.commit()
    
    return {"detail": "Inscripcion eliminada"}