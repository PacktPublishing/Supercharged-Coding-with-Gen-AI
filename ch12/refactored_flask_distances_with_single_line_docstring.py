"""
This module provides a Flask application for calculating distances between two vectors.
It supports Manhattan (L1) and Euclidean (L2) distance metrics.
"""

import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/distances", methods=["POST"])
def calculate_distance():
    """
    Calculate distance between two vectors.

    Expects a JSON payload with the following structure:
        {
            "df1": [float, float, ...],  # First vector
            "df2": [float, float, ...],  # Second vector
            "distance": "L1" or "L2"    # Distance type (Manhattan or Euclidean)
        }

    Returns:
        dict: JSON response with the calculated distance:
            {
                "distance": float
            }
    """
    a, b, dist_type = parse_request_parameters(request)
    dist_func = {"L1": get_manhattan_dist, "L2": get_euclidean_dist}.get(dist_type)
    dist = dist_func(a, b)
    return jsonify({"distance": dist})

def parse_request_parameters(request):
    """
    Parse and validate the request parameters from the JSON payload.

    Args:
        request (flask.Request): The Flask request object containing the JSON payload.

    Returns:
        tuple: A tuple containing:
            - a (np.ndarray): The first vector.
            - b (np.ndarray): The second vector.
            - dist_type (str): The distance type ("L1" or "L2").
    """
    data = request.get_json()
    a = np.array(data.get("df1",))
    b = np.array(data.get("df2",))
    dist_type = data.get("distance")
    return a, b, dist_type

def get_manhattan_dist(a: np.ndarray, b: np.ndarray) -> float:
    """
    Calculate the Manhattan (L1) distance between two vectors.

    Args:
        a (np.ndarray): The first vector.
        b (np.ndarray): The second vector.

    Returns:
        float: The Manhattan distance between the two vectors.
    """
    return np.sum(np.abs(a - b))

def get_euclidean_dist(a: np.ndarray, b: np.ndarray) -> float:
    """
    Calculate the Euclidean (L2) distance between two vectors.

    Args:
        a (np.ndarray): The first vector.
        b (np.ndarray): The second vector.

    Returns:
        float: The Euclidean distance between the two vectors.
    """
    return np.sum((a - b) ** 2)
