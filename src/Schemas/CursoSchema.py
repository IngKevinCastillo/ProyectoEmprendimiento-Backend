from pydantic import BaseModel, field_validator, model_validator
from datetime import date
from Utils.Validacionesutilidades import validar_nombre_utils, validar_descripcion_utils, validar_id_entero

class CursoCrearSchema(BaseModel):
    nombre_curso: str
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
    id_estado: int
    
    @field_validator("nombre_curso")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        return validar_nombre_utils(v, min_len=3, max_len=100, campo="Nombre del curso")

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        return validar_descripcion_utils(v, min_len=20, max_len=2000, campo="Descripción del curso")

    @model_validator(mode="after")
    def validar_fechas(self):
        if self.fecha_fin < self.fecha_inicio:
            raise ValueError("La fecha de fin debe ser mayor o igual a la fecha de inicio.")
        return self
    
    @field_validator("id_estado")
    @classmethod
    def validar_id_curso(cls, v: int) -> int:
        return validar_id_entero(v, min_len=1, max_len=2147483647, campo="id curso")

class CursoRespuestaSchema(BaseModel):
    id_curso: int
    nombre_curso: str
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
    id_estado: int
    
    class Config:
        from_attributes = True
        
class CursoActualizarSchema(BaseModel):
    nombre_curso: str
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
    id_estado: int
    
    @field_validator("nombre_curso")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        return validar_nombre_utils(v, min_len=3, max_len=100, campo="Nombre del curso")

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        return validar_descripcion_utils(v, min_len=20, max_len=2000, campo="Descripción del curso")

    @model_validator(mode="after")
    def validar_fechas(self):
        if self.fecha_fin < self.fecha_inicio:
            raise ValueError("La fecha de fin debe ser mayor o igual a la fecha de inicio.")
        return self
    
    @field_validator("id_estado")
    @classmethod
    def validar_id_curso(cls, v: int) -> int:
        return validar_id_entero(v, min_len=1, max_len=2147483647, campo="id curso")
