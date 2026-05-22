from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Configs.bd import Base

class TipoProyectoModelo(Base):
    __tablename__ = "TipoProyecto"
    
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    
    proyecto = relationship("ProyectoModelo", back_populates="tipo_proyecto")