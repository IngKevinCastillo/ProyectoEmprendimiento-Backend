from pydantic import BaseModel, field_validator
from datetime import timezone, datetime
import re
from Utils.Validacionesutilidades import validar_nombre, validar_fecha_futura, validar_string

class EventoCrearSchema(BaseModel):
    nombre_evento: str
    tipo_evento: str
    fecha: datetime
    lugar:str
    
    @field_validator("nombre_evento")
    @classmethod
    def validar_nombre_evento(cls, v: str) -> str:
        return validar_nombre(v, 1, 50, "nombre_evento")
    
    @field_validator("tipo_evento")
    @classmethod
    def validar_tipo_evento(cls, v: str) -> str:
        return validar_string(v, 1, 30, "tipo_evento")
    
    @field_validator("fecha")
    @classmethod
    def validar_fecha(cls, v: datetime) -> datetime:
        return validar_fecha_futura(v, "fecha")
    
    @field_validator("lugar")
    @classmethod
    def validar_lugar(cls, v: str) -> str:
        return validar_string(v, 1, 60, "lugar")
            
class EventoRespuestaSchema(BaseModel):
    id_evento: int
    nombre_evento: str
    tipo_evento: str
    fecha: datetime
    lugar: str

    class Config:
        from_attributes = True
        
class EventoActualizarSchema(BaseModel):
    nombre_evento: str
    tipo_evento: str
    fecha: datetime
    lugar: str