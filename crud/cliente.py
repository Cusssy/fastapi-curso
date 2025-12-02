from fastapi import FastAPI, Depends, HTTPException, Path, Body, APIRouter

from sqlalchemy.orm import Session
from models.cliente import Cliente

from schemas.cliente import ClienteSchema, ClienteResponse

def get_clients_crud(db: Session):
    clientres = db.query(Cliente).all()
    
    for cliente in clientres:
        print(cliente.items) 
    
    return 


def create_client_crud(cliente: ClienteSchema, db: Session):
    ClientNuevo = Cliente(
        nombre=cliente.nombre,
        usuario=cliente.usuario,
        telefono=cliente.telefono,
        email=cliente.email,
        bio=cliente.bio,
        hashed_password=cliente.hashed_password
        
    
    )
    db.add(ClientNuevo)
    db.commit()
    db.refresh(ClientNuevo)
    return ClientNuevo

def get_client_crud(ClientID: int, db: Session):
    client = db.query(Cliente).filter(Cliente.id == ClientID).first()
    return client

def delete_client_crud(ClientID: int, db: Session):
    client = db.query(Cliente).filter(Cliente.id == ClientID).first()
    
    if not client:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    db.delete(client)
    db.commit()
    return {"msg": "Item eliminado", "client": client}

def update_client_crud(ClientID: int, db: Session, datos: ClienteSchema):
    
    client = db.query(Cliente).filter(Cliente.id == ClientID).first()
    
    if not client:
        raise HTTPException(status_code=404, detail="Item no encontrado")
        
    client.nombre = datos.nombre
    client.usuario = datos.usuario
    client.telefono = datos.telefono
    client.email = datos.email
    client.bio = datos.bio
    client.hashed_password = datos.hashed_password
    
    
    
    db.commit()
    db.refresh(client)
    return client