from pydantic import BaseModel

class ItemSchema(BaseModel):
    nombre: str
    precio: float
    disponible: bool
    
class ItemResponse(BaseModel):
    id: int
    nombre: str
    