from .database import Base, engine
from models.item import Item
from models.cliente import Cliente

Base.metadata.create_all(bind=engine)
