from pydantic import BaseModel
from typing import Optional

class CriterioCrearSchema(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    puntaje_maximo: int

class CriterioActualizarSchema(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    puntaje_maximo: Optional[int] = None

class CriterioRespuestaSchema(BaseModel):
    id_criterio: int
    id_convocatoria: int
    nombre: str
    descripcion: Optional[str]
    puntaje_maximo: int

    class Config:
        from_attributes = True