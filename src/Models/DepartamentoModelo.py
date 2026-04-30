from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Configs.bd import Base

class DepartamentoModelo(Base):
    __tablename__ = "Departamento"
    
    id_departamento = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    latitud = Column(String(30), nullable=False)
    longitud = Column(String(30), nullable=False)
    
    municipio = relationship("MunicipioModelo", back_populates="departamentos")