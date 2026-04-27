from pydantic import BaseModel, field_validator
import re
from Utils.Validacionesutilidades import validar_nombre

class TipoDocumentoCrearSchema(BaseModel):
    nombre: str
    abreviatura: str
    estado: str

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        return validar_nombre(v, 3, 30, "nombre")

    @field_validator("abreviatura")
    @classmethod
    def validar_abreviatura(cls, v: str) -> str:
        v = v.strip()
        if not (2 <= len(v) <= 10):
            raise ValueError("La abreviatura debe tener entre 2 y 10 caracteres.")
        if not re.fullmatch(r"[A-Z]+", v):
            raise ValueError("La abreviatura solo puede contener letras mayúsculas.")
        return v

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, v: str) -> str:
        permitidos = {"Activo", "Inactivo"}
        if v not in permitidos:
            raise ValueError(f"El estado debe ser uno de: {', '.join(permitidos)}.")
        return v


class TipoDocumentoRespuestaSchema(BaseModel):
    id_tipo_documento: int
    nombre: str
    abreviatura: str
    estado: str

    class Config:
        from_attributes = True
        
class TipoDocumentoActualizarSchema(BaseModel):
    nombre: str
    abreviatura: str
    estado: str