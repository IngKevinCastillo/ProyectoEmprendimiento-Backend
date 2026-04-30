from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.SedeControlador import obtener_sede_controlador, listar_sedes_controlador, obtener_sede_por_nombre_controlador
from Schemas.SedeSchemas import SedeRespuestaSchema

router = APIRouter(
    prefix="/sedes",
    tags=["Sedes"],
)

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

@router.get("/nombre/{nombre}", response_model=SedeRespuestaSchema)
async def obtener_sede_nombre(
    nombre: str, db: Session = Depends(get_db), 
    usuario_actual=Depends(obtener_usuario_actual)
):
    sede = obtener_sede_por_nombre_controlador(db, nombre)
    if not sede:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sede no encontrada")
    return sede