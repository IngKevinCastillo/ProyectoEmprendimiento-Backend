from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class ProgramaModelo(Base):
    __tablename__ = "Programa"
    
    id_programa = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    nivel = Column(String(25), nullable=False)
    id_facultad = Column(Integer, ForeignKey("Facultad.id_facultad", ondelete="RESTRICT"), nullable=False) 
    estado = Column(String(10), nullable=False)
    
    facultad = relationship("FacultadModelo", back_populates="programas") 
    usuarios = relationship("UsuarioModelo", back_populates="programa")