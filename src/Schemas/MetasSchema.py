from pydantic import BaseModel, field_validator, ValidationInfo
from datetime import date
from typing import Optional
from Utils.Validacionesutilidades import validar_descripcion_utils, validar_id_entero, validar_fecha

class MetasBaseSchema(BaseModel):
    descripcion: Optional[str] = None
    anio: Optional[date] = None
    id_estado: Optional[int] = None

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: Optional[str]) -> str:
        return validar_descripcion_utils(v, min_len=1, max_len=200, campo="Descripción de la meta")

    @field_validator("anio")
    @classmethod
    def validar_anio(cls, v: Optional[date]) -> Optional[date]:
        if v is None:
            return v
        fecha_str = v.strftime("%d/%m/%Y")
        validar_fecha(fecha_str, "anio")
        return v

    @field_validator("id_estado")
    @classmethod
    def validar_id_estado(cls, v: Optional[int]) -> int:
        return validar_id_entero(v, campo="ID del estado de la meta")
    
class MetasCrearSchema(MetasBaseSchema):
    descripcion: str
    anio: date
    id_estado: int

class MetasRespuestaSchema(BaseModel):
    id_meta: int
    descripcion: str
    anio: date
    id_estado: int

class MetasActualizarSchema(MetasBaseSchema):
    descripcion: Optional[str] = None
    anio: Optional[date] = None
    id_estado: Optional[int] = None