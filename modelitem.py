from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base
from pydantic import BaseModel


class Alumno(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)


class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    precio = Column(Float, nullable=False)
    disponible = Column(Boolean, default=False)
    

class ItemSchema(BaseModel):
    nombre: str
    precio: float
    disponible: bool