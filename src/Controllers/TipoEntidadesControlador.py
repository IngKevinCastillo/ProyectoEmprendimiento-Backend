from sqlalchemy.orm import Session
from Services.TipoEntidadesServicio import crear_tipo_entidad, listar_tipo_entidades, buscar_tipo_entidad, actualizar_tipo_entidad
from Schemas.TipoEntidadesSchema import TipoEntidadCrearSchema, TipoEntidadActualizarSchema

def crear_tipo_entidad_controlador(db: Session, tipo_entidad: TipoEntidadCrearSchema):
    return crear_tipo_entidad(db, tipo_entidad)

def listar_tipo_entidades_controlador(db: Session):
    return listar_tipo_entidades(db)

def buscar_tipo_entidad_controlador(db: Session, id_tipo_entidad: str):
    return buscar_tipo_entidad(db, int(id_tipo_entidad))

def actualizar_tipo_entidad_controlador(db: Session, id_tipo_entidad: str, tipo_entidad: TipoEntidadActualizarSchema):
    return actualizar_tipo_entidad(db, id_tipo_entidad, tipo_entidad)