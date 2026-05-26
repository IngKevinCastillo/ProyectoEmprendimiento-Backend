from sqlalchemy import Column, Integer, Numeric, Text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class PuntajeCriterioModelo(Base):
    __tablename__ = "PuntajesCriterios"

    id_puntaje = Column(Integer, primary_key=True, autoincrement=True)
    id_evaluacion = Column(Integer, ForeignKey("Evaluaciones.id_evaluacion", ondelete="RESTRICT"), nullable=False)
    id_criterio = Column(Integer, ForeignKey("CriteriosEvaluacion.id_criterio", ondelete="RESTRICT"), nullable=False)
    nota = Column(Numeric(3, 1), nullable=False)

    evaluacion = relationship("EvaluacionModelo", back_populates="puntajes")
    criterio = relationship("CriterioEvaluacionModelo", back_populates="puntajes")