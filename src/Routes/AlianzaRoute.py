from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.AlianzaSchema import AlianzaCrearSchema, AlianzaRespuestaSchema, AlianzaActualizarSchema
from Controllers.AlianzaControlador import crear_alianza_controlador, buscar_alianza_controlador, listar_alianzas_controlador, actualizar_alianza_controlador, cambiar_estado_alianza_controlador

router = APIRouter(
    prefix="/alianzas",
    tags=["Alianzas"],
)

@router.post("/", response_model=AlianzaRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_alianza(
    alianza: AlianzaCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    nueva_alianza = crear_alianza_controlador(db, alianza)
    if not nueva_alianza:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return nueva_alianza

@router.get("/", response_model=list[AlianzaRespuestaSchema])
async def listar_alianzas(id_estado: int | None = None, db: Session = Depends(get_db)):
    return listar_alianzas_controlador(db, id_estado)

@router.get("/{id_alianza}", response_model=AlianzaRespuestaSchema)
async def obtener_alianza(id_alianza: str, db: Session = Depends(get_db)):
    alianza = buscar_alianza_controlador(db, id_alianza)
    if not alianza:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alianza no encontrada")
    return alianza

@router.put("/{id_alianza}", response_model=AlianzaRespuestaSchema)
async def actualizar_alianza(
    id_alianza: str,
    datos: AlianzaActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
    ):
    verificar_usuario_admin(usuario_actual)
    alianza = actualizar_alianza_controlador(db, id_alianza, datos)
    if not alianza:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alianza no encontrada")
    return alianza

@router.patch("/{id_alianza}/estado/{id_estado}", response_model=AlianzaRespuestaSchema)
async def cambiar_estado_alianza(
    id_alianza: str,
    id_estado: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    alianza = cambiar_estado_alianza_controlador(db, id_alianza, id_estado)
    if not alianza:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alianza no encontrada")
    return alianza