from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from src.Configs.bd import Base

class IndicadorModelo(Base):
    __tablename__ = "Indicador"
    
    id_indicador      = Column(Integer, primary_key=True)
    nombre_indicador  = Column(String(45), nullable=False)
    formula           = Column(String, nullable=False)
    meta              = Column(Numeric(10,2), nullable=False)
    valor_actual      = Column(Numeric(10,2), nullable=False, default=0.00)