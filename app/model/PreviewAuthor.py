from typing import Optional
from pydantic import BaseModel
from model.Translation import Translation
from model.Image import Image


class PreviewAuthor(BaseModel):
    name: Optional[str]
    previewImage: Optional[Image]
    slogan: Optional[Translation]
