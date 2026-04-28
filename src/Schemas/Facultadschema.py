from pydantic import BaseModel, field_validator
import re
from Utils.Validacionesutilidades import validar_nombre, validar_string

class FacultadCrearSchema(BaseModel):
    nombre: str
    descripcion: str
    estado: str

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        return validar_nombre(v, 5, 80, "nombre")

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        return validar_string(v, 10, 500, "descripcion")

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, v: str) -> str:
        permitidos = {"Activa", "Inactiva"}
        if v not in permitidos:
            raise ValueError(f"El estado debe ser uno de: {', '.join(permitidos)}.")
        return v


class FacultadRespuestaSchema(BaseModel):
    id_facultad: int
    nombre: str
    descripcion: str
    estado: str

    class Config:
        from_attributes = True
        
class FacultadActualizarSchema(BaseModel):
    nombre: str
    descripcion: str
    estado: str