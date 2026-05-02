from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Tipodocumentoschema import TipoDocumentoRespuestaSchema
from Configs.bd import get_db
from Controllers.TipoDocumentoControlador import obtener_tipo_documento_controlador, obtener_tipo_documento_nombre_controlador, listar_tipos_documento_controlador

router = APIRouter(
    prefix="/tipo-documento",
    tags=["Tipo Documento"],
)

@router.get("/", response_model=list[TipoDocumentoRespuestaSchema])
async def listar_tipos_documento(
    db: Session = Depends(get_db),
):
    tipos_documento = listar_tipos_documento_controlador(db)
    return tipos_documento


@router.get("/{id_tipo_documento}", response_model=TipoDocumentoRespuestaSchema)
async def obtener_tipo_documento(
    id_tipo_documento: str, 
    db: Session = Depends(get_db),
):
    tipo_documento = obtener_tipo_documento_controlador(db, id_tipo_documento)
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return tipo_documento

@router.get("/nombre/{nombre}", response_model=TipoDocumentoRespuestaSchema)
async def obtener_tipo_documento_nombre(
    nombre: str, 
    db: Session = Depends(get_db),
):
    tipo_documento = obtener_tipo_documento_nombre_controlador(db, nombre)
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return tipo_documento