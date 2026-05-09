from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class ProyectoPalabraClaveModelo(Base):
    __tablename__ = "ProyectoPalabraClave"
    
    id_proyecto_palabra_clave =Column(Integer, primary_key=True, nullable=True)
    id_proyecto = Column(Integer, ForeignKey("Proyecto.id_proyecto", ondelete="RESTRICT"), nullable=False)
    id_palabra_clave = Column(Integer, ForeignKey("PalabraClave.id_palabra_clave", ondelete="RESTRICT"), nullable=False)
    
    proyecto = relationship("ProyectoModelo", back_populates="proyectopalabrasclave")
    palabrasclave = relationship("PalabraClaveModelo", back_populates="proyectopalabrasclave")