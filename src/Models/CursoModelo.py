from sqlalchemy import Column, Integer, String, TIMESTAMP, Date
from sqlalchemy.orm import relationship
from datetime import date
from Configs.bd import Base
from Models.UsuarioModelo import UsuarioModelo

class CursoModelo(Base):
    __tablename__ = "Curso"
    
    id_curso = Column(Integer, primary_key=True)
    nombre_curso = Column(String(80), nullable=False)
    descripcion = Column(String, nullable=False)
    fecha_inicio = Column(Date, nullable=False) 
    fecha_fin = Column(Date, nullable=False)
        
    inscripciones = relationship("InscripcionModelo", back_populates="curso")
    # certificaciones = relationship("CertificacionModelo", back_populates="curso")
