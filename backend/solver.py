import test_cube
import numpy as np
import cross_solutions
import f2l_solutions
import pprint

'''
=========================================================================================
Communal Subroutines 
=========================================================================================
'''

# Function that gets the colour on the other side of the piece:


def getOtherColor(piece, cube):  # tested
    resultColor = []
    for square in cube.squares:
        if square.pos == piece.pos:
            if square.color != piece.color:
                resultColor.append(square.color)
    return resultColor

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
White Cross Subroutines
=========================================================================================
'''

# Function that gets all white edges:


def getWhiteEdges(cube):  # tested
    resultWhiteEdges = []
    for square in cube.squares:
        if 0 in square.pos:
            # making sure the found piece is an edge piece not a centre
            if (square.pos != square.rot) and (square.color == "white"):
                resultWhiteEdges.append(square)
    return resultWhiteEdges


correctPositionWhiteEdge = {
    "green": [0, -1, -1],
    "red": [1, -1, 0],
    "blue": [0, -1, 1],
    "orange": [-1, -1, 0]
}

# Function that rotates the cube until the correct position for the white edge in the UF position:


def rotateWhiteEdgeToUF(cube, correctPosition, currentPosition, currentRotation):  # tested
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
        oppositeSideColor = getOtherColor(square, cube)[0]
        correctPosition = correctPositionWhiteEdge[oppositeSideColor]
        currentPosition, currentRotation, extraCubeRotations = rotateWhiteEdgeToUF(
            cube, correctPosition, currentPosition, currentRotation)
        solution = getWhiteEdgeSolution(currentPosition, currentRotation)
        doSequenceOfMoves(cube, solution)
        rotateToOriginal(cube)

        whiteCrossSolution.append(extraCubeRotations)
        whiteCrossSolution.append(solution)
        whiteCrossSolution.append(getInverse(extraCubeRotations))

    print(whiteCrossSolution)

    return whiteCrossSolution


'''
=========================================================================================
F2L Subroutines
=========================================================================================
'''

# Function that gets all white corners:


def getWhiteCorners(cube):
    resultWhiteCorners = []
    for square in cube.squares:
        if 0 not in square.pos:
            if square.color == "white":
                resultWhiteCorners.append(square)
    return resultWhiteCorners


# Function that gets all white corners:

def getCorrectPositionWhiteCorner(otherColors):  # tested
    if "green" in otherColors:
        z = -1
    if "blue" in otherColors:
        z = 1
    if "orange" in otherColors:
        x = 1
    if "red" in otherColors:
        x = -1
    correctPosition = [x, 1, z]
    return correctPosition


# Function that rotates the cube until the correct position for the white corner in the DFR position:


def rotateCorrectPositionToDFR(cube, correctPosition, currentCornerPosition, currentCornerRotation):  # tested
    extraCubeRotations = []
    if correctPosition != [1, 1, -1]:
        if correctPosition == [1, 1, 1]:
            move = "Y"
            cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]+1) % 4
        if correctPosition == [-1, 1, 1]:
            move = "Y2"
            cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]+2) % 4
        if correctPosition == [-1, 1, -1]:
            move = "Y'"
            cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]-1) % 4

        moveFace, rotationMatrix = cube.moveToRotationMatrix(move)
        cube.doMove(move)
        extraCubeRotations.append(move)

        currentCornerPosition = list(np.dot(
            rotationMatrix, currentCornerPosition))
        currentCornerRotation = list(np.dot(
            rotationMatrix, currentCornerRotation))

    return currentCornerPosition, currentCornerRotation, extraCubeRotations


# Function that rotates the top layer until the position of the white corner in the UFR position:


def rotateWhiteCornerToUFR(cube, currentCornerPosition):  # tested
    moveCornerToU = {
        # position: [sequence of moves, new position]
        "[1, 1, -1]": [["R", "U", "R'"], [-1, -1, -1]],
        "[1, 1, 1]": [["R'", "U'", "R"], [-1, -1, 1]],
        "[-1, 1, 1]": [["L", "U", "L'"], [1, -1, 1]],
        "[-1, 1, -1]": [["L'", "U'", "L"], [1, -1, -1]]
    }

    moveCornerToUFR = {
        # position: sequence of moves
        "[1, -1, -1]": [],
        "[1, -1, 1]": ["U"],
        "[-1, -1, 1]": ["U2"],
        "[-1, -1, -1]": ["U'"]
    }
    solution = []
    if currentCornerPosition[1] == 1:
        solution.append(moveCornerToU[str(currentCornerPosition)][0])
        doSequenceOfMoves(cube, moveCornerToU[str(currentCornerPosition)][0])
        currentCornerPosition = moveCornerToU[str(currentCornerPosition)][1]

    solution.append(moveCornerToUFR[str(currentCornerPosition)])
    doSequenceOfMoves(cube, moveCornerToUFR[str(currentCornerPosition)])

    return solution


# Function that finds the F2L edge piece:

def getF2LEdge(otherColors, cube):  # tested
    color1 = otherColors[0]
    color2 = otherColors[1]
    for square1 in cube.squares:
        if 0 in square1.pos:
            if square1.color == color1 or square1.color == color2:
                tempPosition = square1.pos
                for square2 in cube.squares:
                    if 0 in square2.pos:
                        if square2.pos == tempPosition and square2 != square1:
                            if square2.color == color1 or square2.color == color2:
                                edgePosition = tempPosition
    return edgePosition


# Function that moves the F2L edge to U:

def rotateF2LEdgeToU(otherColors, cube):

    moveEdgeToU = {
        # position: [sequence of moves, new position]
        "[-1, 0, -1]": [["L'", "U'", "L", "U"], [-1, -1, 0]],
        "[1, 0, -1]": [["U", "R", "U", "R'", "U2"], [0, -1, 1]],
        "[-1, 0, 1]": [["L", "U'", "L'", "U"], [-1, -1, 0]],
        "[1, 0, 1]": [["U", "R'", "U", "R", "U2"], [0, -1, 1]]
    }

    edgePosition = getF2LEdge(otherColors, cube)
    solution = []
    if edgePosition[1] == 0:
        solution.append(moveEdgeToU[str(edgePosition)][0])
        doSequenceOfMoves(cube, moveEdgeToU[str(edgePosition)][0])
        edgePosition = moveEdgeToU[str(edgePosition)][1]

    return solution, edgePosition

# Function that calculates the correct sequence of moves to solve a given F2L pair:


def getF2LSolution(edgePosition, correctPosition, cube):
    getFrontColor = {
        # correctPosition: front color
        "[1, 1, 1]": "orange",
        "[1, 1, -1]": "green",
        "[-1, 1, 1]": "blue",
        "[-1, 1, -1]": "red"
    }

    frontColor = getFrontColor[str(correctPosition)]

    for square in cube.squares:
        if square.pos == edgePosition:
            if square.color == frontColor:
                edgeRotation = square.rot

    for square in cube.squares:
        if square.pos == [1, -1, -1]:
            if square.color == "white":
                cornerRotation = square.rot

    current = str(tuple((cornerRotation, edgePosition, edgeRotation)))
    f2lSolution = f2l_solutions.f2lSolution[current]
    return f2lSolution


# Function that solves the first 2 layers:
def solveF2L(cube):  # tested
    doSequenceOfMoves(cube, ["Z2"])
    f2lSolution = [["Z2"]]
    for square in getWhiteCorners(cube):
        currentCornerPosition = square.pos
        currentCornerRotation = square.rot
        oppositeSideColors = getOtherColor(square, cube)
        correctPosition = getCorrectPositionWhiteCorner(oppositeSideColors)
        currentCornerPosition, currentCornerRotation, extraCubeRotations = rotateCorrectPositionToDFR(
            cube, correctPosition, currentCornerPosition, currentCornerRotation)
        solutionCornerToUFR = rotateWhiteCornerToUFR(
            cube, currentCornerPosition)
        solutionEdgeToU, edgePosition = rotateF2LEdgeToU(
            oppositeSideColors, cube)
        solution = getF2LSolution(edgePosition, correctPosition, cube)
        doSequenceOfMoves(cube, solution)
        rotateToOriginal(cube)

        f2lSolution.append(extraCubeRotations)
        f2lSolution.append(solutionCornerToUFR)
        f2lSolution.append(solutionEdgeToU)
        f2lSolution.append(solution)
        f2lSolution.append(getInverse(extraCubeRotations))

    print(f2lSolution)

    return f2lSolution


if __name__ == "__main__":
    testCube = test_cube.test_cubeInit()
    pprint.pprint(testCube.toDict())
    print(solveWhiteCross(testCube))
    pprint.pprint(testCube.toDict())
