from fastapi import FastAPI, Depends, HTTPException, Path, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from db.dbmanager import get_db

from models.item import Item
from schemas.schemas import ItemSchema, ItemResponse

from routes import item


app = FastAPI()

app.include_router(item.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permite cualquier origen (no recomendable en producción)
    allow_credentials=True,
    allow_methods=["*"],    # permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],    # permite todas las cabeceras
)

@app.get("/")
def get_data():
    return {"msg": "Hola mundo"}