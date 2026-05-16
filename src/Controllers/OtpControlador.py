from Services.OtpServicio import enviar_otp_servicio, verificar_otp_servicio

def EnviarOTPControlador(correo: str):
    return enviar_otp_servicio(correo)

def VerificarOTPControlador(correo: str, token: str) -> bool:
    return verificar_otp_servicio(correo, token)