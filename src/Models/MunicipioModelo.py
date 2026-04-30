from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class MunicipioModelo(Base):
    __tablename__ = "Municipio"
    
    id_municipio = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    id_departamento = Column(Integer, ForeignKey("Departamento.id_departamento", ondelete="RESTRICT"), nullable=False)
    latitud = Column(String(30), nullable=False)
    longitud = Column(String(30), nullable=False)
    
    departamentos = relationship("DepartamentoModelo", back_populates="municipio")    
    usuarios = relationship("UsuarioModelo", back_populates="municipio")