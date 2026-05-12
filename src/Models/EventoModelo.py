from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class EventoModelo(Base):
    __tablename__ = "Evento"
    
    id_evento = Column(Integer, primary_key=True)
    nombre_evento = Column(String(50), nullable=False)
    tipo_evento = Column(String(30), nullable=False)
    fecha = Column(TIMESTAMP, nullable=False)
    lugar = Column(String(60), nullable=False)
    descripcion = Column(String, nullable=False)
    id_estado = Column(Integer, ForeignKey("Estados.id_estado", ondelete="RESTRICT"), nullable=False)
    
    participaciones = relationship("ParticipacionEventoModelo", back_populates="evento")
    estados = relationship("EstadosModelo", back_populates="evento")