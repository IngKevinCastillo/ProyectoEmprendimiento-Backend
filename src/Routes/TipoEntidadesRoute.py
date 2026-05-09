from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.TipoEntidadesSchema import TipoEntidadCrearSchema, TipoEntidadRespuestaSchema, TipoEntidadActualizarSchema
from Controllers.TipoEntidadesControlador import crear_tipo_entidad_controlador, buscar_tipo_entidad_controlador, listar_tipo_entidades_controlador, actualizar_tipo_entidad_controlador

router = APIRouter(
    prefix="/tipo-entidades",
    tags=["Tipo Entidades"],
)

@router.post("/", response_model=TipoEntidadRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_tipo_entidad(
    tipo_entidad: TipoEntidadCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    nuevo = crear_tipo_entidad_controlador(db, tipo_entidad)
    if not nuevo:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return nuevo

@router.get("/", response_model=list[TipoEntidadRespuestaSchema])
async def listar_tipo_entidades(
    db: Session = Depends(get_db)
):
    return listar_tipo_entidades_controlador(db)

@router.get("/{id_tipo_entidad}", response_model=TipoEntidadRespuestaSchema)
async def obtener_tipo_entidad(
    id_tipo_entidad: str,
    db: Session = Depends(get_db)
):
    tipo_entidad = buscar_tipo_entidad_controlador(db, id_tipo_entidad)
    if not tipo_entidad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de entidad no encontrado")
    return tipo_entidad

@router.put("/{id_tipo_entidad}", response_model=TipoEntidadRespuestaSchema)
async def actualizar_tipo_entidad(
    id_tipo_entidad: str,
    datos: TipoEntidadActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    tipo_entidad = actualizar_tipo_entidad_controlador(db, id_tipo_entidad, datos)
    if not tipo_entidad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de entidad no encontrado")
    return tipo_entidad