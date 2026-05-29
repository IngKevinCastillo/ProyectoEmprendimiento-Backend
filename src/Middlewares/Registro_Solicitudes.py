from starlette.middleware.base import BaseHTTPMiddleware
import time


class RegistroSolicitudesMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        inicio = time.time()
        respuesta = await call_next(request)
        duracion = time.time() - inicio
        print(f"Solicitud: {request.method} {request.url} - Tiempo de procesamiento: {duracion:.4f} segundos")
        return respuesta