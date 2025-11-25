"""Color parsing and conversion utilities."""

import re
from typing import Tuple

CSS_COLORS = {
    "black": (0, 0, 0), "white": (255, 255, 255), "red": (255, 0, 0),
    "green": (0, 128, 0), "blue": (0, 0, 255), "yellow": (255, 255, 0),
    "cyan": (0, 255, 255), "magenta": (255, 0, 255), "gray": (128, 128, 128),
    "grey": (128, 128, 128), "silver": (192, 192, 192), "maroon": (128, 0, 0),
    "olive": (128, 128, 0), "lime": (0, 255, 0), "aqua": (0, 255, 255),
    "teal": (0, 128, 128), "navy": (0, 0, 128), "fuchsia": (255, 0, 255),
    "purple": (128, 0, 128), "orange": (255, 165, 0),
}


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    
    if len(hex_color) == 3:
        hex_color = "".join([c * 2 for c in hex_color])
    
    if len(hex_color) != 6:
        raise ValueError(f"Invalid hex color: #{hex_color}")
    
    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)
    except ValueError:
        raise ValueError(f"Invalid hex color: #{hex_color}")


def parse_rgb(rgb_str: str) -> Tuple[int, int, int]:
    """Parse RGB string format."""
    match = re.match(r"rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", rgb_str, re.IGNORECASE)
    if not match:
        raise ValueError(f"Invalid RGB format: {rgb_str}")
    
    r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
    
    if not all(0 <= c <= 255 for c in (r, g, b)):
        raise ValueError(f"RGB values must be 0-255: {rgb_str}")
    
    return (r, g, b)


def parse_color(color_str: str) -> Tuple[int, int, int]:
    """Parse color from various formats."""
    color_str = color_str.strip().lower()
    
    if color_str in CSS_COLORS:
        return CSS_COLORS[color_str]
    
    if color_str.startswith("#"):
        return hex_to_rgb(color_str)
    
    if color_str.startswith("rgb"):
        return parse_rgb(color_str)
    
    raise ValueError(f"Unrecognized color format: {color_str}")
