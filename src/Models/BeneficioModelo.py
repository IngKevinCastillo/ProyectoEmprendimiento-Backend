from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from Configs.bd import Base

class BeneficioModelo(Base):
    __tablename__ = "Beneficios"

    id_beneficio = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=True)

    asignaciones = relationship("BeneficioAsignadoModelo", back_populates="beneficio")