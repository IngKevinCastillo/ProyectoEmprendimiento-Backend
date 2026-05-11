from pydantic import BaseModel, field_validator
from typing import Optional

class EstadosBaseSchema(BaseModel):
    nombre: str
    descripcion: Optional[int] = None

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        v = v.strip()
        if not (3 <= len(v) <= 30):
            raise ValueError("El nombre del estado debe tener entre 3 y 30 caracteres.")
        return v

class EstadosCrearSchema(EstadosBaseSchema):
    pass


class EstadosRespuestaSchema(BaseModel):
    id_estado: int
    nombre: str
    descripcion: Optional[int] = None

    class Config:
        from_attributes = True