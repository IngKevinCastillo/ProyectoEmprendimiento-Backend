from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import HTTPException
from Controllers.DepartamentoControlador import buscar_departamento_controlador, buscar_departamento_nombre_controlador, listar_departamentos_controlador
from Configs.bd import get_db
from Schemas.DepartamentoSchema import DepartamentoRespuestaSchema

router = APIRouter(
    prefix="/departamentos",
    tags=["Departamentos"],
)

@router.get("/{id_departamento}", response_model=DepartamentoRespuestaSchema)
async def buscar_departamento(
    id_departamento: int,
    db: Session = Depends(get_db) 
):
    departamento = buscar_departamento_controlador(db,id_departamento)
    if not departamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departamento no encontrado")
    return departamento

@router.get("/nombre/{nombre}", response_model=DepartamentoRespuestaSchema)
async def buscar_departamento_nombre(
    nombre: str,
    db: Session = Depends(get_db) 
):
    departamento = buscar_departamento_nombre_controlador(db, nombre)
    if not departamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departamento no encontrado")
    return departamento

@router.get("/", response_model=list[DepartamentoRespuestaSchema])
async def listar_departamentos(
    db: Session = Depends(get_db) 
):
    departamento = listar_departamentos_controlador(db)
    if not departamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay departamentos disponibles")
    return departamento