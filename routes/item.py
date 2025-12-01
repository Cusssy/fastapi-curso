from fastapi import FastAPI, Depends, HTTPException, Path, Body, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional, List

from db.dbmanager import get_db

from models.item import Item
from schemas.schemas import ItemSchema, ItemResponse

router = APIRouter(prefix="/items", tags=["Item"])

@router.get("/", response_model=List[ItemResponse])
def get_all_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items


@router.post("/", response_model=ItemResponse)
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    ItemNuevo = Item(
        nombre=item.nombre,
        precio=item.precio,
        disponible=item.disponible
    )
    db.add(ItemNuevo)
    db.commit()
    db.refresh(ItemNuevo)
    return ItemNuevo

@router.get("/{ItemID}")
def get_items(ItemID: int = Path(..., ge=1, description="id del item"), db: Session = Depends(get_db)):
    items = db.query(Item).filter(Item.id == ItemID).first()
    return items

@router.delete("/{ItemID}")
def get_item(ItemID: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == ItemID).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    db.delete(item)
    db.commit()
    return {"msg": "Item eliminado", "item": item}

@router.put("/{ItemID}", response_model=ItemResponse)
def update_item(ItemID: int = Path(..., ge=1, description="id del item"), 
                db: Session = Depends(get_db), datos: ItemSchema = Body()):
    
    item = db.query(Item).filter(Item.id == ItemID).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
        
    item.nombre     = datos.nombre
    item.precio     = datos.precio
    item.disponible = datos.disponible
    
    
    db.commit()
    db.refresh(item)
    return item