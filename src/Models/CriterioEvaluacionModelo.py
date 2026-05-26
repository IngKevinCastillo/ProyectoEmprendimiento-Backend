from sqlalchemy import Column, Integer, String, Text, Numeric
from sqlalchemy.orm import relationship
from Configs.bd import Base

class CriterioEvaluacionModelo(Base):
    __tablename__ = "CriteriosEvaluacion"

    id_criterio = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    porcentaje = Column(Numeric(5, 2), nullable=False)

    puntajes = relationship("PuntajeCriterioModelo", back_populates="criterio")