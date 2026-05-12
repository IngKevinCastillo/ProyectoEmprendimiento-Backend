from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Controllers.InscripcionControlador import cambiar_estado_controlador, actualizar_inscripcion_controlador, buscar_inscripcion_controlador, crear_inscripcion_controlador, eliminar_inscripcion_controlador, listar_inscripciones_curso_controlador, listar_inscripciones_usuario_controlador, verificar_registro_controlador
from Schemas.InscripcionSchema import InscripcionCrearSchema, InscripcionActualizarSchema, InscripcionRespuestaSchema, DatosVerificar
from Schemas.EstadosSchema import CambiarEstado

router=APIRouter(
    prefix="/inscripcion",
    tags=["Inscripcion"],
)

@router.get("/verificar-registro/", response_model=InscripcionRespuestaSchema, status_code=status.HTTP_200_OK)
async def verificar_registro(
    datos: DatosVerificar,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual)
):
    registro = verificar_registro_controlador(db, datos.id_usuario, datos.id_curso)
    if not registro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no tiene ninguna inscripcion en ese curso especificado")
    
    return registro

@router.get("/listar-inscripciones-usuario/{id_usuario}", response_model=list[InscripcionRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_inscripciones_usuario(
    id_usuario: int,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    inscripciones = listar_inscripciones_usuario_controlador(db, id_usuario)
    return inscripciones

@router.get("/listar-inscripciones-curso/{id_curso}", response_model=list[InscripcionRespuestaSchema], status_code=status.HTTP_200_OK)
async def listar_inscripciones_curso(
    id_curso: int,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    inscripciones = listar_inscripciones_curso_controlador(db, id_curso)
    return inscripciones

@router.post("/", response_model=InscripcionRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_inscripcion(
    datos: InscripcionCrearSchema,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual)
):
    inscripcion = crear_inscripcion_controlador(db, datos)
    if not inscripcion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Controlador pendiente")
    return inscripcion

@router.get("/obtener-inscripcion/{id_inscripcion}", response_model=InscripcionRespuestaSchema, status_code=status.HTTP_200_OK)
async def obtener_inscripcion(
    id_inscripcion: int,
    db: Session = Depends(get_db),
    usuario_actual = Depends(obtener_usuario_actual)
):
    inscripcion = buscar_inscripcion_controlador(db, id_inscripcion)
    return inscripcion

@router.put("/{id_inscripcion}", response_model=InscripcionActualizarSchema, status_code=status.HTTP_200_OK)
async def actualizar_inscripcion(
    id_inscripcion: int,
    datos: InscripcionActualizarSchema,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    inscripcion = actualizar_inscripcion_controlador(db, id_inscripcion, datos)
    return inscripcion

@router.put("/cambiar-estado/{id_inscripcion}", response_model=InscripcionRespuestaSchema, status_code=status.HTTP_200_OK)
async def actualizar_inscripcion(
    id_inscripcion: int,
    datos: CambiarEstado,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    inscripcion = cambiar_estado_controlador(db, id_inscripcion, datos)
    return inscripcion


@router.delete("/{id_inscripcion}", status_code=status.HTTP_200_OK)
async def eliminar_inscripcion(
    id_inscripcion: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    inscripcion = eliminar_inscripcion_controlador(db, id_inscripcion)
    return inscripcion