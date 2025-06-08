from flask import Flask, request, jsonify
import pandas as pd
from src.manhattan import get_manhattan_distance

app = Flask(__name__)


@app.route("/manhattan", methods=["POST"])
def calculate_distance():
    data = request.get_json()
    df1 = pd.DataFrame(data["df1"])
    df2 = pd.DataFrame(data["df2"])
    dist = get_manhattan_distance(df1, df2)
    return jsonify({"distance": dist})


if __name__ == "__main__":
    app.run(debug=True)
