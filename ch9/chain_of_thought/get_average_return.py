from typing import Dict

import numpy as np


def get_average_return(
        net_returns: Dict[str, float],
) -> float:
    gross_returns: np.ndarray = get_gross_returns(net_returns)
    gross_average: float = get_geometric_mean(gross_returns)
    net_average: float = get_net_average(gross_average)
    return net_average


def get_gross_returns(
        net_returns: Dict[str, float],
) -> np.ndarray:
    gross_returns: np.ndarray = np.array(list(net_returns.values())) + 1
    return gross_returns


def get_geometric_mean(
        gross_returns: np.ndarray,
) -> float:
    gross_average: float = np.prod(gross_returns) ** (1 / len(gross_returns))
    return gross_average


def get_net_average(
        gross_average: float,
) -> float:
    net_average: float = gross_average - 1
    return net_average