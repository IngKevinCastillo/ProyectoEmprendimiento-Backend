from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Rolesschema import RolesRespuestaSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers import RolesControlador as RolesController
from Core.Seguridad import verificar_usuario_admin

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)

@router.get("/", response_model=list[RolesRespuestaSchema])
async def listar_roles(
    db: Session = Depends(get_db), 
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    roles = RolesController.obtener_roles_controlador(db)
    return roles


@router.get("/{id_rol}", response_model=RolesRespuestaSchema)
async def obtener_rol(
    id_rol: str, db: Session = Depends(get_db), 
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    rol = RolesController.buscar_rol_controlador(db, id_rol)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return rol

@router.get("/nombre/{nombre}", response_model=RolesRespuestaSchema)
async def obtener_rol_por_nombre(
    nombre: str, 
    db: Session = Depends(get_db), 
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    rol = RolesController.buscar_rol_por_nombre_controlador(db, nombre)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return rol