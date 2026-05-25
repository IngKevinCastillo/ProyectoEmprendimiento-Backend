from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.EvaluacionSchema import EvaluacionCrearSchema, EvaluacionRespuestaSchema
from Controllers import EvaluacionControlador

router = APIRouter(
    prefix="/asignaciones/{id_asignacion}/evaluacion",
    tags=["Evaluaciones"],
)

@router.get("/", response_model=EvaluacionRespuestaSchema)
async def obtener_evaluacion(
    id_asignacion: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    evaluacion = EvaluacionControlador.buscar_evaluacion_por_asignacion_controlador(db, id_asignacion)
    if not evaluacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evaluación no encontrada")
    return evaluacion

@router.post("/", response_model=EvaluacionRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_evaluacion(
    id_asignacion: int,
    datos: EvaluacionCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return EvaluacionControlador.crear_evaluacion_controlador(db, id_asignacion, datos)

@router.put("/{id_evaluacion}", response_model=EvaluacionRespuestaSchema)
async def actualizar_comentario(
    id_asignacion: int,
    id_evaluacion: int,
    datos: EvaluacionCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    evaluacion = EvaluacionControlador.actualizar_comentario_controlador(db, id_evaluacion, datos)
    if not evaluacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evaluación no encontrada")
    return evaluacion

@router.patch("/{id_evaluacion}/completar", response_model=EvaluacionRespuestaSchema)
async def completar_evaluacion(
    id_asignacion: int,
    id_evaluacion: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    evaluacion = EvaluacionControlador.completar_evaluacion_controlador(db, id_evaluacion)
    if not evaluacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evaluación no encontrada")
    return evaluacion