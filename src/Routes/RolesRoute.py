from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Rolesschema import RolesCrearSchema, RolesRespuestaSchema
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual
from Controllers import RolesControlador as RolesController
from Core.Seguridad import verificar_usuario_admin

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.post("/", response_model=RolesRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_rol(
    datos: RolesCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    rol = RolesController.crear_rol_controlador(db, datos)
    if not rol:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return rol


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

@router.put("/{id_rol}", response_model=RolesRespuestaSchema)
async def actualizar_rol(
    id_rol: str,
    datos: RolesCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    rol = RolesController.actualizar_rol_controlador(db, id_rol, datos)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return rol


@router.delete("/{id_rol}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_rol(
    id_rol: str,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    eliminado = RolesController.eliminar_rol_controlador(db, id_rol)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return eliminado