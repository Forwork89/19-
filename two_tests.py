import pytest
from app.calculator import Calculator


class TestCalc:


    def setup(self):
        self.calc = Calculator

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 1) == 3