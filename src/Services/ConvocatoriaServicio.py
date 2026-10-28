from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import date
from Models.ConvocatoriaModelo import ConvocatoriaModelo
from Models.TipoConvocatoriaModelo import TipoConvocatoriaModelo
from Schemas.ConvocatoriaSchema import ConvocatoriaCrearSchema, ConvocatoriaActualizarSchema, ESTADOS_VALIDOS

ESTADO_PUBLICADA = ESTADOS_VALIDOS[1]
ESTADO_FINALIZADA = ESTADOS_VALIDOS[0]

def _validar_tipo_convocatoria(db: Session, id_tipo_convocatoria: int):
    tipo = db.query(TipoConvocatoriaModelo).filter(
        TipoConvocatoriaModelo.id_tipo_convocatoria == id_tipo_convocatoria
    ).first()
    if not tipo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de convocatoria no encontrado")
    return tipo

def _verificar_y_finalizar(db: Session, convocatoria: ConvocatoriaModelo):
    if convocatoria.estado == ESTADO_PUBLICADA and convocatoria.fecha_cierre < date.today():
        convocatoria.estado = ESTADO_FINALIZADA
        db.commit()
        db.refresh(convocatoria)
    return convocatoria

def ObtenerConvocatorias(db: Session):
    convocatorias = db.query(ConvocatoriaModelo).all()
    for c in convocatorias:
        _verificar_y_finalizar(db, c)
    return convocatorias

def ObtenerConvocatoriasPublicadas(db: Session):
    convocatorias = db.query(ConvocatoriaModelo).filter(
        ConvocatoriaModelo.estado == ESTADO_PUBLICADA
    ).all()
    for c in convocatorias:
        _verificar_y_finalizar(db, c)
    return db.query(ConvocatoriaModelo).filter(
        ConvocatoriaModelo.estado == ESTADO_PUBLICADA
    ).all()

def BuscarConvocatoria(db: Session, id_convocatoria: int):
    convocatoria = db.query(ConvocatoriaModelo).filter(
        ConvocatoriaModelo.id_convocatoria == id_convocatoria
    ).first()
    if convocatoria:
        _verificar_y_finalizar(db, convocatoria)
    return convocatoria

def CrearConvocatoria(db: Session, datos: ConvocatoriaCrearSchema, id_admin: int):
    _validar_tipo_convocatoria(db, datos.id_tipo_convocatoria)
    nueva = ConvocatoriaModelo(
        **datos.model_dump(),
        creado_por=id_admin,
        estado=ESTADO_PUBLICADA
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def ActualizarConvocatoria(db: Session, id_convocatoria: int, datos: ConvocatoriaActualizarSchema):
    convocatoria = BuscarConvocatoria(db, id_convocatoria)
    if not convocatoria:
        return None
    if convocatoria.estado != ESTADO_PUBLICADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede editar una convocatoria publicada"
        )
    if datos.id_tipo_convocatoria:
        _validar_tipo_convocatoria(db, datos.id_tipo_convocatoria)
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(convocatoria, campo, valor)
    db.commit()
    db.refresh(convocatoria)
    return convocatoria

def EliminarConvocatoria(db: Session, id_convocatoria: int):
    convocatoria = BuscarConvocatoria(db, id_convocatoria)
    if not convocatoria:
        return None
    if convocatoria.estado != ESTADO_PUBLICADA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se puede eliminar una convocatoria publicada"
        )
    db.delete(convocatoria)
    db.commit()
    return True