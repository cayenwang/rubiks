import test_cube

# Function that gets all white edges:


def getWhiteEdges(cube):
    ResultWhiteEdges = []
    for square in cube.squares:
        if 0 in square.pos:
            # making sure the found piece is an edge piece not a centre
            if (square.pos != square.rot) and (square.color == "white"):
                ResultWhiteEdges.append(square)
    return ResultWhiteEdges


if __name__ == "__main__":
    testCube = test_cube.test_cubeInit()
    print(getWhiteEdges(testCube))
