from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Controllers.ConvocatoriasControlador import actualizar_convocatoria_controlador, buscar_convocatoria_controlador, buscar_convocatoria_titulo_controlador, crear_convocatoria_controlador, eliminar_convocatoria_controlador, listar_convocatorias_por_estado_controlador, listar_convocatorias_por_tipo_controlador
from Schemas.ConvocatoriasSchema import ConvocatoriasActualizarSchema, ConvocatoriasCrearSchema, ConvocatoriasRespuestaSchema

router = APIRouter(
    prefix="/convocatorias",
    tags=["Convocatorias"],
)

@router.post("/", response_model=ConvocatoriasCrearSchema, status_code=status.HTTP_201_CREATED)
async def crear_convocatoria(
    datos: ConvocatoriasCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual),
):
    verificar_usuario_admin(usuario_actual)
    convocatoria = crear_convocatoria_controlador(db, datos)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controlador pendiente")
    return convocatoria

@router.get("/titulo/{titulo_convocatoria}", response_model=ConvocatoriasRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_convocatoria_titulo(
    titulo_convocatoria: str,
    db: Session = Depends(get_db)
):
    convocatoria = buscar_convocatoria_titulo_controlador(db, titulo_convocatoria)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    return convocatoria

@router.get("/{id_convocatoria}", response_model=ConvocatoriasRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_convocatoria(
    id_convocatoria: int,
    db: Session = Depends(get_db)
):
    convocatoria = buscar_convocatoria_controlador(db, id_convocatoria)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    return convocatoria

@router.get("/convocatorias-tipo/{tipo_convocatoria}", response_model=list[ConvocatoriasRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_convocatorias_por_tipo(
    tipo_convocatoria: str,
    db: Session = Depends(get_db)
):
    convocatoria = listar_convocatorias_por_tipo_controlador(db, tipo_convocatoria)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatorias no encontradas")
    return convocatoria

@router.get("/estado/{estado_convocatoria}", response_model=list[ConvocatoriasRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_convocatorias_por_estado(
    estado_convocatoria: str,
    db: Session = Depends(get_db)
):
    convocatoria = listar_convocatorias_por_estado_controlador(db, estado_convocatoria)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatorias no encontradas")
    return convocatoria

@router.put("/{id_convocatoria}", response_model=ConvocatoriasActualizarSchema, status_code=status.HTTP_200_OK)
async def actualizar_convocatoria(
    id_convocatoria: int,
    datos: ConvocatoriasActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    convocatoria = actualizar_convocatoria_controlador(db, id_convocatoria, datos)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    return convocatoria

@router.delete("/{id_convocatoria}", status_code=status.HTTP_200_OK)
async def eliminar_convocatoria(
    id_convocatoria: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    convocatoria = eliminar_convocatoria_controlador(db, id_convocatoria)
    if not convocatoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Convocatoria no encontrada")
    return convocatoria