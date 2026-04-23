from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class FacultadModelo(Base):
    __tablename__ = "Facultad"
    
    id_facultad = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(80), nullable=False)
    descripcion = Column(String(500), nullable=False)
    estado = Column(String(10), nullable=False)
    
    programas = relationship("ProgramaModelo", back_populates="facultad")
    usuarios = relationship("UsuarioModelo", back_populates="facultad")