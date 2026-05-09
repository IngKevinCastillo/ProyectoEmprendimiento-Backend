from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Configs.bd import Base

class PalabraClaveModelo(Base):
    __tablename__ = "PalabraClave"
    
    id_palabra_clave = Column(Integer, primary_key=True, nullable=False)
    palabra = Column(String(50), nullable=False, unique=True)
    
    proyectopalabrasclave = relationship("ProyectoPalabraClaveModelo", back_populates="palabrasclave")