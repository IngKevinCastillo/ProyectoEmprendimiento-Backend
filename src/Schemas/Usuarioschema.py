from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import date, datetime
import re
from Utils.Validacionesutilidades import validar_documento, validar_nombre_usuario_utils, validar_int_nulos, validar_int, validar_contrasena_utils, validar_telefono_utils, validar_string, validar_fecha, validar_string_nulos

class UsuarioCrearSchema(BaseModel):
    primer_nombre: str
    segundo_nombre: Optional[str] = None
    primer_apellido: str
    segundo_apellido: str
    correo: EmailStr
    contrasena: str
    fecha_nacimiento: str
    ubicacion_semestral: Optional[int] = None
    id_rol: int
    sexo: str
    id_programa: Optional[int] = None
    id_tipodocumento: int
    numero_documento: str
    telefono: str
    id_facultad: Optional[int] = None
    id_sede: int
    direccion: Optional[str] = None
    id_municipio: int

    # ──────────────── Nombres y apellidos ────────────────

    @field_validator("primer_nombre")
    @classmethod
    def validar_primer_nombre(cls, v: str) -> str:
        return validar_nombre_usuario_utils(v, 1, 30, "primer_nombre")

    @field_validator("segundo_nombre")
    @classmethod
    def validar_segundo_nombre(cls, v: Optional[str]) -> Optional[str]:
        return validar_string_nulos(v, 0, 30, "segundo_nombre")


    @field_validator("primer_apellido")
    @classmethod
    def validar_primer_apellido(cls, v: str) -> str:
        return validar_nombre_usuario_utils(v, 1, 30, "primer_apellido")

    @field_validator("segundo_apellido")
    @classmethod
    def validar_segundo_apellido(cls, v: str) -> str:
        return validar_nombre_usuario_utils(v, 0, 30, "segundo_apellido")

    # ──────────────── Contraseña ────────────────

    @field_validator("contrasena")
    @classmethod
    def validar_contrasena(cls, v: str) -> str:
        return validar_contrasena_utils(v)

    # ──────────────── Fecha de nacimiento ────────────────

    @field_validator("fecha_nacimiento")
    @classmethod
    def validar_fecha_nacimiento(cls, v: date) -> date:
        return validar_fecha(v, "fecha_nacimiento")

    # ──────────────── Semestre ────────────────

    @field_validator("ubicacion_semestral")
    @classmethod
    def validar_semestre_(cls, v: int) -> int:
        return validar_int_nulos(v, 1, 10, "ubicacion_semestral")

    # ──────────────── Sexo ────────────────

    @field_validator("sexo")
    @classmethod
    def validar_sexo(cls, v: str) -> str:
        permitidos = {"Femenino", "Masculino", "Otro"}
        if v not in permitidos:
            raise ValueError(f"El sexo debe ser uno de: {', '.join(permitidos)}.")
        return v

    # ──────────────── IDs (FK) ────────────────

    @field_validator("id_rol", "id_tipodocumento", "id_sede")
    @classmethod
    def validar_ids_positivos(cls, v: int) -> int:
        return validar_int(v, 1, 2147483647, "ID")
    
    @field_validator("id_programa", "id_facultad")
    @classmethod
    def validar_ids_positivos_nulos(cls, v: int) -> int:
        return validar_int_nulos(v, 1, 2147483647, "ID")

    # ──────────────── Número de documento ────────────────

    @field_validator("numero_documento")
    @classmethod
    def validar_numero_documento(cls, v: str) -> str:
        return validar_documento(v, "numero_documento")

    # ──────────────── Teléfono ────────────────

    @field_validator("telefono")
    @classmethod
    def validar_telefono(cls, v: str) -> str:
        return validar_telefono_utils(v, "telefono")
    
    @field_validator("direccion")
    @classmethod
    def validar_direccion(cls, v: str) -> str:
        return validar_string_nulos(v, 6, 80, "direccion")


class UsuarioRespuestaSchema(BaseModel):
    id_usuario: int
    primer_nombre: str
    segundo_nombre: Optional[str]
    primer_apellido: str
    segundo_apellido: str
    correo: str
    fecha_nacimiento: date
    ubicacion_semestral: Optional[int] = None
    id_rol: int
    fecha_registro: datetime
    estado: str
    sexo: str
    id_programa: Optional[int] = None
    id_tipodocumento: int
    numero_documento: str
    telefono: str
    id_facultad: Optional[int] = None
    id_sede: int
    direccion: Optional[str] = None
    id_municipio: int
    id_estado: int

    class Config:
        from_attributes = True
        
class UsuarioActualizarSchema(BaseModel):
    primer_nombre: str
    segundo_nombre: Optional[str]
    primer_apellido: str
    segundo_apellido: str
    correo: str
    fecha_nacimiento: date
    ubicacion_semestral: Optional[int] = None
    id_rol: int
    fecha_registro: datetime
    estado: str
    sexo: str
    id_programa: Optional[int] = None
    id_tipodocumento: int
    numero_documento: str
    telefono: str
    id_facultad: Optional[int] = None
    id_sede: int
    direccion: Optional[str] = None
    id_municipio: int

class UsuarioCambiarContrasena(BaseModel):
    contrasena_anterior: str
    contrasena_nueva: str
    
    @field_validator("contrasena_nueva")
    @classmethod
    def validar_contrasena(cls, v: str) -> str:
        return validar_contrasena_utils(v)
    
class CambiarEstado(BaseModel):
    id_estado_cambiar: int 

class LoginSchema(BaseModel):
    correo: EmailStr
    contrasena: str