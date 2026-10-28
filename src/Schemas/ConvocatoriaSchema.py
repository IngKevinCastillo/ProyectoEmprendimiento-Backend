from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from typing import Final

ESTADOS_VALIDOS: Final[list[str]] = ["Finalizado", "Publicada"]

class ConvocatoriaCrearSchema(BaseModel):
    titulo_convocatoria: str
    descripcion_convocatoria: Optional[str] = None
    fecha_apertura: date
    fecha_cierre: date
    cupos: Optional[int] = None
    requisitos: Optional[str] = None
    id_tipo_convocatoria: int

class ConvocatoriaActualizarSchema(BaseModel):
    titulo_convocatoria: Optional[str] = None
    descripcion_convocatoria: Optional[str] = None
    fecha_apertura: Optional[date] = None
    fecha_cierre: Optional[date] = None
    cupos: Optional[int] = None
    requisitos: Optional[str] = None
    id_tipo_convocatoria: Optional[int] = None

class ConvocatoriaRespuestaSchema(BaseModel):
    id_convocatoria: int
    titulo_convocatoria: str
    descripcion_convocatoria: Optional[str]
    fecha_apertura: date
    fecha_cierre: date
    cupos: Optional[int]
    requisitos: Optional[str]
    estado: str
    creado_por: int
    id_tipo_convocatoria: int
    fecha_creacion: Optional[datetime]

    class Config:
        from_attributes = True