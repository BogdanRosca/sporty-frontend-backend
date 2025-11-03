from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Image(BaseModel):
    id: str
    url: str

class FavouriteImage(BaseModel):
    id: int
    user_id: str
    image_id: str
    sub_id: Optional[str] = None
    created_at: str
    image: Image
