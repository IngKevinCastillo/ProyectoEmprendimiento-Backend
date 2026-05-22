from sqlalchemy import Column, Integer, String, Numeric, Date, Text, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.EstadosModelo import EstadosModelo

class ProyectoModelo(Base):
    __tablename__ = "Proyecto"

    id_proyecto = Column(Integer, primary_key=True, autoincrement=True)
    nombre_proyecto = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    id_estado = Column(Integer, ForeignKey("Estados.id_estado", ondelete="RESTRICT"), nullable=False)
    fecha_creacion = Column(Date, nullable=False, server_default=text("now()"))
    problematica = Column(Text, nullable=True)
    publico_objetivo = Column(Text, nullable=True)
    propuesta_de_valor = Column(Text, nullable=True)
    solucion = Column(Text, nullable=True)
    recursos_clave = Column(Text, nullable=True)
    modelo_de_negocio = Column(Text, nullable=True)
    calificacion = Column(Numeric(precision=3, scale=1), nullable=True)
    id_categoria = Column(Integer, ForeignKey("Categoria.id_categoria", ondelete="RESTRICT"), nullable=False)
    id_tipo_proyecto = Column(Integer, ForeignKey("TipoProyecto.id", ondelete="RESTRICT"), nullable=False)
    id_escala = Column(Integer, ForeignKey("Escala.id", ondelete="RESTRICT"), nullable=False)


    convocatorias = relationship("ConvocatoriasModelo", back_populates="proyecto")
    estados = relationship("EstadosModelo", back_populates="proyecto")
    categoria = relationship("CategoriaModelo", back_populates="proyecto")
    usuarioproyecto = relationship("UsuarioProyectoModelo", back_populates="proyecto")
    proyectopalabrasclave = relationship("ProyectoPalabraClaveModelo", back_populates="proyecto")
    seguimientos = relationship("SeguimientoModelo", back_populates="proyecto")
    tipo_proyecto = relationship("TipoProyectoModelo", back_populates="proyecto")
    escala = relationship("EscalaModelo", back_populates="proyecto")
