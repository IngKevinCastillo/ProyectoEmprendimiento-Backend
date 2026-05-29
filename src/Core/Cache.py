from time import time
from sqlalchemy.orm import Session
from typing import Callable, Any

class Cache:
    _TTL = 3600  # 1 hora en segundos

    def __init__(self):
        self._store: dict[str, dict[str, Any]] = {}

    def obtener(self, categoria: str, clave: str, resolver: Callable) -> Any:
        entrada = self._store.get(categoria, {}).get(clave)
        if entrada is None or (time() - entrada["timestamp"]) > self._TTL:
            if categoria not in self._store:
                self._store[categoria] = {}
            self._store[categoria][clave] = {"valor": resolver(), "timestamp": time()}
        return self._store[categoria][clave]["valor"]

    def limpiar_categoria(self, categoria: str) -> None:
        self._store.pop(categoria, None)

    def limpiar_todo(self) -> None:
        self._store.clear()

    def inspeccionar(self) -> dict:
        ahora = time()
        resultado = {}
        for categoria, entradas in self._store.items():
            resultado[categoria] = {}
            for clave, entrada in entradas.items():
                tiempo_transcurrido = ahora - entrada["timestamp"]
                tiempo_restante = self._TTL - tiempo_transcurrido
                resultado[categoria][clave] = {
                    "valor": entrada["valor"],
                    "tiempo_restante_segundos": round(max(tiempo_restante, 0), 2),
                    "expirado": tiempo_restante <= 0
                }
        return resultado


cache = Cache()