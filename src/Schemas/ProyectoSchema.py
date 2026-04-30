from pydantic import BaseModel, field_validator
from datetime import datetime


class ProyectoCrearSchema(BaseModel):
    nombre_proyecto: str
    descripcion: str
    estado: str

    @field_validator("nombre_proyecto")
    @classmethod
    def validar_nombre_proyecto(cls, v: str) -> str:
        v = v.strip()
        if not (3 <= len(v) <= 100):
            raise ValueError("El nombre del proyecto debe tener entre 3 y 100 caracteres.")
        return v

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        v = v.strip()
        if not (20 <= len(v) <= 2000):
            raise ValueError("La descripción debe tener entre 20 y 2000 caracteres.")
        return v

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, v: str) -> str:
        permitidos = {"En proceso", "Aprobado", "Finalizado"}
        if v not in permitidos:
            raise ValueError(f"El estado debe ser uno de: {', '.join(permitidos)}.")
        return v

    # @field_validator("id_usuario")
    # @classmethod
    # def validar_id_usuario(cls, v: int) -> int:
    #     if v < 1 or v > 2147483647:
    #        raise ValueError("El ID de usuario debe ser un entero positivo válido (1 - 2147483647).")
    #    return v


class ProyectoRespuestaSchema(BaseModel):
    id_proyecto: int
    nombre_proyecto: str
    descripcion: str
    estado: str
    fecha_creacion: datetime
    
    class Config:
        from_attributes = True