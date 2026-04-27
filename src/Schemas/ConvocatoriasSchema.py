from pydantic import BaseModel, field_validator, model_validator
from datetime import date, datetime
from typing import Optional


class ConvocatoriasCrearSchema(BaseModel):
    titulo_convocatoria: str
    descripcion_convocatoria: str
    tipo_convocatoria: str
    fecha_inicio: date
    fecha_cierre: date
    estado_convocatoria: str
    id_usuario: int

    @field_validator("titulo_convocatoria")
    @classmethod
    def validar_titulo(cls, v: str) -> str:
        v = v.strip()
        if len(v) > 150:
            raise ValueError("El título no puede superar los 150 caracteres.")
        if not v:
            raise ValueError("El título no puede estar vacío.")
        return v

    @field_validator("descripcion_convocatoria")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        v = v.strip()
        if len(v) > 450:
            raise ValueError("La descripción no puede superar los 450 caracteres.")
        if not v:
            raise ValueError("La descripción no puede estar vacía.")
        return v

    @field_validator("tipo_convocatoria")
    @classmethod
    def validar_tipo(cls, v: str) -> str:
        permitidos = {"Interna", "Externa", "Concurso", "Oportunidad de emprendimiento"}
        if v not in permitidos:
            raise ValueError(f"El tipo debe ser uno de: {', '.join(permitidos)}.")
        return v

    @field_validator("estado_convocatoria")
    @classmethod
    def validar_estado(cls, v: str) -> str:
        permitidos = {"Borrador", "Publicada", "Cerrada", "Cancelada"}
        if v not in permitidos:
            raise ValueError(f"El estado debe ser uno de: {', '.join(permitidos)}.")
        return v

    @field_validator("id_usuario")
    @classmethod
    def validar_id_usuario(cls, v: int) -> int:
        if v < 1 or v > 2147483647:
            raise ValueError("El ID de usuario debe ser un entero positivo válido.")
        return v

    @model_validator(mode="after")
    def validar_fechas(self):
        if self.fecha_cierre < self.fecha_inicio:
            raise ValueError("La fecha de cierre debe ser mayor o igual a la fecha de inicio.")
        return self


class ConvocatoriasRespuestaSchema(BaseModel):
    Id_convocatoria: int
    titulo_convocatoria: str
    descripcion_convocatoria: str
    tipo_convocatoria: str
    fecha_inicio: date
    fecha_cierre: date
    estado_convocatoria: str
    id_usuario: int
    fecha_registro: datetime

    class Config:
        from_attributes = True