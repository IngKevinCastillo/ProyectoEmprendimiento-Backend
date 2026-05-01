import re
from datetime import datetime, timezone
from typing import Optional

def validar_string(valor: str, min_len: int = 1, max_len: int = 255, campo: str = "Campo") -> str:
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser un texto.")
    valor = valor.strip()
    if not valor:
        raise ValueError(f"{campo} no puede estar vacío.")
    if not (min_len <= len(valor) <= max_len):
        raise ValueError(f"{campo} debe tener entre {min_len} y {max_len} caracteres.")
    return valor

def validar_string_nulos(valor: Optional[str], min_len: int = 1, max_len: int = 255, campo: str = "Campo") -> Optional[str]:
    if valor is None:
        return None
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser un texto.")
    valor = valor.strip()
    if not valor:
        raise ValueError(f"{campo} no puede estar vacío.")
    if not (min_len <= len(valor) <= max_len):
        raise ValueError(f"{campo} debe tener entre {min_len} y {max_len} caracteres.")
    return valor

def validar_nombre(valor: str, min_len: int = 2, max_len: int = 100, campo: str = "Nombre") -> str:
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser un texto.")
    valor = " ".join(valor.split())
    if not valor:
        raise ValueError(f"{campo} no puede estar vacío.")
    if not (min_len <= len(valor) <= max_len):
        raise ValueError(f"{campo} debe tener entre {min_len} y {max_len} caracteres.")
    letras = r"[A-Za-záéíóúÁÉÍÓÚàèìòùäëïöüÄËÏÖÜñÑ]"
    if not re.fullmatch(rf"{letras}+(\s{letras}+)*", valor):
        raise ValueError(f"{campo} solo puede contener letras y espacios simples entre palabras.")
    return valor

def validar_telefono(valor: str, campo: str = "Teléfono") -> str:
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser un texto.")
    valor = valor.strip().replace(" ", "").replace("-", "")
    if valor.startswith("+57"):
        valor = valor[3:]
    elif valor.startswith("57") and len(valor) > 10:
        valor = valor[2:]

    if not valor.isdigit():
        raise ValueError(f"{campo} solo debe contener dígitos.")
    if len(valor) == 10 and valor.startswith("3"):
        return valor 
    if len(valor) in (7, 10):
        return valor 
    raise ValueError(f"{campo} inválido. Debe ser un número colombiano de 7 o 10 dígitos.")

def validar_documento(valor: str, campo: str = "Documento") -> str:
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser un texto.")
    valor = valor.strip().replace(".", "").replace(",", "").replace(" ", "")
    if not re.fullmatch(r"[A-Za-z0-9]{6,12}", valor):
        raise ValueError(
            f"{campo} inválido. Debe tener entre 6 y 12 caracteres alfanuméricos (sin puntos ni espacios)."
        )
    return valor

_DOMINIOS_VALIDOS = {
    "gmail.com", "googlemail.com",
    "hotmail.com", "hotmail.es", "hotmail.co",
    "outlook.com", "outlook.es",
    "live.com", "live.co",
    "yahoo.com", "yahoo.es", "yahoo.co",
    "icloud.com", "me.com", "mac.com",
    "protonmail.com", "proton.me",
    "tutanota.com",
    "unal.edu.co", "udea.edu.co", "uniandes.edu.co",
    "javeriana.edu.co", "eafit.edu.co", "uninorte.edu.co",
    "uis.edu.co", "utb.edu.co", "unicartagena.edu.co",
}

def validar_email(valor: str) -> str:
    if not isinstance(valor, str):
        raise TypeError("El correo debe ser un texto.")
    
    valor = valor.strip().lower()
    
    if not re.fullmatch(r"^[\w\.\+\-]+@[\w\-]+(\.[\w\-]+)+$", valor):
        raise ValueError("Correo electrónico con formato inválido.")
    
    dominio = valor.split("@")

    if dominio != "unicesar.edu.co":
        raise ValueError(
            f"Correo no válido. Solo se aceptan direcciones del dominio @unicesar.edu.co. "
            f"Se recibió: '{valor}'"
        )
    
    return valor

