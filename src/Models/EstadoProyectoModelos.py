from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class EstadoProyectoModelo(Base):
    __tablename__ = "estado_proyecto"
    
    id_estado_proyecto = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(40), nullable=False)
    
    # seguimientos = relationship("SeguimientoModelo", back_populates="estado_proyecto_rel")