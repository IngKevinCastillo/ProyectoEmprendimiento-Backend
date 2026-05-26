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

def eliminar_foto(foto_url: str):
    try:
        ruta = foto_url.split("/fotos/")[-1]
        supabase.storage.from_("fotos").remove([ruta])
    except Exception as e:
        raise Exception(f"Error al eliminar foto: {str(e)}")
    
def subir_pdf(archivo: bytes, nombre_archivo: str) -> str:
    extension = nombre_archivo.split(".")[-1]
    nombre_unico = f"{uuid.uuid4()}.{extension}"
    
    supabase.storage.from_("documentos").upload(
        path=nombre_unico,
        file=archivo,
        file_options={"content-type": "application/pdf"}
    )
    
    url = supabase.storage.from_("documentos").get_public_url(nombre_unico)
    return url

def eliminar_pdf(pdf_url: str):
    try:
        ruta = pdf_url.split("/documentos/")[-1]
        supabase.storage.from_("documentos").remove([ruta])
    except Exception as e:
        raise Exception(f"Error al eliminar PDF: {str(e)}")