from pydantic import BaseModel

class ProgramaRespuestaSchema(BaseModel):
    id_programa: int
    nombre: str
    nivel: str
    id_facultad: int
    estado: str
    
    class Config:
        from_attributes = True

    