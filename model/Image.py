from pydantic import BaseModel
from model import Translation


class Image(BaseModel):
    relative_path: str
    icon_size: str
    sm_size: str
    md_size: str
    lg_size: str
    description: Translation
