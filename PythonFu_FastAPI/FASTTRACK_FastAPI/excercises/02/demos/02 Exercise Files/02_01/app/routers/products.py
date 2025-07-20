from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.product import product_repository
router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/")
def list_products( db: Session = Depends(get_db)):
    """
    Retrieve all products
    """
    product_items= product_repository.get_all(db)
    return product_items

