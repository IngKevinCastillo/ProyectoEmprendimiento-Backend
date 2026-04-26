from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.RolesModelo import RolesModelo
from Models.ProgramaModelo import ProgramaModelo
from Models.TipoDocumentoModelo import TipoDocumentoModelo
from Models.FacultadModelo import FacultadModelo

class UsuarioModelo(Base):
    __tablename__ = "Usuario"
    
    id_usuario = Column(Integer, primary_key=True)
    primer_nombre = Column(String(30), nullable=False)
    segundo_nombre = Column(String(30), nullable=True)
    primer_apellido = Column(String(30), nullable=False)
    segundo_apellido = Column(String(30), nullable=False)
    correo = Column(String(45), nullable=False, unique=True)
    contrasena = Column(String(100), nullable=False) #modificar diccionario
    id_rol = Column(Integer, ForeignKey("Roles.id_rol", ondelete="RESTRICT"), nullable=False)
    fecha_registro = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
    estado = Column(String(10), nullable=False, default="Activo")
    fecha_nacimiento = Column(TIMESTAMP, nullable=False)
    ubicacion_semestral = Column(Integer, nullable=True)
    sexo = Column(String(30), nullable=False)
    id_programa = Column(Integer, ForeignKey("Programa.id_programa", ondelete="RESTRICT"), nullable=True)
    id_tipodocumento = Column(Integer, ForeignKey("TipoDocumento.id_tipo_documento", ondelete="RESTRICT"), nullable=False)
    numero_documento = Column(String(30), nullable=False, unique=True)
    telefono = Column(String(10), nullable=False)
    id_facultad = Column(Integer, ForeignKey("Facultad.id_facultad", ondelete="RESTRICT"), nullable=True)
    
    rol = relationship("RolesModelo", back_populates="usuarios")
    programa = relationship("ProgramaModelo", back_populates="usuarios")
    tipodocumento = relationship("TipoDocumentoModelo", back_populates="usuarios")
    facultad = relationship("FacultadModelo", back_populates="usuarios")
    #asesorias = relationship("AsesoriasModelo", back_populates="usuario")
    #certificaciones = relationship("CertificacionModelo", back_populates="usuario")
    convocatorias = relationship("ConvocatoriasModelo", back_populates="usuario")
    inscripciones = relationship("InscripcionModelo", back_populates="usuario")
    participaciones = relationship("ParticipacionEventoModelo", back_populates="usuario")
    #postulaciones = relationship("PostulacionesModelo", back_populates="usuario")
    #proyectos = relationship("ProyectoModelo", back_populates="usuario")
    #seguimientos = relationship("SeguimientoModelo", back_populates="usuario_responsable")
    