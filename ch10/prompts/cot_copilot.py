import numpy as np
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/distances", methods=["POST"]) 
def calculate_distance(): 
    a, b, dist_type = parse_request_parameters(request) 
    dist_func = {"L1": get_manhattan_dist, "L2": get_euclidean_dist}.get(dist_type) 
    dist = dist_func(a, b) 
    return jsonify({"distance": dist}) 


def parse_request_parameters(request): 
    data = request.get_json() 
    a = np.array(data.get("df1")) 
    b = np.array(data.get("df2")) 
    dist_type = data.get("distance") 
    return a, b, dist_type 
 
 
def get_manhattan_dist(a, b): 
    print("Info: computing L1 distance...") 
    return np.sum(np.abs(a - b)) 
 
 
def get_euclidean_dist(a, b): 
    print("Info: computing L2 distance...") 
    dist_2 = 0 
    for i in range(len(a)): 
        for j in range(len(a[i])): 
            dist_2 += (a[i][j] - b[i][j]) ** 2 
    return np.sqrt(dist_2) 