from pydantic import BaseModel
from typing import Optional

class ItemSchema(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    disponible: bool
    
class ItemResponse(BaseModel):
    id: int
    nombre: str
