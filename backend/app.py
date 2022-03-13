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
    optimised = optimise(flat)
    response = {
        "moves": optimised
    }
    return json.dumps(response)


aCube = cube()
aCube.buildCube("wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy")


@app.route("/getSquaresOnFace", methods=["POST"])
def getSquaresOnFace():
    requestData = request.get_json()
    face = requestData["face"]
    squaresOnFace = aCube.doMove(face)
    squaresList = []
    for square in squaresOnFace:
        squaresList.append(square.toDict())
    squaresDict = {
        "squaresOnFace": squaresList
    }

    return json.dumps(squaresDict)


@app.route("/getRotationMatrix", methods=["POST"])
def getRotationMatrix():
    requestData = request.get_json()
    face = requestData["face"]
    moveType, rotationMatrix, axis, angle = aCube.moveToRotationMatrix(face)
    matrixDict = {
        "rotationMatrix": rotationMatrix,
        "axis": axis,
        "angle": angle
    }
    return json.dumps(matrixDict)
