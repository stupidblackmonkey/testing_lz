import math


def solv(a: float, b: float, c: float, d: float) -> float:

    diff_ab = a - b
    diff_cd = c - d

    if diff_ab < 0:
        raise ValueError("Нельзя извлечь корень: a - b < 0")

    if diff_cd == 0:
        raise ValueError("Деление на ноль: c - d == 0")

    return math.sqrt(diff_ab) / diff_cd


