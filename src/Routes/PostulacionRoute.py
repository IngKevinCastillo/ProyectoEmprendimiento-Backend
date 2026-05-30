from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.PostulacionSchema import (PostulacionCrearSchema, PostulacionActualizarSchema, PostulacionCambiarEstadoSchema, PostulacionRespuestaSchema, IntegrantesPostulacionRespuestaSchema)
from Controllers import PostulacionControlador


router = APIRouter(
    prefix="/convocatorias/{id_convocatoria}/postulaciones",
    tags=["Postulaciones"],
)

@router.post("/", response_model=PostulacionRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_postulacion(
    id_convocatoria: int,
    datos: PostulacionCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return PostulacionControlador.crear_postulacion_controlador(db, id_convocatoria, datos)

@router.get("/", response_model=list[PostulacionRespuestaSchema])
async def listar_postulaciones(
    id_convocatoria: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return PostulacionControlador.obtener_postulaciones_por_convocatoria_controlador(db, id_convocatoria)

@router.get("/{id_postulacion}", response_model=PostulacionRespuestaSchema)
async def obtener_postulacion(
    id_convocatoria: int,
    id_postulacion: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    postulacion = PostulacionControlador.buscar_postulacion_controlador(db, id_postulacion)
    if not postulacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Postulación no encontrada")
    return postulacion

@router.get("/{id_postulacion}/integrantes", response_model=IntegrantesPostulacionRespuestaSchema)
async def obtener_integrantes_postulacion(
    id_convocatoria: int,
    id_postulacion: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return PostulacionControlador.obtener_integrantes_postulacion_controlador(db, id_postulacion)

@router.put("/{id_postulacion}", response_model=PostulacionRespuestaSchema)
async def actualizar_postulacion(
    id_convocatoria: int,
    id_postulacion: int,
    datos: PostulacionActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    postulacion = PostulacionControlador.actualizar_postulacion_controlador(db, id_postulacion, datos)
    if not postulacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Postulación no encontrada")
    return postulacion

@router.patch("/{id_postulacion}/estado", response_model=PostulacionRespuestaSchema)
async def cambiar_estado_postulacion(
    id_convocatoria: int,
    id_postulacion: int,
    datos: PostulacionCambiarEstadoSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    postulacion = PostulacionControlador.cambiar_estado_postulacion_controlador(db, id_postulacion, datos.id_estado)
    if not postulacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Postulación no encontrada")
    return postulacion

@router.delete("/{id_postulacion}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_postulacion(
    id_convocatoria: int,
    id_postulacion: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    resultado = PostulacionControlador.eliminar_postulacion_controlador(db, id_postulacion)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Postulación no encontrada")

router_proyecto = APIRouter(
    prefix="/proyectos/{id_proyecto}/postulaciones",
    tags=["Postulaciones"],
)

@router_proyecto.get("/", response_model=list[PostulacionRespuestaSchema])
async def listar_postulaciones_por_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return PostulacionControlador.obtener_postulaciones_por_proyecto_controlador(db, id_proyecto)