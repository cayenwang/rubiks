import test_cube

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


def rotateToUF(cube, correctPosition):  # tested
    extraCubeRotations = []
    if correctPosition == [-1, -1, 0]:
        cube.doMove("Y'")
        cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]-1) % 4
        extraCubeRotations.append("Y'")

    if correctPosition == [0, -1, 1]:
        cube.doMove("Y2")
        cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]+2) % 4
        extraCubeRotations.append("Y2")

    if correctPosition == [1, -1, 0]:
        cube.doMove("Y")
        cube.offsetFromOriginal[1] = (cube.offsetFromOriginal[1]+1) % 4
        extraCubeRotations.append("Y")

    return extraCubeRotations


if __name__ == "__main__":
    testCube = test_cube.test_cubeInit()
    print(getWhiteEdges(testCube))
