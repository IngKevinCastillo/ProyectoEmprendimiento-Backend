from pydantic import BaseModel, field_validator, ValidationInfo
from datetime import date
from typing import Optional
from Utils.Validacionesutilidades import validar_nombre_utils, validar_descripcion_utils, validar_id_entero, validar_calificacion


class ProyectoBaseSchema(BaseModel):
    nombre_proyecto: Optional[str] = None
    descripcion: Optional[str] = None
    id_estado: Optional[int] = None
    id_categoria: Optional[int] = None
    problematica: Optional[str] = None
    publico_objetivo: Optional[str] = None
    propuesta_de_valor: Optional[str] = None
    solucion: Optional[str] = None
    recursos_clave: Optional[str] = None
    modelo_de_negocio: Optional[str] = None
    calificacion: Optional[float] = None

    @field_validator("nombre_proyecto")
    @classmethod
    def validar_nombre_proyecto(cls, v: Optional[str]) -> str:
        return validar_nombre_utils(v, min_len=3, max_len=100, campo="Nombre del proyecto")

    @field_validator("descripcion")
    @classmethod
    def validar_descripcion_proyecto(cls, v: Optional[str]) -> str:
        return validar_descripcion_utils(v, min_len=20, max_len=2000, campo="Descripción del proyecto")

    @field_validator("id_estado")
    @classmethod
    def validar_id_estado(cls, v: Optional[int]) -> int:
        return validar_id_entero(v, campo="ID del estado del proyecto") 

    @field_validator("id_categoria")
    @classmethod
    def validar_id_categoria(cls, v: Optional[int]) -> int:
        return validar_id_entero(v, campo="ID de la categoría")

    @field_validator("calificacion")
    @classmethod
    def validar_calificacion(cls, v: Optional[float]) -> float:
        return validar_calificacion(v)
    
    @field_validator("problematica", "publico_objetivo", "propuesta_de_valor", "solucion", "recursos_clave", "modelo_de_negocio")
    @classmethod
    def validar_campos_opcionales(cls, v: Optional[str], info: ValidationInfo) -> Optional[str]:
        return validar_descripcion_utils(v, min_len=20, max_len=2000, campo=info.field_name)

    

class ProyectoCrearSchema(ProyectoBaseSchema):
    nombre_proyecto: str
    descripcion: str
    id_estado: int
    id_categoria: int


class ProyectoRespuestaSchema(BaseModel):
    id_proyecto: int
    nombre_proyecto: str
    descripcion: str
    id_estado: int
    id_categoria: int
    fecha_creacion: date
    problematica: Optional[str] = None
    publico_objetivo: Optional[str] = None
    propuesta_de_valor: Optional[str] = None
    solucion: Optional[str] = None
    recursos_clave: Optional[str] = None
    modelo_de_negocio: Optional[str] = None
    calificacion: Optional[float] = None

    class Config:
        from_attributes = True

class ProyectoActualizarSchema(ProyectoBaseSchema):
    nombre_proyecto: Optional[str] = None
    descripcion: Optional[str] = None
    id_estado: Optional[int] = None
    id_categoria: Optional[int] = None
    calificacion: Optional[float] = None
    problematica: Optional[str] = None
    publico_objetivo: Optional[str] = None
    propuesta_de_valor: Optional[str] = None
    solucion: Optional[str] = None
    recursos_clave: Optional[str] = None
    modelo_de_negocio: Optional[str] = None