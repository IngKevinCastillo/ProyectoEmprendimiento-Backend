from sqlalchemy import Column, Integer, String, Boolean, DateTime
from Configs.bd import Base

class OTPModelo(Base):
    __tablename__ = "OTP"

    id = Column(Integer, primary_key=True)
    correo = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    expiracion = Column(DateTime, nullable=False)
    usado = Column(Boolean, default=False)