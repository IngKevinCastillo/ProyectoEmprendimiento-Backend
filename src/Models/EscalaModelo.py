from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Configs.bd import Base

class EscalaModelo(Base):
    __tablename__ = "Escala"
    
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)

    proyecto = relationship("ProyectoModelo", back_populates="escala")