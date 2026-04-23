from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Rolesschema import RolesCrearSchema, RolesRespuestaSchema
from Configs.bd import get_db
from Routes.UsuarioRoute import obtener_usuario_actual

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
    rol = None  # RolesController.crear(db, datos)
    if not rol:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return rol


@router.get("/", response_model=list[RolesRespuestaSchema])
async def listar_roles(db: Session = Depends(get_db)):
    roles = []  # RolesController.listar_todos(db)
    return roles


@router.get("/{id_rol}", response_model=RolesRespuestaSchema)
async def obtener_rol(id_rol: int, db: Session = Depends(get_db)):
    rol = None  # RolesController.obtener_por_id(db, id_rol)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return rol


@router.put("/{id_rol}", response_model=RolesRespuestaSchema)
async def actualizar_rol(
    id_rol: int,
    datos: RolesCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    rol = None  # RolesController.actualizar(db, id_rol, datos)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return rol


@router.delete("/{id_rol}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_rol(
    id_rol: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    eliminado = None  # RolesController.eliminar(db, id_rol)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return eliminado