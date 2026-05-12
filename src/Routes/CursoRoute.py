from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Configs.bd import get_db
from datetime import date
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.CursoSchema import CursoCrearSchema, CursoRespuestaSchema, CursoActualizarSchema
from Controllers.CursoControlador import cambiar_estado_controlador, crear_curso_controlador, buscar_curso_controlador,eliminar_curso_controlador, actualizar_curso_controlador, listar_cursos_contolador, buscar_curso_nombre_contolador
from Schemas.EstadosSchema import CambiarEstado

router = APIRouter(
    prefix="/cursos",
    tags=["Cursos"],
)

@router.post("/", response_model=CursoRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_curso(
    curso: CursoCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    nuevo_curso = crear_curso_controlador(db, curso)
    if not nuevo_curso:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return nuevo_curso

@router.get("/{id_curso}", response_model=CursoRespuestaSchema, status_code=status.HTTP_200_OK)
async def obtener_curso(
    id_curso: int, 
    db: Session = Depends(get_db)
):
    curso = buscar_curso_controlador(db, id_curso)
    return curso

@router.get("/nombre{nombre}", response_model=CursoRespuestaSchema, status_code=status.HTTP_200_OK)
async def obtener_curso_nombre(
    nombre: str, 
    db: Session = Depends(get_db)
):
    curso = buscar_curso_nombre_contolador(db, nombre)
    return curso

@router.get("/", response_model=list[CursoRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_cursos(
    db: Session = Depends(get_db)
):
    cursos = listar_cursos_contolador(db)
    return cursos

@router.put("/{id_curso}", response_model=CursoRespuestaSchema, status_code=status.HTTP_200_OK)
async def actualizar_curso(
    id_curso: int,
    datos: CursoActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    curso = actualizar_curso_controlador(db, id_curso, datos)
    return curso

@router.put("/cambiar-estado/{id_curso}", response_model=CursoRespuestaSchema, status_code=status.HTTP_200_OK)
async def cambiar_estado_curso(
    id_curso: int,
    datos: CambiarEstado,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    curso = cambiar_estado_controlador(db, id_curso, datos)
    return curso

@router.delete("/{id_curso}", status_code=status.HTTP_200_OK)
async def eliminar_curso(
    id_curso: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    eliminado = eliminar_curso_controlador(db, id_curso)
    return eliminado