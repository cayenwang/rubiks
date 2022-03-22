from flask import Flask, request
from flask_cors import CORS
import json

from .cube import cube
from .solver import *

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def hello_world():
    # go to localhost:5000 to check the flask server is running
    return "<h1>I'm up and running!</h1>"


@app.route("/solve", methods=["POST"])
def solve():
    request_data = request.get_json()
    # receives the cube data in the form of a string
    cubestr = request_data["cube"]
    # builds a cube using that string
    acube = cube()
    acube.buildCube(cubestr)
    # solves the cube
    moves = solveCube(acube)
    # flatten and optimise the solution
    flat = flatten(moves)
    optimised = optimise(flat)
    # returns the solution
    response = {
        "moves": optimised
    }
    return json.dumps(response)


# builds a solved cube for use in the three functions below
aCube = cube()
aCube.buildCube("wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy")


@app.route("/getSquaresOnFace", methods=["POST"])
def getSquaresOnFace():
    requestData = request.get_json()
    # receives the face from which the squares need to be fetched
    face = requestData["face"]
    # gets a list of squares that are on the face
    # doMove() both does the move AND returns the list of squares moved
    squaresOnFace = aCube.doMove(face)
    # convert the list of squares into a dictionary that can be JSON.dumps'ed
    squaresList = []
    for square in squaresOnFace:
        squaresList.append(square.toDict())
    # return the list of squares
    squaresDict = {
        "squaresOnFace": squaresList
    }
    return json.dumps(squaresDict)


@app.route("/getARotationMatrix", methods=["POST"])
def getRotationMatrix():
    requestData = request.get_json()
    # receives the move for which the rotation matrix need to be fetched
    face = requestData["face"]
    # find the all the rotation matrix, axis and angle using moveToRotationMatrix()
    # moveType is a dummy variable
    moveType, rotationMatrix, axis, angle = aCube.moveToRotationMatrix(face)
    # return the found values
    matrixDict = {
        "rotationMatrix": rotationMatrix,
        "axis": axis,
        "angle": angle
    }
    return json.dumps(matrixDict)


@app.route("/getCubeState", methods=["POST"])
def getARotationMatrix():
    requestData = request.get_json()
    # receives the scramble
    scramble = requestData["scramble"]
    # does the scramble on a solved cube
    doSequenceOfMoves(aCube, scramble)
    # decomposes the scrambled cube into its cubeState
    cubeState = aCube.decompose()
    # returns the cubeState
    cubeDict = {
        "cubeState": cubeState
    }
    return json.dumps(cubeDict)
