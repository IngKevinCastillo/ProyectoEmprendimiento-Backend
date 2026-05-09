from pydantic import BaseModel, field_validator
from Utils.Validacionesutilidades import validar_nombre

class TipoEntidadCrearSchema(BaseModel):
    nombre_tipo_entidad: str

    @field_validator("nombre_tipo_entidad")
    @classmethod
    def validar_nombre_tipo_entidad(cls, v: str) -> str:
        return validar_nombre(v, min_len=3, max_len=100, campo="Nombre del tipo de entidad")


class TipoEntidadRespuestaSchema(BaseModel):
    id_tipo_entidad: int
    nombre_tipo_entidad: str

    class Config:
        from_attributes = True


class TipoEntidadActualizarSchema(BaseModel):
    nombre_tipo_entidad: str