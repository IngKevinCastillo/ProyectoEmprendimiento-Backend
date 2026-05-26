from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class CriterioRespuestaSchema(BaseModel):
    id_criterio: int
    nombre: str
    descripcion: Optional[str]
    porcentaje: Decimal

    class Config:
        from_attributes = True