from pydantic import BaseModel, field_validator
from datetime import date, datetime
from Utils.Validacionesutilidades import validar_nombre_utils, validar_descripcion_no_nulo, validar_id_entero
from enum import Enum
from typing import Optional

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
    descripcion: str
    url_evento: Optional[str]
    
    @field_validator("tipo_evento", mode="before")
    @classmethod
    def validar_tipo_evento(cls, v):
        valores_validos = [e.value for e in TipoEvento]
        if v not in valores_validos:
            raise ValueError(
                f"'{v}' no es válido. Los tipos permitidos son: {', '.join(valores_validos)}"
            )
        return v
    
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
    
    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        return validar_descripcion_no_nulo(v, 20, 2000, "Descripcion")

class EventoRespuestaSchema(BaseModel):
    id_evento: int
    nombre_evento: str
    tipo_evento: str
    fecha: datetime
    lugar: str
    descripcion: str
    id_estado: int
    url_evento: Optional[str]

    class Config:
        from_attributes = True
        
class ConsultarFechas(BaseModel):
    fecha_inicio: date
    fecha_fin: date

class EventoActualizarSchema(BaseModel):
    nombre_evento: str
    tipo_evento: str
    fecha: datetime
    lugar: str
    descripcion: str
    url_evento: Optional[str]
    
    @field_validator("tipo_evento", mode="before")
    @classmethod
    def validar_tipo_evento(cls, v):
        valores_validos = [e.value for e in TipoEvento]
        if v not in valores_validos:
            raise ValueError(
                f"'{v}' no es válido. Los tipos permitidos son: {', '.join(valores_validos)}"
            )
        return v
    
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
    
    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        return validar_descripcion_no_nulo(v, 20, 2000, "Descripcion")
