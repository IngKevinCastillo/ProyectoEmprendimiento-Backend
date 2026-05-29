from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.MesasModelo import MesasModelo
from Models.UsuarioModelo import UsuarioModelo
from Models.UsuarioProyectoModelo import UsuarioProyectoModelo
from Utils.Mapeadorutilidades import auto_mapear
from Schemas.Usuarioschema import UsuarioActualizarSchema
from Schemas.EstadosSchema import CambiarEstado
from typing import Final
from Services.SupabaseClienteServicio import supabase

ESTADO_ELIMINADO: Final = 6

def buscar_usuario(db: Session, id: int):
    return db.query(UsuarioModelo).filter(UsuarioModelo.id_usuario == id).first()

def buscar_telefono(db:Session, telefono: str):
    return db.query(UsuarioModelo).filter(UsuarioModelo.telefono == telefono).first()

def buscar_usuario_por_correo(db: Session, correo: str):
    return db.query(UsuarioModelo).filter(UsuarioModelo.correo == correo).first()

def buscar_usuario_por_documento(db: Session, documento: int):
    return db.query(UsuarioModelo).filter(UsuarioModelo.numero_documento == str(documento)).first()

def BuscarTutorDeMesa(db: Session, id_mesa: int):
    return db.query(UsuarioModelo).join(MesasModelo, MesasModelo.cedula_tutor == UsuarioModelo.numero_documento).filter(MesasModelo.id == id_mesa).first()

def ListarUsuariosPorProyecto(db: Session, id_proyecto: int):
    return (db.query(UsuarioModelo).join(UsuarioProyectoModelo, UsuarioModelo.id_usuario == UsuarioProyectoModelo.id_usuario).filter(UsuarioProyectoModelo.id_proyecto == id_proyecto).all())

def listar_usuarios(db: Session):
    return db.query(UsuarioModelo).filter(UsuarioModelo.id_estado != ESTADO_ELIMINADO).all()

def cambiar_estado(db: Session, documento: int, estado: CambiarEstado):
    existente = buscar_usuario_por_documento(db, documento)
    
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario especificado no existe.")
    
    existente.id_estado = estado.id_estado_cambiar
    
    db.commit()
    db.refresh(existente)
    return existente

def eliminar_usuario(db: Session, numero_documento: int):
    usuario = buscar_usuario_por_documento(db, numero_documento)
    
    if not usuario or usuario.id_estado  == ESTADO_ELIMINADO:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")

    usuario.id_estado = ESTADO_ELIMINADO

    db.commit()
    db.refresh(usuario)
    return {"detail": "Usuario eliminado"}

def actualizar_usuario_id(db: Session, usuario: UsuarioActualizarSchema, id_usuario: int):
    existente = buscar_usuario(db, id_usuario)
    if not existente or existente.id_estado  == ESTADO_ELIMINADO:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")
    
    if(existente.id_rol is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un rol")
    
    if(existente.id_tipodocumento is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un tipo de documento")
    
    auto_mapear(existente, usuario, excluir=["id_usuario", "contrasena"])

    db.commit()
    db.refresh(existente)
    return existente

def actualizar_usuario_documento(db: Session, usuario: UsuarioActualizarSchema, documento: int):
    existente = buscar_usuario_por_documento(db, documento)
    if not existente or existente.id_estado  == ESTADO_ELIMINADO:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")
    
    if(existente.id_rol is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un rol")
    
    if(existente.id_tipodocumento is None):
        raise HTTPException(status_code=400, detail="El usuario debe estar asociado a un tipo de documento")
    
    auto_mapear(existente, usuario, excluir=["id_usuario", "contrasena", "correo"])

    db.commit()
    db.refresh(existente)
    return existente

def CambiarContrasena(db: Session, correo: str, contrasena_anterior: str, contrasena_nueva: str):
    from Core.Seguridad import HashearContrasena, VerificarContrasena
    existente = buscar_usuario_por_correo(db, correo)
    if not existente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if not VerificarContrasena(contrasena_anterior, existente.contrasena):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas. No se puede cambiar la contraseña")

    existente.contrasena = HashearContrasena(contrasena_nueva)
    db.commit()
    db.refresh(existente)

    try:
        usuario_supabase = supabase.auth.admin.list_users()
        usuario = next((u for u in usuario_supabase if u.email == correo), None)
        if usuario:
            supabase.auth.admin.update_user_by_id(
                usuario.id,
                {"password": contrasena_nueva}
            )
    except Exception as e:
        raise Exception(f"Error al actualizar en la nube: {str(e)}")

    return existente

def RecuperarContrasena(db: Session, correo: str, contrasena_nueva: str):
    from Core.Seguridad import HashearContrasena
    existente = buscar_usuario_por_correo(db, correo)
    if not existente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    existente.contrasena = HashearContrasena(contrasena_nueva)
    db.commit()
    db.refresh(existente)

    try:
        usuario_supabase = supabase.auth.admin.list_users()
        usuario = next((u for u in usuario_supabase if u.email == correo), None)
        if usuario:
            supabase.auth.admin.update_user_by_id(
                usuario.id,
                {"password": contrasena_nueva}
            )
    except Exception as e:
        raise Exception(f"Error al actualizar en la nube: {str(e)}")

    return existente

def CambiarCorreo(db: Session, correo_actual: str, correo_nuevo: str):
    existente = buscar_usuario_por_correo(db, correo_actual)
    if not existente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    existente.correo = correo_nuevo

    db.commit()
    db.refresh(existente)

    try:
        usuario_supabase = supabase.auth.admin.list_users()
        usuario = next((u for u in usuario_supabase if u.email == correo_actual), None)
        if usuario:
            supabase.auth.admin.update_user_by_id(
                usuario.id,
                {"email": correo_nuevo}
            )
    except Exception as e:
        raise Exception(f"Error al actualizar en la nube: {str(e)}")
    return existente