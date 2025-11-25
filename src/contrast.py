"""Core contrast ratio calculation and WCAG compliance checking."""

from typing import Tuple, Dict


def relative_luminance(rgb: Tuple[int, int, int]) -> float:
    """Calculate relative luminance using WCAG formula."""
    r, g, b = [c / 255.0 for c in rgb]
    
    def adjust(channel: float) -> float:
        if channel <= 0.03928:
            return channel / 12.92
        return ((channel + 0.055) / 1.055) ** 2.4
    
    r_adj = adjust(r)
    g_adj = adjust(g)
    b_adj = adjust(b)
    
    return 0.2126 * r_adj + 0.7152 * g_adj + 0.0722 * b_adj


def calculate_contrast_ratio(color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> float:
    """Calculate contrast ratio between two colors."""
    lum1 = relative_luminance(color1)
    lum2 = relative_luminance(color2)
    
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    return (lighter + 0.05) / (darker + 0.05)


def check_wcag_compliance(ratio: float, level: str = "AA", large_text: bool = False) -> Dict[str, bool]:
    """Check if contrast ratio meets WCAG standards."""
    if level.upper() == "AA":
        threshold = 3.0 if large_text else 4.5
    elif level.upper() == "AAA":
        threshold = 4.5 if large_text else 7.0
    else:
        raise ValueError(f"Invalid WCAG level: {level}. Use 'AA' or 'AAA'.")
    
    passes = ratio >= threshold
    
    return {
        "passes": passes,
        "ratio": ratio,
        "threshold": threshold,
        "level": level.upper(),
        "large_text": large_text,
    }


def suggest_adjustment(ratio: float, target_ratio: float) -> str:
    """Suggest color adjustments to meet target ratio."""
    if ratio >= target_ratio:
        return "Colors already meet the requirement."
    
    diff = target_ratio - ratio
    
    if diff < 1.0:
        return "Try slightly adjusting brightness of one color."
    elif diff < 2.0:
        return "Consider lightening the lighter color or darkening the darker color."
    else:
        return "Significant adjustment needed. Try using much lighter or darker colors."
