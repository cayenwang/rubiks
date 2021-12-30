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


def getOtherColor(piece, cube):
    ResultColor = ""
    for square in cube.squares:
        if square.pos == piece.pos:
            if square != piece:
                ResultColor = square.color
    return ResultColor


if __name__ == "__main__":
    testCube = test_cube.test_cubeInit()
    print(getWhiteEdges(testCube))
