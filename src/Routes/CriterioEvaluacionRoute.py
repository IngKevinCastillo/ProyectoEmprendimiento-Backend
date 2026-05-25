from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.CriterioEvaluacionSchema import CriterioCrearSchema, CriterioActualizarSchema, CriterioRespuestaSchema
from Controllers import CriterioEvaluacionControlador

router = APIRouter(
    prefix="/convocatorias/{id_convocatoria}/criterios",
    tags=["Criterios de Evaluación"],
)

@router.get("/", response_model=list[CriterioRespuestaSchema])
async def listar_criterios(
    id_convocatoria: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return CriterioEvaluacionControlador.obtener_criterios_controlador(db, id_convocatoria)

@router.post("/", response_model=CriterioRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_criterio(
    id_convocatoria: int,
    datos: CriterioCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return CriterioEvaluacionControlador.crear_criterio_controlador(db, id_convocatoria, datos)

@router.put("/{id_criterio}", response_model=CriterioRespuestaSchema)
async def actualizar_criterio(
    id_convocatoria: int,
    id_criterio: int,
    datos: CriterioActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    criterio = CriterioEvaluacionControlador.actualizar_criterio_controlador(db, id_criterio, datos)
    if not criterio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Criterio no encontrado")
    return criterio

@router.delete("/{id_criterio}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_criterio(
    id_convocatoria: int,
    id_criterio: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    resultado = CriterioEvaluacionControlador.eliminar_criterio_controlador(db, id_criterio)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Criterio no encontrado")