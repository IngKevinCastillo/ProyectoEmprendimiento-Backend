from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Tipodocumentoschema import TipoDocumentoCrearSchema, TipoDocumentoRespuestaSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual

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
    tipo_documento = None  # TipoDocumentoController.crear(db, datos)
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return tipo_documento


@router.get("/", response_model=list[TipoDocumentoRespuestaSchema])
async def listar_tipos_documento(db: Session = Depends(get_db)):
    tipos_documento = []  # TipoDocumentoController.listar_todos(db)
    return tipos_documento


@router.get("/{id_tipo_documento}", response_model=TipoDocumentoRespuestaSchema)
async def obtener_tipo_documento(id_tipo_documento: int, db: Session = Depends(get_db)):
    tipo_documento = None  # TipoDocumentoController.obtener_por_id(db, id_tipo_documento)
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return tipo_documento


@router.put("/{id_tipo_documento}", response_model=TipoDocumentoRespuestaSchema)
async def actualizar_tipo_documento(
    id_tipo_documento: int,
    datos: TipoDocumentoCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    tipo_documento = None  # TipoDocumentoController.actualizar(db, id_tipo_documento, datos)
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return tipo_documento


@router.delete("/{id_tipo_documento}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_tipo_documento(
    id_tipo_documento: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = None  # TipoDocumentoController.eliminar(db, id_tipo_documento)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return eliminado