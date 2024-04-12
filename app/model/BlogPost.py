from _datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from model.Translation import Translation
from model.Content import Content
from model.Image import Image
from model.Author import Author


class BlogPost(BaseModel):
    author: Optional[Author]
    date: Optional[datetime]
    tag: List[str]
    title: Optional[Translation]
    slug: Optional[Translation]
    description: Optional[Translation]
    content: Optional[Content]
    title_image: Optional[Image]

    class Config:
        arbitrary_types_allowed = True