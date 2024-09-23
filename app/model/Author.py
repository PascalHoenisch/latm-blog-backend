from typing import Optional
from model.Translation import Translation
from model.Image import Image, ProcessedImage
from pydantic import BaseModel


class Author(BaseModel):
    about: Optional[Translation]
    image: Optional[Image]
    hidden: Optional[bool]
    name: Optional[str]
    previewImage: Optional[Image]
    slogan: Optional[Translation]


class ProcessedAuthor(BaseModel):
    name: str
    slogan: str
    image: ProcessedImage


class PreviewAuthor(BaseModel):
    name: Optional[str]
    previewImage: Optional[Image]
    slogan: Optional[Translation]
