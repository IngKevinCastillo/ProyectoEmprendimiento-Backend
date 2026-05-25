from sqlalchemy import Column, Integer, Text, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from Configs.bd import Base

class EvaluacionModelo(Base):
    __tablename__ = "Evaluaciones"

    id_evaluacion = Column(Integer, primary_key=True, autoincrement=True)
    id_asignacion = Column(Integer, ForeignKey("AsignacionEvaluadores.id_asignacion", ondelete="RESTRICT"), nullable=False, unique=True)
    comentario_general = Column(Text, nullable=True)
    puntaje_total = Column(Integer, nullable=True)
    estado = Column(String(20), nullable=False, server_default=text("'pendiente'"))
    fecha_evaluacion = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    asignacion = relationship("AsignacionEvaluadorModelo", back_populates="evaluacion")
    puntajes = relationship("PuntajeCriterioModelo", back_populates="evaluacion", cascade="all, delete-orphan")