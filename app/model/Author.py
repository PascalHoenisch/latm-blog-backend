from typing import Optional
from model.Translation import Translation
from model.Image import Image, ProcessedImage
from model.PreviewAuthor import PreviewAuthor
from pydantic import BaseModel


class Author(PreviewAuthor):
    about: Optional[Translation]
    image: Optional[Image]
    hidden: Optional[bool]


class ProcessedAuthor(BaseModel):
    name: str
    slogan: str
    image: ProcessedImage
