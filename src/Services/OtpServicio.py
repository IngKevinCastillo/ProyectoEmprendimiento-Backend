from Services.SupabaseClienteServicio import supabase
from fastapi import HTTPException, status
from gotrue.errors import AuthApiError

def enviar_otp_servicio(correo: str):
    try:
        supabase.auth.sign_in_with_otp({"email": correo})
        return True
    except AuthApiError as e:
        raise HTTPException(status_code=e.status, detail=f"Error de autenticación: {e.message}")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Error interno del servidor: {str(e)}"
        )

def verificar_otp_servicio(correo: str, token: str):
    try:
        supabase.auth.verify_otp({
            "email": correo,
            "token": token,
            "type": "email"
        })
        return True
    except Exception as e:
        return False