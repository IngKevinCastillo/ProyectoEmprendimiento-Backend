from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import HTTPException
from Controllers.MunicipioControlador import buscar_municipio_nombre_controlador, buscar_municipio_controlador, listar_municipios_controlador
from Configs.bd import get_db
from Schemas.MunicipioSchema import MunicipioRespuestaSchema

router = APIRouter(
    prefix="/municipios",
    tags=["Municipios"],
)

@router.get("/{id_municipio}", response_model=MunicipioRespuestaSchema)
async def buscar_municipio(
    id_municipio: int,
    db: Session = Depends(get_db) 
):
    municipio = buscar_municipio_controlador(db,id_municipio)
    if not municipio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Municipio no encontrado")
    return municipio 

@router.get("/nombre/{nombre}", response_model=MunicipioRespuestaSchema)
async def buscar_municipio_nombre(
    nombre: str,
    db: Session = Depends(get_db) 
):
    municipio = buscar_municipio_nombre_controlador(db, nombre)
    if not municipio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Municipio no encontrado")
    return municipio

@router.get("/", response_model=list[MunicipioRespuestaSchema])
async def listar_municipios(
    db: Session = Depends(get_db) 
):
    municipio = listar_municipios_controlador(db)
    if not municipio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay municipios disponibles")
    return municipio