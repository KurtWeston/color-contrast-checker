"""Tests for CLI interface."""

import pytest
from io import StringIO
from src.cli import main, format_color_block


class TestFormatColorBlock:
    def test_format_color(self):
        result = format_color_block((255, 0, 0))
        assert "\033[48;2;255;0;0m" in result
        assert "\033[0m" in result


class TestCliMain:
    def test_valid_hex_colors(self):
        result = main(["#000000", "#FFFFFF"])
        assert result == 0
    
    def test_valid_named_colors(self):
        result = main(["black", "white"])
        assert result == 0
    
    def test_large_text_flag(self):
        result = main(["#000000", "#FFFFFF", "--large"])
        assert result == 0
    
    def test_invalid_color(self):
        result = main(["notacolor", "white"])
        assert result == 1
    
    def test_rgb_format(self):
        result = main(["rgb(0, 0, 0)", "rgb(255, 255, 255)"])
        assert result == 0