from sqlalchemy import Boolean, Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class SeguimientoModelo(Base):
    __tablename__ = "Seguimiento"
    
    id_seguimiento_emprendimiento = Column(Integer, primary_key=True, nullable=False)
    id_proyecto = Column(Integer, ForeignKey("Proyecto.id_proyecto", ondelete="RESTRICT"), nullable=False)
    observaciones = Column(String(400), nullable=False)
    id_usuario_responsable = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False)
    fecha_registro = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    estado = Column(String(15), nullable=False)
    avance_porcentaje = Column(Numeric(5, 2), nullable=False)
    aspecto_revisado = Column(String(200), nullable=False)
    id_mesas = Column(Integer, ForeignKey("Mesas.id", ondelete="RESTRICT"), nullable=False)
    transferir_mesa = Column(Boolean, nullable=False, server_default=text("false"))
    
    proyecto = relationship("ProyectoModelo", back_populates="seguimientos")
    usuario_responsable = relationship("UsuarioModelo", back_populates="seguimientos")
    estados = relationship("EstadosModelo", back_populates="seguimientos")
    mesas = relationship("MesasModelo", back_populates="seguimientos")