from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class SedeModelo(Base):
    __tablename__ = "Sede"
    
    id_sede = Column(Integer, primary_key=True, nullable=False)
    # id_facultad = Column(Integer, ForeignKey("Facultad.id_facultad", ondelete="RESTRICT"), nullable=False)
    # id_programa = Column(Integer, ForeignKey("Programa.id_programa", ondelete="RESTRICT"), nullable=False)
    nombre = Column(String(30), nullable=False)
    ciudad = Column(String(45), nullable=True)
    
    usuarios = relationship("UsuarioModelo", back_populates="sede")