from sqlalchemy import Column, Integer, String, TIMESTAMP, Date
from sqlalchemy.orm import relationship
from datetime import date
from Configs.bd import Base

class CategoriaModelo(Base):
    __tablename__ = "Categoria"
    
    id_categoria = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(100), nullable=False)
    
    proyecto = relationship("ProyectoModelo", back_populates="categoria")