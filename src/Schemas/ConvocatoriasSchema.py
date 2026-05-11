from pydantic import BaseModel, field_validator, model_validator
from datetime import date
from enum import Enum
from Utils.Validacionesutilidades import validar_string, validar_id_entero, validar_nombre_utils, validar_descripcion_utils


class TipoConvocatoria(str, Enum):
    INTERNA = "Interna"
    EXTERNA = "Externa"
    CONCURSO = "Concurso"
    EMPRENDIMIENTO = "Emprendimiento"

class ConvocatoriasBaseSchema(BaseModel):
    titulo_convocatoria: str
    descripcion_convocatoria: str
    tipo_convocatoria: TipoConvocatoria
    fecha_inicio: date
    fecha_cierre: date
    id_proyecto: int
    url_convocatoria: str
    id_estado: int
    
    @field_validator("tipo_convocatoria", mode="before")
    @classmethod
    def validar_tipo_convocatoria(cls, v):
        valores_validos = [e.value for e in TipoConvocatoria]
        if v not in valores_validos:
            raise ValueError(
                f"'{v}' no es válido. Los tipos permitidos son: {', '.join(valores_validos)}"
            )
        return v

    @field_validator("id_proyecto")
    @classmethod
    def validar_id_proyecto(cls, v: int) -> int:
        return validar_id_entero(v, campo="ID de usuario")
    
    @field_validator("id_estado")
    @classmethod
    def validar_id_estado(cls, v: int) -> int:
        return validar_id_entero(v, campo="ID de estado")

    @field_validator("titulo_convocatoria")
    @classmethod
    def validar_tema(cls, v: str) -> str:
        return validar_nombre_utils(v, min_len=3, max_len=100, campo="Tema de la asesoría")

    @field_validator("descripcion_convocatoria")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        return validar_descripcion_utils(v, min_len=20, max_len=2000, campo="Descripción de la convocatoria")

    @model_validator(mode="after")
    def validar_fechas(self):
        if self.fecha_cierre < self.fecha_inicio:
            raise ValueError("La fecha de cierre debe ser mayor o igual a la fecha de inicio.")
        return self

    @field_validator("url_convocatoria")
    @classmethod
    def validar_url(cls, v: str) -> str:
        return validar_string(v, 12, 255, "url convocatoria")



class ConvocatoriasCrearSchema(ConvocatoriasBaseSchema):
    pass


class ConvocatoriasActualizarSchema(ConvocatoriasBaseSchema):
    pass


class ConvocatoriasRespuestaSchema(BaseModel):
    id_convocatoria: int
    titulo_convocatoria: str
    descripcion_convocatoria: str
    tipo_convocatoria: TipoConvocatoria
    fecha_inicio: date
    fecha_cierre: date
    id_proyecto: int
    fecha_registro: date
    url_convocatoria: str
    id_estado: int

    class Config:
        from_attributes = True