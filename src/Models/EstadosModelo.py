from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class EstadosModelo(Base):
    __tablename__ = "Estados"
    
    id_estado = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(40), nullable=False)
    descripcion = Column(String(40), nullable=True)
    
    proyecto = relationship("ProyectoModelo", back_populates="estados")
    seguimientos = relationship("SeguimientoModelo", back_populates="estados")
    evento = relationship("EventoModelo", back_populates="estados")
    curso = relationship("CursoModelo", back_populates="estados")
    usuarios = relationship("UsuarioModelo", back_populates="estados")
    participaciones = relationship("ParticipacionEventoModelo", back_populates="estados")
    inscripciones = relationship("InscripcionModelo", back_populates="estados")
    alianzas = relationship("AlianzaModelo", back_populates="estados")
    convocatorias = relationship("ConvocatoriaModelo", back_populates="estado")
    evaluaciones = relationship("EvaluacionModelo", back_populates="estado")
    postulaciones = relationship("PostulacionModelo", back_populates="estado")
    rol = relationship("RolesModelo", back_populates="estado")