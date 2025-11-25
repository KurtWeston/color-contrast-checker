"""Tests for color parsing and conversion."""

import pytest
from src.colors import hex_to_rgb, parse_rgb, parse_color


class TestHexToRgb:
    def test_six_digit_hex(self):
        assert hex_to_rgb("#FF0000") == (255, 0, 0)
        assert hex_to_rgb("#00FF00") == (0, 255, 0)
        assert hex_to_rgb("#0000FF") == (0, 0, 255)
    
    def test_three_digit_hex(self):
        assert hex_to_rgb("#F00") == (255, 0, 0)
        assert hex_to_rgb("#0F0") == (0, 255, 0)
        assert hex_to_rgb("#ABC") == (170, 187, 204)
    
    def test_without_hash(self):
        assert hex_to_rgb("FF0000") == (255, 0, 0)
    
    def test_invalid_hex_length(self):
        with pytest.raises(ValueError, match="Invalid hex color"):
            hex_to_rgb("#FF")
    
    def test_invalid_hex_characters(self):
        with pytest.raises(ValueError, match="Invalid hex color"):
            hex_to_rgb("#GGGGGG")


class TestParseRgb:
    def test_valid_rgb(self):
        assert parse_rgb("rgb(255, 0, 0)") == (255, 0, 0)
        assert parse_rgb("rgb(0,255,0)") == (0, 255, 0)
    
    def test_case_insensitive(self):
        assert parse_rgb("RGB(100, 150, 200)") == (100, 150, 200)
    
    def test_out_of_range(self):
        with pytest.raises(ValueError, match="RGB values must be 0-255"):
            parse_rgb("rgb(256, 0, 0)")
    
    def test_invalid_format(self):
        with pytest.raises(ValueError, match="Invalid RGB format"):
            parse_rgb("rgb(100, 200)")


class TestParseColor:
    def test_css_named_colors(self):
        assert parse_color("red") == (255, 0, 0)
        assert parse_color("white") == (255, 255, 255)
        assert parse_color("black") == (0, 0, 0)
    
    def test_hex_colors(self):
        assert parse_color("#FF0000") == (255, 0, 0)
        assert parse_color("#F00") == (255, 0, 0)
    
    def test_rgb_colors(self):
        assert parse_color("rgb(255, 0, 0)") == (255, 0, 0)
    
    def test_unrecognized_format(self):
        with pytest.raises(ValueError, match="Unrecognized color format"):
            parse_color("notacolor")