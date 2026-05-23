from pydantic import BaseModel, field_validator, ValidationInfo
from Utils.Validacionesutilidades import validar_id_entero
from typing import Optional

class ParticipacionEventoCrearSchema(BaseModel):
    id_usuario: int
    id_evento: int
    id_rol: int

    @field_validator("id_usuario", "id_evento", "id_rol")
    @classmethod
    def validar_ids_positivos(cls, v: int, info: ValidationInfo) -> int:
        campo = info.field_name.replace("_", " ").capitalize()
        return validar_id_entero(v, campo=campo)

class ParticipacionEventoRespuestaSchema(BaseModel):
    id_participacion_evento: int
    id_usuario: int
    id_evento: int
    id_rol: int
    id_estado: int

    class Config:
        from_attributes = True
        
class ParticipacionActualizarSchema(BaseModel):
    id_usuario: Optional[int] = None
    id_evento: Optional[int] = None
    id_rol: Optional[int] = None