from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class ApoyoGeneralTipoEntidadesModelo(Base):
    __tablename__ = "ApoyoGeneral"
    
    id_apoyo_general = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(100), nullable=False)