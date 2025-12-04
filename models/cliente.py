from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from db.database import Base

class Cliente(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    usuario = Column(String(50), nullable=False)
    telefono = Column(String(9), nullable=True)
    email = Column(String(50), nullable=False)
    bio = Column(String(200), default=False)
    hashed_password = Column(String(100), nullable=False)
    
    # 1 a muchos: un cliente puede tener muchos items
    items = relationship("Item", back_populates="cliente")

