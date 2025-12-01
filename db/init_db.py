from database import Base, engine
from models.item import Alumno

Base.metadata.create_all(bind=engine)
