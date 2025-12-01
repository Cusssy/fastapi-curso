from fastapi import FastAPI, Depends, HTTPException, Path, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional, List

from db.dbmanager import get_db

from models.item import Item
from schemas.schemas import ItemSchema, ItemResponse


app = FastAPI()

# Lista de orígenes permitidos
origins = [
    "http://localhost:5500",  # si tu frontend corre aquí
    "http://127.0.0.1:5500",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],  # permite cualquier origen (no recomendable en producción)
    allow_origins=origins,  # permite solo esos orígenes
    allow_credentials=True,
    allow_methods=["*"],    # permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],    # permite todas las cabeceras
)




contador = 0

@app.get("/data")
def get_data():
    return {"msg": "Hola alumnos"}

# @app.post("/afegirItem/",tags=["Item"])
# def afegir_item(item: Item):
#     global contador
#     item_temp = item.model_dump()
#     item_temp["id"] = contador
#     contador += 1
#     return {"msg": "Item afegit", "item": item}

@app.get("/items", tags=["Item"], response_model=List[ItemResponse])
def get_all_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

@app.post("/items", tags=["Item"], response_model=ItemResponse)
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

@app.get("/items/{ItemID}", tags=["Item"])
def get_items(ItemID: int = Path(..., ge=1, description="id del item"), db: Session = Depends(get_db)):
    items = db.query(Item).filter(Item.id == ItemID).first()
    return items

@app.delete("/items/{ItemID}", tags=["Item"])
def get_item(ItemID: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == ItemID).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    db.delete(item)
    db.commit()
    return {"msg": "Item eliminado", "item": item}

@app.put("/items/{ItemID}", tags=["Item"], response_model=ItemResponse)
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