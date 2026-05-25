from pydantic import BaseModel
from typing import Optional

class BeneficioCrearSchema(BaseModel):
    nombre: str
    tipo: str
    descripcion: Optional[str] = None

class BeneficioActualizarSchema(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    descripcion: Optional[str] = None

class BeneficioRespuestaSchema(BaseModel):
    id_beneficio: int
    nombre: str
    tipo: str
    descripcion: Optional[str]

    class Config:
        from_attributes = True