from pydantic import BaseModel, Field

class LocationCreate(BaseModel):
    """Schema for creating a new location"""
    name: str = Field(..., min_length=1, max_length=100)
    address: str = Field(..., min_length=5, max_length=200)
    capacity: int = Field(..., gt=0)