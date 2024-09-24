import markdown
import re

from model.BlogPost import SizeOption
from helper.image_tools import generate_signed_url


def convert_to_html(content: str, size: SizeOption):
    """
    Function that takes a Markdown text containing text and images, and converts it to HTML.
    Images paths are prefixed with the given size.
    
    Args:
    content (str): A Markdown string containing text and image links.
    size (SizeOption): The size option to be added to image paths.
    
    Returns:
    str: Combined HTML string.
    """

    def replace_image_paths(match):
        img_path = match.group(2)
        signed_url = generate_signed_url(relative_path=img_path, size=size)
        return f'![{match.group(1)}]({signed_url})'

    # Regex pattern to find Markdown image tags ![alt](src)
    pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

    # Replace image paths with signed URLs
    updated_content = re.sub(pattern, replace_image_paths, content)

    # Convert Markdown text to HTML
    html_output = markdown.markdown(updated_content)

    return html_output
