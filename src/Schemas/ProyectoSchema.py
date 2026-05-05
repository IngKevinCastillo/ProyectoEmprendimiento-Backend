from pydantic import BaseModel, field_validator
from datetime import datetime
from Utils.Validacionesutilidades import validar_nombre, validar_descripcion, validar_id_entero

class ProyectoCrearSchema(BaseModel):
    nombre_proyecto: str
    descripcion: str
    id_estado_proyecto: int

    @field_validator("nombre_proyecto")
    @classmethod
    def validar_nombre_proyecto(cls, v: str) -> str:
        return validar_nombre(v, min_len=3, max_len=100, campo="Nombre del proyecto")

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        return validar_descripcion(v, min_len=20, max_len=2000, campo="Descripción del proyecto")

    @field_validator("id_estado_proyecto")
    @classmethod
    def validar_id_usuario(cls, v: int) -> int:
        return validar_id_entero(v, campo="ID del estado del proyecto")


class ProyectoRespuestaSchema(BaseModel):
    id_proyecto: int
    nombre_proyecto: str
    descripcion: str
    id_estado_proyecto: int
    fecha_creacion: datetime
    
    class Config:
        from_attributes = True