from pydantic import BaseModel, field_validator

class EstadoProyectoBaseSchema(BaseModel):
    nombre: str

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        v = v.strip()
        if not (3 <= len(v) <= 30):
            raise ValueError("El nombre del estado debe tener entre 3 y 30 caracteres.")
        return v

class EstadoProyectoCrearSchema(EstadoProyectoBaseSchema):
    pass


class EstadoProyectoRespuestaSchema(BaseModel):
    id_estado_proyecto: int
    nombre: str

    class Config:
        from_attributes = True