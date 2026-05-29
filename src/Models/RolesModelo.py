from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class RolesModelo(Base):
    __tablename__ = "Roles"
    
    id_rol = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    id_estado = Column(Integer, ForeignKey("Estados.id_estado"), nullable=False)
    
    usuarios = relationship("UsuarioModelo", back_populates="rol")
    usuarioproyecto = relationship("UsuarioProyectoModelo", back_populates="rol")
    participaciones = relationship("ParticipacionEventoModelo", back_populates="rol")
    estado = relationship("EstadosModelo", back_populates="rol")