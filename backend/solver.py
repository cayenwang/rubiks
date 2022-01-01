import test_cube
import numpy as np
import cross_solutions

# Function that gets all white edges:


def getWhiteEdges(cube):  # tested
    ResultWhiteEdges = []
    for square in cube.squares:
        if 0 in square.pos:
            # making sure the found piece is an edge piece not a centre
            if (square.pos != square.rot) and (square.color == "white"):
                ResultWhiteEdges.append(square)
    return ResultWhiteEdges

# Function that gets the colour on the other side of the piece:


def getOtherColor(piece, cube):  # tested
    for square in cube.squares:
        if square.pos == piece.pos:
            if square.color != piece.color:
                ResultColor = square.color
    return ResultColor


correctPositionWhiteEdge = {
    "green": [0, -1, -1],
    "red": [1, -1, 0],
    "blue": [0, -1, 1],
    "orange": [-1, -1, 0]
}

# Function that rotates the cube until it has the correct position for the white edge in the UF position:


def rotateToUF(cube, correctPosition, currentPosition, currentRotation):  # tested
    extraCubeRotations = []
    if correctPosition == [-1, -1, 0]:
        move = "Y'"
        cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]-1) % 4
    if correctPosition == [0, -1, 1]:
        move = "Y2"
        cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]+2) % 4

    if correctPosition == [1, -1, 0]:
        move = "Y"
        cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]+1) % 4

    moveFace, rotationMatrix = cube.moveToRotationMatrix(move)
    cube.doMove(move)
    extraCubeRotations.append(move)

    currentPosition = list(np.dot(
        rotationMatrix, currentPosition))
    currentRotation = list(np.dot(
        rotationMatrix, currentRotation))

    return currentPosition, currentRotation, extraCubeRotations


# Function that calculates the correct sequence of moves to solve a given white edge piece: #tested
def getWhiteEdgeSolution(currentPosition, currentRotation):
    current = str(tuple((currentPosition, currentRotation)))
    crossSolution = cross_solutions.crossSolution[current]
    return crossSolution

# Procedure that carries out an inputted sequence of moves, in the format of an array, on the cube in memory:


def doSequenceOfMoves(cube, sequence):
    for move in sequence:
        print("before:", repr(move), cube.toDict()["squares"][0])
        print('----------')
        cube.doMove(move)
        print("after:", repr(move), cube.toDict()["squares"][0])
        print('----------')


if __name__ == "__main__":
    print('Hi')
