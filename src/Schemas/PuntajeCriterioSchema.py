from pydantic import BaseModel
from typing import Optional

class PuntajeCriterioCrearSchema(BaseModel):
    id_criterio: int
    puntaje_obtenido: int
    comentario: Optional[str] = None

class PuntajeCriterioActualizarSchema(BaseModel):
    puntaje_obtenido: Optional[int] = None
    comentario: Optional[str] = None

class PuntajeCriterioRespuestaSchema(BaseModel):
    id_puntaje: int
    id_evaluacion: int
    id_criterio: int
    puntaje_obtenido: int
    comentario: Optional[str]

    class Config:
        from_attributes = True