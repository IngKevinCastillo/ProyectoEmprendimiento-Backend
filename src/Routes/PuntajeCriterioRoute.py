from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Schemas.PuntajeCriterioSchema import (
    PuntajeCriterioCrearSchema,
    PuntajeCriterioActualizarSchema,
    PuntajeCriterioRespuestaSchema
)
from Controllers import PuntajeCriterioControlador

router = APIRouter(
    prefix="/evaluaciones/{id_evaluacion}/puntajes",
    tags=["Puntajes por Criterio"],
)

@router.get("/", response_model=list[PuntajeCriterioRespuestaSchema])
async def listar_puntajes(
    id_evaluacion: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return PuntajeCriterioControlador.obtener_puntajes_por_evaluacion_controlador(db, id_evaluacion)

@router.post("/", response_model=PuntajeCriterioRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_puntaje(
    id_evaluacion: int,
    datos: PuntajeCriterioCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return PuntajeCriterioControlador.crear_puntaje_controlador(db, id_evaluacion, datos)

@router.put("/{id_puntaje}", response_model=PuntajeCriterioRespuestaSchema)
async def actualizar_puntaje(
    id_evaluacion: int,
    id_puntaje: int,
    datos: PuntajeCriterioActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    puntaje = PuntajeCriterioControlador.actualizar_puntaje_controlador(db, id_puntaje, datos)
    if not puntaje:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Puntaje no encontrado")
    return puntaje

@router.delete("/{id_puntaje}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_puntaje(
    id_evaluacion: int,
    id_puntaje: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    resultado = PuntajeCriterioControlador.eliminar_puntaje_controlador(db, id_puntaje)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Puntaje no encontrado")