from Configs.bd import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

class MesasModelo(Base):
    __tablename__ = "Mesas"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    cedula_tutor = Column(String, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False)
    cedulas_docentes = Column(ARRAY(String), nullable=True)

    usuarios = relationship("UsuarioModelo", foreign_keys=[cedula_tutor], back_populates="mesas")