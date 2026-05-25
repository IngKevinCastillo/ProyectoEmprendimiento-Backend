from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.BeneficioSchema import BeneficioCrearSchema, BeneficioActualizarSchema, BeneficioRespuestaSchema
from Controllers import BeneficioControlador

router = APIRouter(
    prefix="/beneficios",
    tags=["Beneficios"],
)

@router.get("/", response_model=list[BeneficioRespuestaSchema])
async def listar_beneficios(
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return BeneficioControlador.obtener_beneficios_controlador(db)

@router.get("/{id_beneficio}", response_model=BeneficioRespuestaSchema)
async def obtener_beneficio(
    id_beneficio: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    beneficio = BeneficioControlador.buscar_beneficio_controlador(db, id_beneficio)
    if not beneficio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Beneficio no encontrado")
    return beneficio

@router.post("/", response_model=BeneficioRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_beneficio(
    datos: BeneficioCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    return BeneficioControlador.crear_beneficio_controlador(db, datos)

@router.put("/{id_beneficio}", response_model=BeneficioRespuestaSchema)
async def actualizar_beneficio(
    id_beneficio: int,
    datos: BeneficioActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    beneficio = BeneficioControlador.actualizar_beneficio_controlador(db, id_beneficio, datos)
    if not beneficio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Beneficio no encontrado")
    return beneficio

@router.delete("/{id_beneficio}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_beneficio(
    id_beneficio: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    resultado = BeneficioControlador.eliminar_beneficio_controlador(db, id_beneficio)
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Beneficio no encontrado")