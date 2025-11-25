"""Command-line interface for color contrast checker."""

import argparse
import sys
from typing import Optional

from .colors import parse_color
from .contrast import calculate_contrast_ratio, check_wcag_compliance, suggest_adjustment


def format_color_block(rgb: tuple) -> str:
    """Format color as ANSI colored block."""
    r, g, b = rgb
    return f"\033[48;2;{r};{g};{b}m  \033[0m"


def print_results(fg_rgb: tuple, bg_rgb: tuple, fg_str: str, bg_str: str, args) -> None:
    """Print formatted contrast check results."""
    ratio = calculate_contrast_ratio(fg_rgb, bg_rgb)
    
    print(f"\n{'='*60}")
    print(f"Color Contrast Analysis")
    print(f"{'='*60}")
    print(f"\nForeground: {fg_str} {format_color_block(fg_rgb)} RGB{fg_rgb}")
    print(f"Background: {bg_str} {format_color_block(bg_rgb)} RGB{bg_rgb}")
    print(f"\nContrast Ratio: {ratio:.2f}:1")
    
    large_text = args.large if hasattr(args, 'large') else False
    
    for level in ["AA", "AAA"]:
        result = check_wcag_compliance(ratio, level, large_text)
        status = "\033[92mPASS\033[0m" if result["passes"] else "\033[91mFAIL\033[0m"
        text_type = "Large Text" if large_text else "Normal Text"
        print(f"\nWCAG {level} ({text_type}): {status}")
        print(f"  Required: {result['threshold']:.1f}:1")
        
        if not result["passes"]:
            suggestion = suggest_adjustment(ratio, result["threshold"])
            print(f"  Suggestion: {suggestion}")
    
    print(f"\n{'='*60}\n")


def main(argv: Optional[list] = None) -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Check color contrast ratios for WCAG accessibility compliance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument("foreground", help="Foreground color (hex, rgb(), or CSS name)")
    parser.add_argument("background", help="Background color (hex, rgb(), or CSS name)")
    parser.add_argument(
        "-l", "--large",
        action="store_true",
        help="Check for large text (lower threshold)",
    )
    
    args = parser.parse_args(argv)
    
    try:
        fg_rgb = parse_color(args.foreground)
        bg_rgb = parse_color(args.background)
        print_results(fg_rgb, bg_rgb, args.foreground, args.background, args)
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
