from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.RolesModelo import RolesModelo

class UsuarioModelo(Base):
    __tablename__ = "Usuario"
    
    id_usuario = Column(Integer, primarykey=True)
    primer_nombre = Column(String(30), nullable=False)
    segundo_nombre = Column(String(30), nullable=True)
    primer_apellido = Column(String(30), nullable=False)
    segundo_apellido = Column(String(30), nullable=False)
    correo = Column(String(45), nullable=False, unique=True)
    contrasena = Column(String(30), nullable=False)
    id_rol = Column(Integer, ForeignKey("RolesModelo.id_rol", ondelete="RESTRICT"), nullable=False)
    fecha_registro = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
    estado = Column(String(10), nullable=False, default="Activo")
    fecha_nacimiento = Column(TIMESTAMP, nullable=False)
    ubicacion_semestral = Column(Integer, nullable=True)
    sexo = Column(String(30), nullable=False)
    id_programa = Column(Integer, nullable=True)
    id_tipodocumento = Column(Integer, nullable=True)
    numero_documento = Column(String(30), nullable=False, unique=True)
    telefono = Column(String(10), nullable=False)
    id_facultad = Column(Integer, nullable=True)
    
    rol = relationship("RolesModelo", back_populates="Usuario")