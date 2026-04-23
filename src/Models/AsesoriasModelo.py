from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.UsuarioModelo import UsuarioModelo

class AsesoriasModelo(Base):
    __tablename__ = "Asesorias"
    
    id_asesoria = Column(Integer, primary_key=True, nullable=False)
    tema_asesoria = Column(String(150), nullable=False)
    descripcion_asesoria = Column(String(400), nullable=False)
    fecha_asesoria = Column(TIMESTAMP, nullable=False)
    hora_inicio_asesoria = Column(TIMESTAMP, nullable=False)
    hora_fin_asesoria = Column(TIMESTAMP, nullable=False)
    id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False)
    estado_asesoria = Column(String(20), nullable=False)
    
    usuario = relationship("UsuarioModelo", back_populates="asesorias")