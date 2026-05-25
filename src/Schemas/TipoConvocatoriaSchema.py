from pydantic import BaseModel
from typing import Optional

class TipoConvocatoriaCrearSchema(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class TipoConvocatoriaActualizarSchema(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class TipoConvocatoriaRespuestaSchema(BaseModel):
    id_tipo_convocatoria: int
    nombre: str
    descripcion: Optional[str]

    class Config:
        from_attributes = True