from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.Usuarioschema import UsuarioCrearSchema, UsuarioRespuestaSchema, LoginSchema
from Configs.bd import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
)


@router.post("/", response_model=UsuarioRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_usuario(datos: UsuarioCrearSchema, db: Session = Depends(get_db)):
    usuario = None  # UsuarioController.crear(db, datos)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return usuario


@router.get("/", response_model=list[UsuarioRespuestaSchema])
async def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = []  # UsuarioController.listar_todos(db)
    return usuarios


@router.get("/{id_usuario}", response_model=UsuarioRespuestaSchema)
async def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = None  # UsuarioController.obtener_por_id(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.put("/{id_usuario}", response_model=UsuarioRespuestaSchema)
async def actualizar_usuario(id_usuario: int, datos: UsuarioCrearSchema, db: Session = Depends(get_db)):
    usuario = None  # UsuarioController.actualizar(db, id_usuario, datos)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.delete("/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    eliminado = None  # UsuarioController.eliminar(db, id_usuario)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return eliminado        


@router.post("/login")
async def login(datos: LoginSchema, db: Session = Depends(get_db)):
    token = None  # UsuarioController.login(db, datos)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return token