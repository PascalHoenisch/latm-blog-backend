from typing import Optional
from pydantic import BaseModel
from model.Translation import Translation
from model.Image import Image


class Author(BaseModel):
    about: Optional[Translation]
    image: Optional[Image]
    name: Optional[str]
    previewImage: Optional[Image]
    slogan: Optional[Translation]
    hidden: Optional[bool]
