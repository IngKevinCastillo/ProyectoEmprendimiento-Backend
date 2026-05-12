from sqlalchemy.orm import Session
from Schemas.InscripcionSchema import InscripcionCrearSchema, InscripcionActualizarSchema
from Models.InscripcionModelo import InscripcionModelo
from fastapi import HTTPException, status
from Services.UsuarioServicio import buscar_usuario
from Services.CursoServicio import buscar_curso
from Utils.Mapeadorutilidades import auto_mapear
from Schemas.EstadosSchema import CambiarEstado
from typing import Final

ESTADO_ELIMINADO: Final = 6
ESTADO_ACTIVO: Final = 8

def crear_inscripcion(db: Session, inscripcion: InscripcionCrearSchema):
    existente = buscar_usuario(db, inscripcion.id_usuario)
    consultado = buscar_curso(db, inscripcion.id_curso)
    registro_existente = verificar_registro(db, inscripcion.id_usuario, inscripcion.id_curso)
    
    if not existente or existente.id_estado == ESTADO_ELIMINADO:
        raise HTTPException(status_code=404, detail="El usuario especificado no existe")
    
    if not consultado or consultado.id_estado == ESTADO_ELIMINADO:
        raise HTTPException(status_code=404, detail="El curso especificado no existe")
    
    if registro_existente:
        raise HTTPException(status_code=409, detail="No se puede crear la inscripcion. Ya estas inscrito en este curso")
    
    nueva_inscripcion = InscripcionModelo(
        id_usuario=inscripcion.id_usuario,
        id_curso=inscripcion.id_curso,
        fecha_inscripcion=inscripcion.fecha_inscripcion,
        id_estado=ESTADO_ACTIVO
    )
    
    db.add(nueva_inscripcion)
    db.commit()
    db.refresh(nueva_inscripcion)
    return nueva_inscripcion

def listar_inscripciones_curso(db: Session, id_curso: int):
    existente = buscar_curso(db, id_curso)
    
    if not existente or existente.id_estado == ESTADO_ELIMINADO:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El curso especificado no existe")
    
    inscripciones = db.query(InscripcionModelo).filter(
        InscripcionModelo.id_curso == id_curso,
        InscripcionModelo.id_estado != ESTADO_ELIMINADO
    ).all()
    
    if not inscripciones:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay inscripciones en el curso")
    
    return inscripciones

def buscar_inscripcion(db: Session, id_inscripcion: int):
    existente = db.query(InscripcionModelo).filter(
        InscripcionModelo.id_inscripcion == id_inscripcion,
        InscripcionModelo.id_estado != ESTADO_ELIMINADO
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La inscripcion especificada no existe.")
    
    return existente

def listar_inscripciones_usuario(db: Session, id_usuario: int):
    existentes = db.query(InscripcionModelo).filter(
        InscripcionModelo.id_usuario == id_usuario,
        InscripcionModelo.id_estado != ESTADO_ELIMINADO
    ).all()
    
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No tiene inscripciones el usuario.")
    
    return existentes

def verificar_registro(db: Session, id_usuario: int, id_curso: int):
    existente = db.query(InscripcionModelo).filter(
        InscripcionModelo.id_usuario == id_usuario, InscripcionModelo.id_curso == id_curso,
        InscripcionModelo.id_estado != ESTADO_ELIMINADO
    ).first()
    return existente

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
    
    existente.id_estado = ESTADO_ELIMINADO
    
    db.commit()
    db.refresh(existente)
    
    return {"detail": "Inscripcion eliminada"}

def cambiar_estado(db: Session, id_inscripcion: int, estado: CambiarEstado):
    existente = db.query(InscripcionModelo).filter(
        InscripcionModelo.id_inscripcion == id_inscripcion
    ).first()
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La inscripcion especificada no existe.")
    
    existente.id_estado = estado.id_estado_cambiar
    
    db.commit()
    db.refresh(existente)
    return existente