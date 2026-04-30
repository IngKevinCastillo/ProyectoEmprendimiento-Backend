from pydantic import BaseModel

class SedeRespuestaSchema(BaseModel):
    id_sede: int
    nombre: str
    ciudad: str

    class Config:
        from_attributes = True
