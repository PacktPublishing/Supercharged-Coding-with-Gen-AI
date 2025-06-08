from typing import Dict


def get_geometric_mean(
        net_returns: Dict[str, float],
) -> float:
    product: float = 1
    for key in net_returns:
        product *= net_returns[key]
    geometric_mean: float = product ** (1 / len(net_returns))
    return geometric_mean
