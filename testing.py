import pytest
import math
from equation import solv

cases = [(9, 5, 7, 3), (5, 5, 10, 8), (3, 5, 10, 8), (9, 4, 7, 7)]

for a, b, c, d in cases:
    try:
        print(a, b, c, d, solv(a, b, c, d))
    except Exception as e:
        print(a, b, c, d, e)


def test_normal_case():
    assert solv(9, 5, 7, 3) == 0.5

def test_zero_under_root():
    assert solv(5, 5, 10, 8) == 0.0

def test_negative_under_root():
    with pytest.raises(ValueError) as e:
        solv(3, 5, 10, 8)
    assert "a - b < 0" in str(e.value)

def test_division_by_zero():
    with pytest.raises(ValueError) as e:
        solv(9, 4, 7, 7)
    assert "c - d = 0" in str(e.value)

def test_float_values():
    res = solv(5.5, 1.5, 4.0, 1.0)
    exp = math.sqrt(4.0) / 3.0
    assert res == exp
