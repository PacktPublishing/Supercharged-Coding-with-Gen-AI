def get_eucleadian_distance(
        x1: float, 
        x2: float,
        y1: float,
        y2: float,
        ) -> float:
    distance: float = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance