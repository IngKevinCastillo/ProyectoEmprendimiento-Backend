from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from Configs.bd import get_db
from Core.Seguridad import obtener_usuario_actual, verificar_usuario_admin
from Schemas.AlianzaSchema import AlianzaCrearSchema, AlianzaRespuestaSchema, AlianzaActualizarSchema
from Controllers.AlianzaControlador import crear_alianza_controlador, buscar_alianza_controlador, listar_alianzas_controlador, actualizar_alianza_controlador, cambiar_estado_alianza_controlador
from Controllers import StotageControlador
import json

router = APIRouter(
    prefix="/alianzas",
    tags=["Alianzas"],
)

@router.post("/", response_model=AlianzaRespuestaSchema, status_code=status.HTTP_201_CREATED)
async def crear_alianza(
    datos: str = Form(...),
    convenio: UploadFile = File(None),
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)

    try:
        alianza_data = AlianzaCrearSchema(**json.loads(datos))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Datos inválidos: {str(e)}")

    if convenio:
        contenido = await convenio.read()
        pdf_url = StotageControlador.subir_foto_controlador(contenido, convenio.filename)
        alianza_data.convenio_pdf_url = pdf_url

    nueva_alianza = crear_alianza_controlador(db, alianza_data)
    if not nueva_alianza:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Controller pendiente")
    return nueva_alianza

@router.get("/", response_model=list[AlianzaRespuestaSchema])
async def listar_alianzas(id_estado: int | None = None, db: Session = Depends(get_db)):
    return listar_alianzas_controlador(db, id_estado)

@router.get("/{id_alianza}", response_model=AlianzaRespuestaSchema)
async def obtener_alianza(id_alianza: str, db: Session = Depends(get_db)):
    alianza = buscar_alianza_controlador(db, id_alianza)
    if not alianza:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alianza no encontrada")
    return alianza

@router.put("/{id_alianza}", response_model=AlianzaRespuestaSchema)
async def actualizar_alianza(
    id_alianza: str,
    datos: str = Form(...),
    convenio: UploadFile = File(None),
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)

    try:
        alianza_data = AlianzaActualizarSchema(**json.loads(datos))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Datos inválidos: {str(e)}")

    if convenio:
        existente = buscar_alianza_controlador(db, id_alianza)
        contenido = await convenio.read()

        if existente.convenio_pdf_url is not None:
            StotageControlador.eliminar_foto_controlador(existente.convenio_pdf_url)

        pdf_url = StotageControlador.subir_foto_controlador(contenido, convenio.filename)
        alianza_data.convenio_pdf_url = pdf_url

    alianza = actualizar_alianza_controlador(db, id_alianza, alianza_data)
    if not alianza:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alianza no encontrada")
    return alianza

@router.patch("/{id_alianza}/estado/{id_estado}", response_model=AlianzaRespuestaSchema)
async def cambiar_estado_alianza(
    id_alianza: str,
    id_estado: int,
    db: Session = Depends(get_db),
    usuario_actual=Depends(obtener_usuario_actual)
):
    verificar_usuario_admin(usuario_actual)
    alianza = cambiar_estado_alianza_controlador(db, id_alianza, id_estado)
    if not alianza:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alianza no encontrada")
    return alianza