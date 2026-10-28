from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class EstadosModelo(Base):
    __tablename__ = "Estados"
    
    id_estado = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(40), nullable=False)
    descripcion = Column(String(40), nullable=True)
    evento = relationship("EventoModelo", back_populates="estados")
    curso = relationship("CursoModelo", back_populates="estados")
    participaciones = relationship("ParticipacionEventoModelo", back_populates="estados")
    inscripciones = relationship("InscripcionModelo", back_populates="estados")
    alianzas = relationship("AlianzaModelo", back_populates="estados")
    evaluaciones = relationship("EvaluacionModelo", back_populates="estado")
    postulaciones = relationship("PostulacionModelo", back_populates="estado")
    beneficios_asignados = relationship("BeneficioAsignadoModelo", back_populates="estado")
    metas = relationship("MetasModelo", back_populates="estado")
