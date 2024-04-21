from _datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from model.Translation import Translation
from model.Image import Image
from model.PreviewAuthor import PreviewAuthor


class PreviewBlogPost(BaseModel):
    author: Optional[PreviewAuthor]
    date: Optional[datetime]
    tag: List[str]
    title: Optional[Translation]
    slug: Optional[Translation]
    description: Optional[Translation]
    title_image: Optional[Image]

    class Config:
        arbitrary_types_allowed = True
