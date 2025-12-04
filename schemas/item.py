from pydantic import BaseModel
from typing import Optional


class ItemSchema(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    disponible: bool
    cliente_id: Optional[int] = None


class ItemResponse(BaseModel):
    id: int
    nombre: str
    
    class config:
        from_attributes = True


class ItemClienteResponse(BaseModel):
    id: int
    nombre: str
    precio: float
    disponible: bool
    cliente_id: Optional[int] = None

    class config:
        from_attributes = True


