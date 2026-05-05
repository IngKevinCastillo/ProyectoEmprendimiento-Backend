from pydantic import BaseModel
from Utils.Validacionesutilidades import validar_nombre_usuario

class TipoDocumentoRespuestaSchema(BaseModel):
    id_tipo_documento: int
    nombre: str
    abreviatura: str
    estado: str

    class Config:
        from_attributes = True