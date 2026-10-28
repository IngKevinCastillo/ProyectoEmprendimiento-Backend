from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class RolesModelo(Base):
    __tablename__ = "Roles"
    
    id_rol = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    estado = Column(String(15), nullable=False)
    
    usuarios = relationship("UsuarioModelo", back_populates="rol")
    usuarioproyecto = relationship("UsuarioProyectoModelo", back_populates="rol")
    participaciones = relationship("ParticipacionEventoModelo", back_populates="rol")