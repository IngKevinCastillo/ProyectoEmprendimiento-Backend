from pydantic import BaseModel, field_validator, ValidationInfo
from datetime import date
from Utils.Validacionesutilidades import validar_id_entero

class InscripcionCrearSchema(BaseModel):
    id_usuario: int
    id_curso: int
    fecha_inscripcion: date
    
    @field_validator("id_usuario", "id_curso")
    @classmethod
    def validar_ids(cls, v: int, info: ValidationInfo) -> int:
        campo = info.field_name.replace("_", " ").capitalize()
        return validar_id_entero(v, campo=campo)
    
class InscripcionRespuestaSchema(BaseModel):
    id_inscripcion: int
    id_usuario: int
    id_curso: int
    fecha_inscripcion: date
    id_estado: int
    
    class Config:
        from_attributes = True
        
class InscripcionActualizarSchema(BaseModel):
    id_usuario: int
    id_curso: int
    fecha_inscripcion: date

class DatosVerificar(BaseModel):
    id_usuario: int
    id_curso: int