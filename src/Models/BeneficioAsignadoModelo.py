from sqlalchemy import Column, Integer, Text, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from Configs.bd import Base

class BeneficioAsignadoModelo(Base):
    __tablename__ = "BeneficiosAsignados"

    id_beneficio_asignado = Column(Integer, primary_key=True, autoincrement=True)
    id_convocatoria = Column(Integer, ForeignKey("Convocatorias.id_convocatoria", ondelete="RESTRICT"), nullable=False)
    id_proyecto = Column(Integer, ForeignKey("Proyecto.id_proyecto", ondelete="RESTRICT"), nullable=False)
    id_beneficio = Column(Integer, ForeignKey("Beneficios.id_beneficio", ondelete="RESTRICT"), nullable=False)
    descripcion_entrega = Column(Text, nullable=True)
    estado = Column(String(20), nullable=False, server_default=text("'pendiente'"))
    fecha_asignacion = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    asignado_por = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False)

    convocatoria = relationship("ConvocatoriaModelo", back_populates="beneficios_asignados")
    proyecto = relationship("ProyectoModelo", back_populates="beneficios_asignados")
    beneficio = relationship("BeneficioModelo", back_populates="asignaciones")