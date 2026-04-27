from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Configs.bd import Base

class UsuarioProyectoModelo(Base):
    __tablename__ = "usuario_proyecto"
    
    id_usuario_proyecto = Column(Integer, primary_key=True, nullable=False)
    id_proyecto = Column(Integer, ForeignKey("Proyecto.id_proyecto", ondelete="RESTRICT"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="RESTRICT"), nullable=False)