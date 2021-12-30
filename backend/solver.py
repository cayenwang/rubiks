import test_cube
import numpy as np

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


'''
# Function that calculates the correct sequence of moves to solve a given white edge piece:
def getWhiteEdgeSolution(currentPosition, currentOrientation):
    resultSolution = []
    correctPosition = [0, -1,-1]
    correctOrientation = [0, -1,0]
    if CurrentPosition = CorrectPosition
       if CurrentOrientation = CorrectOrientation
           ResultSolution.append()
        else

ResultSolution.append(“F”+“U’”+“R”+“U”)

   ...	// other cases of where the white edge piece could be and appending the corresponding sequence of moves to ResultSolution

    return ResultSolution
'''


if __name__ == "__main__":
    testCube = test_cube.test_cubeInit()
    print(getWhiteEdges(testCube))
