from sqlalchemy import Column, Integer, String, Text, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from datetime import date

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
    fecha_registro_alianza = Column(Date, default=date.today)

    tipo_entidad = relationship("TipoEntidadesModelo", back_populates="alianzas")