from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship
from Configs.bd import Base

class PostulacionModelo(Base):
    __tablename__ = "Postulaciones"

    id_postulacion = Column(Integer, primary_key=True, autoincrement=True)
    id_convocatoria = Column(Integer, ForeignKey("Convocatorias.id_convocatoria", ondelete="RESTRICT"), nullable=False)
    id_proyecto = Column(Integer, ForeignKey("Proyecto.id_proyecto", ondelete="RESTRICT"), nullable=False)
    estado = Column(String(20), nullable=False, server_default=text("'borrador'"))
    respuestas = Column(Text, nullable=True)
    fecha_postulacion = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    convocatoria = relationship("ConvocatoriaModelo", back_populates="postulaciones")
    proyecto = relationship("ProyectoModelo", back_populates="postulaciones")
    asignaciones = relationship("AsignacionEvaluadorModelo", back_populates="postulacion")