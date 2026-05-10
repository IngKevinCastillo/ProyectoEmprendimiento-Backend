from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.AlianzaSchema import AlianzaCrearSchema, AlianzaRespuestaSchema, AlianzaActualizarSchema
from Controllers.AlianzaControlador import crear_alianza_controlador, buscar_alianza_controlador, listar_alianzas_controlador, actualizar_alianza_controlador, activar_alianza_controlador, desactivar_alianza_controlador

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
async def listar_alianzas(activo: bool | None = None, db: Session = Depends(get_db)):
    return listar_alianzas_controlador(db, activo)

@router.get("/{id_alianza}", response_model=AlianzaRespuestaSchema)
async def obtener_alianza(
    id_alianza: str,
    db: Session = Depends(get_db)
):
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

@router.patch("/{id_alianza}/activar")
async def activar_alianza_endpoint(
    id_alianza: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)):
    verificar_usuario_admin(usuario_actual)
    return activar_alianza_controlador(db, id_alianza)

@router.patch("/{id_alianza}/desactivar")
async def desactivar_alianza_endpoint(
    id_alianza: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)):
    verificar_usuario_admin(usuario_actual)
    return desactivar_alianza_controlador(db,id_alianza)