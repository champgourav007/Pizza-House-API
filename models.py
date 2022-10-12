from typing import List
import uuid
from pydantic import BaseModel
from datetime import datetime

class Orders(BaseModel):
    order : List[str] = []
    orderTime : datetime = datetime.now()
    
class OrderView(BaseModel):
    id : str
    order : List[str]
    orderTime : datetime