"""Tests for contrast ratio calculations and WCAG compliance."""

import pytest
from src.contrast import (
    relative_luminance,
    calculate_contrast_ratio,
    check_wcag_compliance,
    suggest_adjustment,
)


class TestRelativeLuminance:
    def test_black(self):
        assert relative_luminance((0, 0, 0)) == 0.0
    
    def test_white(self):
        lum = relative_luminance((255, 255, 255))
        assert 0.99 < lum <= 1.0
    
    def test_gray(self):
        lum = relative_luminance((128, 128, 128))
        assert 0.2 < lum < 0.3


class TestCalculateContrastRatio:
    def test_black_white(self):
        ratio = calculate_contrast_ratio((0, 0, 0), (255, 255, 255))
        assert 20.9 < ratio < 21.1
    
    def test_same_color(self):
        ratio = calculate_contrast_ratio((128, 128, 128), (128, 128, 128))
        assert ratio == 1.0
    
    def test_order_independence(self):
        ratio1 = calculate_contrast_ratio((0, 0, 0), (255, 255, 255))
        ratio2 = calculate_contrast_ratio((255, 255, 255), (0, 0, 0))
        assert ratio1 == ratio2


class TestCheckWcagCompliance:
    def test_aa_normal_pass(self):
        result = check_wcag_compliance(4.6, "AA", False)
        assert result["passes"] is True
        assert result["threshold"] == 4.5
    
    def test_aa_normal_fail(self):
        result = check_wcag_compliance(4.0, "AA", False)
        assert result["passes"] is False
    
    def test_aa_large_text(self):
        result = check_wcag_compliance(3.1, "AA", True)
        assert result["passes"] is True
        assert result["threshold"] == 3.0
    
    def test_aaa_normal(self):
        result = check_wcag_compliance(7.5, "AAA", False)
        assert result["passes"] is True
        assert result["threshold"] == 7.0
    
    def test_invalid_level(self):
        with pytest.raises(ValueError, match="Invalid WCAG level"):
            check_wcag_compliance(5.0, "BB")


class TestSuggestAdjustment:
    def test_already_meets(self):
        suggestion = suggest_adjustment(5.0, 4.5)
        assert "already meet" in suggestion.lower()
    
    def test_small_adjustment(self):
        suggestion = suggest_adjustment(4.0, 4.5)
        assert "slightly" in suggestion.lower()
    
    def test_significant_adjustment(self):
        suggestion = suggest_adjustment(2.0, 7.0)
        assert "significant" in suggestion.lower() or "much" in suggestion.lower()