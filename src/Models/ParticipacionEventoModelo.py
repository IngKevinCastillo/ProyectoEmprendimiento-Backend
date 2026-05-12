from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.EventoModelo import EventoModelo
from Models.RolesModelo import RolesModelo
from Models.UsuarioModelo import UsuarioModelo

class ParticipacionEventoModelo(Base):
    __tablename__ = "ParticipacionEvento"
    
    id_participacion_evento = Column(Integer, primary_key=True, nullable=False)
    id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False)
    id_evento = Column(Integer, ForeignKey("Evento.id_evento", ondelete="RESTRICT"), nullable=False)
    Id_rol = Column(Integer, ForeignKey("Roles.id_rol", ondelete="RESTRICT"), nullable=False)
    id_estado = Column(Integer, ForeignKey("Estados.id_estado", ondelete="RESTRICT"), nullable=False)
    
    usuarios = relationship("UsuarioModelo", back_populates="participaciones")
    evento = relationship("EventoModelo", back_populates="participaciones")
    rol = relationship("RolesModelo", back_populates="participaciones")
    estados = relationship("EstadosModelo", back_populates="participaciones")