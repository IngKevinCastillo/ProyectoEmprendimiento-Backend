from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from sqlalchemy import Date

class ConvocatoriasModelo(Base):
    __tablename__ = "Convocatorias"
    
    id_convocatoria = Column(Integer, primary_key=True, nullable=False)
    titulo_convocatoria = Column(String(150), nullable=False)
    descripcion_convocatoria = Column(String(450), nullable=False)
    tipo_convocatoria = Column(String(30), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_cierre = Column(Date, nullable=False)
    estado_convocatoria = Column(String(20), nullable=False)
    id_proyecto = Column(Integer, ForeignKey("Proyecto.id_proyecto", ondelete="RESTRICT"), nullable=False)
    fecha_registro = Column(Date, nullable=False)
    url_convocatoria = Column(String, nullable=False)
    
    proyecto = relationship("ProyectoModelo", back_populates="convocatorias")
