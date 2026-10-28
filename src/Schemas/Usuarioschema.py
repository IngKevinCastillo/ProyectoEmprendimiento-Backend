from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import date, datetime
import re
from Utils.Validacionesutilidades import (
    validar_nombre_usuario_utils, 
    validar_int_nulos, 
    validar_int,
    validar_contrasena_utils,
    validar_telefono_utils
)

class UsuarioBaseSchema(BaseModel):
    primer_nombre: Optional[str] = None
    segundo_nombre: Optional[str] = None
    primer_apellido: Optional[str] = None
    segundo_apellido: Optional[str] = None
    correo: Optional[str] = None
    contrasena: Optional[str] = None
    fecha_nacimiento: Optional[str] = None
    ubicacion_semestral: Optional[int] = None
    id_rol: Optional[int] = None
    sexo: Optional[str] = None
    id_programa: Optional[int] = None
    id_tipodocumento: Optional[int] = None
    numero_documento: Optional[str] = None
    telefono: Optional[str] = None
    id_facultad: Optional[int] = None
    id_sede: Optional[int] = None
    direccion: Optional[str] = None
    id_municipio: Optional[int] = None

    @field_validator("primer_nombre")
    @classmethod
    def validar_primer_nombre(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        return validar_nombre_usuario_utils(v, 1, 30, "primer_nombre", permite_numeros=False)

    @field_validator("segundo_nombre")
    @classmethod
    def validar_segundo_nombre(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        return validar_nombre_usuario_utils(v, 1, 30, "segundo_nombre", permite_numeros=False)

    @field_validator("primer_apellido")
    @classmethod
    def validar_primer_apellido(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        return validar_nombre_usuario_utils(v, 1, 30, "primer_apellido", permite_numeros=True)

    @field_validator("segundo_apellido")
    @classmethod
    def validar_segundo_apellido(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        return validar_nombre_usuario_utils(v, 1, 30, "segundo_apellido", permite_numeros=True)

    @field_validator("contrasena")
    @classmethod
    def validar_contrasena(cls, valor: Optional[str]) -> Optional[str]:
        if valor is None:
            return None
        return validar_contrasena_utils(valor, "contrasena")

    @field_validator("fecha_nacimiento")
    @classmethod
    def validar_fecha_nacimiento_campo(cls, valor: Optional[str]) -> Optional[str]:
        if valor is None:
            return None
        min_edad = 15
        max_edad= 120
        if not isinstance(valor, str):
            raise TypeError(f"La fecha de nacimiento debe ser un texto en formato DD/MM/YYYY.")
        valor = valor.strip()
        if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", valor):
            raise ValueError(f"La fecha de nacimiento debe tener el formato DD/MM/YYYY (ej. 15/08/2000).")
        
        try:
            fecha_nacimiento = datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"La fecha de nacimiento no es una fecha válida (ej. 31/02/2000 no existe).")
        
        hoy = datetime.now()
        if fecha_nacimiento.date() >= hoy.date():
            raise ValueError(f"La fecha de nacimiento debe ser menor a la fecha actual. No se permiten fechas futuras.")
        
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        
        if edad < min_edad:
            raise ValueError(f"La fecha de nacimiento debe corresponder a una edad válida (mínimo {min_edad} años).")
        if edad > max_edad:
            raise ValueError(f"La fecha de nacimiento debe corresponder a una edad válida (máximo {max_edad} años).")
        
        return fecha_nacimiento

    @field_validator("ubicacion_semestral")
    @classmethod
    def validar_semestre_(cls, v: Optional[int]) -> Optional[int]:
        return validar_int_nulos(v, 1, 10, "ubicacion_semestral")

    @field_validator("sexo")
    @classmethod
    def validar_sexo(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        permitidos = {"Femenino", "Masculino", "Otro"}
        if v not in permitidos:
            raise ValueError(f"El sexo debe ser uno de: {', '.join(permitidos)}.")
        return v

    @field_validator("id_rol", "id_tipodocumento", "id_municipio", "id_sede")
    @classmethod
    def validar_ids_requeridos(cls, v: Optional[int], info) -> Optional[int]:
        if v is None:
            return None
        return validar_int(v, 1, 2147483647, info.field_name)
    
    @field_validator("id_programa", "id_facultad")
    @classmethod
    def validar_ids_opcionales(cls, v: Optional[int], info) -> Optional[int]:
        return validar_int_nulos(v, 1, 2147483647, info.field_name)

    @field_validator("numero_documento")
    @classmethod
    def validar_numero_documento(cls, valor: Optional[str]) -> Optional[str]:
        if valor is None:
            return None
        if not isinstance(valor, str):
            raise TypeError(f"numero_documento debe ser un texto.")
        valor = valor.strip().replace(".", "").replace(",", "").replace(" ", "")
        if not re.fullmatch(r"[A-Za-z0-9]{6,20}", valor):
            raise ValueError(
                f"numero_documento inválido. Debe tener entre 6 y 20 caracteres alfanuméricos (sin puntos ni espacios)."
        )
        return valor

    @field_validator("telefono")
    @classmethod
    def validar_telefono(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None
        return validar_telefono_utils(v, "telefono")
    
    @field_validator("direccion")
    @classmethod
    def validar_direccion(cls, valor: Optional[str]) -> Optional[str]:
        if valor is None:
            return None
        
        if not isinstance(valor, str):
            raise TypeError(f"La direccion debe ser un texto.")
        
        valor = " ".join(valor.split())
        
        if not valor:
            raise ValueError(f"La direccion no puede estar vacía.")
        
        if len(valor) > 255:
            raise ValueError(f"La direccion debe tener máximo 255 caracteres.")
        
        if not re.fullmatch(r"[A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s#\-./,()°ª]{1,255}", valor):
            raise ValueError(
                f"La direccion contiene caracteres no permitidos. "
                f"Se permiten: letras, números, espacios y símbolos (#, -, ., /)."
            )
        
        return valor


class UsuarioCrearSchema(UsuarioBaseSchema):
    primer_nombre: str
    primer_apellido: str
    segundo_apellido: str
    correo: EmailStr
    contrasena: str
    fecha_nacimiento: str
    id_rol: int
    sexo: str
    id_tipodocumento: int
    numero_documento: str
    telefono: str
    id_sede: int
    id_municipio: int


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
    sexo: str
    id_programa: Optional[int] = None
    id_tipodocumento: int
    numero_documento: str
    telefono: str
    id_facultad: Optional[int] = None
    id_sede: int
    direccion: Optional[str] = None
    id_municipio: int
    id_estado: str

    class Config:
        from_attributes = True

class UsuarioActualizarSchema(UsuarioBaseSchema):
    pass

class UsuarioCambiarContrasena(BaseModel):
    contrasena_anterior: str
    contrasena_nueva: str
    
    @field_validator("contrasena_nueva")
    @classmethod
    def validar_contrasena(cls, v: str) -> str:
        return validar_contrasena_utils(v)
    
class UsuarioRecuperarContrasena(BaseModel):
    correo: str
    contrasena_nueva: str
    
    @field_validator("contrasena_nueva")
    @classmethod
    def validar_contrasena(cls, v: str) -> str:
        return validar_contrasena_utils(v)
    
class UsuarioCambiarCorreo(BaseModel):
    correo_nuevo: str

class LoginSchema(BaseModel):
    correo: EmailStr
    contrasena: str