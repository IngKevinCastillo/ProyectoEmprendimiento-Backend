from pydantic import BaseModel

class RolesRespuestaSchema(BaseModel):
    id_rol: int
    nombre: str
    id_estado: int

    class Config:
        from_attributes = True
