import numpy as np
import random

from .cube import *
from .cross_solutions import *
from .f2l_solutions import *
from .oll_solutions import *
from .pll_solutions import *

'''
=========================================================================================
Communal Subroutines
=========================================================================================
'''

# Function that gets the colour on the other side of the piece:
def getOtherColor(piece, cube):  # tested
    resultColor = []
    # looks through all squares and finds the square with the same position
    for square in cube.squares:
        if square.pos == piece.pos:
            # and makes sure the colour is not the same (ie the found square isnt the same square)
            if square.color != piece.color:
                resultColor.append(square.color)
    return resultColor


# Procedure that carries out an inputted sequence of moves,
# in the format of an array, on the cube in memory:
def doSequenceOfMoves(cube, sequence):  # tested
    for move in sequence:
        cube.doMove(move)


# Procedure that returns the cube to its original orientation (White Up, Green front):
def rotateToOriginal(cube):  # tested
    # offset is in the format [x,y,z]
    offset = cube.offsetFromOriginal
    for i in range(3):
        # for each index of offset, if it is not 0, do cube rotation and decrement the
        # offset. repeat until the offset is 0
        while offset[i] != 0:
            if i == 0:
                cube.doMove("X'")
            if i == 1:
                cube.doMove("Y'")
            if i == 2:
                cube.doMove("Z'")
            offset[i] = offset[i]-1


# Function that finds the inverse of a sequence of cube rotations:
def getInverse(sequence):
    resultInverse = []
    # define the inverse of the angle
    inverse = {
        "1": "'",
        "'": "",
        "2": "2"
    }
    # for each move
    for move in reversed(sequence):
        # the keep the the first letter of the move as that will be the same
        inverseMove = move[0]
        # calculate what the angle of the move is
        if len(move) == 2:
            direction = move[1]
        else:
            direction = 1
        # find the inverse of that angle using the above dicitonary
        inverseDirection = inverse[str(direction)]
        inverseMove += inverseDirection
        resultInverse.append(inverseMove)

    return resultInverse


'''
=========================================================================================
White Cross Subroutines
=========================================================================================
'''

# Function that gets all white edges:
def getWhiteEdges(cube):  # tested
    resultWhiteEdges = []
    # loop through all squares
    for square in cube.squares:
        # only squares with a 0 in the position can be an edge
        # corner pieces have only 1s and -1s
        if 0 in square.pos:
            # making sure the found piece is an edge piece not a centre
            if (square.pos != square.rot) and (square.color == "white"):
                resultWhiteEdges.append(square)
    return resultWhiteEdges

# if the other colour of the white edge is the key, this returns where the correct position is
correctPositionWhiteEdge = {
    "green": [0, -1, -1],
    "red": [1, -1, 0],
    "blue": [0, -1, 1],
    "orange": [-1, -1, 0]
}

