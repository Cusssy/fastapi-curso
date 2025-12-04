from fastapi import FastAPI, Depends, HTTPException, Path, Body, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional, List

from db.dbmanager import get_db

from models.cliente import Cliente
from schemas.cliente import ClienteSchema, ClienteItemsResponse

from crud.cliente import get_clients_crud, create_client_crud, get_client_crud, delete_client_crud, update_client_crud

router = APIRouter(prefix="/clients", tags=["client"])

@router.get("/", response_model=List[ClienteItemsResponse])
def get_clients(db: Session = Depends(get_db)):
    return get_clients_crud(db)

@router.post("/", response_model=ClienteItemsResponse)
def create_client(cliente: ClienteSchema ,db: Session = Depends(get_db)):
    return create_client_crud(cliente, db)

@router.get("/{ClientID}")
def get_client(ClientID: int = Path(..., ge=1, description="id del client"), db: Session = Depends(get_db)):
    return get_client_crud(ClientID, db)

@router.delete("/{ClientID}")
def delete_client(ClientID: int, db: Session = Depends(get_db)):
    return delete_client_crud(ClientID, db)

@router.put("/{ClientID}", response_model=ClienteItemsResponse)
def update_client(ClientID: int = Path(..., ge=1, description="id del client"), db: Session = Depends(get_db), datos: ClienteSchema = Body()):
    return update_client_crud(ClientID, db, datos)