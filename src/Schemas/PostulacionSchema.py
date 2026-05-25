from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostulacionCrearSchema(BaseModel):
    id_proyecto: int
    respuestas: Optional[str] = None

class PostulacionActualizarSchema(BaseModel):
    respuestas: Optional[str] = None

class PostulacionRespuestaSchema(BaseModel):
    id_postulacion: int
    id_convocatoria: int
    id_proyecto: int
    estado: str
    respuestas: Optional[str]
    fecha_postulacion: Optional[datetime]

    class Config:
        from_attributes = True