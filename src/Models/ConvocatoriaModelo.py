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
    id_estado = Column(Integer, ForeignKey("Estados.id_estado"), nullable=False, server_default=text("19"))
    creado_por = Column(Integer, ForeignKey("Usuario.id_usuario"), nullable=False)
    id_tipo_convocatoria = Column(Integer, ForeignKey("TipoConvocatoria.id_tipo_convocatoria"), nullable=False)
    fecha_creacion = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    estado = relationship("EstadosModelo", back_populates="convocatorias")
    tipo_convocatoria = relationship("TipoConvocatoriaModelo", back_populates="convocatorias")
    criterios = relationship("CriterioEvaluacionModelo", back_populates="convocatoria", cascade="all, delete-orphan")
    postulaciones = relationship("PostulacionModelo", back_populates="convocatoria")
    beneficios_asignados = relationship("BeneficioAsignadoModelo", back_populates="convocatoria")