from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Schemas.CriterioEvaluacionSchema import CriterioRespuestaSchema
from Controllers import CriterioEvaluacionControlador

router = APIRouter(
    prefix="/criterios",
    tags=["Criterios de Evaluación"],
)

@router.get("/", response_model=list[CriterioRespuestaSchema])
async def listar_criterios(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return CriterioEvaluacionControlador.obtener_criterios_controlador(db)

@router.get("/{id_criterio}", response_model=CriterioRespuestaSchema)
async def obtener_criterio(
    id_criterio: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    criterio = CriterioEvaluacionControlador.buscar_criterio_controlador(db, id_criterio)
    if not criterio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Criterio no encontrado")
    return criterio