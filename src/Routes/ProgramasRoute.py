from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Programaschema import ProgramaRespuestaSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.ProgramaControlador import buscar_programa_controlador, obtener_programas_controlador
router = APIRouter(
    prefix="/programas",
    tags=["Programas"],
)


@router.get("/", response_model=list[ProgramaRespuestaSchema])
async def listar_programas(db: Session = Depends(get_db)):
    programas = obtener_programas_controlador(db)
    return programas


@router.get("/{id_programa}", response_model=ProgramaRespuestaSchema)
async def obtener_programa(id_programa: int, db: Session = Depends(get_db)):
    programa = buscar_programa_controlador(db, id_programa)
    if not programa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Programa no encontrado")
    return programa
