import pytest
from bmi_calculator import calculate_bmi

def test_underweight():
    assert calculate_bmi(5, 10, 120) == (17.2, "Underweight")

def test_normal_weight():
    assert calculate_bmi(5, 10, 150) == (21.5, "Normal weight")

def test_overweight():
    assert calculate_bmi(5, 10, 180) == (25.8, "Overweight")

def test_obese():
    assert calculate_bmi(5, 10, 220) == (31.6, "Obese")

# Edge Cases
def test_boundary_underweight_to_normal():
    assert calculate_bmi(5, 10, 129) == (18.5, "Normal weight")

def test_boundary_normal_to_overweight():
    assert calculate_bmi(5, 10, 174) == (25.0, "Overweight")  

def test_boundary_overweight_to_obese():
    assert calculate_bmi(5, 10, 205) == (29.4, "Overweight")  

