from pydantic import BaseModel, field_validator, model_validator, EmailStr, HttpUrl
from datetime import date
from typing import Optional
from Schemas.EstadosSchema import EstadosRespuestaSchema
from Utils.Validacionesutilidades import validar_nombre_utils, validar_telefono_utils

class AlianzaBaseSchema(BaseModel):
    nombre_entidad: str
    sitio_web_url: HttpUrl
    id_tipo_entidad: int
    id_estado: int
    representante_entidad: str
    correo_contacto: EmailStr
    telefono_contacto: str
    fecha_inicio_alianza: date
    fecha_fin_alianza: date

    @field_validator("nombre_entidad")
    @classmethod
    def validar_nombre_entidad(cls, v: str) -> str:
        return validar_nombre_utils(v, 3, 100, "Nombre de la entidad")

    @field_validator("representante_entidad")
    @classmethod
    def validar_representante(cls, v: str) -> str:
        return validar_nombre_utils(v, 3, 100, "Representante")

    @field_validator("telefono_contacto")
    @classmethod
    def validar_telefono(cls, v: str) -> str:
        if v is None:
            return v
        return validar_telefono_utils(v)
    
    @model_validator(mode="after")
    def validar_fechas(self):
        if (self.fecha_inicio_alianza and self.fecha_fin_alianza and self.fecha_inicio_alianza > self.fecha_fin_alianza):
            raise ValueError("La fecha de inicio no puede ser mayor que la fecha de fin")
        return self

class AlianzaCrearSchema(AlianzaBaseSchema):
    pass

class AlianzaRespuestaSchema(BaseModel):
    id_alianza: int
    nombre_entidad: str
    sitio_web_url: HttpUrl
    id_tipo_entidad: int
    estados: EstadosRespuestaSchema
    representante_entidad: str
    correo_contacto: EmailStr
    telefono_contacto: str
    fecha_inicio_alianza: date
    fecha_fin_alianza: date
    fecha_registro_alianza: date
    id_estado: int

    class Config:
        from_attributes = True


class AlianzaActualizarSchema(BaseModel):
    nombre_entidad: Optional[str] = None
    sitio_web_url: Optional[HttpUrl] = None
    id_tipo_entidad: Optional[int] = None
    id_estado: Optional[int] = None
    representante_entidad: Optional[str] = None
    correo_contacto: Optional[EmailStr] = None
    telefono_contacto: Optional[str] = None
    fecha_inicio_alianza: Optional[date] = None
    fecha_fin_alianza: Optional[date] = None

    @field_validator("nombre_entidad")
    @classmethod
    def validar_nombre_entidad(cls, v: str) -> str:
        if v is None:
            return v
        return validar_nombre_utils(v, 3, 100, "Nombre de la entidad")
    
    @field_validator("telefono_contacto")
    @classmethod
    def validar_telefono(cls, v):
        if v is None:
            return v
        return validar_telefono_utils(v)
    
    @model_validator(mode="after")
    def validar_fechas(self):
        if (self.fecha_inicio_alianza and self.fecha_fin_alianza and self.fecha_inicio_alianza > self.fecha_fin_alianza):
            raise ValueError("La fecha de inicio no puede ser mayor que la fecha de fin")
        return self
    