def validar_int(
    valor: int,
    min_val: Optional[int] = None,
    max_val: Optional[int] = None,
    campo: str = "Campo"
) -> int:
    
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise TypeError(f"{campo} debe ser un número entero.")
    if min_val is not None and valor < min_val:
        raise ValueError(f"{campo} debe ser mayor o igual a {min_val}.")
    if max_val is not None and valor > max_val:
        raise ValueError(f"{campo} debe ser menor o igual a {max_val}.")
    return valor

def validar_int_nulos(
    valor: Optional[int],
    min_val: Optional[int] = None,
    max_val: Optional[int] = None,
    campo: str = "Campo"
) -> Optional[int]:
    if valor is None:
        return None
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise TypeError(f"{campo} debe ser un número entero.")
    if min_val is not None and valor < min_val:
        raise ValueError(f"{campo} debe ser mayor o igual a {min_val}.")
    if max_val is not None and valor > max_val:
        raise ValueError(f"{campo} debe ser menor o igual a {max_val}.")
    return valor

def validar_fecha_futura(valor: datetime, campo: str = "Fecha") -> datetime:
    if not isinstance(valor, datetime):
        raise TypeError(f"{campo} debe ser un objeto datetime.")
    hoy = datetime.now(timezone.utc).date()
    if valor.date() <= hoy:
        raise ValueError(f"{campo} debe ser posterior a la fecha actual ({hoy}).")
    return valor

def validar_rango_fechas(
    fecha_inicio: datetime,
    fecha_fin: datetime,
    campo_inicio: str = "Fecha inicio",
    campo_fin: str = "Fecha fin"
) -> tuple[datetime, datetime]:
    if not isinstance(fecha_inicio, datetime) or not isinstance(fecha_fin, datetime):
        raise TypeError("Las fechas deben ser objetos datetime.")
    if fecha_inicio >= fecha_fin:
        raise ValueError(f"{campo_inicio} debe ser anterior a {campo_fin}.")
    return fecha_inicio, fecha_fin

def validar_password(valor: str) -> str:
    if not isinstance(valor, str):
        raise TypeError("La contraseña debe ser un texto.")
    errores = []
    if len(valor) < 8:
        errores.append("al menos 8 caracteres")
    if not re.search(r"[A-Z]", valor):
        errores.append("una letra mayúscula")
    if not re.search(r"[a-z]", valor):
        errores.append("una letra minúscula")
    if not re.search(r"\d", valor):
        errores.append("un número")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', valor):
        errores.append("un carácter especial (!@#$%...)")
    if errores:
        raise ValueError("La contraseña debe tener: " + ", ".join(errores) + ".")
    return valor

def validar_hora(valor: str, campo: str = "Hora") -> str:
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser un texto en formato HH:MM.")
    if not re.fullmatch(r"([01]\d|2[0-3]):([0-5]\d)", valor.strip()):
        raise ValueError(f"{campo} inválida. Formato esperado: HH:MM (ej. 08:30, 23:59).")
    return valor.strip()

def validar_bool(valor, campo: str = "Campo") -> bool:
    if not isinstance(valor, bool):
        raise ValueError(f"{campo} debe ser verdadero (True) o falso (False).")
    return valor

def validar_fecha(valor: str, campo: str = "Fecha") -> datetime:
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser un texto en formato DD/MM/YYYY.")
    valor = valor.strip()
    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", valor):
        raise ValueError(f"{campo} debe tener el formato DD/MM/YYYY (ej. 15/08/2000).")
    try:
        return datetime.strptime(valor, "%d/%m/%Y")
    except ValueError:
        raise ValueError(f"{campo} no es una fecha valida (ej. 31/02/2000 no existe).")