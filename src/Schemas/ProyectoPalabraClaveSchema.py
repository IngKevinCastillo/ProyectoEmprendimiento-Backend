from pydantic import BaseModel, field_validator
from Utils.Validacionesutilidades import validar_id_entero
from typing import Optional

class ProyectoPalabraClaveCrearSchema(BaseModel):
    id_proyecto: int
    id_palabra_clave: int
    
    @field_validator("id_proyecto", "id_palabra_clave")
    @classmethod
    def validar_int(cls, v: int) -> int:
        return validar_id_entero(v, "id", 1, 2147483647)


class ProyectoPalabraClaveActualizarSchema(BaseModel):
    id_proyecto: Optional[int] = None
    id_palabra_clave: Optional[int] = None
    
    @field_validator("id_proyecto", "id_palabra_clave")
    @classmethod
    def validar_int(cls, v: int) -> int:
        return validar_id_entero(v, "id", 1, 2147483647)
    
class ProyectoPalabraClaveRespuestaSchema(BaseModel):
    id_proyecto_palabra_clave: int
    id_proyecto: int
    id_palabra_clave: int
    
    class Config:
        from_attributes = True
      