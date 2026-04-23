from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Configs.bd import get_db

app = FastAPI()

@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"mensaje": "Conectado a Supabase"}