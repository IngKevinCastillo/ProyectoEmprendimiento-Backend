from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from Configs.bd import get_db
from Controllers.MetasControlador import buscar_meta_controlador, obtener_metas_controlador, obtener_metas_por_anio_controlador, obtener_metas_por_estado_controlador, crear_meta_controlador, actualizar_meta_controlador, eliminar_meta_controlador
from Schemas.MetasSchema import MetasCrearSchema, MetasRespuestaSchema, MetasActualizarSchema

router = APIRouter(
    prefix="/metas",
    tags=["Metas"],
)

@router.get("/{id_meta}", response_model=MetasRespuestaSchema)
async def buscar_meta(
    id_meta: str,
    db: Session = Depends(get_db) 
):
    meta = buscar_meta_controlador(db, id_meta)
    if not meta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meta no encontrada")
    return meta


@router.get("/", response_model=list[MetasRespuestaSchema])
async def obtener_metas(
    db: Session = Depends(get_db) 
):
    metas = obtener_metas_controlador(db)
    if not metas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay metas disponibles")
    return metas


@router.get("/anio/{anio}", response_model=list[MetasRespuestaSchema])
async def obtener_metas_por_anio(
    anio: str,
    db: Session = Depends(get_db) 
):
    metas = obtener_metas_por_anio_controlador(db, anio)
    if not metas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay metas disponibles para el año especificado")
    return metas


@router.get("/estado/{estado}", response_model=list[MetasRespuestaSchema])
async def obtener_metas_por_estado(
    estado: str,
    db: Session = Depends(get_db) 
):
    metas = obtener_metas_por_estado_controlador(db, estado)
    if not metas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay metas disponibles para el estado especificado")
    return metas


@router.post("/", response_model=MetasRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_meta(
    meta: MetasCrearSchema,
    db: Session = Depends(get_db) 
):
    creado = crear_meta_controlador(db, meta)
    if not creado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se pudo crear la meta")
    return creado


@router.put("/{id_meta}", response_model=MetasRespuestaSchema)
async def actualizar_meta(
    id_meta: int,
    datos_actualizados: MetasActualizarSchema,
    db: Session = Depends(get_db) 
):
    actualizado = actualizar_meta_controlador(db, id_meta, datos_actualizados)
    if not actualizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se pudo actualizar la meta")
    return actualizado


@router.delete("/{id_meta}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_meta(
    id_meta: int,
    db: Session = Depends(get_db) 
):
    eliminado = eliminar_meta_controlador(db, id_meta)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meta no encontrada")
    return eliminado
