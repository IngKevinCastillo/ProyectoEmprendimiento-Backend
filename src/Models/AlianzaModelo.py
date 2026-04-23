from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.TipoEntidadesModelo import TipoEntidadesModelo

class AlianzasModelo(Base):
    __tablename__ = "Alianzas"
    
    id_alianza = Column(Integer, primary_key=True, nullable=False)
    nombre_entidad = Column(String(150), nullable=False)
    id_tipo_entidad = Column(Integer, ForeignKey("TipoEntidades.id_tipo_entidad", ondelete="RESTRICT"), nullable=False)
    representante_entidad = Column(String(120), nullable=False)
    cargo_representante = Column(String(80), nullable=False)
    correo_contacto = Column(String(120), nullable=False)
    telefono_contacto = Column(String(20), nullable=False)
    id_apoyo_general = Column(Integer, nullable=False) # Este campo se refiere al ID del apoyo general que se brinda a los estudiantes (puede ser un programa, curso, etc.)
    fecha_inicio_alianza = Column(TIMESTAMP, nullable=False)
    fecha_fin_alianza = Column(TIMESTAMP, nullable=False)
    estado_alianza = Column(String(20), nullable=False)
    fecha_registro = Column(TIMESTAMP, nullable=False)
    url_documento_soporte = Column(String, nullable=False)
    
    tipo_entidad = relationship("TipoEntidadesModelo", back_populates="Alianzas")