from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class TipoDocumentoModelo(Base):
    __tablename__ = "TipoDocumento"
    
    id_tipo_documento = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    abreviatura = Column(String(10), nullable=False)
    estado = Column(String(10), nullable=False)