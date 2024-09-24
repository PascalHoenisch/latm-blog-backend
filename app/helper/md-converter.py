import markdown

from model.BlogPost import SizeOption


def convert_to_html(content: str, size: SizeOption):
    """
    Function that takes an array of text (Markdown) and Image, and converts them to HTML.
    Images paths are prefixed with the given size.
    
    Args:
    content (list): A list containing text (Markdown) and image dictionary.
                    Example: ['Some text', {'type': 'image', 'src': 'path/to/image.jpg'}]
    size (str): The size prefix to be added to image paths.
    
    Returns:
    str: Combined HTML string.
    """
    html_output = ""

    for item in content:
        if isinstance(item, str):
            # Convert Markdown text to HTML
            html_output += markdown.markdown(item)
        elif isinstance(item, dict) and item.get('type') == 'image':
            image_path = item.get('src', '')
            # Prefix the image path with the given size
            prefixed_image_path = f"{size}/{image_path}"
            html_output += f'<img src="{prefixed_image_path}" />'

    return html_output
