from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
import traceback

class ManejoErroresMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            print(f"ERROR CAPTURADO: {type(e).__name__}: {str(e)}")
            traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"error": type(e).__name__, "mensaje": str(e)}
        )