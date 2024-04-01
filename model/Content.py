from pydantic import BaseModel
from model import Translation


class Content(BaseModel):
    md: Translation
    sm_html: Translation
    md_html: Translation
    lg_html: Translation
