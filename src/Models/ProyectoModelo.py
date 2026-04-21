from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from src.Configs.bd import Base
from src.Models.UsuarioModelo import UsuarioModelo

class ProyectoModelo(Base):
    __tablename__ = "Proyecto"
    
    id_proyecto = Column(Integer, primary_key=True)
    nombre_proyecto = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(String(25), nullable=False)
    fecha_creacion = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
    id_usuario = Column(Integer, ForeignKey("UsuarioModelo.id_usuario"), nullable=False)
    
    usuario = relationship("UsuarioModelo", back_populates="Proyecto")