from sqlalchemy import Column, Integer, String, Boolean, Float
from db.database import Base



class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    precio = Column(Float, nullable=False)
    disponible = Column(Boolean, default=False)
