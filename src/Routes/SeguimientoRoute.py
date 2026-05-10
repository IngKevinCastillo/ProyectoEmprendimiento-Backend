from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.SeguimientoSchema import SeguimientoCrearSchema, SeguimientoRespuestaSchema, SeguimientoActualizarSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.SeguimientoControlador import (
    crear_seguimiento_controlador,
    obtener_seguimientos_controlador,
    obtener_seguimientos_por_estado_controlador,
    obtener_seguimiento_por_usuario_responsable_controlador,
    obtener_seguimientos_por_proyecto_controlador,
    buscar_seguimiento_controlador,
    buscar_ultimo_seguimiento_por_proyecto_controlador,
    eliminar_seguimiento_controlador,
    actualizar_seguimiento_controlador,
)

router = APIRouter(
    prefix="/seguimientos",
    tags=["Seguimientos"],
)


@router.post("/", response_model=SeguimientoRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_seguimiento(
    datos: SeguimientoCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return crear_seguimiento_controlador(db, datos)


@router.get("/", response_model=list[SeguimientoRespuestaSchema])
async def listar_seguimientos(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return obtener_seguimientos_controlador(db)


@router.get("/estado/{id_estado}", response_model=list[SeguimientoRespuestaSchema])
async def listar_seguimientos_por_estado(
    id_estado: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return obtener_seguimientos_por_estado_controlador(db, id_estado)


@router.get("/proyecto/{id_proyecto}", response_model=list[SeguimientoRespuestaSchema])
async def listar_seguimientos_por_proyecto(
    id_proyecto: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return obtener_seguimientos_por_proyecto_controlador(db, id_proyecto)


@router.get("/responsable/{id_usuario_responsable}", response_model=list[SeguimientoRespuestaSchema])
async def listar_seguimientos_por_responsable(
    id_usuario_responsable: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return obtener_seguimiento_por_usuario_responsable_controlador(db, id_usuario_responsable)


@router.get("/{id_seguimiento}", response_model=SeguimientoRespuestaSchema)
async def obtener_seguimiento(
    id_seguimiento: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    seguimiento = buscar_seguimiento_controlador(db, id_seguimiento)
    if not seguimiento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seguimiento no encontrado")
    return seguimiento

@router.get("/proyecto/ultimo/{id_proyecto}", response_model=SeguimientoRespuestaSchema)
async def obtener_ultimo_seguimiento_por_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    seguimiento = buscar_ultimo_seguimiento_por_proyecto_controlador(db, id_proyecto)
    if not seguimiento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontró ningún seguimiento para este proyecto")
    return seguimiento


@router.put("/{id_seguimiento}", response_model=SeguimientoRespuestaSchema)
async def actualizar_seguimiento(
    id_seguimiento: str,
    datos: SeguimientoActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return actualizar_seguimiento_controlador(db, id_seguimiento, datos)


@router.delete("/{id_seguimiento}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_seguimiento(
    id_seguimiento: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminar_seguimiento_controlador(db, id_seguimiento)