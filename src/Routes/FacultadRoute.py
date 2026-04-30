from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Facultadschema import FacultadRespuestaSchema
from Configs.bd import get_db
from Schemas.Programaschema import ProgramaRespuestaSchema
from Core.Seguridad import obtener_usuario_actual
from Controllers.FacultadControlador import obtener_facultades_contolador, buscar_facultad_contolador, buscar_facultad_nombre_contolador, obtener_programas_por_facultad_contolador

router = APIRouter(
    prefix="/facultades",
    tags=["Facultades"],
)

@router.get("/", response_model=list[FacultadRespuestaSchema])
async def listar_facultades(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    facultades = obtener_facultades_contolador(db)
    return facultades

@router.get("/programas/{id_facultad}", response_model=list[ProgramaRespuestaSchema])
async def listar_facultades_por_programas(
    id_facultad: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    facultades = obtener_programas_por_facultad_contolador(db, id_facultad)
    return facultades


@router.get("/{id_facultad}", response_model=FacultadRespuestaSchema)
async def obtener_facultad(
    id_facultad: str, 
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    facultad = buscar_facultad_contolador(db, id_facultad)
    if not facultad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad no encontrada")
    return facultad

@router.get("/nombre/{nombre}", response_model=FacultadRespuestaSchema)
async def obtener_facultad_nombre(
    nombre: str, 
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    facultad = buscar_facultad_nombre_contolador(db, nombre)
    if not facultad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad no encontrada")
    return facultad
