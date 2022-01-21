
import solver
import pprint
import test_cube


class printColors:
    PASS = "\033[90m"
    FAIL = "\033[95m"
    RESET = "\033[0m"


testCube = test_cube.test_cubeInit()

'''
# Test template
def test_function():
    # Given:
    test___ = ___
    expectedDictionary = {
            ___
        }
    # When:

    # Then:
    if ___ == expectedDictionary:
        print("Test ___: " + printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test ___: " + printColors.FAIL + "failed" + printColors.RESET)
'''

# Test getting white edges


def test_getWhiteEdges():
    # Given:
    resultSquares = solver.getWhiteEdges(testCube)
    resultSquaresDict = {
        'squares': []
    }
    for square in resultSquares:
        resultSquaresDict["squares"].append(square.toDict())

    expectedDictionary = {'squares': [{'color': 'white', 'position': [1, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'white', 'position': [
                                          1, 0, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white',
                                          'position': [-1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'white', 'position': [-1, 1, 0], 'rotation': [0, 1, 0]}]}
    # When:

    # Then:
    if resultSquaresDict == expectedDictionary:
        print("Test getting white edges: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test getting white edges: " +
              printColors.FAIL + "failed" + printColors.RESET)

# Test getting other color


def test_getOtherColor():
    # Given:
    testPiece = test_cube.test_squareInit()
    expectedColor = ["green", "red"]
    # When:
    print(solver.getOtherColor(testPiece, testCube))
    # Then:
    if solver.getOtherColor(testPiece, testCube) == expectedColor:
        print("Test getting other color: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test getting other color: " +
              printColors.FAIL + "failed" + printColors.RESET)

# Test rotate to UF


def test_rotateToUF():
    # Given:
    expectedDictionary = {'squares': [{'color': 'yellow',
                                       'position': [1, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'yellow',
                                       'position': [0, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'blue',
                                       'position': [-1, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'green', 'position': [
                                          1, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'white', 'position': [
                                          0, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'white',
                                       'position': [-1, -1, 0],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                       'position': [1, -1, 1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'green', 'position': [
                                          0, -1, 1], 'rotation': [0, -1, 0]},
                                      {'color': 'red',
                                          'position': [-1, -1, 1], 'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                       'position': [1, -1, -1],
                                       'rotation': [1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          1, -1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'blue', 'position': [
                                          1, -1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          1, 0, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'orange', 'position': [
                                          1, 0, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'yellow', 'position': [
                                          1, 0, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'blue', 'position': [
                                          1, 1, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'blue', 'position': [
                                          1, 1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, 1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'yellow', 'position': [
                                          1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'orange', 'position': [
                                          0, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green',
                                       'position': [-1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'orange', 'position': [
                                          1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green', 'position': [
                                          0, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'white',
                                          'position': [-1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'orange', 'position': [
                                          1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'yellow', 'position': [
                                          0, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green',
                                          'position': [-1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'yellow',
                                       'position': [-1, -1, 1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'orange',
                                       'position': [-1, -1, 0],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'orange',
                                       'position': [-1, -1, -1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'green', 'position': [-1,
                                                                      0, 1], 'rotation': [-1, 0, 0]},
                                      {'color': 'red',
                                          'position': [-1, 0, 0], 'rotation': [-1, 0, 0]},
                                      {'color': 'green',
                                       'position': [-1, 0, -1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'white', 'position': [-1,
                                                                      1, 1], 'rotation': [-1, 0, 0]},
                                      {'color': 'blue',
                                          'position': [-1, 1, 0], 'rotation': [-1, 0, 0]},
                                      {'color': 'white',
                                       'position': [-1, 1, -1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'white',
                                       'position': [-1, -1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [
                                          0, -1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'green',
                                       'position': [1, -1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'yellow',
                                       'position': [-1, 0, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [
                                          0, 0, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white', 'position': [
                                          1, 0, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [-1,
                                       1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [
                                          0, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'red', 'position': [
                                          1, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white', 'position': [
                                          1, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [
                                          0, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'red',
                                          'position': [-1, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'white', 'position': [
                                          1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'yellow', 'position': [
                                          0, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red',
                                          'position': [-1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'yellow', 'position': [
                                          1, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'orange', 'position': [
                                          0, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [-1, 1, -1], 'rotation': [0, 1, 0]}]}
    currentPosition, currentRotation, extraCubeRotations = solver.rotateToUF(
        testCube, [0, -1, 1], [-1, 1, 0], [0, 1, 0])
    # When:

    # Then:
    if testCube.toDict() == expectedDictionary and extraCubeRotations == ["Y2"] and currentPosition == [1, 1, 0] and currentRotation == [0, 1, 0]:
        print("Test rotate to UF: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test rotate to UF: " +
              printColors.FAIL + "failed" + printColors.RESET)

# Test getting the cross solution


def test_getWhiteEdgeSolution():
    # Given:
    testCurrentPosition = [1, 1, 0]
    testCurrentRotation = [0, 1, 0]
    expectedResult = ["D'", "F2"]
    # When:

    # Then:
    if solver.getWhiteEdgeSolution(testCurrentPosition, testCurrentRotation) == expectedResult:
        print("Test getting the cross solution: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test getting the cross solution: " +
              printColors.FAIL + "failed" + printColors.RESET)

# Test doing a sequence of moves:


def test_doSequenceOfMoves():  # tested given rotateToUF had been called first
    # Given:
    testSequence = ["D'", "F2"]
    solver.doSequenceOfMoves(testCube, testSequence)
    expectedDictionary = {'squares': [{'color': 'yellow',
                                       'position': [-1, 1, -1],
                                       'rotation': [0, 1, 0]},
                                      {'color': 'yellow', 'position': [
                                          0, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'blue', 'position': [
                                          1, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'green', 'position': [
                                          1, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'white', 'position': [
                                          0, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'white',
                                       'position': [-1, -1, 0],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                       'position': [1, -1, 1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'green', 'position': [
                                          0, -1, 1], 'rotation': [0, -1, 0]},
                                      {'color': 'red',
                                          'position': [-1, -1, 1], 'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                       'position': [-1, 1, -1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          1, -1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'blue', 'position': [
                                          1, -1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'red',
                                          'position': [-1, 0, -1], 'rotation': [-1, 0, 0]},
                                      {'color': 'orange', 'position': [
                                          1, 0, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'yellow', 'position': [
                                          1, 0, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'blue', 'position': [
                                          1, -1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [
                                          0, -1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'green',
                                       'position': [-1, -1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'yellow', 'position': [
                                          1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'orange', 'position': [
                                          0, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green',
                                          'position': [-1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'orange', 'position': [
                                          1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green', 'position': [
                                          0, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'white',
                                          'position': [-1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'orange',
                                       'position': [-1, -1, -1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'yellow', 'position': [
                                          1, 1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, 1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'yellow',
                                       'position': [-1, -1, 1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'orange',
                                       'position': [-1, -1, 0],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'orange', 'position': [
                                          1, 1, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'green',
                                          'position': [-1, 0, 1], 'rotation': [-1, 0, 0]},
                                      {'color': 'red',
                                          'position': [-1, 0, 0], 'rotation': [-1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, 0, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'white', 'position': [
                                          1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          0, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'white',
                                          'position': [-1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'white', 'position': [
                                          1, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [
                                          0, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'green',
                                       'position': [-1, 1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'yellow',
                                       'position': [1, 0, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [
                                          0, 0, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white',
                                       'position': [-1, 0, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'blue',
                                          'position': [-1, 1, 1], 'rotation': [-1, 0, 0]},
                                      {'color': 'blue',
                                          'position': [-1, 1, 0], 'rotation': [-1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          1, -1, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'white',
                                       'position': [-1, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'red', 'position': [
                                          1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [
                                          1, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'white',
                                       'position': [0, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'yellow', 'position': [
                                          0, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [
                                          0, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'yellow',
                                       'position': [1, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                          'position': [-1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [-1, 1, 1], 'rotation': [0, 1, 0]}]}

    # When:

    # Then:
    if testCube.toDict() == expectedDictionary:
        print("Test doing a sequence of moves: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test doing a sequence of moves: " +
              printColors.FAIL + "failed" + printColors.RESET)

# Test returning to original orientation


def test_rotateToOriginal():  # tested given rotateToUF and doSequenceOfMoves had been called first
    # Given:
    solver.rotateToOriginal(testCube)
    expectedDictionary = {'squares': [{'color': 'yellow', 'position': [1, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'yellow', 'position': [
                                          0, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'blue',
                                          'position': [-1, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'green',
                                       'position': [-1, -1, 0],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'white', 'position': [
                                          0, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'white', 'position': [
                                          1, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                       'position': [-1, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'green',
                                       'position': [0, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'red', 'position': [
                                          1, -1, -1], 'rotation': [0, -1, 0]},
                                      {'color': 'orange', 'position': [
                                          1, 1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'red',
                                          'position': [-1, -1, 0], 'rotation': [-1, 0, 0]},
                                      {'color': 'blue',
                                       'position': [-1, -1, -1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          1, 0, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'orange',
                                       'position': [-1, 0, 0],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'yellow',
                                       'position': [-1, 0, -1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'blue',
                                          'position': [-1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          0, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green', 'position': [
                                          1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'yellow',
                                       'position': [-1, -1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'orange',
                                       'position': [0, -1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'green',
                                       'position': [1, -1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'orange',
                                       'position': [-1, 0, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'green', 'position': [
                                          0, 0, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white', 'position': [
                                          1, 0, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'orange', 'position': [
                                          1, -1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'yellow',
                                       'position': [-1, 1, 0],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'green',
                                       'position': [-1, 1, -1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'yellow',
                                       'position': [1, -1, -1],
                                       'rotation': [1, 0, 0]},
                                      {'color': 'orange', 'position': [
                                          1, -1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'orange',
                                       'position': [-1, 1, 1],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, 0, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          1, 0, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'green',
                                          'position': [-1, 0, 1], 'rotation': [-1, 0, 0]},
                                      {'color': 'white',
                                       'position': [-1, 1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [
                                          0, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white', 'position': [
                                          1, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white',
                                          'position': [-1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          0, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green', 'position': [
                                          1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'yellow',
                                          'position': [-1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          0, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'white', 'position': [
                                          1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          1, 1, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'blue', 'position': [
                                          1, 1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'red',
                                          'position': [-1, -1, 1], 'rotation': [-1, 0, 0]},
                                      {'color': 'white', 'position': [
                                          1, -1, 1], 'rotation': [0, -1, 0]},
                                      {'color': 'red',
                                          'position': [-1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red',
                                          'position': [-1, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'white', 'position': [
                                          0, -1, 1], 'rotation': [0, -1, 0]},
                                      {'color': 'yellow', 'position': [
                                          0, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [
                                          0, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'yellow',
                                       'position': [-1, -1, 1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'orange', 'position': [
                                          1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [1, 1, -1], 'rotation': [0, 1, 0]}]}

    # When:

    # Then:
    if testCube.toDict() == expectedDictionary:
        print("Test returning to original orientation: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test returning to original orientation: " +
              printColors.FAIL + "failed" + printColors.RESET)


# Test solving white cross
def test_solveWhiteCross():
    # Given:
    solver.solveWhiteCross(testCube)
    expectedDictionary = {'squares': [{'color': 'yellow', 'position': [1, 1, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'yellow',
                                       'position': [1, 0, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [
                                          1, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'green',
                                       'position': [-1, 0, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'white', 'position': [
                                          0, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'white',
                                       'position': [-1, -1, 0],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                       'position': [-1, 1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'green', 'position': [
                                          1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [
                                          1, -1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'orange', 'position': [
                                          1, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'red',
                                          'position': [-1, 0, -1], 'rotation': [-1, 0, 0]},
                                      {'color': 'blue',
                                          'position': [-1, 1, -1], 'rotation': [-1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          1, -1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'orange',
                                       'position': [-1, 0, 0],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'yellow',
                                       'position': [-1, 1, 0],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'blue',
                                          'position': [-1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          0, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green',
                                          'position': [-1, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'yellow',
                                       'position': [-1, 1, -1],
                                       'rotation': [0, 1, 0]},
                                      {'color': 'orange', 'position': [
                                          1, 1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'orange',
                                          'position': [-1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'green', 'position': [
                                          0, 0, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white',
                                       'position': [0, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                          'position': [-1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'yellow', 'position': [
                                          0, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green',
                                       'position': [1, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'yellow',
                                       'position': [1, -1, 1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                       'position': [-1, -1, 0],
                                       'rotation': [-1, 0, 0]},
                                      {'color': 'orange', 'position': [
                                          1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green',
                                       'position': [0, -1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'red', 'position': [
                                          1, 0, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, 0, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'white', 'position': [
                                          1, -1, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'blue',
                                          'position': [-1, 0, 1], 'rotation': [-1, 0, 0]},
                                      {'color': 'white',
                                       'position': [-1, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'white', 'position': [
                                          1, 1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'blue', 'position': [
                                          1, 0, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'yellow', 'position': [
                                          1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          0, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'white', 'position': [
                                          1, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'blue',
                                       'position': [-1, -1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'blue', 'position': [
                                          0, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'red',
                                          'position': [-1, -1, 1], 'rotation': [-1, 0, 0]},
                                      {'color': 'white',
                                          'position': [-1, 1, 1], 'rotation': [-1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          0, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [
                                          1, -1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white', 'position': [
                                          0, -1, 1], 'rotation': [0, -1, 0]},
                                      {'color': 'yellow', 'position': [
                                          0, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red',
                                          'position': [-1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'yellow',
                                       'position': [-1, -1, 1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'orange', 'position': [
                                          0, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'red',
                                       'position': [-1, -1, -1],
                                       'rotation': [-1, 0, 0]}]}
    # When:

    # Then:
    if testCube.toDict() == expectedDictionary:
        print("Test solving white cross: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test solving white cross: " +
              printColors.FAIL + "failed" + printColors.RESET)


'''
=========================================================================================
End of White Cross Testing
=========================================================================================
'''

# Test getting the correct position of white corners


def test_getCorrectPositionWhiteCorner():
    # Given:
    testSquare = test_cube.test_squareInit()
    otherColors = solver.getOtherColor(testSquare, testCube)
    expectedResult = [1, -1, 1]
    # When:

    # Then:
    if solver.getCorrectPositionWhiteCorner(otherColors) == expectedResult:
        print("Test getting the correct position of white corners: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test getting the correct position of white corners: " +
              printColors.FAIL + "failed" + printColors.RESET)

# Test getting the F2L edge:


def test_getF2LEdge():
    # Given:
    testSquare = test_cube.test_squareInit()
    otherColors = solver.getOtherColor(testSquare, testCube)
    expectedResult = [1, 1, 0]
    # When:
    print(solver.getF2LEdge(otherColors, testCube))
    # Then:
    if solver.getF2LEdge(otherColors, testCube) == expectedResult:
        print("Test getting the F2L edge: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test getting the F2L edge: " +
              printColors.FAIL + "failed" + printColors.RESET)


print("======================================== TESTING ========================================")
'''
# White Cross Testing

test_getWhiteEdges()
print("---")
test_getOtherColor()
print("---")
test_rotateToUF()
print("---")
test_getWhiteEdgeSolution()
print("---")
test_doSequenceOfMoves()
print("---")
test_rotateToOriginal()
print("---")
test_solveWhiteCross()
print("---")
'''
test_getCorrectPositionWhiteCorner()
print("---")
test_getF2LEdge()
print("=========================================================================================")
