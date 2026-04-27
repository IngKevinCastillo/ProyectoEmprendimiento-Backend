from pydantic import BaseModel, field_validator
import re
from Utils.Validacionesutilidades import validar_nombre, validar_int

class ProgramaCrearSchema(BaseModel):
    nombre: str
    nivel: str
    id_facultad: int
    estado: str

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        return validar_nombre(v, 5, 100, "nombre")

    @field_validator("nivel")
    @classmethod
    def validar_nivel(cls, v: str) -> str:
        permitidos = {"Técnico", "Tecnólogo", "Profesional", "Especialización"}
        if v not in permitidos:
            raise ValueError(f"El nivel debe ser uno de: {', '.join(permitidos)}.")
        return v

    @field_validator("id_facultad")
    @classmethod
    def validar_id_facultad(cls, v: int) -> int:
        return validar_int(v, 1, 2147483647, "id_facultad")

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, v: str) -> str:
        permitidos = {"Activo", "Inactivo"}
        if v not in permitidos:
            raise ValueError(f"El estado debe ser uno de: {', '.join(permitidos)}.")
        return v


class ProgramaRespuestaSchema(BaseModel):
    id_programa: int
    nombre: str
    nivel: str
    id_facultad: int
    estado: str

    class Config:
        from_attributes = True
        
class ProgramaActualizarSchema(BaseModel):
    nombre: str
    nivel: str
    id_facultad: int
    estado: str