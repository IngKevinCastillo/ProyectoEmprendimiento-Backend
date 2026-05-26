from sqlalchemy import Column, Integer, String, TIMESTAMP, Date, ForeignKey
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
    id_estado = Column(Integer, ForeignKey("Estados.id_estado", ondelete="RESTRICT"), nullable=False)
    foto_url = Column(String, nullable=True)

    inscripciones = relationship("InscripcionModelo", back_populates="curso")
    estados = relationship("EstadosModelo", back_populates="curso")
