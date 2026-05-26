from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime

class EvaluacionCrearSchema(BaseModel):
    comentario_general: Optional[str] = None

class EvaluacionRespuestaSchema(BaseModel):
    id_evaluacion: int
    id_asignacion: int
    comentario_general: Optional[str]
    puntaje_total: Optional[Decimal]
    id_estado: int
    fecha_evaluacion: Optional[datetime]

    class Config:
        from_attributes = True