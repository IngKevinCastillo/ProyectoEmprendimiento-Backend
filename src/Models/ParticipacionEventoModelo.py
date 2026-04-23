from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base
from Models.EventoModelo import EventoModelo
from Models.RolesModelo import RolesModelo
from Models.UsuarioModelo import UsuarioModelo

class ParticipacionEventoModelo(Base):
    __tablename__ = "ParticipacionEvento"
    
    id_participacion = Column(Integer, primary_key=True, nullable=False)
    id_usuario = Column(Integer, ForeignKey("UsuarioModelo.id_usuario", ondelete="RESTRICT"), nullable=False)
    id_evento = Column(Integer, ForeignKey("EventoModelo.id_evento", ondelete="RESTRICT"), nullable=False)
    Id_rol = Column(Integer, ForeignKey("RolesModelo.id_rol", ondelete="RESTRICT"), nullable=False)
    
    usuario = relationship("UsuarioModelo", back_populates="ParticipacionEvento")
    evento = relationship("EventoModelo", back_populates="ParticipacionEvento")
    rol = relationship("RolesModelo", back_populates="ParticipacionEvento")