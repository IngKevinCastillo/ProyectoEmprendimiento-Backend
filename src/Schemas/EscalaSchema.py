from pydantic import BaseModel

class EscalaRespuestaSchema(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True
