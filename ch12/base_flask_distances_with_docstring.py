import numpy as np
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/distances", methods=["POST"])
def calculate_distance():
    """
    Calculates the distance between two matrices using either L1 (Manhattan) or L2 (Euclidean) distance.
    This function expects a JSON payload with the following keys:
        - "distance": A string specifying the type of distance ("L1" or "L2").
        - "df1": The first matrix (as a list of lists or array-like).
        - "df2": The second matrix (as a list of lists or array-like).
    Returns:
        flask.Response: A JSON response containing either:
            - {"distance": <computed_distance>} if successful.
            - {"error": <error_message>} if the input is invalid or matrices have different shapes.
    Raises:
        None. All errors are returned as JSON responses.
    """

    data = request.get_json()
    dist_type = data.get("distance")
    if dist_type == "L1":
        a = data.get("df1")
        b = data.get("df2")
        if np.asarray(a).shape != np.asarray(b).shape:
            return jsonify({"error": "Matrices must have the same shape"})
        dist = np.sum(np.abs(a - b))
        return jsonify({"distance": dist})
    elif dist_type == "L2":
        a = data.get("df1")
        b = data.get("df2")
        if np.asarray(a).shape != np.asarray(b).shape:
            return jsonify({"error": "Matrices must have the same shape"})
        dist = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                dist += (a[i][j] - b[i][j]) ** 2
        dist = np.sqrt(dist)
        return jsonify({"distance": dist})
    else:
        return jsonify({"error": "Invalid distance type"})