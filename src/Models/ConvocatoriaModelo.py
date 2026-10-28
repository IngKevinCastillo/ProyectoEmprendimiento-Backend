from sqlalchemy import Column, Integer, String, Text, Date, TIMESTAMP, ForeignKey, text
from Configs.bd import Base
from sqlalchemy.orm import relationship

class ConvocatoriaModelo(Base):
    __tablename__ = "Convocatorias"

    id_convocatoria = Column(Integer, primary_key=True)
    titulo_convocatoria = Column(String(150), nullable=False)
    descripcion_convocatoria = Column(Text, nullable=True)
    fecha_apertura = Column(Date, nullable=False)
    fecha_cierre = Column(Date, nullable=False)
    cupos = Column(Integer, nullable=True)
    requisitos = Column(Text, nullable=True)
    estado = Column(String(15), nullable=False)
    creado_por = Column(Integer, ForeignKey("Usuario.id_usuario"), nullable=False)
    id_tipo_convocatoria = Column(Integer, ForeignKey("TipoConvocatoria.id_tipo_convocatoria"), nullable=False)
    fecha_creacion = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    tipo_convocatoria = relationship("TipoConvocatoriaModelo", back_populates="convocatorias")
    postulaciones = relationship("PostulacionModelo", back_populates="convocatoria")
    beneficios_asignados = relationship("BeneficioAsignadoModelo", back_populates="convocatoria")