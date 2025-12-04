from pydantic import BaseModel
from typing import Optional, List
from .item import ItemClienteResponse

class ClienteSchema(BaseModel):
    id: Optional[int] = None
    nombre: str
    usuario: str
    telefono: str
    email: str
    bio: str
    hashed_password: str    
    
    class config:
        orm_mode = True
    

class ClienteResponse(BaseModel):
    id: int
    nombre: str
    
    class config:
        orm_mode = True

class ClienteItemsResponse(BaseModel):
    id: int
    nombre: str
    usuario: str
    telefono: str
    email: str
    bio: str
    items: List[ItemClienteResponse] = []
    
    class config:
        orm_mode = True
