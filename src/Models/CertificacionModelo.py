from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from src.Configs.bd import Base
from src.Models.UsuarioModelo import UsuarioModelo

class CertificacionModelo(Base):
    __tablename__ = "Certificacion"
    
    id_certificacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("UsuarioModelo.id_usuario", ondelete="RESTRICT"), nullable=False)
    nombre_certificacion = Column(String(80), nullable=False)
    fecha_certificacion = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
    
    usuario = relationship("UsuarioModelo", back_populates="Certificacion")
    