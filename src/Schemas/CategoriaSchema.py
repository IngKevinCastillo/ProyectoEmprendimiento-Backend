from  pydantic import BaseModel
    
class CategoriaRespuestaSchema(BaseModel):
    id_categoria: int
    nombre_categoria: str
    
    class Config:
        from_attributes = True