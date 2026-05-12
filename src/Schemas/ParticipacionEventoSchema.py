from pydantic import BaseModel, field_validator, ValidationInfo
from Utils.Validacionesutilidades import validar_id_entero

class ParticipacionEventoCrearSchema(BaseModel):
    id_usuario: int
    id_evento: int
    Id_rol: int

    @field_validator("id_usuario", "id_evento", "Id_rol")
    @classmethod
    def validar_ids_positivos(cls, v: int, info: ValidationInfo) -> int:
        campo = info.field_name.replace("_", " ").capitalize()
        return validar_id_entero(v, campo=campo)

class ParticipacionEventoRespuestaSchema(BaseModel):
    id_participacion_evento: int
    id_usuario: int
    id_evento: int
    Id_rol: int
    id_estado: int

    class Config:
        from_attributes = True
        
class ParticipacionActualizarSchema(BaseModel):
    id_usuario: int
    id_evento: int
    Id_rol: int