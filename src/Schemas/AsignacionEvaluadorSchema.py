from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AsignacionCrearSchema(BaseModel):
    id_evaluador: int

class AsignacionRespuestaSchema(BaseModel):
    id_asignacion: int
    id_postulacion: int
    id_evaluador: int
    fecha_asignacion: Optional[datetime]

    class Config:
        from_attributes = True

class AsignacionEvaluadorDetalleSchema(BaseModel):
    id_asignacion: int
    id_postulacion: int
    id_evaluador: int
    fecha_asignacion: Optional[datetime]
    nombre_proyecto: str
    id_proyecto: int

    class Config:
        from_attributes = True