from pydantic import BaseModel

class TipoProyectoRespuestaSchema(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True
