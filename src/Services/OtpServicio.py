import random
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi_mail import FastMail, MessageSchema, MessageType
from Models.OTPModelo import OTPModelo
from Models.UsuarioModelo import UsuarioModelo
from Core.Correo import conf

def generar_codigo() -> str:
    return str(random.randint(100000, 999999))

async def enviar_otp_servicio(correo: str, db: Session):
    usuario = db.query(UsuarioModelo).filter(
        UsuarioModelo.correo == correo
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Si el correo esta registrado, recibiras un codigo en breve"
        )

    db.query(OTPModelo).filter(
        OTPModelo.correo == correo,
        OTPModelo.usado == False
    ).update({"usado": True})
    db.commit()

    codigo = generar_codigo()
    expiracion = datetime.now() + timedelta(minutes=10)

    otp = OTPModelo(
        correo=correo,
        codigo=codigo,
        expiracion=expiracion,
        usado=False
    )
    db.add(otp)
    db.commit()

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Codigo de verificacion - UPC Emprendimiento</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background-color: #f4f4f4; font-family: 'Segoe UI', Arial, sans-serif; }}
        .wrapper {{ max-width: 600px; margin: 40px auto; background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 24px rgba(0,0,0,0.10); }}
        .header {{ background: linear-gradient(135deg, #2e7d32 0%, #388e3c 60%, #f9a825 100%); padding: 36px 40px 28px; text-align: center; position: relative; }}
        .header::after {{ content: ''; display: block; position: absolute; bottom: 0; left: 0; right: 0; height: 6px; background: #f9a825; }}
        .logo-circle {{ width: 90px; height: 90px; border-radius: 50%; background: #fff; margin: 0 auto 16px; display: flex; align-items: center; justify-content: center; border: 4px solid #f9a825; overflow: hidden; }}
        .logo-circle img {{ width: 80px; height: 80px; object-fit: contain; border-radius: 50%; }}
        .header h1 {{ color: #ffffff; font-size: 20px; font-weight: 700; letter-spacing: 0.5px; margin-bottom: 4px; }}
        .header p {{ color: #e8f5e9; font-size: 13px; }}
        .body {{ padding: 40px 44px 32px; }}
        .greeting {{ font-size: 16px; color: #2e7d32; font-weight: 600; margin-bottom: 12px; }}
        .message {{ font-size: 15px; color: #444; line-height: 1.7; margin-bottom: 28px; }}
        .otp-box {{ background: linear-gradient(135deg, #e8f5e9 0%, #fff9c4 100%); border: 2px solid #2e7d32; border-radius: 12px; padding: 28px 20px; text-align: center; margin-bottom: 28px; }}
        .otp-label {{ font-size: 12px; color: #388e3c; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px; }}
        .otp-code {{ font-size: 44px; font-weight: 800; letter-spacing: 12px; color: #1b5e20; font-family: 'Courier New', monospace; }}
        .otp-expiry {{ font-size: 12px; color: #888; margin-top: 10px; }}
        .warning {{ background: #fff8e1; border-left: 4px solid #f9a825; border-radius: 6px; padding: 14px 18px; margin-bottom: 28px; }}
        .warning p {{ font-size: 13px; color: #795548; line-height: 1.6; }}
        .warning strong {{ color: #e65100; }}
        .divider {{ border: none; border-top: 1px solid #e0e0e0; margin: 24px 0; }}
        .footer {{ background: #f9f9f9; padding: 24px 40px; text-align: center; border-top: 1px solid #e8e8e8; }}
        .footer-logo {{ display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 10px; }}
        .footer-dot {{ width: 10px; height: 10px; border-radius: 50%; background: #2e7d32; }}
        .footer-dot.yellow {{ background: #f9a825; }}
        .footer p {{ font-size: 12px; color: #aaa; line-height: 1.6; }}
        .footer a {{ color: #2e7d32; text-decoration: none; }}
        .university {{ font-size: 13px; color: #555; font-weight: 600; margin-bottom: 4px; }}
    </style>
    </head>
    <body>
    <div class="wrapper">
        <div class="header">
        <div class="logo-circle">
            <span style="font-size:32px;font-weight:900;color:#2e7d32">UE</span>
        </div>
        <h1>UPC Emprendimiento y Desarrollo Empresarial</h1>
        <p>Universidad Popular del Cesar</p>
        </div>
        <div class="body">
        <p class="greeting">Hola,</p>
        <p class="message">
            Recibimos una solicitud para verificar tu identidad en la plataforma de
            <strong>Emprendimiento UPC</strong>. Usa el siguiente codigo de verificacion
            para continuar. Este codigo es de un solo uso.
        </p>
        <div class="otp-box">
            <div class="otp-label">Tu codigo de verificacion</div>
            <div class="otp-code">{codigo}</div>
            <div class="otp-expiry">Este codigo expira en 10 minutos</div>
        </div>
        <div class="warning">
            <p>
            <strong>No compartas este codigo</strong> con nadie. El equipo de
            Emprendimiento UPC jamas te pedira este codigo por ningun otro medio.
            Si no solicitaste este codigo, ignora este mensaje.
            </p>
        </div>
        <hr class="divider">
        <p style="font-size:13px;color:#888;text-align:center;">
            Si tienes problemas, contacta al equipo de soporte en
            <a href="mailto:unicesaremprendimiento@gmail.com" style="color:#2e7d32;">unicesaremprendimiento@gmail.com</a>
        </p>
        </div>
        <div class="footer">
        <div class="footer-logo">
            <div class="footer-dot"></div>
            <div class="footer-dot yellow"></div>
            <div class="footer-dot"></div>
        </div>
        <p class="university">Universidad Popular del Cesar</p>
        <p>Valledupar, Cesar - Colombia</p>
        <p style="margin-top:8px;">Este es un mensaje automatico, por favor no respondas a este correo.</p>
        </div>
    </div>
    </body>
    </html>
    """

    mensaje = MessageSchema(
        subject="Codigo de verificacion - UPC Emprendimiento",
        recipients=[correo],
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(mensaje)

    return {"detail": "Si el correo esta registrado, recibiras un codigo en breve"}

def verificar_otp_servicio(correo: str, codigo: str, db: Session):
    otp = db.query(OTPModelo).filter(
        OTPModelo.correo == correo,
        OTPModelo.codigo == codigo,
        OTPModelo.usado == False
    ).order_by(OTPModelo.id.desc()).first()

    if not otp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Codigo invalido"
        )

    if datetime.now() > otp.expiracion:
        otp.usado = True
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El codigo ha expirado"
        )

    otp.usado = True
    db.commit()
    return {"detail": "Codigo verificado correctamente"}