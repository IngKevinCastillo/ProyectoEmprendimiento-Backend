from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Configs.bd import engine, Base, get_db

from Routes import (
    AlianzaRoute, ParticipacionEventoRoute, TipoEntidadesRoute, UsuarioRoute, TipoDocumentoRoute, RolesRoute, ProgramasRoute,
    FacultadRoute, Eventoroute, CursoRoute, UsuarioProyectoRoute,
    SedeRoute, DepartamentosRoute, MunicipioRoute, ProyectoRoute,
    InscripcionRoute, ConvocatoriasRoute, CategoriaRoute, PalabraClaveRoute,
    ProyectoPalabraClaveRoutes
)

from Models.ProyectoModelo import ProyectoModelo

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Emprendimientos", version="1.0", docs_url="/docs")

app.include_router(UsuarioRoute.router)
app.include_router(TipoDocumentoRoute.router)
app.include_router(RolesRoute.router)
app.include_router(ProgramasRoute.router)
app.include_router(FacultadRoute.router)
app.include_router(Eventoroute.router)
app.include_router(CursoRoute.router)
app.include_router(UsuarioProyectoRoute.router)
app.include_router(SedeRoute.router)
app.include_router(DepartamentosRoute.router)
app.include_router(MunicipioRoute.router)
app.include_router(ProyectoRoute.router)
app.include_router(ParticipacionEventoRoute.router)
app.include_router(InscripcionRoute.router)
app.include_router(ConvocatoriasRoute.router)

app.include_router(CategoriaRoute.router)
app.include_router(PalabraClaveRoute.router)
app.include_router(ProyectoPalabraClaveRoutes.router)

app.include_router(AlianzaRoute.router)
app.include_router(TipoEntidadesRoute.router)

@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"mensaje": "Conectado a Supabase"}