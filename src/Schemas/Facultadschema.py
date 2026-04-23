from pydantic import BaseModel, field_validator
import re


class FacultadCrearSchema(BaseModel):
    nombre: str
    descripcion: str
    estado: str

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        v = v.strip()
        if not (5 <= len(v) <= 80):
            raise ValueError("El nombre de la facultad debe tener entre 5 y 80 caracteres.")
        if not re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ\s]+", v):
            raise ValueError("El nombre de la facultad solo puede contener letras y espacios.")
        return v

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        v = v.strip()
        if not (10 <= len(v) <= 500):
            raise ValueError("La descripción debe tener entre 10 y 500 caracteres.")
        return v

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