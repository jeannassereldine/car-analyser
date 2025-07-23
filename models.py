from typing import Optional
from pydantic import BaseModel, Field


class Car(BaseModel): 
    brand: Optional[str] = Field(default=None ,description='the brand of the car')
    color: Optional[str] = Field(default=None, description='the color of the car')
    type: Optional[str] = Field(default=None, description='Type of the car, e.g., sedan, SUV')
    other_details: Optional[str] = Field(default=None, description='Other useful details about the car')
