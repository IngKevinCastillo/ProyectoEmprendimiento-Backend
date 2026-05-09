from pydantic import BaseModel

class FacultadRespuestaSchema(BaseModel):
    id_facultad: int
    nombre: str
    descripcion: str
    estado: str

    class Config:
        from_attributes = True
        