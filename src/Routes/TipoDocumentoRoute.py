from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Tipodocumentoschema import TipoDocumentoCrearSchema, TipoDocumentoRespuestaSchema, TipoDocumentoActualizarSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.TipoDocumentoControlador import crear_tipo_documento_controlador, obtener_tipo_documento_controlador, eliminar_tipo_documento_controlador, actualizar_tipo_documento_controlador, obtener_tipo_documento_nombre_controlador, listar_tipos_documento_controlador

router = APIRouter(
    prefix="/tipo-documento",
    tags=["Tipo Documento"],
)


@router.post("/", response_model=TipoDocumentoRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_tipo_documento(
    datos: TipoDocumentoCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    tipo_documento = crear_tipo_documento_controlador(db, datos)
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return tipo_documento


@router.get("/", response_model=list[TipoDocumentoRespuestaSchema])
async def listar_tipos_documento(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    tipos_documento = listar_tipos_documento_controlador(db)
    return tipos_documento


@router.get("/{id_tipo_documento}", response_model=TipoDocumentoRespuestaSchema)
async def obtener_tipo_documento(
    id_tipo_documento: str, 
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    tipo_documento = obtener_tipo_documento_controlador(db, id_tipo_documento)
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return tipo_documento

@router.get("/nombre/{nombre}", response_model=TipoDocumentoRespuestaSchema)
async def obtener_tipo_documento_nombre(
    nombre: str, 
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    tipo_documento = obtener_tipo_documento_nombre_controlador(db, nombre)
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return tipo_documento

@router.put("/{id_tipo_documento}", response_model=TipoDocumentoRespuestaSchema)
async def actualizar_tipo_documento(
    id_tipo_documento: str,
    datos: TipoDocumentoActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    tipo_documento = actualizar_tipo_documento_controlador(db, datos, id_tipo_documento)
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return tipo_documento


@router.delete("/{id_tipo_documento}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_tipo_documento(
    id_tipo_documento: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = eliminar_tipo_documento_controlador(db, id_tipo_documento)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return eliminado