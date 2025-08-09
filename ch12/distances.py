import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/distances", methods=["POST"])
def calculate_distance():
    """Calculate distance between two arrays from a POST request."""
    a, b, dist_type = parse_request_parameters(request)
    dist_func = {"L1": get_manhattan_dist, "L2": get_euclidean_dist}.get(dist_type)
    dist = dist_func(a, b)
    return jsonify({"distance": dist})


def parse_request_parameters(request):
    """Parse arrays and distance type from a Flask request."""
    data = request.get_json()
    a = np.array(data.get("df1",))
    b = np.array(data.get("df2",))
    distance_type = data.get("distance")
    return a, b, distance_type  

def get_manhattan_dist(a: np.ndarray, b: np.ndarray) -> float:
    """Return the Manhattan (L1) distance between two arrays."""
    return np.sum(np.abs(a - b))


def get_euclidean_dist(a: np.ndarray, b: np.ndarray) -> float:
    """Return the squared Euclidean (L2) distance between two arrays."""
    return np.sqrt(np.sum((a - b) ** 2))


def get_euclidean_squared_dist(a: np.ndarray, b: np.ndarray) -> float:
    """Return the squared Euclidean (L2) distance between two arrays."""
    return np.sum((a - b) ** 2)