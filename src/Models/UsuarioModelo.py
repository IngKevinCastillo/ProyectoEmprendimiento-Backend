from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from src.Configs.bd import Base
from src.Models.RolModelo import RolModelo

class UsuarioModelo(Base):
    __tablename__ = "Usuario"
    
    id_usuario = Column(Integer, primarykey=True)
    nombre_usuario = Column(String(50), nullable=False)
    correo = Column(String(45), nullable=False, unique=True)
    contrasena = Column(String(30), nullable=False)
    id_rol = Column(Integer, ForeignKey("RolModelo.id_rol", ondelete="RESTRICT"), nullable=False)
    fecha_registro = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
    estado = Column(String(10), nullable=False, default="Activo")
    
    rol = relationship("RolModelo", back_populates="Usuario")