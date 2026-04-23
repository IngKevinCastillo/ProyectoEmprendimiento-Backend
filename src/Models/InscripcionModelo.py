from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.UsuarioModelo import UsuarioModelo
from Models.CursoModelo import CursoModelo

class InscripcionModelo(Base):
    __tablename__ = "Inscripcion"
    
    id_inscripcion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False, unique=True)
    id_curso = Column(Integer, ForeignKey("Curso.id_curso", ondelete="RESTRICT"), nullable=False, unique=True)
    fecha_inscripcion = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
    
    usuario = relationship("UsuarioModelo", back_populates="inscripciones")
    curso = relationship("CursoModelo", back_populates="inscripciones")
    