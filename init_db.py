from database import Base, engine
from modelitem import Alumno

Base.metadata.create_all(bind=engine)
