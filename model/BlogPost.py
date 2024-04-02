import datetime
import array

from typing import Optional
from pydantic import BaseModel
from model import Translation, Content, Image


class BlogPost(BaseModel):
    author: Optional[str]
    date: datetime
    tag: array
    title: Translation
    slug: Translation
    description: Translation
    content: Content
    title_image: Image