# Function that rotates the cube until the correct position for the white edge in the UF position:
def rotateWhiteEdgeToUF(cube, correctPosition, currentPosition, currentRotation):  # tested
    extraCubeRotations = []
    # if the correct position isnt already UF
    if correctPosition != [0, -1, -1]:
        # do Y/Y'/Y2 until the correct position is in UF
        # and change the offsetFromOriginal accordingly to reflect this cube rotation
        if correctPosition == [-1, -1, 0]:
            move = "Y'"
            cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]-1) % 4
        if correctPosition == [0, -1, 1]:
            move = "Y2"
            cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]+2) % 4
        if correctPosition == [1, -1, 0]:
            move = "Y"
            cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]+1) % 4

        # get the rotation matrix for that move
        moveFace, rotationMatrix, a, b = cube.moveToRotationMatrix(move)
        # do the move
        cube.doMove(move)
        extraCubeRotations.append(move)
        # apply the rotation matrix to these tracking variables so they follow the cube rotation
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
        # find other side colour
        oppositeSideColor = getOtherColor(square, cube)[0]
        # determine the correct position for the piece
        correctPosition = correctPositionWhiteEdge[oppositeSideColor]
        # rotate the cube until the correct position is in UF
        currentPosition, currentRotation, extraCubeRotations = rotateWhiteEdgeToUF(
            cube, correctPosition, currentPosition, currentRotation)
        # find the solution
        solution = getWhiteEdgeSolution(currentPosition, currentRotation)
        doSequenceOfMoves(cube, solution)
        rotateToOriginal(cube)

        # append everything to the solution
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
        # check that the square is a corner (corners only have 1s and -1s in) their position
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
def rotateCorrectPositionToDFR(cube, correctPosition, currentCornerPosition, currentCornerRotation):
    # similar to rotateToUF (read comments from above)
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
    # if the corner is in the bottom layer, these are the moves to get it to U layer
    moveCornerToU = {
        # position: [sequence of moves, new position]
        "[1, 1, -1]": [["R", "U", "R'"], [-1, -1, -1]],
        "[1, 1, 1]": [["R'", "U'", "R"], [-1, -1, 1]],
        "[-1, 1, 1]": [["L", "U", "L'"], [1, -1, 1]],
        "[-1, 1, -1]": [["L'", "U'", "L"], [1, -1, -1]]
    }
    # once the corner is in the top layer, these moves will move it to UFR
    moveCornerToUFR = {
        # position: sequence of moves
        "[1, -1, -1]": [],
        "[1, -1, 1]": ["U"],
        "[-1, -1, 1]": ["U2"],
        "[-1, -1, -1]": ["U'"]
    }
    solution = []
    # if it is not in the top layer
    if currentCornerPosition[1] == 1:
        # move to top layer
        solution.append(moveCornerToU[str(currentCornerPosition)][0])
        doSequenceOfMoves(cube, moveCornerToU[str(currentCornerPosition)][0])
        currentCornerPosition = moveCornerToU[str(currentCornerPosition)][1]
    # move to UFR
    solution.append(moveCornerToUFR[str(currentCornerPosition)])
    doSequenceOfMoves(cube, moveCornerToUFR[str(currentCornerPosition)])

    return solution


# Function that finds the F2L edge piece:
def getF2LEdge(otherColors, cube):  # tested
    color1 = otherColors[0]
    color2 = otherColors[1]
    for square1 in cube.squares:
        # looping through all edges
        if 0 in square1.pos:
            # if the square's colour is one of color1 or color2
            if square1.color == color1 or square1.color == color2:
                # store it temporarily
                tempPosition = square1.pos
                for square2 in cube.squares:
                    # loop through all edges again
                    if 0 in square2.pos:
                        # if square2 is in the same position and isn't the same 
                        # square as square 1
                        if square2.pos == tempPosition and square2 != square1:
                            # if it is the other colour of color1 and color2
                            if square2.color == color1 or square2.color == color2:
                                # we have found the edge piece
                                edgePosition = tempPosition
    return edgePosition


# Function that moves the F2L edge to U:
def rotateF2LEdgeToU(otherColors, cube):
    # if the edge isnt in U, these are the moves to get it there
    moveEdgeToU = {
        # position: [sequence of moves, new position]
        "[-1, 0, -1]": [["L'", "U'", "L", "U"], [-1, -1, 0]],
        "[1, 0, -1]": [["U", "R", "U", "R'", "U2"], [0, -1, 1]],
        "[-1, 0, 1]": [["L", "U'", "L'", "U"], [-1, -1, 0]],
        "[1, 0, 1]": [["U", "R'", "U", "R", "U2"], [0, -1, 1]]
    }
    # find the edge
    edgePosition = getF2LEdge(otherColors, cube)
    solution = []
    # if it isnt in U
    if edgePosition[1] == 0:
        # move it to U
        solution.append(moveEdgeToU[str(edgePosition)][0])
        doSequenceOfMoves(cube, moveEdgeToU[str(edgePosition)][0])
        edgePosition = moveEdgeToU[str(edgePosition)][1]

    return solution, edgePosition

