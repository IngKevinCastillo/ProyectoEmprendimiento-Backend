from pydantic import BaseModel, field_validator
from typing import Optional
import re


class SedeCrearSchema(BaseModel):
    # id_facultad: int
    # id_programa: int
    nombre: str
    ciudad: Optional[str] = None

    # @field_validator("id_facultad", "id_programa")
    # @classmethod
    # def validar_ids_positivos(cls, v: int) -> int:
    #     if v < 1 or v > 2147483647:
    #         raise ValueError("El ID debe ser un entero positivo válido (1 - 2147483647).")
    #     return v

    @field_validator("nombre", "ciudad")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        v = v.strip()
        if not (5 <= len(v) <= 50):
            raise ValueError("El nombre debe tener entre 5 y 50 caracteres.")
        if not re.fullmatch(r"[A-Za-z0-9áéíóúÁÉÍÓÚüÜñÑ\s]+", v):
            raise ValueError("El nombre solo puede contener letras, números y espacios.")
        return v

    @field_validator("ciudad")
    @classmethod
    def validar_ciudad(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if not (5 <= len(v) <= 50):
            raise ValueError("La ciudad debe tener entre 5 y 50 caracteres.")
        if not re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ\s]+", v):
            raise ValueError("La ciudad solo puede contener letras y espacios.")
        return v


class SedeRespuestaSchema(BaseModel):
    # id_sede: int
    # id_facultad: int
    id_programa: int
    nombre: str
    ciudad: Optional[str]

    class Config:
        from_attributes = True
        
class SedeActualizarSchema(BaseModel):
    # id_facultad: Optional[int] = None
    # id_programa: Optional[int] = None
    nombre: str
    ciudad: str