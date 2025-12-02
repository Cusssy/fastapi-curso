from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base



class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    precio = Column(Float, nullable=False)
    disponible = Column(Boolean, default=False)
    
    cliente_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    
    # 1 a 1: muchos items pueden pertenecer a un cliente
    cliente = relationship("Cliente", back_populates="items")
