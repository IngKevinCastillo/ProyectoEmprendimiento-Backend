from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Configs.bd import engine, Base, get_db
from Routes import UsuarioRoute, TipoDocumentoRoute, RolesRoute, ProgramasRoute, FacultadRoute

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Emprendimientos", version="1.0")

app.include_router(UsuarioRoute.router)
app.include_router(TipoDocumentoRoute.router)
app.include_router(RolesRoute.router)
app.include_router(ProgramasRoute.router)
app.include_router(FacultadRoute.router)

@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"mensaje": "Conectado a Supabase"}