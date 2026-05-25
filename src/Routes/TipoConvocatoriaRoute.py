from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.TipoConvocatoriaSchema import (
    TipoConvocatoriaCrearSchema,
    TipoConvocatoriaActualizarSchema,
    TipoConvocatoriaRespuestaSchema
)
from Controllers import TipoConvocatoriaControlador

router = APIRouter(
    prefix="/tipo-convocatoria",
    tags=["Tipo Convocatoria"],
)

@router.get("/", response_model=list[TipoConvocatoriaRespuestaSchema])
async def listar_tipos_convocatoria(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return TipoConvocatoriaControlador.obtener_tipos_convocatoria_controlador(db)

@router.get("/{id_tipo_convocatoria}", response_model=TipoConvocatoriaRespuestaSchema)
async def obtener_tipo_convocatoria(
    id_tipo_convocatoria: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    tipo = TipoConvocatoriaControlador.buscar_tipo_convocatoria_controlador(db, id_tipo_convocatoria)
    if not tipo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de convocatoria no encontrado")
    return tipo

@router.post("/", response_model=TipoConvocatoriaRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_tipo_convocatoria(
    datos: TipoConvocatoriaCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return TipoConvocatoriaControlador.crear_tipo_convocatoria_controlador(db, datos)

@router.put("/{id_tipo_convocatoria}", response_model=TipoConvocatoriaRespuestaSchema)
async def actualizar_tipo_convocatoria(
    id_tipo_convocatoria: int,
    datos: TipoConvocatoriaActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    tipo = TipoConvocatoriaControlador.actualizar_tipo_convocatoria_controlador(db, id_tipo_convocatoria, datos)
    if not tipo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de convocatoria no encontrado")
    return tipo

@router.delete("/{id_tipo_convocatoria}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_tipo_convocatoria(
    id_tipo_convocatoria: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    resultado = TipoConvocatoriaControlador.eliminar_tipo_convocatoria_controlador(db, id_tipo_convocatoria)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de convocatoria no encontrado")