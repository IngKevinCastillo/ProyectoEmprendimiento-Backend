from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends
from Configs.bd import get_db
from Controllers.PalabraClaveControlador import crear_palabra_clave_controlador, actualizar_palabra_clave_controlador, buscar_palabra_clave_controlador, buscar_palabra_clave_palabra_controlador, listar_palabras_clave_controlador
from Schemas.PalabraClaveSchema import PalabraClaveActualizarSchema, PalabraClaveCrearSchema, PalabraClaveRespuestaSchema
from Core.Seguridad import obtener_usuario_actual

router = APIRouter(
    prefix="/palabra-clave",
    tags=["Palabra Clave"],
)

@router.post("/", response_model=PalabraClaveCrearSchema, status_code=status.HTTP_201_CREATED)
async def crear_palabra_clave(
    datos: PalabraClaveCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual)
):
    palabra_clave = crear_palabra_clave_controlador(db, datos)
    if not palabra_clave:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controlador pendiente")
    return palabra_clave

@router.get("/{id_palabra_clave}", response_model=PalabraClaveRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_palabra_clave(
    id_palabra_clave: int,
    db: Session = Depends(get_db)
):
    palabra_clave = buscar_palabra_clave_controlador(db, id_palabra_clave)
    if not palabra_clave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Palabra clave no encontrada")
    return palabra_clave

@router.get("/palabra-clave/{palabra}", response_model=PalabraClaveRespuestaSchema, status_code=status.HTTP_200_OK)
async def buscar_palabra_clave_palabra(
    palabra: str,
    db: Session = Depends(get_db)
):
    palabra_clave = buscar_palabra_clave_palabra_controlador(db, palabra)
    if not palabra_clave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Palabra clave no encontrada")
    return palabra_clave

@router.get("/", response_model=list[PalabraClaveRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_palabras_clave(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    palabra_clave = listar_palabras_clave_controlador(db)
    if not palabra_clave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay palabras claves disponibles")
    return palabra_clave

@router.put("/{id_palabra_clave}", response_model=PalabraClaveActualizarSchema, status_code=status.HTTP_200_OK)
async def actualizar_palabra_clave(
    id_palabra_clave: int,
    datos: PalabraClaveActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    palabra_clave = actualizar_palabra_clave_controlador(db, id_palabra_clave, datos)
    if not palabra_clave:
        raise HTTPException(status_code=status.HTTP_404_NO_CONTENT, detail="Palabra clave no encontrada")
    return palabra_clave