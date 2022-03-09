from flask import Flask, request
from flask_cors import CORS
import json

from .cube import cube
from .solver import *

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def hello_world():
    return "<h1>I'm up and running!</h1>"


@app.route("/solve", methods=["POST"])
def solve():
    request_data = request.get_json()
    cubestr = request_data["cube"]
    acube = cube()
    acube.buildCube(cubestr)
    moves = solveCube(acube)
    flat = flatten(moves)
    response = {
        "moves": flat
    }
    return json.dumps(response)


@app.route("/getSquaresOnFace", methods=["POST"])
def getSquaresOnFace():
    requestData = request.get_json()
    face = requestData["face"]
    aCube = cube()
    aCube.buildCube("wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy")
    squaresOnFace = aCube.getSquaresOnFace(face)
    squaresList = []
    for square in squaresOnFace:
        squaresList.append(square.toDict())
    squaresDict = {
        "squaresOnFace": squaresList
    }
    return json.dumps(squaresDict)
