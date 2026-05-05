from pydantic import BaseModel, field_validator, model_validator
from datetime import date, time
from Utils.Validacionesutilidades import validar_id_entero,validar_nombre, validar_descripcion       
from enum import Enum

class EstadoAsesoria(str, Enum):
    PROGRAMADA = "Programada"
    REALIZADA = "Realizada"
    CANCELADA = "Cancelada"
    REPROGRAMADA = "Reprogramada"

class AsesoriasCrearSchema(BaseModel):
    tema_asesoria: str
    descripcion_asesoria: str
    fecha_asesoria: date
    hora_inicio_asesoria: time
    hora_fin_asesoria: time
    id_usuario: int
    estado_asesoria: EstadoAsesoria

    @field_validator("id_usuario")
    @classmethod
    def validar_id_entero(cls, v: int) -> int:
        return validar_id_entero(v, campo="ID de usuario")

    @field_validator("tema_asesoria")
    @classmethod
    def validar_tema(cls, v: str) -> str:
        return validar_nombre(v, min_len=3, max_len=100, campo="Tema de la asesoría")

    @field_validator("descripcion_asesoria")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        return validar_descripcion(v, min_len=20, max_len=2000, campo="Descripción de la asesoría")

    @model_validator(mode="after")
    def validar_horas(self):
        if self.hora_fin_asesoria <= self.hora_inicio_asesoria:
            raise ValueError("La hora de fin debe ser mayor a la hora de inicio.")
        return self


class AsesoriasRespuestaSchema(BaseModel):
    id_asesoria: int
    tema_asesoria: str
    descripcion_asesoria: str
    fecha_asesoria: date
    hora_inicio_asesoria: time
    hora_fin_asesoria: time
    id_usuario: int
    estado_asesoria: EstadoAsesoria

    class Config:
        from_attributes = True