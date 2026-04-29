from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Facultadschema import FacultadCrearSchema, FacultadRespuestaSchema, FacultadActualizarSchema
from Configs.bd import get_db
from Schemas.Programaschema import ProgramaRespuestaSchema
from Core.Seguridad import obtener_usuario_actual
from Controllers.FacultadControlador import crear_facultad_contolador, obtener_facultades_contolador, buscar_facultad_contolador, eliminar_facultad_contolador, actualizar_facultad_contolador, buscar_facultad_nombre_contolador, obtener_programas_por_facultad_contolador

router = APIRouter(
    prefix="/facultades",
    tags=["Facultades"],
)


@router.post("/", response_model=FacultadRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_facultad(
    datos: FacultadCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    facultad = crear_facultad(db, datos)
    if not facultad:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return facultad


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

@router.put("/{id_facultad}", response_model=FacultadRespuestaSchema)
async def actualizar_facultad(
    id_facultad: int,
    datos: FacultadActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    facultad = actualizar_facultad_contolador(db, id_facultad, datos)
    if not facultad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad no encontrada")
    return facultad


@router.delete("/{id_facultad}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_facultad(
    id_facultad: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = eliminar_facultad_contolador(db, id_facultad)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad no encontrada")
    return eliminado