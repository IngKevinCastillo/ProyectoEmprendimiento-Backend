from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.ProyectoModelo import ProyectoModelo
from Models.UsuarioModelo import UsuarioModelo
from Models.EstadoEmprendimientoModelos import EstadoEmprendimientoModelo

class SeguimientoModelo(Base):
    __tablename__ = "Seguimiento"
    
    id_seguimiento_emprendimiento = Column(Integer, primary_key=True, nullable=False)
    id_proyecto = Column(Integer, ForeignKey("Proyecto.id_proyecto", ondelete="RESTRICT"), nullable=False)
    observaciones = Column(String(400), nullable=False)
    id_usuario_responsable = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False)
    fecha_registro = Column(TIMESTAMP, nullable=False)
    id_estado_emprendimiento = Column(Integer, ForeignKey("EstadoEmprendimiento.id_estado_emprendimiento", ondelete="RESTRICT"), nullable=False)
    avance_porcentaje = Column(Numeric(5, 2), nullable=False)
    
    proyecto = relationship("ProyectoModelo", back_populates="seguimientos")
    usuario_responsable = relationship("UsuarioModelo", back_populates="seguimientos")
    estado_emprendimiento_rel = relationship("EstadoEmprendimientoModelo", back_populates="seguimientos")