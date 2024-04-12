from typing import Optional
from model.Content import Content
from model.PreviewBlogPost import PreviewBlogPost


class BlogPost(PreviewBlogPost):
    content: Optional[Content]
