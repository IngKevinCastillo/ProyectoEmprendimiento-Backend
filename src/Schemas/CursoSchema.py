from pydantic import BaseModel, field_validator
from datetime import date

class CursoCrearSchema(BaseModel):
    nombre_curso: str
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
    
    @field_validator("nombre_curso")
    @classmethod
    def validar_nombre_curso(cls, v: str) -> str:
        v = v.strip()
        if not (3 <= len(v) <= 80):
            raise ValueError("El nombre del estado debe tener entre 3 y 80 caracteres.")
        return v
    
    @field_validator("descripcion")
    @classmethod
    def validar_descripcion(cls, v: str) -> str:
        v = v.strip()
        if not (3 <= len(v) <= 80):
            raise ValueError("La descripción debe tener entre 3 y 80 caracteres.")
        return v
    
class CursoRespuestaSchema(BaseModel):
    id_curso: int
    nombre_curso: str
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
    
    class Config:
        from_attributes = True
        
class CursoActualizarSchema(BaseModel):
    nombre_curso: str
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
    
