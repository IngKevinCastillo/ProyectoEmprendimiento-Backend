from Core.Seguridad import Settings
from supabase import create_client

supabase = create_client(
    Settings.SUPABASE_URL,
    Settings.SUPABASE_SERVICE_KEY
)