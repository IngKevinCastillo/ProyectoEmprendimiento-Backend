from pydantic import BaseModel, field_validator
from datetime import date, datetime
from Utils.Validacionesutilidades import validar_nombre_utils
from enum import Enum

class TipoEvento(str, Enum):
    INTERNA = "Interna"
    EXTERNA = "Externa"
    CONCURSO = "Concurso"
    EMPRENDIMIENTO = "Emprendimiento"


class EventoCrearSchema(BaseModel):
    nombre_evento: str
    tipo_evento: TipoEvento
    fecha: date
    lugar:str
#    descripcion: str
    
    @field_validator("nombre_evento")
    @classmethod
    def validar_nombre_evento(cls, v: str) -> str:
        return validar_nombre_utils(v, min_len=3, max_len=100, campo="Nombre del evento")
    
    @field_validator("lugar")
    @classmethod
    def validar_lugar(cls, v: str) -> str:
        v = v.strip()
        if not (3 <= len(v) <= 100):
            raise ValueError("El nombre del lugar del evento debe tener entre 3 y 100 caracteres.")
        return v

class EventoRespuestaSchema(BaseModel):
    id_evento: int
    nombre_evento: str
    tipo_evento: str
    fecha: datetime
    lugar: str
    descripcion: str

    class Config:
        from_attributes = True
        
class EventoActualizarSchema(BaseModel):
    nombre_evento: str
    tipo_evento: str
    fecha: datetime
    lugar: str
    descripcion: str