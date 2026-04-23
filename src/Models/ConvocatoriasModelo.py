from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.UsuarioModelo import UsuarioModelo

class ConvocatoriasModelo(Base):
    __tablename__ = "Convocatorias"
    
    Id_convocatoria = Column(Integer, primary_key=True, nullable=False)
    titulo_convocatoria = Column(String(150), nullable=False)
    descripcion_convocatoria = Column(String(450), nullable=False)
    tipo_convocatoria = Column(String(30), nullable=False)
    fecha_inicio = Column(TIMESTAMP, nullable=False)
    fecha_cierre = Column(TIMESTAMP, nullable=False)
    estado_convocatoria = Column(String(20), nullable=False)
    id_usuario = Column(Integer, ForeignKey("UsuarioModelo.id_usuario", ondelete="RESTRICT"), nullable=False)
    fecha_registro = Column(TIMESTAMP, nullable=False)
    
    usuario = relationship("UsuarioModelo", back_populates="Convocatorias")