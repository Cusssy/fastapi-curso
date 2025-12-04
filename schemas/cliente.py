from pydantic import BaseModel
from typing import Optional, List
from .item import ItemResponse

class ClienteSchema(BaseModel):
    id: Optional[int] = None
    nombre: str
    usuario: str
    telefono: str
    email: str
    bio: str
    hashed_password: str    
    
class ClienteResponse(BaseModel):
    id: Optional[int] = None
    nombre: str
    usuario: str
    telefono: str
    email: str
    bio: str
    items: List[ItemResponse] = []
