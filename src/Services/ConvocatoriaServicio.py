from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.ConvocatoriaModelo import ConvocatoriaModelo
from Schemas.ConvocatoriaSchema import ConvocatoriaCrearSchema, ConvocatoriaActualizarSchema
from Models.TipoConvocatoriaModelo import TipoConvocatoriaModelo

TRANSICIONES_VALIDAS = {
    "borrador": ["publicada"],
    "publicada": ["cerrada"],
    "cerrada": ["finalizada"],
    "finalizada": []
}

def validar_tipo_convocatoria(db: Session, id_tipo_convocatoria: int):          
    tipo = db.query(TipoConvocatoriaModelo).filter(TipoConvocatoriaModelo.id_tipo_convocatoria == id_tipo_convocatoria).first()
    if not tipo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de convocatoria no encontrado")
    return tipo

def ObtenerConvocatorias(db: Session):
    return db.query(ConvocatoriaModelo).all()

def ObtenerConvocatoriasPublicadas(db: Session):
    return db.query(ConvocatoriaModelo).filter(
        ConvocatoriaModelo.estado == "publicada"
    ).all()

def BuscarConvocatoria(db: Session, id_convocatoria: int):
    return db.query(ConvocatoriaModelo).filter(
        ConvocatoriaModelo.id_convocatoria == id_convocatoria
    ).first()

def CrearConvocatoria(db: Session, datos: ConvocatoriaCrearSchema, id_admin: int):
    nueva = ConvocatoriaModelo(
        **datos.model_dump(),
        creado_por=id_admin,
        estado="borrador"
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def ActualizarConvocatoria(db: Session, id_convocatoria: int, datos: ConvocatoriaActualizarSchema):
    convocatoria = BuscarConvocatoria(db, id_convocatoria)
    if not convocatoria:
        return None
    if convocatoria.estado not in ("borrador",):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede editar una convocatoria en estado borrador"
        )
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(convocatoria, campo, valor)
    db.commit()
    db.refresh(convocatoria)
    return convocatoria

def CambiarEstadoConvocatoria(db: Session, id_convocatoria: int, nuevo_estado: str):
    convocatoria = BuscarConvocatoria(db, id_convocatoria)
    if not convocatoria:
        return None
    estados_permitidos = TRANSICIONES_VALIDAS.get(convocatoria.estado, [])
    if nuevo_estado not in estados_permitidos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se puede pasar de '{convocatoria.estado}' a '{nuevo_estado}'"
        )
    convocatoria.estado = nuevo_estado
    db.commit()
    db.refresh(convocatoria)
    return convocatoria

def EliminarConvocatoria(db: Session, id_convocatoria: int):
    convocatoria = BuscarConvocatoria(db, id_convocatoria)
    if not convocatoria:
        return None
    if convocatoria.estado != "borrador":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede eliminar una convocatoria en estado borrador"
        )
    db.delete(convocatoria)
    db.commit()
    return True