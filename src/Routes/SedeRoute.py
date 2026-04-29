from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.SedeControlador import crear_sede_contolador, obtener_sede_controlador, actualizar_sede_controlador, eliminar_sede_controlador, listar_sedes_controlador, obtener_sede_por_nombre_controlador
from Schemas.SedeSchemas import SedeCrearSchema, SedeActualizarSchema, SedeRespuestaSchema

router = APIRouter(
    prefix="/sedes",
    tags=["Sedes"],
)

@router.post("/", response_model=SedeRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_sede(
    datos: SedeCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    sede = crear_sede_contolador(db, datos)
    if not sede:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return sede

@router.get("/", response_model=list[SedeRespuestaSchema])
async def listar_sedes(
    db: Session = Depends(get_db), 
    usuario_actual=Depends(obtener_usuario_actual)
):
    sedes = listar_sedes_controlador(db)
    return sedes

@router.get("/{id_Sede}", response_model=SedeRespuestaSchema)
async def obtener_sede(
    id_Sede: str, db: Session = Depends(get_db), 
    usuario_actual=Depends(obtener_usuario_actual)
):
    sede = obtener_sede_controlador(db, id_Sede)
    if not sede:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sede no encontrada")
    return sede

@router.get("/nombre/{id_Sede}", response_model=SedeRespuestaSchema)
async def obtener_sede_nombre(
    id_Sede: str, db: Session = Depends(get_db), 
    usuario_actual=Depends(obtener_usuario_actual)
):
    sede = obtener_sede_por_nombre_controlador(db, id_Sede)
    if not sede:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sede no encontrada")
    return sede

@router.put("/{id_sede}", response_model=SedeRespuestaSchema)
async def actualizar_sede(
    id_sede: str,
    datos: SedeActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    sede = actualizar_sede_controlador(db, id_sede, datos)
    if not sede:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sede no encontrada")
    return sede


@router.delete("/{id_sede}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_sede(
    id_sede: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = eliminar_sede_controlador(db, id_sede)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sede no encontrada")
    return eliminado