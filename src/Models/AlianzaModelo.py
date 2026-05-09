from sqlalchemy import Column, Integer, String, Text, Boolean, Date, ForeignKey, func
from sqlalchemy.orm import relationship
from Configs.bd import Base

class AlianzaModelo(Base):
    __tablename__ = "Alianzas"

    id_alianza                = Column(Integer, primary_key=True, autoincrement=True)
    nombre_entidad            = Column(String, nullable=False)
    sitio_web_url             = Column(String, nullable=False)
    id_tipo_entidad           = Column(Integer, ForeignKey("TipoEntidades.id_tipo_entidad"), nullable=False)
    activo                    = Column(Boolean, nullable=False, default=True)
    representante_entidad     = Column(String, nullable=False)
    correo_contacto           = Column(String, nullable=False)
    telefono_contacto         = Column(String, nullable=False)
    fecha_inicio_alianza      = Column(Date, nullable=False)
    fecha_fin_alianza         = Column(Date, nullable=False) 
    fecha_registro_alianza = Column(Date, server_default=func.now())

    tipo_entidad = relationship("TipoEntidadesModelo", back_populates="alianzas")