from pydantic import BaseModel, field_validator


class RolesCrearSchema(BaseModel):
    nombre: str
    estado: str

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        permitidos = {"estudiante", "docente", "egresado", "directivo", "administrativo"}
        if v.lower() not in permitidos:
            raise ValueError(f"El rol debe ser uno de: {', '.join(permitidos)}.")
        return v.capitalize()

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, v: str) -> str:
        permitidos = {"Activo", "Inactivo"}
        if v not in permitidos:
            raise ValueError(f"El estado debe ser uno de: {', '.join(permitidos)}.")
        return v


class RolesRespuestaSchema(BaseModel):
    id_rol: int
    nombre: str
    estado: str

    class Config:
        from_attributes = True
        
class RolesActualizarSchema(BaseModel):
    nombre: str
    estado: str