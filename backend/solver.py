import test_cube
import numpy as np
import cross_solutions
import pprint

# Function that gets the colour on the other side of the piece:


def getOtherColor(piece, cube):  # tested
    for square in cube.squares:
        if square.pos == piece.pos:
            if square.color != piece.color:
                ResultColor = square.color
    return ResultColor

# Procedure that carries out an inputted sequence of moves, in the format of an array, on the cube in memory:


def doSequenceOfMoves(cube, sequence):  # tested
    for move in sequence:
        cube.doMove(move)


# Procedure that returns the cube to its original orientation (White Up, Green front):


def rotateToOriginal(cube):  # tested
    offset = cube.offsetFromOriginal
    for i in range(3):
        while offset[i] != 0:
            if i == 0:
                cube.doMove("X'")
            if i == 1:
                cube.doMove("Y'")
            if i == 2:
                cube.doMove("Z'")
            offset[i] = offset[i]-1


# Function that finds the inverse of a sequence of cube rotations:
# (only cube rotations, not moves)
def getInverse(sequence):
    resultInverse = []
    inverse = {
        "X": "X'",
        "Y": "Y'",
        "Z": "Z'",
        "X'": "X",
        "Y'": "Y",
        "Z'": "Z",
        "X2": "X2",
        "Y2": "Y2",
        "Z2": "Z2"
    }
    for move in reversed(sequence):
        resultInverse.append(inverse[move])
    return resultInverse


'''
=========================================================================================
Subroutines that are only for solving the white cross
=========================================================================================
'''

# Function that gets all white edges:


def getWhiteEdges(cube):  # tested
    ResultWhiteEdges = []
    for square in cube.squares:
        if 0 in square.pos:
            # making sure the found piece is an edge piece not a centre
            if (square.pos != square.rot) and (square.color == "white"):
                ResultWhiteEdges.append(square)
    return ResultWhiteEdges


correctPositionWhiteEdge = {
    "green": [0, -1, -1],
    "red": [1, -1, 0],
    "blue": [0, -1, 1],
    "orange": [-1, -1, 0]
}

# Function that rotates the cube until it has the correct position for the white edge in the UF position:


def rotateToUF(cube, correctPosition, currentPosition, currentRotation):  # tested
    extraCubeRotations = []
    if correctPosition != [0, -1, -1]:
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


# Function that calculates the correct sequence of moves to solve a given white edge piece:
def getWhiteEdgeSolution(currentPosition, currentRotation):  # tested
    current = str(tuple((currentPosition, currentRotation)))
    crossSolution = cross_solutions.crossSolution[current]
    return crossSolution


# Function that solves the white cross:
def solveWhiteCross(cube):  # tested
    whiteCrossSolution = []
    for square in getWhiteEdges(cube):
        currentPosition = square.pos
        currentRotation = square.rot
        oppositeSideColor = getOtherColor(square, cube)
        correctPosition = correctPositionWhiteEdge[oppositeSideColor]
        currentPosition, currentRotation, extraCubeRotations = rotateToUF(
            cube, correctPosition, currentPosition, currentRotation)
        solution = getWhiteEdgeSolution(currentPosition, currentRotation)
        doSequenceOfMoves(cube, solution)
        rotateToOriginal(cube)

        whiteCrossSolution.append(extraCubeRotations)
        whiteCrossSolution.append(solution)
        whiteCrossSolution.append(getInverse(extraCubeRotations))

    return whiteCrossSolution


if __name__ == "__main__":
    testCube = test_cube.test_cubeInit()
    pprint.pprint(testCube.toDict())
    print(solveWhiteCross(testCube))
    pprint.pprint(testCube.toDict())
