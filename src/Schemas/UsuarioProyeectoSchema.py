from pydantic import BaseModel, field_validator


class UsuarioProyectoCrearSchema(BaseModel):
    id_proyecto: int
    id_usuario: int

    @field_validator("id_proyecto", "id_usuario")
    @classmethod
    def validar_ids_positivos(cls, v: int) -> int:
        if v < 1 or v > 2147483647:
            raise ValueError("El ID debe ser un entero positivo válido (1 - 2147483647).")
        return v


class UsuarioProyectoRespuestaSchema(BaseModel):
    id_usuario_proyecto: int
    id_proyecto: int
    id_usuario: int

    class Config:
        from_attributes = True