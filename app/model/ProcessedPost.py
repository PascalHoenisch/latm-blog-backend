from _datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from model.Image import ProcessedImage
from model.Author import ProcessedAuthor
from enum import Enum


class ProcessedPost(BaseModel):
    author: Optional[ProcessedAuthor]
    date: Optional[datetime]
    tag: List[str]
    title: str
    slug: str
    description: str
    content: str
    title_image: Optional[ProcessedImage]


class SizeOption(Enum):
    sm_html = 'sm'
    md_html = 'md'
    lg_html = 'lg'
