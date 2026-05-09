from  pydantic import BaseModel, field_validator, model_validator
from Utils.Validacionesutilidades import validar_id_entero, validar_string
    
class CategoriaRespuestaSchema(BaseModel):
    id_categoria: int
    nombre_categoria: str
    
    class Config:
        from_attributes = True