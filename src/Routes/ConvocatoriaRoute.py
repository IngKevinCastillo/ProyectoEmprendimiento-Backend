from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.ConvocatoriaSchema import (ConvocatoriaCrearSchema, ConvocatoriaActualizarSchema, ConvocatoriaRespuestaSchema)
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Controllers import ConvocatoriaControlador

router = APIRouter(
    prefix="/convocatorias",
    tags=["Convocatorias"],
)

# --- Admin ---

@router.get("/", response_model=list[ConvocatoriaRespuestaSchema])
async def listar_convocatorias(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return ConvocatoriaControlador.obtener_convocatorias_controlador(db)

@router.post("/", response_model=ConvocatoriaRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_convocatoria(
    datos: ConvocatoriaCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return ConvocatoriaControlador.crear_convocatoria_controlador(db, datos, usuario_actual.id_usuario)

@router.put("/{id_convocatoria}", response_model=ConvocatoriaRespuestaSchema)
async def actualizar_convocatoria(
    id_convocatoria: int,
    datos: ConvocatoriaActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    convocatoria = ConvocatoriaControlador.actualizar_convocatoria_controlador(db, id_convocatoria, datos)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    return convocatoria

@router.patch("/{id_convocatoria}/estado", response_model=ConvocatoriaRespuestaSchema)
async def cambiar_estado(
    id_convocatoria: int,
    nuevo_estado: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    convocatoria = ConvocatoriaControlador.cambiar_estado_convocatoria_controlador(db, id_convocatoria, nuevo_estado)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    return convocatoria

@router.delete("/{id_convocatoria}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_convocatoria(
    id_convocatoria: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    resultado = ConvocatoriaControlador.eliminar_convocatoria_controlador(db, id_convocatoria)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")

# --- Emprendedor ---

@router.get("/publicas", response_model=list[ConvocatoriaRespuestaSchema])
async def listar_convocatorias_publicas(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    return ConvocatoriaControlador.obtener_convocatorias_publicadas_controlador(db)

@router.get("/{id_convocatoria}", response_model=ConvocatoriaRespuestaSchema)
async def obtener_convocatoria(
    id_convocatoria: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    convocatoria = ConvocatoriaControlador.buscar_convocatoria_controlador(db, id_convocatoria)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    return convocatoria