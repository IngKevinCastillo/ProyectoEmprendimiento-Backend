from sqlalchemy import Column, Integer, String, Numeric, Date, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.EstadoProyectoModelo import EstadoProyectoModelo

class ProyectoModelo(Base):
    __tablename__ = "Proyecto"
    
    id_proyecto = Column(Integer, primary_key=True)
    nombre_proyecto = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=False)
    id_estado_proyecto = Column(Integer, ForeignKey("estado_proyecto.id_estado_proyecto", ondelete="RESTRICT"), nullable=False)
    fecha_creacion = Column(Date, nullable=False, server_default=text("now()"))

    # seguimientos = relationship("SeguimientoModelo", back_populates="proyectos")
    convocatorias = relationship("ConvocatoriasModelo", back_populates="proyecto")
    estado_proyecto = relationship("EstadoProyectoModelo", back_populates="proyecto")
    usuarioproyecto = relationship("UsuarioProyectoModelo", back_populates="proyecto")
    proyectopalabrasclave = relationship("ProyectoPalabraClaveModelo", back_populates="proyecto")
