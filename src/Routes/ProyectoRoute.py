from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.ProyectoSchema import ProyectoCrearSchema, ProyectoRespuestaSchema, ProyectoActualizarSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.ProyectoControlador import (
    crear_emprendimiento_controlador,
    obtener_emprendimientos_controlador,
    obtener_emprendimientos_por_estado_controlador,
    obtener_emprendimientos_por_categoria_controlador,
    buscar_emprendimiento_controlador,
    buscar_emprendimiento_por_nombre_controlador,
    eliminar_emprendimiento_controlador,
    actualizar_emprendimiento_controlador
)

router = APIRouter(
    prefix="/proyectos",
    tags=["Proyectos"],
)


@router.post("/", response_model=ProyectoRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_proyecto(
    datos: ProyectoCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    proyecto = crear_emprendimiento_controlador(db, datos)
    if not proyecto:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="No fue posible crear el proyecto")
    return proyecto


@router.get("/", response_model=list[ProyectoRespuestaSchema])
async def listar_proyectos(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return obtener_emprendimientos_controlador(db)


@router.get("/nombre/{nombre_proyecto}", response_model=ProyectoRespuestaSchema)
async def obtener_proyecto_por_nombre(
    nombre_proyecto: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    proyecto = buscar_emprendimiento_por_nombre_controlador(db, nombre_proyecto)
    if not proyecto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proyecto no encontrado")
    return proyecto


@router.get("/estado/{id_estado}", response_model=list[ProyectoRespuestaSchema])
async def listar_proyectos_por_estado(
    id_estado: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return obtener_emprendimientos_por_estado_controlador(db, id_estado)


@router.get("/categoria/{id_categoria}", response_model=list[ProyectoRespuestaSchema])
async def listar_proyectos_por_categoria(
    id_categoria: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return obtener_emprendimientos_por_categoria_controlador(db, id_categoria)


@router.get("/{id_proyecto}", response_model=ProyectoRespuestaSchema)
async def obtener_proyecto(
    id_proyecto: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    proyecto = buscar_emprendimiento_controlador(db, id_proyecto)
    if not proyecto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proyecto no encontrado")
    return proyecto


@router.put("/{id_proyecto}", response_model=ProyectoRespuestaSchema)
async def actualizar_proyecto(
    id_proyecto: str,
    datos: ProyectoActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    proyecto = actualizar_emprendimiento_controlador(db, datos, id_proyecto)
    if not proyecto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proyecto no encontrado")
    return proyecto


@router.delete("/{id_proyecto}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_proyecto(
    id_proyecto: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminar_emprendimiento_controlador(db, id_proyecto)