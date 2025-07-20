from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.product import product_repository
from app.schemas.product import ProductCreate
from app.core.responses import not_found
router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/")
def list_products(
    search: str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve products with optional search and pagination
    """
    if search:
        return product_repository.search(db, search, skip=skip, limit=limit)
    else:
        return product_repository.get_all(db, skip=skip, limit=limit)

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a product by ID 
    """
    product = product_repository.get(db, product_id)
    if not product:
       not_found("Product", product_id)
    return product

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product
    """
    return product_repository.create(
        db, 
        name=product.name,
        description=product.description,
        sku=product.sku,
        price=product.price
    )

