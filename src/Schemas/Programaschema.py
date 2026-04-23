from pydantic import BaseModel, field_validator
import re


class ProgramaCrearSchema(BaseModel):
    nombre: str
    nivel: str
    id_facultad: int
    estado: str

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        v = v.strip()
        if not (5 <= len(v) <= 100):
            raise ValueError("El nombre del programa debe tener entre 5 y 100 caracteres.")
        return v

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
        if v < 1 or v > 2147483647:
            raise ValueError("El ID de facultad debe ser un entero positivo válido (1 - 2147483647).")
        return v

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