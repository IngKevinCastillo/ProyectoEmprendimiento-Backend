from pydantic import BaseModel, field_validator, ValidationInfo
from Utils.Validacionesutilidades import validar_id_entero

class UsuarioProyectoCrearSchema(BaseModel):
    id_proyecto: int
    id_usuario: int
    id_rol: int

    @field_validator("id_proyecto", "id_usuario", "id_rol")
    @classmethod
    def validar_ids_positivos(cls, v: int, info: ValidationInfo) -> int:
        campo = info.field_name.replace("_", " ").capitalize()
        return validar_id_entero(v, campo=campo)

class UsuarioProyectoRespuestaSchema(BaseModel):
    id_usuario_proyecto: int
    id_proyecto: int
    id_usuario: int
    id_rol: int

    class Config:
        from_attributes = True
        
class UsuarioProyectoActualizarSchema(BaseModel):
    id_proyecto: int
    id_usuario: int
    id_rol: int
