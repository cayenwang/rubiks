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


@app.route("/solve", methods=["POST"])
def solve():
    request_data = request.get_json()
    cubestr = request_data["cube"]
    acube = cube()
    acube.buildCube(cubestr)
    moves = solveCube(acube)
    flat = flatten(moves)
    response = {
        "moves": moves
    }
    return json.dumps(response)


@app.route("/jsonExample", methods=["POST"])
def json_example():
    # I hope the request data comes in in the form
    # {
    #   "language": "python"
    # }
    # As with a GET fetch the relevant data!
    # It is common practice to first parse the request data
    # Read in the string format - convert it to your Python representation i.e. classes
    # This could be a two step process i.e. JSON string -> JSON Object -> Class (through constructor)
    request_data = request.get_json()
    language = request_data["language"]
    # Then you would make requests to your own code and gather that data necessary
    # I.e. get relevant state

    # Then you would process all the gathered data
    # This could be something like -> solve_this_cube(arbitrary_cube)
    # move_sequences = solve_this_cube(arbitrary_cube)

    # Compose the JSON response in a JSON Object
    # Translate your classes back to JSON
    # I.e. change your move_sequences to a JSON object/Python Dictionary
    status = "success" if (language == "python") else "failure"
    json_response = {"status": status}

    # Return the JSON string of your request
    return json.dumps(json_response)
