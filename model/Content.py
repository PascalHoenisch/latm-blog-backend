from pydantic import BaseModel
from model.Translation import Translation
from typing import Optional


class Content(BaseModel):
    md: Optional[Translation]
    sm_html: Optional[Translation]
    md_html: Optional[Translation]
    lg_html: Optional[Translation]
