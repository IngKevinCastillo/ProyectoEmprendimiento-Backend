from pydantic import BaseModel, field_validator
from Models.MunicipioModelo import MunicipioModelo
from Utils.Validacionesutilidades import validar_nombre, validar_id_entero

class MunicipioRespuestaSchema(BaseModel):
    id_municipio: int
    nombre: str
    id_departamento: int
    latitud: str
    longitud: str
    
    class Config:
        from_attributes = True
