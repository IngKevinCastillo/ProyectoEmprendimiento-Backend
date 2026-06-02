from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.BeneficioAsignadoSchema import (
    BeneficioAsignadoCambiarEstadoSchema,
    BeneficioAsignadoCrearSchema,
    BeneficioAsignadoActualizarSchema,
    BeneficioAsignadoRespuestaSchema
)
from Controllers import BeneficioAsignadoControlador

router = APIRouter(
    prefix="/convocatorias/{id_convocatoria}/beneficios-asignados",
    tags=["Beneficios Asignados"],
)

@router.get("/", response_model=list[BeneficioAsignadoRespuestaSchema])
async def listar_beneficios_asignados(
    id_convocatoria: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return BeneficioAsignadoControlador.obtener_beneficios_asignados_por_convocatoria_controlador(db, id_convocatoria)

@router.get("/{id_beneficio_asignado}", response_model=BeneficioAsignadoRespuestaSchema)
async def obtener_beneficio_asignado(
    id_convocatoria: int,
    id_beneficio_asignado: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    beneficio_asignado = BeneficioAsignadoControlador.buscar_beneficio_asignado_controlador(db, id_beneficio_asignado)
    if not beneficio_asignado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Beneficio asignado no encontrado")
    return beneficio_asignado

@router.post("/", response_model=BeneficioAsignadoRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_beneficio_asignado(
    id_convocatoria: int,
    datos: BeneficioAsignadoCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return BeneficioAsignadoControlador.crear_beneficio_asignado_controlador(db, id_convocatoria, datos, usuario_actual.id_usuario)

@router.put("/{id_beneficio_asignado}", response_model=BeneficioAsignadoRespuestaSchema)
async def actualizar_beneficio_asignado(
    id_convocatoria: int,
    id_beneficio_asignado: int,
    datos: BeneficioAsignadoActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    beneficio_asignado = BeneficioAsignadoControlador.actualizar_beneficio_asignado_controlador(db, id_beneficio_asignado, datos)
    if not beneficio_asignado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Beneficio asignado no encontrado")
    return beneficio_asignado

@router.patch("/{id_beneficio_asignado}/estado", response_model=BeneficioAsignadoRespuestaSchema)
async def cambiar_estado_beneficio_asignado(
    id_convocatoria: int,
    id_beneficio_asignado: int,
    datos: BeneficioAsignadoCambiarEstadoSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    beneficio_asignado = BeneficioAsignadoControlador.cambiar_estado_beneficio_asignado_controlador(
        db, id_beneficio_asignado, datos.id_estado
    )
    if not beneficio_asignado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Beneficio asignado no encontrado")
    return beneficio_asignado

@router.delete("/{id_beneficio_asignado}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_beneficio_asignado(
    id_convocatoria: int,
    id_beneficio_asignado: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    resultado = BeneficioAsignadoControlador.eliminar_beneficio_asignado_controlador(db, id_beneficio_asignado)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Beneficio asignado no encontrado")

# --- Emprendedor: ver beneficios de su proyecto ---

router_proyecto = APIRouter(
    prefix="/proyectos/{id_proyecto}/beneficios-asignados",
    tags=["Beneficios Asignados"],
)

@router_proyecto.get("/", response_model=list[BeneficioAsignadoRespuestaSchema])
async def listar_beneficios_por_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return BeneficioAsignadoControlador.obtener_beneficios_asignados_por_proyecto_controlador(db, id_proyecto)