from fastapi import FastAPI, Depends, HTTPException, Path, Body, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional, List

from db.dbmanager import get_db

from models.item import Item
from schemas.item import ItemSchema, ItemResponse

from crud.item import get_items_crud, create_item_crud, get_item_crud, delete_item_crud, update_item_crud

router = APIRouter(prefix="/items", tags=["Item"])

@router.get("/", response_model=List[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return get_items_crud(db)

@router.post("/", response_model=ItemResponse)
def create_item(datos: ItemSchema = Body(...), db: Session = Depends(get_db)):
    return create_item_crud(datos, db)

@router.get("/{ItemID}")
def get_item(ItemID: int = Path(..., ge=1, description="id del item"), db: Session = Depends(get_db)):
    return get_item_crud(ItemID, db)

@router.delete("/{ItemID}")
def delete_item(ItemID: int, db: Session = Depends(get_db)):
    return delete_item_crud(ItemID, db)

@router.put("/{ItemID}", response_model=ItemResponse)
def update_item(ItemID: int = Path(..., ge=1, description="id del item"), db: Session = Depends(get_db), datos: ItemSchema = Body()):
    return update_item_crud(ItemID, datos, db)