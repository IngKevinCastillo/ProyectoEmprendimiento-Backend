from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing import Optional
from datetime import date, datetime
import re


class UsuarioCrearSchema(BaseModel):
    primer_nombre: str
    segundo_nombre: Optional[str] = None
    primer_apellido: str
    segundo_apellido: str
    correo: EmailStr
    contrasena: str
    fecha_nacimiento: date
    ubicacion_semestral: int
    id_rol: int
    estado: str = "Activo"
    sexo: str
    id_programa: int
    id_tipodocumento: int
    numero_documento: str
    telefono: str
    id_facultad: int

    # ──────────────── Nombres y apellidos ────────────────

    @field_validator("primer_nombre")
    @classmethod
    def validar_primer_nombre(cls, v: str) -> str:
        v = v.strip()
        if not (1 <= len(v) <= 30):
            raise ValueError("El primer nombre debe tener entre 1 y 30 caracteres.")
        if not re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+", v):
            raise ValueError("El primer nombre solo puede contener letras.")
        return v

    @field_validator("segundo_nombre")
    @classmethod
    def validar_segundo_nombre(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if len(v) == 0:
            return None
        if len(v) > 30:
            raise ValueError("El segundo nombre no puede superar los 30 caracteres.")
        if not re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+", v):
            raise ValueError("El segundo nombre solo puede contener letras.")
        return v

    @field_validator("primer_apellido")
    @classmethod
    def validar_primer_apellido(cls, v: str) -> str:
        v = v.strip()
        if not (1 <= len(v) <= 30):
            raise ValueError("El primer apellido debe tener entre 1 y 30 caracteres.")
        if not re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+", v):
            raise ValueError("El primer apellido solo puede contener letras.")
        return v

    @field_validator("segundo_apellido")
    @classmethod
    def validar_segundo_apellido(cls, v: str) -> str:
        v = v.strip()
        if not (0 <= len(v) <= 30):
            raise ValueError("El segundo apellido no puede superar los 30 caracteres.")
        if v and not re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+", v):
            raise ValueError("El segundo apellido solo puede contener letras.")
        return v

    # ──────────────── Contraseña ────────────────

    @field_validator("contrasena")
    @classmethod
    def validar_contrasena(cls, v: str) -> str:
        if " " in v:
            raise ValueError("La contraseña no puede contener espacios.")
        if not (8 <= len(v) <= 30):
            raise ValueError("La contraseña debe tener entre 8 y 30 caracteres.")
        if not re.search(r"[A-Z]", v):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", v):
            raise ValueError("La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r"[0-9]", v):
            raise ValueError("La contraseña debe contener al menos un número.")
        return v

    # ──────────────── Fecha de nacimiento ────────────────

    @field_validator("fecha_nacimiento")
    @classmethod
    def validar_fecha_nacimiento(cls, v: date) -> date:
        hoy = date.today()
        fecha_minima = date(1900, 1, 1)
        if v >= hoy:
            raise ValueError("La fecha de nacimiento debe ser anterior a la fecha actual.")
        if v < fecha_minima:
            raise ValueError("La fecha de nacimiento no puede ser anterior al 01/01/1900.")
        return v

    # ──────────────── Semestre ────────────────

    @field_validator("ubicacion_semestral")
    @classmethod
    def validar_semestre(cls, v: int) -> int:
        if not (1 <= v <= 10):
            raise ValueError("El semestre debe estar entre 1 y 10.")
        return v

    # ──────────────── Estado ────────────────

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, v: str) -> str:
        permitidos = {"Activo", "Inactivo"}
        if v not in permitidos:
            raise ValueError(f"El estado debe ser uno de: {', '.join(permitidos)}.")
        return v

    # ──────────────── Sexo ────────────────

    @field_validator("sexo")
    @classmethod
    def validar_sexo(cls, v: str) -> str:
        permitidos = {"Femenino", "Masculino", "Otro"}
        if v not in permitidos:
            raise ValueError(f"El sexo debe ser uno de: {', '.join(permitidos)}.")
        return v

    # ──────────────── IDs (FK) ────────────────

    @field_validator("id_rol", "id_programa", "id_tipodocumento", "id_facultad")
    @classmethod
    def validar_ids_positivos(cls, v: int) -> int:
        if v < 1 or v > 2147483647:
            raise ValueError("El ID debe ser un entero positivo válido (1 - 2147483647).")
        return v

    # ──────────────── Número de documento ────────────────

    @field_validator("numero_documento")
    @classmethod
    def validar_numero_documento(cls, v: str) -> str:
        v = v.strip()
        if not re.fullmatch(r"[0-9]{1,30}", v):
            raise ValueError("El número de documento debe contener solo dígitos (máximo 30).")
        if int(v) < 1:
            raise ValueError("El número de documento debe ser un valor positivo.")
        return v

    # ──────────────── Teléfono ────────────────

    @field_validator("telefono")
    @classmethod
    def validar_telefono(cls, v: str) -> str:
        v = v.strip()
        if not re.fullmatch(r"3[0-9]{9}", v):
            raise ValueError("El teléfono debe tener exactamente 10 dígitos y comenzar por 3.")
        return v


class UsuarioRespuestaSchema(BaseModel):
    id_usuario: int
    primer_nombre: str
    segundo_nombre: Optional[str]
    primer_apellido: str
    segundo_apellido: str
    correo: str
    fecha_nacimiento: date
    ubicacion_semestral: int
    id_rol: int
    fecha_registro: datetime
    estado: str
    sexo: str
    id_programa: int
    id_tipodocumento: int
    numero_documento: str
    telefono: str
    id_facultad: int

    class Config:
        from_attributes = True


class LoginSchema(BaseModel):
    correo: EmailStr
    contrasena: str