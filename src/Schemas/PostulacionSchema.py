from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostulacionCrearSchema(BaseModel):
    id_proyecto: int
    respuestas: Optional[str] = None

class PostulacionActualizarSchema(BaseModel):
    respuestas: Optional[str] = None

class PostulacionCambiarEstadoSchema(BaseModel):
    id_estado: int

class PostulacionRespuestaSchema(BaseModel):
    id_postulacion: int
    id_convocatoria: int
    id_proyecto: int
    id_estado: int
    respuestas: Optional[str]
    fecha_postulacion: Optional[datetime]

    class Config:
        from_attributes = True


#Integrantes postulacion
class IntegranteProyectoSchema(BaseModel):
    id_usuario: int
    primer_nombre: str
    segundo_nombre: Optional[str]
    primer_apellido: str
    segundo_apellido: str
    correo: str
    numero_documento: str
    telefono: str
    id_rol: int

    class Config:
        from_attributes = True

class IntegrantesPostulacionRespuestaSchema(BaseModel):
    id_proyecto: int
    propietario: IntegranteProyectoSchema
    integrantes: list[IntegranteProyectoSchema]

    class Config:
        from_attributes = True