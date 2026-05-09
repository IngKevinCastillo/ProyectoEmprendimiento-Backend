from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, APIRouter
from Configs.bd import get_db
from Schemas.CategoriaSchema import CategoriaRespuestaSchema
from Controllers.CategoriaControlador import buscar_categoria_controlador, buscar_categoria_nombre_controlador, listar_categorias_controlador

router = APIRouter(
    prefix="/categoria",
    tags=["Categoria"],
)

@router.get("/{id_categoria}", response_model=CategoriaRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_categoria(
    id_categoria: int,
    db: Session = Depends(get_db)
):
    existente = buscar_categoria_controlador(db, id_categoria)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La categoria especificada no existe.")
    return existente

@router.get("/nombre/{nombre_categoria}", response_model=CategoriaRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_categoria_nombre(
    nombre_categoria: str,
    db: Session = Depends(get_db)
):
    existente = buscar_categoria_nombre_controlador(db, nombre_categoria)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La categoria especificada no existe.")
    return existente

@router.get("/", response_model=list[CategoriaRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_categorias(
    db: Session = Depends(get_db)
):
    existente = listar_categorias_controlador(db)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay categorias disponibles.")
    return existente