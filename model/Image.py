from typing import Optional

from pydantic import BaseModel
from model.Translation import Translation


class Image(BaseModel):
    relative_path: Optional[str]
    icon_size: Optional[str]
    sm_size: Optional[str]
    md_size: Optional[str]
    lg_size: Optional[str]
    description: Optional[Translation]
