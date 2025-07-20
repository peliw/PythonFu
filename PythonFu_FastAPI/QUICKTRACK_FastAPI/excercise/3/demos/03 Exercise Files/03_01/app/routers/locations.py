from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.location import location_repository
from app.schemas.location import LocationCreate
from app.core.responses import not_found

router = APIRouter(
    prefix="/locations",
    tags=["Locations"]
)


@router.get("/")
def list_locations(    search: str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve locations with optional search and pagination
    """
    if search:
        return location_repository.search(db, search, skip=skip, limit=limit)
    else:
        return location_repository.get_all(db, skip=skip, limit=limit)

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a product by ID without any error handling
    """
    location = location_repository.get(db, product_id)
    if not location:
       not_found("Product", product_id)
    return location


@router.post("/")
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    """
    Create a new location
    """
    return location_repository.create(
        db, 
        name=location.name,
        address=location.address,
        capacity=location.capacity
    )