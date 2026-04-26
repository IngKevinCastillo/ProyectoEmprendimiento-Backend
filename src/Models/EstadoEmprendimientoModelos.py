from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class EstadoEmprendimientoModelo(Base):
    __tablename__ = "estado_emprendimiento"
    
    id_estado_emprendimiento = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(40), nullable=False)
    
    seguimientos = relationship("SeguimientoModelo", back_populates="estado_emprendimiento_rel")