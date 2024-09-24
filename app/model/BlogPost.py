from datetime import datetime
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel
from model.Author import PreviewAuthor, ProcessedAuthor
from model.Content import Content
from model.Image import Image, ProcessedImage
from model.Translation import Translation


class BlogPost(BaseModel):
    content: Optional[Content]


class PreviewBlogPost(BaseModel):
    author: Optional[PreviewAuthor]
    date: Optional[datetime]
    tag: List[str]
    title: Optional[Translation]
    slug: Optional[Translation]
    description: Optional[Translation]
    title_image: Optional[Image]
    id: Optional[int]

    class Config:
        arbitrary_types_allowed = True


class ProcessedPreviewPost(BaseModel):
    author: Optional[ProcessedAuthor]
    date: Optional[datetime]
    tag: List[str]
    title: str
    slug: str
    description: str
    title_image: Optional[ProcessedImage]
    id: Optional[str]
    

class ProcessedPost(ProcessedPreviewPost):
    content: str


class SizeOption(Enum):
    sm_html = 'sm'
    md_html = 'md'
    lg_html = 'lg'
    