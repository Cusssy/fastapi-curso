from fastapi import FastAPI, Depends, HTTPException, Path, Body, APIRouter

from sqlalchemy.orm import Session, joinedload
from models.item import Item

from schemas.cliente_item import ItemSchema, ItemResponse

def get_items_crud(db: Session):
    return db.query(Item).all()

def get_items_clientes_crud(db: Session):
    return db.query(Item).options(joinedload(Item.cliente)).all()

def get_item_crud(ItemID: int, db: Session):
    items = db.query(Item).filter(Item.id == ItemID).first()
    return items

def get_item_cliente_crud(ItemID: int, db: Session):
    return db.query(Item).options(joinedload(Item.cliente)).filter(Item.id == ItemID).first()


def create_item_crud(item: ItemSchema, db: Session):
    ItemNuevo = Item(
        nombre=item.nombre,
        precio=item.precio,
        disponible=item.disponible,
        cliente_id=item.cliente_id
    )
    db.add(ItemNuevo)
    db.commit()
    db.refresh(ItemNuevo)
    return ItemNuevo

def delete_item_crud(ItemID: int, db: Session):
    item = db.query(Item).filter(Item.id == ItemID).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    db.delete(item)
    db.commit()
    return {"msg": "Item eliminado", "item": item}

def update_item_crud(ItemID: int, db: Session, datos: ItemSchema):
    
    item = db.query(Item).filter(Item.id == ItemID).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
        
    item.nombre     = datos.nombre
    item.precio     = datos.precio
    item.disponible = datos.disponible
    item.cliente_id = datos.cliente_id
    
    
    db.commit()
    db.refresh(item)
    return item