from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from src.Configs.bd import Base

class RolModelo(Base):
    __tablename__ = "Rol"
    
    id_rol = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    estado = Column(String(10), nullable=False)