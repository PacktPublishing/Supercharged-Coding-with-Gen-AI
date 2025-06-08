import numpy as np
import pandas as pd


def get_manhattan_distance(
        df1: pd.DataFrame,
        df2: pd.DataFrame,
) -> np.float64:
    element_wise_dist: pd.DataFrame = (df1 - df2).abs()
    dist: float = element_wise_dist.sum().sum().astype(float)
    return dist


coordinates_a : pd.DataFrame = pd.DataFrame({
        "x": [0, 1, 2],
        "y": [0, 1, 2],
        "z": [0, 1, 2]
})

coordinates_a._constructor_from_mgr(
    coordinates_a._mgr,
    coordinates_a.axes,
)

