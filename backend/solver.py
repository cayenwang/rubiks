
from .cube import *
import numpy as np
from .cross_solutions import *
from .f2l_solutions import *
from .oll_solutions import *
from .pll_solutions import *
import random

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
        "1": "'",
        "'": "",
        "2": "2"
    }
    for move in reversed(sequence):
        inverseMove = move[0]
        if len(move) == 2:
            direction = move[1]
        else:
            direction = 1
        inverseDirection = inverse[str(direction)]
        inverseMove += inverseDirection
        resultInverse.append(inverseMove)

    '''
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
    '''
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

        moveFace, rotationMatrix, a, b = cube.moveToRotationMatrix(move)
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
    aCrossSolution = crossSolution[current]
    return aCrossSolution


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

        moveFace, rotationMatrix, a, b = cube.moveToRotationMatrix(move)
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
    af2lSolution = f2lSolution[current]
    return af2lSolution


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

    return f2lSolution


'''
=========================================================================================
OLL Subroutines
=========================================================================================
'''


# Function to determine what the top layer looks like:
def getTopLayerFormatOLL(cube):  # tested
    # top layer looks like:       xxx
    # where o represents        x ooo x
    # a square on the U         x ooo x
    # face and x represents     x ooo x
    # a square around the         xxx
    # U layer
    topLayer = [[0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0]]

    positionToCoordinate = {
        # (position,rotation): [row,column]
        "([-1, -1, 1], [0, 0, 1])": [0, 0],
        "([0, -1, 1], [0, 0, 1])": [0, 1],
        "([1, -1, 1], [0, 0, 1])": [0, 2],
        "([-1, -1, 1], [-1, 0, 0])": [1, 0],
        "([-1, -1, 1], [0, -1, 0])": [1, 1],
        "([0, -1, 1], [0, -1, 0])": [1, 2],
        "([1, -1, 1], [0, -1, 0])": [1, 3],
        "([1, -1, 1], [1, 0, 0])": [1, 4],
        "([-1, -1, 0], [-1, 0, 0])": [2, 0],
        "([-1, -1, 0], [0, -1, 0])": [2, 1],
        "([0, -1, 0], [0, -1, 0])": [2, 2],
        "([1, -1, 0], [0, -1, 0])": [2, 3],
        "([1, -1, 0], [1, 0, 0])": [2, 4],
        "([-1, -1, -1], [-1, 0, 0])": [3, 0],
        "([-1, -1, -1], [0, -1, 0])": [3, 1],
        "([0, -1, -1], [0, -1, 0])": [3, 2],
        "([1, -1, -1], [0, -1, 0])": [3, 3],
        "([1, -1, -1], [1, 0, 0])": [3, 4],
        "([-1, -1, -1], [0, 0, -1])": [4, 0],
        "([0, -1, -1], [0, 0, -1])": [4, 1],
        "([1, -1, -1], [0, 0, -1])": [4, 2]
    }

    for square in cube.getSquaresOnFace("U"):
        if square.color == "yellow":
            position = square.pos
            rotation = square.rot
            coordinate = positionToCoordinate[str(tuple((position, rotation)))]
            topLayer[coordinate[0]][coordinate[1]] = 1

    return topLayer

# Function to determine the OLL case:


def getOLLSolution(cube):  # tested
    aOLLSolution = []
    topLayer = getTopLayerFormatOLL(cube)
    while str(topLayer) not in topLayerToOLLCase.keys():
        doSequenceOfMoves(cube, ["U"])
        aOLLSolution.append(["U"])
        topLayer = getTopLayerFormatOLL(cube)
    OLLCase = topLayerToOLLCase[str(topLayer)]
    caseSolution = OLLSolution[OLLCase]

    doSequenceOfMoves(cube, caseSolution)
    aOLLSolution.append(caseSolution)

    return aOLLSolution


