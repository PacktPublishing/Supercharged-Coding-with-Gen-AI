import numpy as np

def get_area(
        radius: float,
        ) -> float:
    """
    Compute the area of a circle given its radius.
    """
    area: float = np.pi * radius ** 2
    return area


def get_arithmetic_mean(
        x1: float, 
        x2: float,
        ) -> float:
    """
    Compute the arithmetic mean of two numbers.
    """
    arithmetic_mean: float = (x1 + x2) / 2
    return arithmetic_mean


def get_euclidean_distance(
        x1: float, 
        y1: float, 
        x2: float, 
        y2: float,
        ) -> float:
    """
    Compute the Euclidean distance between two points in 2D space.
    """
    distance: float = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
