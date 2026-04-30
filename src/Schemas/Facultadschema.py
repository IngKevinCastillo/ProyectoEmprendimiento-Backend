from pydantic import BaseModel, field_validator
import re
from Utils.Validacionesutilidades import validar_nombre, validar_string

class FacultadRespuestaSchema(BaseModel):
    id_facultad: int
    nombre: str
    descripcion: str
    estado: str

    class Config:
        from_attributes = True
        