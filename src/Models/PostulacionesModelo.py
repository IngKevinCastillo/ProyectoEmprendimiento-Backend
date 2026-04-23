from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.ConvocatoriasModelo import ConvocatoriasModelo
from Models.UsuarioModelo import UsuarioModelo

class PostulacionesModelo(Base):
    __tablename__ = "Postulaciones"
    
    id_postulacion = Column(Integer, primary_key=True, nullable=False)
    id_convocatoria = Column(Integer, ForeignKey("ConvocatoriasModelo.Id_convocatoria", ondelete="RESTRICT"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("UsuarioModelo.id_usuario", ondelete="RESTRICT"), nullable=False)
    informacion_adicional = Column(String(400), nullable=False)
    id_plan_negocio = Column(Integer, nullable=False)
    fecha_registro = Column(TIMESTAMP, nullable=False)
    
    convocatoria = relationship("ConvocatoriasModelo", back_populates="Postulaciones")
    usuario = relationship("UsuarioModelo", back_populates="Postulaciones")