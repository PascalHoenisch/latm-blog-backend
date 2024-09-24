import base64
import hmac
from hashlib import sha1
from helper.env import config

from model.BlogPost import SizeOption


def generate_signed_url(relative_path: str, size: SizeOption):
    # Step 1: Read the base URL and secret key from environment variables
    base_url = config["THUMBOR_URL"]
    security_key = config['THUMBOR_SECRET']

    if not base_url or not security_key:
        raise ValueError('Environment variables THUMBOR_URL and/or THUMBOR_SECRET are missing')

    # Note: Add constant size options that cater to different devices with appropriate paddings
    size_values = {
        'icon': '100x100/filters:round_corner(20,255,255,255)', # 'icon' is a small, rounded-corner thumbnail.
        'sm': '300x300',  # Smartphone: Small size, minimal padding
        'md': '1024x768',  # Tablet: Medium size, moderate padding
        'lg': '1920x1080'  # Big screens: Large size, greater padding
    }

    # Determine the size from the size option
    if size in size_values:
        size = size_values[size]
    else:
        raise ValueError(f'Invalid size option: {size}')

    # Step 2: Construct the URL that we want to sign
    url_to_sign = f"/{size}/{relative_path}"

    # Step 3: Create the signature using HMAC and the security key
    signature = base64.urlsafe_b64encode(
        hmac.new(security_key.encode(), url_to_sign.encode(), sha1).digest()
    ).decode().strip('=')

    # Step 4: Construct the complete signed URL
    signed_url = f"{base_url}/{signature}{url_to_sign}"

    return signed_url
