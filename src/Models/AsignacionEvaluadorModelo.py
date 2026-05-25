from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from Configs.bd import Base

class AsignacionEvaluadorModelo(Base):
    __tablename__ = "AsignacionEvaluadores"

    id_asignacion = Column(Integer, primary_key=True, autoincrement=True)
    id_postulacion = Column(Integer, ForeignKey("Postulaciones.id_postulacion", ondelete="RESTRICT"), nullable=False)
    id_evaluador = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False)
    fecha_asignacion = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    postulacion = relationship("PostulacionModelo", back_populates="asignaciones")
    evaluador = relationship("UsuarioModelo", back_populates="asignaciones")
    evaluacion = relationship("EvaluacionModelo", back_populates="asignacion", uselist=False)