# Function that calculates the correct sequence of moves to solve a given F2L pair:
def getF2LSolution(edgePosition, correctPosition, cube):
    # the colour with priority is the front colour
    getFrontColor = {
        # correctPosition: front color
        "[1, 1, 1]": "orange",
        "[1, 1, -1]": "green",
        "[-1, 1, 1]": "blue",
        "[-1, 1, -1]": "red"
    }
    # determine what the front colour is
    frontColor = getFrontColor[str(correctPosition)]
    # find the square that is part of the f2l edge piece and is the front colour
    for square in cube.squares:
        if square.pos == edgePosition:
            if square.color == frontColor:
                # that square's rotation defines the rotation of the piece
                edgeRotation = square.rot
    # find the white corner
    for square in cube.squares:
        if square.pos == [1, -1, -1]:
            if square.color == "white":
                # that square's rotation defines the rotation of the piece
                cornerRotation = square.rot
    # send these three pieces of information to the f2l solution dictionary
    current = str(tuple((cornerRotation, edgePosition, edgeRotation)))
    af2lSolution = f2lSolution[current]
    return af2lSolution


# Function that solves the first 2 layers:
def solveF2L(cube):  # tested
    # first do a Z2 to get yellow on top 
    doSequenceOfMoves(cube, ["Z2"])
    f2lSolution = [["Z2"]]
    # for each white corner
    for square in getWhiteCorners(cube):
        currentCornerPosition = square.pos
        currentCornerRotation = square.rot
        # find the other colours
        oppositeSideColors = getOtherColor(square, cube)
        # find the correct position for the corner
        correctPosition = getCorrectPositionWhiteCorner(oppositeSideColors)
        # rotate the cube until the correct position is in DFR
        currentCornerPosition, currentCornerRotation, extraCubeRotations = rotateCorrectPositionToDFR(
            cube, correctPosition, currentCornerPosition, currentCornerRotation)
        # get the white corner to UFR
        solutionCornerToUFR = rotateWhiteCornerToUFR(
            cube, currentCornerPosition)
        # get the edge to U
        solutionEdgeToU, edgePosition = rotateF2LEdgeToU(
            oppositeSideColors, cube)
        # find the solution
        solution = getF2LSolution(edgePosition, correctPosition, cube)
        doSequenceOfMoves(cube, solution)
        rotateToOriginal(cube)
        # append everything to the solution
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

    # dictionary that converts the position and rotation of the square
    # to its index in topLayer
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
    # for every square on the top face
    for square in cube.getSquaresOnFace("U"):
        # if it is yellow
        if square.color == "yellow":
            position = square.pos
            rotation = square.rot
            # find it's coordinate in topLayer
            coordinate = positionToCoordinate[str(tuple((position, rotation)))]
            # set that value to be 1
            topLayer[coordinate[0]][coordinate[1]] = 1

    return topLayer

# Function to determine the OLL case:
def getOLLSolution(cube):  # tested
    aOLLSolution = []
    # get the top layer format
    topLayer = getTopLayerFormatOLL(cube)
    # if the top Layer is not in the dictionary
    while str(topLayer) not in topLayerToOLLCase.keys():
        # do a U move
        doSequenceOfMoves(cube, ["U"])
        aOLLSolution.append(["U"])
        topLayer = getTopLayerFormatOLL(cube)
    # repeat that loop until the key is found
    # find the oll case using the dictionary
    OLLCase = topLayerToOLLCase[str(topLayer)]
    # find the solution using the dictionary
    caseSolution = OLLSolution[OLLCase]

    # do the solution
    doSequenceOfMoves(cube, caseSolution)
    aOLLSolution.append(caseSolution)

    return aOLLSolution


'''
=========================================================================================
PLL Subroutines
=========================================================================================
'''

# Function to get the squares in the PLL band:
def getSquaresInBand(cube):
    resultSquares = []
    for square in cube.squares:
        # if the square is in the top layer and isnt on the U face
        if square.pos[1] == -1 and square.rot != [0, -1, 0]:
            resultSquares.append(square)
    return resultSquares

