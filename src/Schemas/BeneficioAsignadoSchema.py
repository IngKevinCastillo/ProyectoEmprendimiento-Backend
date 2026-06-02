from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BeneficioAsignadoCrearSchema(BaseModel):
    id_proyecto: int
    id_beneficio: int
    descripcion_entrega: Optional[str] = None

class BeneficioAsignadoActualizarSchema(BaseModel):
    descripcion_entrega: Optional[str] = None

class BeneficioAsignadoCambiarEstadoSchema(BaseModel):
    id_estado: int

class BeneficioAsignadoRespuestaSchema(BaseModel):
    id_beneficio_asignado: int
    id_convocatoria: int
    id_proyecto: int
    id_beneficio: int
    descripcion_entrega: Optional[str]
    id_estado: int
    fecha_asignacion: Optional[datetime]
    asignado_por: int

    class Config:
        from_attributes = True