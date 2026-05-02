from pydantic import BaseModel, field_validator


class ParticipacionEventoCrearSchema(BaseModel):
    id_usuario: int
    id_evento: int
    Id_rol: int

    @field_validator("id_usuario", "id_evento", "Id_rol")
    @classmethod
    def validar_ids_positivos(cls, v: int) -> int:
        if v < 1 or v > 2147483647:
            raise ValueError("El ID debe ser un entero positivo válido (1 - 2147483647).")
        return v


class ParticipacionEventoRespuestaSchema(BaseModel):
    id_participacion_evento: int
    id_usuario: int
    id_evento: int
    Id_rol: int

    class Config:
        from_attributes = True
        
class ParticipacionActualizarSchema(BaseModel):
    id_usuario: int
    id_evento: int
    Id_rol: int