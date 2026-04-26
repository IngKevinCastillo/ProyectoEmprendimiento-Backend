from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Facultadschema import FacultadCrearSchema, FacultadRespuestaSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual

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
    facultad = None  # FacultadController.crear(db, datos)
    if not facultad:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return facultad


@router.get("/", response_model=list[FacultadRespuestaSchema])
async def listar_facultades(db: Session = Depends(get_db)):
    facultades = []  # FacultadController.listar_todos(db)
    return facultades


@router.get("/{id_facultad}", response_model=FacultadRespuestaSchema)
async def obtener_facultad(id_facultad: int, db: Session = Depends(get_db)):
    facultad = None  # FacultadController.obtener_por_id(db, id_facultad)
    if not facultad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad no encontrada")
    return facultad


@router.put("/{id_facultad}", response_model=FacultadRespuestaSchema)
async def actualizar_facultad(
    id_facultad: int,
    datos: FacultadCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    facultad = None  # FacultadController.actualizar(db, id_facultad, datos)
    if not facultad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad no encontrada")
    return facultad


@router.delete("/{id_facultad}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_facultad(
    id_facultad: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = None  # FacultadController.eliminar(db, id_facultad)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Facultad no encontrada")
    return eliminado