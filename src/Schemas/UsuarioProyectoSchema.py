from pydantic import BaseModel

class UsuarioProyectoCrearSchema(BaseModel):
    id_proyecto: int
    id_usuario: int

class UsuarioProyectoRespuestaSchema(BaseModel):
    id_usuario_proyecto: int
    id_proyecto: int
    id_usuario: int
    
    class Config:
        from_attributes = True
        
class UsuarioProyectoActualizarSchema(BaseModel):
    id_proyecto: int
    id_usuario: int
    