# Function to sort the squares in the PLL band to be sequencial:
def sortSquaresInBand(cube):
    bandFormat = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    # converts position and rotation of a square to its index in bandFormat
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
    # create the band format
    for square in getSquaresInBand(cube):
        position = square.pos
        rotation = square.rot
        # find the index of the square in bandFormat
        index = posAndRotToIndex[str(tuple((position, rotation)))]
        # set that value to be its encoded colour
        bandFormat[index] = colorToNumber[square.color]
    # convert the number colour code into a string (eg 0 -> "0")
    stringBandFormat = [str(index) for index in bandFormat]
    # join the band format into one string
    result = ''.join(stringBandFormat)
    return result

# Function to align the last layer:
def UAlign(cube):
    for square in cube.squares:
        # find the colour of the square in UF facing F
        if square.pos == [0, -1, -1] and square.rot == [0, 0, -1]:
            color = square.color
    # the AUF is as below depending on the colour found above
    movesToAlign = {
        "green": [],
        "orange": ["U'"],
        "blue": ["U2"],
        "red": ["U"]
    }

    doSequenceOfMoves(cube, movesToAlign[color])

    return movesToAlign[color]

# Function to determine the PLL case:
def getPLLSolution(cube):  # tested
    PLLSolution = []
    # get the band Format
    bandFormat = sortSquaresInBand(cube)
    # if the bandformat is not a key
    while str(bandFormat) not in topBandToCase.keys():
        # check seeing whether the current pll case matches
        # the dictionary but just in a different colour scheme
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
    # use dictionaries to find the PLL case and solution
    PLLCase = topBandToCase[str(bandFormat)]
    caseSolution = pllSolution[PLLCase]
    # do the solution
    doSequenceOfMoves(cube, caseSolution)
    PLLSolution.append(caseSolution)
    # fix AUF
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
    f2lSolution = solveF2L(cube)
    ollSolution = getOLLSolution(cube)
    pllSolution = getPLLSolution(cube)

    completeSolution.append(whiteCrossSolution)
    completeSolution.append(f2lSolution)
    completeSolution.append(ollSolution)
    completeSolution.append(pllSolution)

    return completeSolution

# flatten the solution (list of lists) into one flat list
def flatten(listOfLists):
    if len(listOfLists) == 0:
        return listOfLists
    if isinstance(listOfLists[0], list):
        return flatten(listOfLists[0]) + flatten(listOfLists[1:])
    return listOfLists[:1] + flatten(listOfLists[1:])

# replace redundant moves (eg Y + Y')
def optimise(flatList):
    flag = True
    # flag is true if a replacement has been made
    # keep looping until no replacements are made
    while flag == True:
        flag = False
        for i in range(len(flatList)-1):
            if not (i == len(flatList)-1):
                # get two adjacent moves
                move1 = flatList[i]
                move2 = flatList[i+1]
                # if the second move exists and isnt a blank space
                if not (move2 == ''):
                    # find the move type of the two moves
                    moveType1 = move1[0]
                    moveType2 = move2[0]
                    # if theyre the same
                    if moveType1 == moveType2:
                        # combine the moves by calculating their total angle
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
                        # replace the two moves with the combined move
                        flatList.pop(i)
                        flatList[i] = combined
                        # add a blank to the end to keep the list length consistent
                        flatList.append('')
                        # and set the flag to be true as a swap has been made
                        flag = True
        # remove all blank spaces
        try:
            while True:
                flatList.remove('')
        except ValueError:
            pass
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
    # find 20 random moves
    for i in range(20):
        index = random.randint(0, 17)
        scramble.append(indexToMove[index])
    return scramble

# Check if the final cube is solved:
def isSolved(cube):
    flag = True
    # for each centre position
    for position in [[0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1]]:
        for centre in cube.squares:
            if centre.pos == position:
                # loop through all squares
                for square in cube.squares:
                    # if the square's rotation = the centre's position 
                    # (ie if the square is on the face)
                    if square.rot == centre.pos:
                        # if the square isnt the same colour as the centre, 
                        # the cube isnt solved
                        if square.color != centre.color:
                            flag = False

    return flag
