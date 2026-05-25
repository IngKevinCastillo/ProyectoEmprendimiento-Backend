from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Configs.bd import Base

class TipoConvocatoriaModelo(Base):
    __tablename__ = "TipoConvocatoria"

    id_tipo_convocatoria = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(150), nullable=True)

    convocatorias = relationship("ConvocatoriaModelo", back_populates="tipo_convocatoria")