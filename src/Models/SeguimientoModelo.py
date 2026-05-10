from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.ProyectoModelo import ProyectoModelo
from Models.UsuarioModelo import UsuarioModelo

class SeguimientoModelo(Base):
    __tablename__ = "Seguimiento"
    
    id_seguimiento_emprendimiento = Column(Integer, primary_key=True, nullable=False)
    id_proyecto = Column(Integer, ForeignKey("Proyecto.id_proyecto", ondelete="RESTRICT"), nullable=False)
    observaciones = Column(String(400), nullable=False)
    id_usuario_responsable = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False)
    fecha_registro = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    id_estado_proyecto = Column(Integer, ForeignKey("estado_proyecto.id_estado_proyecto", ondelete="RESTRICT"), nullable=False)
    avance_porcentaje = Column(Numeric(5, 2), nullable=False)
    
    proyecto = relationship("ProyectoModelo", back_populates="seguimientos")
    usuario_responsable = relationship("UsuarioModelo", back_populates="seguimientos")
    estado_proyecto = relationship("EstadoProyectoModelo", back_populates="seguimientos")