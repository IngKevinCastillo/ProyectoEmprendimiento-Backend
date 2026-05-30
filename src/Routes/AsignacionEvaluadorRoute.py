from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.AsignacionEvaluadorSchema import AsignacionCrearSchema, AsignacionEvaluadorDetalleSchema, AsignacionRespuestaSchema
from Controllers import AsignacionEvaluadorControlador

router = APIRouter(
    prefix="/convocatorias/{id_convocatoria}/postulaciones/{id_postulacion}/asignaciones",
    tags=["Asignación de Evaluadores"],
)

@router.get("/", response_model=list[AsignacionRespuestaSchema])
async def listar_asignaciones(
    id_convocatoria: int,
    id_postulacion: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return AsignacionEvaluadorControlador.obtener_asignaciones_por_postulacion_controlador(db, id_postulacion)

@router.post("/", response_model=AsignacionRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_asignacion(
    id_convocatoria: int,
    id_postulacion: int,
    datos: AsignacionCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return AsignacionEvaluadorControlador.crear_asignacion_controlador(db, id_postulacion, datos)

@router.delete("/{id_asignacion}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_asignacion(
    id_convocatoria: int,
    id_postulacion: int,
    id_asignacion: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    resultado = AsignacionEvaluadorControlador.eliminar_asignacion_controlador(db, id_asignacion)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asignación no encontrada")

router_evaluador = APIRouter(
    prefix="/evaluador/{id_evaluador}/asignaciones",
    tags=["Asignación de Evaluadores"],
)

@router_evaluador.get("/", response_model=list[AsignacionEvaluadorDetalleSchema])
async def listar_mis_asignaciones(
    id_evaluador: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return AsignacionEvaluadorControlador.obtener_asignaciones_por_evaluador_controlador(db, id_evaluador)