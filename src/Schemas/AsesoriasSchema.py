from pydantic import BaseModel, field_validator, model_validator
from datetime import date, time


class AsesoriasCrearSchema(BaseModel):
    tema_asesoria: str
    descripcion_asesoria: str
    fecha_asesoria: date
    hora_inicio_asesoria: time
    hora_fin_asesoria: time
    id_usuario: int
    estado_asesoria: str

    @field_validator("tema_asesoria")
    @classmethod
    def validar_tema(cls, v: str) -> str:
        v = v.strip()
        if len(v) > 150 or not v:
            raise ValueError("El tema debe tener entre 1 y 150 caracteres.")
        return v

    @field_validator("descripcion_asesoria")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        v = v.strip()
        if len(v) > 400 or not v:
            raise ValueError("La descripción debe tener entre 1 y 400 caracteres.")
        return v

    @field_validator("id_usuario")
    @classmethod
    def validar_id_usuario(cls, v: int) -> int:
        if v < 1 or v > 2147483647:
            raise ValueError("El ID de usuario debe ser un entero positivo válido.")
        return v

    @field_validator("estado_asesoria")
    @classmethod
    def validar_estado(cls, v: str) -> str:
        permitidos = {"Programada", "Realizada", "Cancelada", "Reprogramada"}
        if v not in permitidos:
            raise ValueError(f"El estado debe ser uno de: {', '.join(permitidos)}.")
        return v

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
    estado_asesoria: str

    class Config:
        from_attributes = True