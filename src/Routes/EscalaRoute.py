from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.EscalaSchema import EscalaRespuestaSchema
from Configs.bd import get_db
from Controllers.EscalaModeloControlador import buscar_escala_controlador, buscar_escala_nombre_controlador, listar_escalas_controlador

router = APIRouter(
    prefix="/escala",
    tags=["Escala"],
)

@router.get("/", response_model=list[EscalaRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_escalas(
    db: Session = Depends(get_db)
):
    existentes = listar_escalas_controlador(db)
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existen escalas.")
    return existentes


@router.get("/{id}", response_model=EscalaRespuestaSchema, status_code=status.HTTP_200_OK)
async def obtener_escala(
    id: int, 
    db: Session = Depends(get_db)
):
    existente = buscar_escala_controlador(db, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La escala especificada no existe.")
    return existente

@router.get("/nombre-escala/{nombre}", response_model=EscalaRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_escala_nombre(
    nombre: str, 
    db: Session = Depends(get_db)
):
    existente = buscar_escala_nombre_controlador(db, nombre)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La escala especificada no existe.")
    return existente