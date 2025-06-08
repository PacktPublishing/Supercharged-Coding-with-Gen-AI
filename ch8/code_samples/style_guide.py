import numpy as np

def get_area(
        radius: float,
        ) -> float:
    area: float = np.pi * radius ** 2
    return area


def get_arithmetic_mean(
        x1: float, 
        x2: float,
        ) -> float:
    arithmetic_mean: float = (x1 + x2) / 2
    return arithmetic_mean
