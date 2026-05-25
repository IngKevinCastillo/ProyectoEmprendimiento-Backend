from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class CriterioEvaluacionModelo(Base):
    __tablename__ = "CriteriosEvaluacion"

    id_criterio = Column(Integer, primary_key=True)
    id_convocatoria = Column(Integer, ForeignKey("Convocatorias.id_convocatoria"), nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    puntaje_maximo = Column(Integer, nullable=False)

    convocatoria = relationship("ConvocatoriaModelo", back_populates="criterios")
    puntajes = relationship("PuntajeCriterioModelo", back_populates="criterio", cascade="all, delete-orphan")