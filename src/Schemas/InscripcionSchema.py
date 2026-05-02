from pydantic import BaseModel, field_validator
from datetime import date
from Utils.Validacionesutilidades import validar_fecha

class InscripcionCrearSchema(BaseModel):
    id_usuario: int
    id_curso: int
    fecha_inscripcion: str
    
    @field_validator("id_usuario", "id_curso")
    @classmethod
    def validar_ids_positivos(cls, v: int) -> int:
        if v < 1 or v > 2147483647:
            raise ValueError("El ID debe ser un entero positivo válido (1 - 2147483647).")
        return v
    
    @field_validator("fecha_inscripcion")
    @classmethod
    def validar_fecha(cls, v: date) -> date:
        return validar_fecha(v, "fecha_inscripcion")


class InscripcionRespuestaSchema(BaseModel):
    id_inscripcion: int
    id_usuario: int
    id_curso: int
    fecha_inscripcion: date
    
    class Config:
        from_attributes = True
        
class InscripcionActualizarSchema(BaseModel):
    id_usuario: int
    id_curso: int
    fecha_inscripcion: date

class DatosVerificar(BaseModel):
    id_usuario: int
    id_curso: int