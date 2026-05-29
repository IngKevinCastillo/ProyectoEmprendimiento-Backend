from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class MetasModelo(Base):
    __tablename__ = "Metas"
    
    id_meta = Column(Integer, primary_key=True)
    descripcion = Column(String(200), nullable=False)
    anio = Column(Date, nullable=False)
    id_estado = Column(Integer, ForeignKey("Estados.id_estado"), nullable=False)
    
    estado = relationship("EstadosModelo", back_populates="metas")