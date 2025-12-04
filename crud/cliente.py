from fastapi import FastAPI, Depends, HTTPException, Path, Body, APIRouter

from sqlalchemy.orm import Session
from models.cliente import Cliente

from schemas.cliente import ClienteSchema, ClienteResponse

def get_clients_crud(db: Session):
    clientsres = db.query(Cliente).all()
    
    if not clientsres:
        raise HTTPException(status_code=404, detail="No hay clientes registrados")
    
    return clientsres

def get_client_crud(ClienteID: int,db: Session):
    clientres = db.query(Cliente).filter(Cliente.id == ClienteID).first()
    
    if not clientres:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    
    return clientres


def create_client_crud(cliente: ClienteSchema, db: Session):
    ClientNuevo = Cliente(**cliente.model_dump())
    
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
    
    client = get_client_crud(ClientID, db)
    
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