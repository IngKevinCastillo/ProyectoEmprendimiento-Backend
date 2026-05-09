from sqlalchemy import Column, Integer, String, Text, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class AlianzaModelo(Base):
    __tablename__ = "Alianzas"

    id_alianza        = Column(Integer, primary_key=True, autoincrement=True)
    nombre_entidad    = Column(String, nullable=False)
    descripcion       = Column(Text, nullable=True)
    sitio_web_url     = Column(String, nullable=False)
    id_tipo_entidad   = Column(Integer, ForeignKey("TipoEntidades.id_tipo_entidad"), nullable=False)
    activo            = Column(Boolean, nullable=False, default=True)
    representante     = Column(String, nullable=False)
    correo_contacto   = Column(String, nullable=False)
    telefono_contacto = Column(String, nullable=False)
    fecha_inicio      = Column(Date, nullable=False)
    fecha_fin         = Column(Date, nullable=False)
    
    tipo_entidad = relationship("TipoEntidadesModelo", back_populates="alianzas")