'''
# Function that solves the OLL:


def solveOLL(cube):  # not doing the moves correctly
    print("before")
    for square in cube.squares:
        if square.pos[1] == -1 and square.rot == [0, -1, 0]:
            pprint.pprint(square.toDict())
    for square in cube.squares:
        if square.pos[1] == -1 and square.rot != [0, -1, 0]:
            pprint.pprint(square.toDict())

    OLLSolution = getOLLSolution(cube)
    for sequence in OLLSolution:
        print('Before')
        for square in cube.squares:
            if square.pos[1] == -1 and square.rot == [0, -1, 0]:
                pprint.pprint(square.toDict())
        doSequenceOfMoves(cube, sequence)
        print(sequence)
        print("after")
        for square in cube.squares:
            if square.pos[1] == -1 and square.rot == [0, -1, 0]:
                pprint.pprint(square.toDict())
    print(OLLSolution)

    print("after")
    for square in cube.squares:
        if square.pos[1] == -1 and square.rot == [0, -1, 0]:
            pprint.pprint(square.toDict())
    for square in cube.squares:
        if square.pos[1] == -1 and square.rot != [0, -1, 0]:
            pprint.pprint(square.toDict())

    return(OLLSolution)
'''

'''
=========================================================================================
PLL Subroutines
=========================================================================================
'''

# Function to get the squares in the PLL band:


def getSquaresInBand(cube):
    resultSquares = []
    for square in cube.squares:
        if square.pos[1] == -1 and square.rot != [0, -1, 0]:
            resultSquares.append(square)
    return resultSquares

# Function to sort the squares in the PLL band to be sequencial:


def sortSquaresInBand(cube):
    bandFormat = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    posAndRotToIndex = {
        # (position,rotation): index
        "([-1, -1, -1], [0, 0, -1])": 0,
        "([0, -1, -1], [0, 0, -1])": 1,
        "([1, -1, -1], [0, 0, -1])": 2,
        "([1, -1, -1], [1, 0, 0])": 3,
        "([1, -1, 0], [1, 0, 0])": 4,
        "([1, -1, 1], [1, 0, 0])": 5,
        "([1, -1, 1], [0, 0, 1])": 6,
        "([0, -1, 1], [0, 0, 1])": 7,
        "([-1, -1, 1], [0, 0, 1])": 8,
        "([-1, -1, 1], [-1, 0, 0])": 9,
        "([-1, -1, 0], [-1, 0, 0])": 10,
        "([-1, -1, -1], [-1, 0, 0])": 11
    }
    colorToNumber = {
        "green": 0,
        "orange": 1,
        "blue": 2,
        "red": 3
    }

    for square in getSquaresInBand(cube):
        position = square.pos
        rotation = square.rot
        index = posAndRotToIndex[str(tuple((position, rotation)))]
        bandFormat[index] = colorToNumber[square.color]
    stringBandFormat = [str(index) for index in bandFormat]
    result = ''.join(stringBandFormat)
    return result

# Function to align the last layer:


def UAlign(cube):
    for square in cube.squares:
        if square.pos == [0, -1, -1] and square.rot == [0, 0, -1]:
            color = square.color
    movesToAlign = {
        "green": [],
        "orange": ["U"],
        "blue": ["U2"],
        "red": ["U'"]
    }

    doSequenceOfMoves(cube, movesToAlign[color])

    return movesToAlign[color]

# Function to determine the PLL case:


def getPLLSolution(cube):  # tested
    PLLSolution = []
    bandFormat = sortSquaresInBand(cube)
    while str(bandFormat) not in topBandToCase.keys():
        # not rotating the top face but seeing whether the current pll case
        # matches the dictionary but just in a different colour scheme
        counter = 0
        while str(bandFormat) not in topBandToCase.keys() and counter != 4:
            bandFormat = str(int(bandFormat)+111111111111).replace("4", "0")
            counter += 1
        # out of the loop, we've determined the current pll case isnt one in the
        # dictionary and hence we need to rotate the top layer and check again
        if str(bandFormat) not in topBandToCase.keys():
            doSequenceOfMoves(cube, ["U"])
            PLLSolution.append(["U"])
            bandFormat = sortSquaresInBand(cube)
    PLLCase = topBandToCase[str(bandFormat)]
    caseSolution = pllSolution[PLLCase]

    doSequenceOfMoves(cube, caseSolution)
    PLLSolution.append(caseSolution)

    movesToAlign = UAlign(cube)
    PLLSolution.append(movesToAlign)

    return PLLSolution


'''
=========================================================================================
Complete Solution
=========================================================================================
'''


