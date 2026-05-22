from sqlalchemy.orm import Session
from Schemas.MesasSchema import MesasResultadoSchema
from Controllers.MesasControlador import buscar_mesa_por_docente_controlador, buscar_mesa_por_nombre_controlador, buscar_mesa_controlador, buscar_mesa_por_tutor_controlador, listar_mesas_controlador
from fastapi import HTTPException, status, Depends, APIRouter
from Configs.bd import get_db

router = APIRouter(
    prefix="/mesas",
    tags=["Mesas"]
)

@router.get("/{id}", response_model=MesasResultadoSchema, status_code=status.HTTP_200_OK)
async def buscar_mesa(
    id: int, 
    db: Session = Depends(get_db)
):
    existente = buscar_mesa_controlador(db, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La mesa especificada no existe.")
    return existente

@router.get("/", response_model=list[MesasResultadoSchema], status_code=status.HTTP_200_OK)
async def listar_mesas(
    db: Session = Depends(get_db)
):
    existentes = listar_mesas_controlador(db)
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen mesas disponibles.")
    return existentes

@router.get("/docente/{documento}", response_model=MesasResultadoSchema, status_code=status.HTTP_200_OK)
async def buscar_mesa_por_docente(
    documento: str, 
    db: Session = Depends(get_db)
):
    existente = buscar_mesa_por_docente_controlador(db, documento)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La mesa especificada no existe.")
    return existente

@router.get("/nombre/{nombre}", response_model=MesasResultadoSchema, status_code=status.HTTP_200_OK)
async def buscar_mesa_por_nombre(
    nombre: str, 
    db: Session = Depends(get_db)
):
    existente = buscar_mesa_por_nombre_controlador(db, nombre)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La mesa especificada no existe.")
    return existente

@router.get("/tutor/{documento}", response_model=MesasResultadoSchema, status_code=status.HTTP_200_OK)
async def buscar_mesa_por_tutor(
    documento: str, 
    db: Session = Depends(get_db)
):
    existente = buscar_mesa_por_tutor_controlador(db, documento)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La mesa especificada no existe.")
    return existente