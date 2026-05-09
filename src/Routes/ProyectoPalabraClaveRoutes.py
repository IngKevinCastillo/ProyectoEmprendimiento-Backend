from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends, APIRouter
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers.ProyectoPalabraClaveControlador import actualizar_proyecto_palabra_clave_controlador, buscar_proyecto_palabra_clave_controlador, crear_proyecto_palabra_clave_controlador, elimina_proyecto_palabra_clave_controlador, listar_proyecto_palabra_clave_controlador
from Schemas.ProyectoPalabraClaveSchema import ProyectoPalabraClaveActualizarSchema, ProyectoPalabraClaveCrearSchema, ProyectoPalabraClaveRespuestaSchema

router = APIRouter(
    prefix="/proyecto-palabra-clave",
    tags=["Proyecto Palabra Clave"],
)

@router.post("/", response_model=ProyectoPalabraClaveCrearSchema, status_code=status.HTTP_201_CREATED)
async def crear_proyecto_palabra_clave(
    datos: ProyectoPalabraClaveCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual)
):
    proyecto_palabra_clave = crear_proyecto_palabra_clave_controlador(db, datos)
    if not proyecto_palabra_clave:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="No fue posible crear el proyecto palabra clave")
    return proyecto_palabra_clave

@router.get("/{id_proyecto_palabra_clave}", response_model=ProyectoPalabraClaveRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_proyecto_palabra_clave(
    id_proyecto_palabra_clave: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    existente = buscar_proyecto_palabra_clave_controlador(db, id_proyecto_palabra_clave)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El proyecto palabra clave especificado no existe.")
    return existente

@router.get("/listar/{id_proyecto}", response_model=list[ProyectoPalabraClaveRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_proyecto_palabra_clave(
    id_proyecto: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    existentes = listar_proyecto_palabra_clave_controlador(db, id_proyecto)
    if not existentes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningun proyecto palabra clave.")
    return existentes

@router.put("/{id_proyecto_palabra_clave}", response_model=ProyectoPalabraClaveActualizarSchema, status_code=status.HTTP_200_OK)
async def actualizar_proyecto_palabra_clave(
    id_proyecto_palabra_clave: int,
    datos: ProyectoPalabraClaveActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    proyecto_palabra_clave = actualizar_proyecto_palabra_clave_controlador(db, id_proyecto_palabra_clave, datos)
    if not proyecto_palabra_clave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El Proyecto palabra clave especificado no existe.")
    return proyecto_palabra_clave

@router.delete("/{id_proyecto_palabra_clave}", status_code=status.HTTP_200_OK)
async def elimina_proyecto_palabra_clave(
    id_proyecto_palabra_clave: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    proyecto_palabra_clave = elimina_proyecto_palabra_clave_controlador(db, id_proyecto_palabra_clave)
    if not proyecto_palabra_clave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El Proyecto palabra clave especificado no existe.")
    return proyecto_palabra_clave