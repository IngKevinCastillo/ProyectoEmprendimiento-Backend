from pydantic import BaseModel, field_validator, model_validator
from datetime import date
from typing import Optional
from Utils.Validacionesutilidades import validar_nombre, validar_descripcion

class AlianzaCrearSchema(BaseModel):
    nombre_entidad: str
    descripcion: Optional[str] = None
    sitio_web_url: str
    id_tipo_entidad: int
    orden: Optional[int] = 0
    activo: Optional[bool] = True
    representante: str
    correo_contacto: str
    telefono_contacto: str
    fecha_inicio: date
    fecha_fin: date

    @field_validator("nombre_entidad")
    @classmethod
    def validar_nombre_entidad(cls, v: str) -> str:
        return validar_nombre(v, min_len=3, max_len=100, campo="Nombre de la entidad")

    @field_validator("representante")
    @classmethod
    def validar_representante(cls, v: str) -> str:
        return validar_nombre(v, min_len=3, max_len=100, campo="Representante")

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion_alianza(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return validar_descripcion(v, min_len=20, max_len=2000, campo="Descripción de la alianza")

    @field_validator("correo_contacto")
    @classmethod
    def validar_correo(cls, v: str) -> str:
        if "@" not in v or "." not in v:
            raise ValueError("El correo de contacto no es válido.")
        return v.strip().lower()

    @field_validator("telefono_contacto")
    @classmethod
    def validar_telefono(cls, v: str) -> str:
        if not v.replace("+", "").replace(" ", "").isdigit():
            raise ValueError("El teléfono de contacto solo debe contener números.")
        return v.strip()

    @field_validator("sitio_web_url")
    @classmethod
    def validar_url(cls, v: str) -> str:
        if not v.startswith("http://") and not v.startswith("https://"):
            raise ValueError("La URL debe comenzar con http:// o https://")
        return v.strip()

    @model_validator(mode="after")
    def validar_fechas(self):
        if self.fecha_fin < self.fecha_inicio:
            raise ValueError("La fecha de fin debe ser mayor o igual a la fecha de inicio.")
        return self


class AlianzaRespuestaSchema(BaseModel):
    id_alianza: int
    nombre_entidad: str
    descripcion: Optional[str]
    sitio_web_url: str
    id_tipo_entidad: int
    orden: int
    activo: bool
    representante: str
    correo_contacto: str
    telefono_contacto: str
    fecha_inicio: date
    fecha_fin: date

    class Config:
        from_attributes = True


class AlianzaActualizarSchema(BaseModel):
    nombre_entidad: str
    descripcion: Optional[str] = None
    sitio_web_url: str
    id_tipo_entidad: int
    orden: Optional[int] = 0
    activo: Optional[bool] = True
    representante: str
    correo_contacto: str
    telefono_contacto: str
    fecha_inicio: date
    fecha_fin: date