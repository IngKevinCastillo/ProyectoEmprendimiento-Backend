from sqlalchemy.orm import Session
from Services.RolServicio import BuscarRolPorNombre
from Services.EstadosServicio import BuscarEstadosPorNombre

_cache = {}

def obtener_id_rol(db: Session, nombre: str) -> int:
    if f"rol_{nombre}" not in _cache:
        rol = BuscarRolPorNombre(db, nombre)
        _cache[f"rol_{nombre}"] = rol.id_rol
    return _cache[f"rol_{nombre}"]

def obtener_id_estado(db: Session, nombre: str) -> int:
    if f"estado_{nombre}" not in _cache:
        estado = BuscarEstadosPorNombre(db, nombre)
        _cache[f"estado_{nombre}"] = estado.id_estado
    return _cache[f"estado_{nombre}"]