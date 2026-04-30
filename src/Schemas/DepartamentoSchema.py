from pydantic import BaseModel, field_validator
from Models.DepartamentoModelo import DepartamentoModelo

class DepartamentoRespuestaSchema(BaseModel):
    id_departamento: int
    nombre: str
    latitud:str
    longitud: str
    
    class Config:
        from_attributes = True