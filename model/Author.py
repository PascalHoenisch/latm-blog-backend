from pydantic import BaseModel
from model import Translation, Image


class Author(BaseModel):
    about: Translation
    image: Image
    name: str
    previewImage: Image
    slogan: Translation
    hidden: bool
