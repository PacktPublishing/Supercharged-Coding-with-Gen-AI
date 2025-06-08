import pandas as pd

coordinates_a : pd.DataFrame = pd.DataFrame({
        "x": [0, 1, 2],
        "y": [0, 1, 2],
        "z": [0, 1, 2]
})

coordinates_a._constructor_from_mgr(
    coordinates_a._mgr,
    coordinates_a.axes,
)


