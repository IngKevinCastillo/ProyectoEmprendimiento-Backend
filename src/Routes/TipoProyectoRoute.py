from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.TipoProyectoSchema import TipoProyectoRespuestaSchema
from Configs.bd import get_db
from Controllers.TipoProyectoControlador import buscar_tipo_proyecto_controlador, buscar_tipo_proyecto_por_nombre_controlador, listar_tipos_proyectos_controlador

router = APIRouter(
    prefix="/tipo-proyecto",
    tags=["Tipo Proyecto"],
)

@router.get("/", response_model=list[TipoProyectoRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_tipos_proyectos(
    db: Session = Depends(get_db)
):
    existentes = listar_tipos_proyectos_controlador(db)
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen tipos proyecto.")
    return existentes


@router.get("/{id}", response_model=TipoProyectoRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_tipo_proyecto(
    id: int, 
    db: Session = Depends(get_db)
):
    existente = buscar_tipo_proyecto_controlador(db, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El tipo proyecto especificada no existe.")
    return existente

@router.get("/nombre-tipo-proyecto/{nombre}", response_model=TipoProyectoRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_tipo_proyecto_por_nombre(
    nombre: str, 
    db: Session = Depends(get_db)
):
    existente = buscar_tipo_proyecto_por_nombre_controlador(db, nombre)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El tipo proyecto especificada no existe.")
    return existente