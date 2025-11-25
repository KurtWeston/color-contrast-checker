"""Color Contrast Checker - WCAG accessibility compliance tool."""

__version__ = "1.0.0"
__author__ = "Color Contrast Checker"

from .contrast import calculate_contrast_ratio, check_wcag_compliance
from .colors import parse_color, hex_to_rgb

__all__ = [
    "calculate_contrast_ratio",
    "check_wcag_compliance",
    "parse_color",
    "hex_to_rgb",
]
