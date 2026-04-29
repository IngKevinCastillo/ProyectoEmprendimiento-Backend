from pydantic import BaseModel, field_validator


class EstadoProyectoCrearSchema(BaseModel):
    nombre: str

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        v = v.strip()
        if not (3 <= len(v) <= 40):
            raise ValueError("El nombre del estado debe tener entre 3 y 40 caracteres.")
        return v


class EstadoProyectoRespuestaSchema(BaseModel):
    id_estado_proyecto: int
    nombre: str

    class Config:
        from_attributes = True