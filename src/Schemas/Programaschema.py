from pydantic import BaseModel, field_validator
import re
from Utils.Validacionesutilidades import validar_nombre_usuario, validar_int

class ProgramaRespuestaSchema(BaseModel):
    id_programa: int
    nombre: str
    nivel: str
    id_facultad: int
    estado: str
    
    class Config:
        from_attributes = True

    