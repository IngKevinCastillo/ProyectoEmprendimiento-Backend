from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Programaschema import ProgramaCrearSchema, ProgramaRespuestaSchema, ProgramaActualizarSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.ProgramaControlador import actualizar_programa_controlador, buscar_programa_controlador, buscar_programa_nombre_controlador, crear_programa_controlador, eliminar_programa_controlador, obtener_programas_controlador
router = APIRouter(
    prefix="/programas",
    tags=["Programas"],
)


@router.post("/", response_model=ProgramaRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_programa(
    datos: ProgramaCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    programa = crear_programa_controlador(db, datos)
    if not programa:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return programa


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


@router.put("/{id_programa}", response_model=ProgramaRespuestaSchema)
async def actualizar_programa(
    id_programa: int,
    datos: ProgramaActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    programa = actualizar_programa_controlador(db, datos, id_programa)
    if not programa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Programa no encontrado")
    return programa


@router.delete("/{id_programa}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_programa(
    id_programa: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = eliminar_programa_controlador(db, id_programa)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Programa no encontrado")
    return eliminado