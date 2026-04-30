from pydantic import BaseModel

class SedeRespuestaSchema(BaseModel):
    nombre: str
    ciudad: str

    class Config:
        from_attributes = True
