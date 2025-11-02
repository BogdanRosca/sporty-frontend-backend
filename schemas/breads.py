from pydantic import BaseModel

class Weight(BaseModel):
    imperial: str
    metric: str

class Height(BaseModel):
    imperial: str
    metric: str

class Image(BaseModel):
    id: str
    width: int
    height: int
    url: str

class DogBreedDetails(BaseModel):
    weight: Weight
    height: Height
    id: int
    name: str
    bred_for: str = None
    breed_group: str = None
    life_span: str = None
    temperament: str = None
    reference_image_id: str = None
    image: Image = None