def solveCube(cube):
    completeSolution = []
    whiteCrossSolution = solveWhiteCross(cube)
    print("cross done")
    f2lSolution = solveF2L(cube)
    print("f2l done")
    ollSolution = getOLLSolution(cube)
    print("oll done")
    pllSolution = getPLLSolution(cube)
    print("pll done")

    completeSolution.append(whiteCrossSolution)
    completeSolution.append(f2lSolution)
    completeSolution.append(ollSolution)
    completeSolution.append(pllSolution)

    return completeSolution


def flatten(listOfLists):
    if len(listOfLists) == 0:
        return listOfLists
    if isinstance(listOfLists[0], list):
        return flatten(listOfLists[0]) + flatten(listOfLists[1:])
    return listOfLists[:1] + flatten(listOfLists[1:])


def optimise(flatList):
    print(flatList)
    flag = True
    while flag == True:
        flag = False
        for i in range(len(flatList)-1):
            if not (i == len(flatList)-1):
                move1 = flatList[i]
                move2 = flatList[i+1]
                if not (move2 == ''):
                    moveType1 = move1[0]
                    moveType2 = move2[0]
                    if moveType1 == moveType2:
                        combined = moveType1
                        if len(move1) == 1:
                            moveAngle1 = 1
                        elif move1[1] == "'":
                            moveAngle1 = -1
                        elif move1[1] == "2":
                            moveAngle1 = 2
                        if len(move2) == 1:
                            moveAngle2 = 1
                        elif move2[1] == "'":
                            moveAngle2 = -1
                        elif move2[1] == "2":
                            moveAngle2 = 2
                        totalAngle = moveAngle1 + moveAngle2
                        if totalAngle == 0 or totalAngle == 4:
                            combined = ''
                        elif totalAngle == 2 or totalAngle == -2:
                            combined = combined + "2"
                        elif totalAngle == 3:
                            combined = combined + "'"
                        flatList.pop(i)
                        flatList[i] = combined
                        flatList.append('')
                        flag = True
        try:
            while True:
                flatList.remove('')
        except ValueError:
            pass
        print(flatList)
    return flatList


'''
=========================================================================================
Further Testing
=========================================================================================
'''

# Generate solved cube:


def buildSolvedCube():
    testCube = cube.cube()
    testCube.buildCube(
        "wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy")
    return testCube


# Generate a random scramble:
def randomScramble():
    indexToMove = {
        0: "U",
        1: "U'",
        2: "U2",
        3: "D",
        4: "D'",
        5: "D2",
        6: "L",
        7: "L'",
        8: "L2",
        9: "R",
        10: "R'",
        11: "R2",
        12: "B",
        13: "B'",
        14: "B2",
        15: "F",
        16: "F'",
        17: "F2",
    }
    scramble = []
    for i in range(20):
        index = random.randint(0, 17)
        scramble.append(indexToMove[index])
    return scramble

# Check if the final cube is solved:


def isSolved(cube):
    flag = True
    for position in [[0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1]]:
        for centre in cube.squares:
            if centre.pos == position:
                for square in cube.squares:
                    if square.rot == centre.pos:
                        if square.color != centre.color:
                            flag = False

    return flag


if __name__ == "__main__":
    # testCube = test_cube.test_cubeInit()

    testCube = buildSolvedCube()
    scramble = randomScramble()
    # scramble = ['L', 'U', "L'", 'R2', 'R', "L'", 'R2', 'U2', 'D2', "B'", 'R2', "F'", 'F', 'L2', 'U2', 'R', 'F', 'R2', 'D2', 'L']
    # ['L', 'F', 'L2', 'F2', "U'", 'L', "F'", "R'", 'R', "F'", 'L', 'F2', 'B2', "R'", 'B2', 'D2', "B'", 'R', 'F2', 'R']
    print(scramble)
    doSequenceOfMoves(testCube, scramble)
    solution = solveCube(testCube)

    # GETS THE INVERSE SOLUTION: ie goes from solved cube to scrambled state
    flat = flatten(solution)
    optimised = optimise(flat)
    print("flat", flat)

    print("optimised", optimised)
    '''
    print("flat:", flat)
    inverse = getInverse(flat)
    print("inverse:", inverse)
    '''
    print(flat)
    print(isSolved(testCube))
    # pprint.pprint(testCube.toDict())
    #print("SOMETHING IS BROKEN. IDK WHERE. FIND IT LATER :)")
