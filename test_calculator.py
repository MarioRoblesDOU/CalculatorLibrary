"""
Unit tests for the calculator library
"""

import calculatordef


class TestCalculator:

    def test_addition(self):
        assert calculatordef.add(2, 2) == 4

    def test_subtraction(self):
        assert calculatordef.subtract(4, 2) == 2