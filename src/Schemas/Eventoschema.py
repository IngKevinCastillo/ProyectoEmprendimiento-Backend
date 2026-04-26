from pydantic import BaseModel, field_validator
from datetime import timezone, datetime
import re

class EventoCrearSchema(BaseModel):
    nombre_evento: str
    tipo_evento: str
    fecha: datetime
    lugar:str
    
    @field_validator("nombre_evento")
    @classmethod
    def validar_nombre_evento(cls, v: str) -> str:
        v = v.strip()
        if not (1 <= len(v) <= 50):
            raise ValueError("El primer nombre del evento debe tener entre 1 y 50 caracteres.")
        if not re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+", v):
            raise ValueError("El nombre del evento solo puede contener letras.")
        return v
    
    @field_validator("tipo_evento")
    @classmethod
    def validar_tipo_evento(cls, v: str) -> str:
        v = v.strip()
        if not (1 <= len(v) <= 30):
            raise ValueError("El tipo de evento debe tener entre 1 y 30 caracteres.")
        if not re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+", v):
            raise ValueError("El tipo de evento solo puede contener letras.")
        return v
    
    @field_validator("fecha")
    @classmethod
    def validar_fecha(cls, v: datetime) -> datetime:
        hoy = datetime.now(timezone.utc).date()
        if v <= hoy:
            raise ValueError("La fecha del evento debe ser posterior al dia de hoy.")
        return v
    
    @field_validator("lugar")
    @classmethod
    def validar_lugar(cls, v: str) -> str:
        v = v.strip()
        if not (1 <= len(v) <= 60):
            raise ValueError("El lugar del evento debe tener entre 1 y 60 caracteres.")
        if not re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+", v):
            raise ValueError("El lugar del evento solo puede contener letras.")
        return v
            
class EventoRespuestaSchema(BaseModel):
    id_evento: int
    nombre_evento: str
    tipo_evento: str
    fecha: datetime
    lugar: str

    class Config:
        from_attributes = True