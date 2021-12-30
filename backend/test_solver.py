
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
    expectedColor = "orange"
    # When:

    # Then:
    if solver.getOtherColor(testPiece, testCube) == expectedColor:
        print("Test getting other color: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test getting other color: " +
              printColors.FAIL + "failed" + printColors.RESET)


print("======================================== TESTING ========================================")
# test_getWhiteEdges()
test_getOtherColor()
print("=========================================================================================")
