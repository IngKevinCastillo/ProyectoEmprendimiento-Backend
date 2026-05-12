from pydantic import BaseModel, field_validator
from Utils.Validacionesutilidades import validar_string

class PalabraClaveCrearSchema(BaseModel):
    palabra: str
    
    @field_validator("palabra")
    @classmethod
    def validar_palabra(cls, v: str) -> str:
        return validar_string(v, 3, 50, "palabra")
    
class PalabraClaveRespuestaSchema(BaseModel):
    id_palabra_clave: int
    palabra: str
    
    class Config:
        from_attributes = True
        
class PalabraClaveActualizarSchema(BaseModel):
    palabra: str
    
    @field_validator("palabra")
    @classmethod
    def validar_palabra(cls, v: str) -> str:
        return validar_string(v, 3, 50, "palabra")