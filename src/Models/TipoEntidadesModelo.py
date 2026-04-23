from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class TipoEntidadesModelo(Base):
    __tablename__ = "TipoEntidades"
    
    id_tipo_entidad = Column(Integer, primary_key=True, nullable=False)
    nombre_tipo_entidad = Column(String(40), nullable=False)
    
    alianzas = relationship("AlianzasModelo", back_populates="tipo_entidad")