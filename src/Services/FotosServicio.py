from Services.SupabaseClienteServicio import supabase
import uuid

def subir_foto(archivo: bytes, nombre_archivo: str) -> str:
    extension = nombre_archivo.split(".")[-1]
    nombre_unico = f"{uuid.uuid4()}.{extension}"
    
    supabase.storage.from_("fotos").upload(
        path=nombre_unico,
        file=archivo,
        file_options={"content-type": "image/jpeg"}
    )
    
    url = supabase.storage.from_("fotos").get_public_url(nombre_unico)
    return url