from flask import Flask, request, jsonify
import numpy as np


app = Flask(__name__)


@app.route("/distances", methods=["POST"])
def calculate_distance():
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