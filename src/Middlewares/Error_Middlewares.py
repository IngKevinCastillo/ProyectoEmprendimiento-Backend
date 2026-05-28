from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

class ManejoErroresMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"detail": "Ocurrió un error interno en el servidor."}
            )