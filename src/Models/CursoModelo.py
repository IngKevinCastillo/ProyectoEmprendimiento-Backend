from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from Configs.bd import Base
from Models.UsuarioModelo import UsuarioModelo

class CursoModelo(Base):
    __tablename__ = "Curso"
    
    id_curso = Column(Integer, primary_key=True)
    nombre_curso = Column(String(80), nullable=False)
    descripcion = Column(String, nullable=False)
    fecha_inicio = Column(datetime, nullable=False)
    fecha_fin = Column(datetime, nullable=False)
    
    inscripciones = relationship("InscripcionModelo", back_populates="curso")
