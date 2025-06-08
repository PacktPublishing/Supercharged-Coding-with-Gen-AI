import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/distances", methods=["POST"])
def calculate_distance():
    data = request.get_json()
    dist_type = data.get("distance")
    if dist_type == "L1":
        print("Info: computing L1 distance...")
        a = data.get("df1")
        b = data.get("df2")
        dist = np.sum(np.abs(a - b))
        return jsonify({"distance": dist})
    elif dist_type == "L2":
        print("Info: computing L2 distance...")
        a = data.get("df1")
        b = data.get("df2")
        dist_2 = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                dist_2 += (a[i][j] - b[i][j]) ** 2
        dist = dist_2 ** 0.5
        return jsonify({"distance": dist})


if __name__ == "__main__":
    app.run(debug=True)
