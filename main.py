from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional, List

from dbmanager import get_db

from modelitem import Item, ItemSchema


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
@app.post("/items", tags=["Item"], response_model=None)
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