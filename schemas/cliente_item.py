from typing import Optional, List
from pydantic import BaseModel

# ------------ Input ------------
class ItemSchema(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    disponible: bool
    cliente_id: Optional[int] = None
    
class ClienteSchema(BaseModel):
    id: Optional[int] = None
    nombre: str
    usuario: str
    telefono: str
    email: str
    bio: str
    hashed_password: str    
    
    class config:
        from_attributes = True
        
class ClienteSimple(BaseModel):
    pass

# ------------ Output ------------

class ItemResponse(BaseModel):
    id: int
    nombre: str
    
    class config:
        from_attributes = True
        
class ClienteItemsResponse(BaseModel):
    items: List["ItemClienteResponse"] = []
    
    class config:
        from_attributes = True        

class ClienteResponse(BaseModel):
    id: int
    nombre: str
    
    class config:
        from_attributes = True
        

class ItemClienteResponse(BaseModel):
    cliente: Optional["ClienteResponse"] = None

    class config:
        from_attributes = True


