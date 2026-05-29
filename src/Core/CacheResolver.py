from sqlalchemy.orm import Session
from Core.Cache import cache
from Services.RolServicio import BuscarRolPorNombre
from Services.EstadosServicio import BuscarEstadosPorNombre
from Services.MesasServicio import buscar_mesa

def obtener_id_rol(db: Session, nombre: str) -> int:
    return cache.obtener("roles", nombre, lambda: BuscarRolPorNombre(db, nombre).id_rol)

def obtener_id_estado(db: Session, nombre: str) -> int:
    return cache.obtener("estados", nombre, lambda: BuscarEstadosPorNombre(db, nombre).id_estado)

def obtener_nombre_mesa_por_id(db: Session, id_mesa: int) -> str:
    def resolver():
        mesa = buscar_mesa(db, id_mesa)
        return mesa.nombre if mesa else None
    return cache.obtener("mesas", str(id_mesa), resolver)