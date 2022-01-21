import cube
import pprint


class printColors:
    PASS = "\033[90m"
    FAIL = "\033[95m"
    RESET = "\033[0m"


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

# Test square initialisation


def test_squareInit():
    # Given:
    testSquare = cube.square([1, 1, 1], [1, 0, 0], "white")
    expectedDictionary = {
        "position": [1, 1, 1],
        "rotation": [1, 0, 0],
        "color": "white"
    }
    # When:

    # Then:
    if testSquare.toDict() == expectedDictionary:
        print("Test square initialisation: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test square initialisation: " +
              printColors.FAIL + "failed" + printColors.RESET)

    return testSquare


# Test cube initialisation
def test_cubeInit():
    # Given:
    testCube = cube.cube()
    testCube.buildCube(
        "yybgwwogrorbroybbgyogogwoygyoogrgwbwwbgybwbbrwrrwyryor")
    expectedDictionary = {
        'squares': [{'position': [-1, -1, 1], 'rotation': [0, -1, 0], 'color': 'yellow'},
                    {'position': [0, -1, 1],
                        'rotation': [0, -1, 0], 'color': 'yellow'},
                    {'position': [1, -1, 1],
                        'rotation': [0, -1, 0], 'color': 'blue'},
                    {'position': [-1, -1, 0],
                        'rotation': [0, -1, 0], 'color': 'green'},
                    {'position': [0, -1, 0],
                        'rotation': [0, -1, 0], 'color': 'white'},
                    {'position': [1, -1, 0],
                        'rotation': [0, -1, 0], 'color': 'white'},
                    {'position': [-1, -1, -1],
                        'rotation': [0, -1, 0], 'color': 'orange'},
                    {'position': [0, -1, -1],
                        'rotation': [0, -1, 0], 'color': 'green'},
                    {'position': [1, -1, -1],
                        'rotation': [0, -1, 0], 'color': 'red'},
                    {'position': [-1, -1, 1],
                        'rotation': [-1, 0, 0], 'color': 'orange'},
                    {'position': [-1, -1, 0],
                        'rotation': [-1, 0, 0], 'color': 'red'},
                    {'position': [-1, -1, -1],
                        'rotation': [-1, 0, 0], 'color': 'blue'},
                    {'position': [-1, 0, 1],
                        'rotation': [-1, 0, 0], 'color': 'red'},
                    {'position': [-1, 0, 0],
                        'rotation': [-1, 0, 0], 'color': 'orange'},
                    {'position': [-1, 0, -1],
                        'rotation': [-1, 0, 0], 'color': 'yellow'},
                    {'position': [-1, 1, 1],
                        'rotation': [-1, 0, 0], 'color': 'blue'},
                    {'position': [-1, 1, 0],
                        'rotation': [-1, 0, 0], 'color': 'blue'},
                    {'position': [-1, 1, -1],
                        'rotation': [-1, 0, 0], 'color': 'green'},
                    {'position': [-1, -1, -1],
                        'rotation': [0, 0, -1], 'color': 'yellow'},
                    {'position': [0, -1, -1],
                        'rotation': [0, 0, -1], 'color': 'orange'},
                    {'position': [1, -1, -1],
                        'rotation': [0, 0, -1], 'color': 'green'},
                    {'position': [-1, 0, -1],
                        'rotation': [0, 0, -1], 'color': 'orange'},
                    {'position': [0, 0, -1],
                        'rotation': [0, 0, -1], 'color': 'green'},
                    {'position': [1, 0, -1],
                        'rotation': [0, 0, -1], 'color': 'white'},
                    {'position': [-1, 1, -1],
                        'rotation': [0, 0, -1], 'color': 'orange'},
                    {'position': [0, 1, -1],
                        'rotation': [0, 0, -1], 'color': 'yellow'},
                    {'position': [1, 1, -1],
                        'rotation': [0, 0, -1], 'color': 'green'},
                    {'position': [1, -1, -1],
                        'rotation': [1, 0, 0], 'color': 'yellow'},
                    {'position': [1, -1, 0],
                        'rotation': [1, 0, 0], 'color': 'orange'},
                    {'position': [1, -1, 1],
                        'rotation': [1, 0, 0], 'color': 'orange'},
                    {'position': [1, 0, -1],
                        'rotation': [1, 0, 0], 'color': 'green'},
                    {'position': [1, 0, 0], 'rotation': [
                        1, 0, 0], 'color': 'red'},
                    {'position': [1, 0, 1], 'rotation': [
                        1, 0, 0], 'color': 'green'},
                    {'position': [1, 1, -1],
                        'rotation': [1, 0, 0], 'color': 'white'},
                    {'position': [1, 1, 0], 'rotation': [
                        1, 0, 0], 'color': 'blue'},
                    {'position': [1, 1, 1], 'rotation': [
                        1, 0, 0], 'color': 'white'},
                    {'position': [1, -1, 1],
                        'rotation': [0, 0, 1], 'color': 'white'},
                    {'position': [0, -1, 1],
                        'rotation': [0, 0, 1], 'color': 'blue'},
                    {'position': [-1, -1, 1],
                        'rotation': [0, 0, 1], 'color': 'green'},
                    {'position': [1, 0, 1], 'rotation': [
                        0, 0, 1], 'color': 'yellow'},
                    {'position': [0, 0, 1], 'rotation': [
                        0, 0, 1], 'color': 'blue'},
                    {'position': [-1, 0, 1],
                        'rotation': [0, 0, 1], 'color': 'white'},
                    {'position': [1, 1, 1], 'rotation': [
                        0, 0, 1], 'color': 'blue'},
                    {'position': [0, 1, 1], 'rotation': [
                        0, 0, 1], 'color': 'blue'},
                    {'position': [-1, 1, 1],
                        'rotation': [0, 0, 1], 'color': 'red'},
                    {'position': [-1, 1, -1],
                        'rotation': [0, 1, 0], 'color': 'white'},
                    {'position': [0, 1, -1],
                        'rotation': [0, 1, 0], 'color': 'red'},
                    {'position': [1, 1, -1],
                        'rotation': [0, 1, 0], 'color': 'red'},
                    {'position': [-1, 1, 0],
                        'rotation': [0, 1, 0], 'color': 'white'},
                    {'position': [0, 1, 0], 'rotation': [
                        0, 1, 0], 'color': 'yellow'},
                    {'position': [1, 1, 0], 'rotation': [
                        0, 1, 0], 'color': 'red'},
                    {'position': [-1, 1, 1],
                        'rotation': [0, 1, 0], 'color': 'yellow'},
                    {'position': [0, 1, 1], 'rotation': [
                        0, 1, 0], 'color': 'orange'},
                    {'position': [1, 1, 1], 'rotation': [0, 1, 0], 'color': 'red'}]
    }
    # When:

    # Then:
    if testCube.toDict() == expectedDictionary:
        print("Test cube initialisation: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test cube initialisation: " +
              printColors.FAIL + "failed" + printColors.RESET)

    return testCube

# Test getting squares on face


def test_getSquaresOnFace():
    # Given:
    testFace = "U"
    testCube = test_cubeInit()
    resultSquares = testCube.getSquaresOnFace(testFace)
    resultSquaresDict = {
        'squares': []
    }
    for square in resultSquares:
        resultSquaresDict["squares"].append(square.toDict())

    expectedDictionary = {
        'squares': [{'position': [-1, -1, 1], 'rotation': [0, -1, 0], 'color': 'yellow'},
                    {'position': [0, -1, 1],
                        'rotation': [0, -1, 0], 'color': 'yellow'},
                    {'position': [1, -1, 1],
                        'rotation': [0, -1, 0], 'color': 'blue'},
                    {'position': [-1, -1, 0],
                        'rotation': [0, -1, 0], 'color': 'green'},
                    {'position': [0, -1, 0],
                        'rotation': [0, -1, 0], 'color': 'white'},
                    {'position': [1, -1, 0],
                        'rotation': [0, -1, 0], 'color': 'white'},
                    {'position': [-1, -1, -1],
                        'rotation': [0, -1, 0], 'color': 'orange'},
                    {'position': [0, -1, -1],
                        'rotation': [0, -1, 0], 'color': 'green'},
                    {'position': [1, -1, -1],
                        'rotation': [0, -1, 0], 'color': 'red'},
                    {'position': [-1, -1, 1],
                        'rotation': [-1, 0, 0], 'color': 'orange'},
                    {'position': [-1, -1, 0],
                        'rotation': [-1, 0, 0], 'color': 'red'},
                    {'position': [-1, -1, -1],
                        'rotation': [-1, 0, 0], 'color': 'blue'},
                    {'position': [-1, -1, -1],
                        'rotation': [0, 0, -1], 'color': 'yellow'},
                    {'position': [0, -1, -1],
                        'rotation': [0, 0, -1], 'color': 'orange'},
                    {'position': [1, -1, -1],
                        'rotation': [0, 0, -1], 'color': 'green'},
                    {'position': [1, -1, -1],
                        'rotation': [1, 0, 0], 'color': 'yellow'},
                    {'position': [1, -1, 0],
                        'rotation': [1, 0, 0], 'color': 'orange'},
                    {'position': [1, -1, 1],
                        'rotation': [1, 0, 0], 'color': 'orange'},
                    {'position': [1, -1, 1],
                        'rotation': [0, 0, 1], 'color': 'white'},
                    {'position': [0, -1, 1],
                        'rotation': [0, 0, 1], 'color': 'blue'},
                    {'position': [-1, -1, 1], 'rotation': [0, 0, 1], 'color': 'green'}]
    }
    # When:

    # Then:
    if resultSquaresDict == expectedDictionary:
        print("Test getting squares on face: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test getting squares on face: " +
              printColors.FAIL + "failed" + printColors.RESET)

# Test rotation matrix


def test_getRotationMatrix():
    # Given:
    testAxis = "Y"
    testAngle = 2
    expectedMatrix = [[-1, 0, 0], [0, 1, 0], [0, 0, -1]]
    # When:

    # Then:
    if cube.cube.getRotationMatrix(testAxis, testAngle) == expectedMatrix:
        print("Test getting rotation matrix: " +
              printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test getting rotation matrix: " +
              printColors.FAIL + "failed" + printColors.RESET)


# Test move
def test_doMove():
    # Given:
    testMove = "B'"
    testCube = test_cubeInit()
    testCube.doMove(testMove)
    expectedDictionary = {'squares': [{'color': 'yellow', 'position': [1, -1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'yellow', 'position': [
                                          1, 0, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'blue', 'position': [
                                          1, 1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, -1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'white', 'position': [
                                          1, 0, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'white', 'position': [
                                          1, 1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'orange',
                                       'position': [1, -1, -1],
                                       'rotation': [1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, 0, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          1, 1, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'orange',
                                       'position': [1, -1, 1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'red', 'position': [
                                          1, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'blue', 'position': [
                                          1, -1, -1], 'rotation': [0, -1, 0]},
                                      {'color': 'red', 'position': [
                                          0, -1, 1], 'rotation': [0, -1, 0]},
                                      {'color': 'orange',
                                       'position': [0, -1, 0],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'yellow',
                                       'position': [0, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'blue',
                                          'position': [-1, -1, 1], 'rotation': [0, -1, 0]},
                                      {'color': 'blue',
                                          'position': [-1, -1, 0], 'rotation': [0, -1, 0]},
                                      {'color': 'green',
                                       'position': [-1, -1, -1],
                                       'rotation': [0, -1, 0]},
                                      {'color': 'yellow',
                                       'position': [1, -1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'orange',
                                       'position': [1, 0, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'green', 'position': [
                                          1, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'orange',
                                       'position': [-1, 0, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'green', 'position': [
                                          0, 0, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'white', 'position': [
                                          1, 0, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'orange',
                                       'position': [-1, 1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'yellow',
                                       'position': [0, 1, -1],
                                       'rotation': [0, 0, -1]},
                                      {'color': 'green', 'position': [
                                          1, 1, -1], 'rotation': [0, 0, -1]},
                                      {'color': 'yellow',
                                       'position': [1, -1, -1],
                                       'rotation': [1, 0, 0]},
                                      {'color': 'orange', 'position': [
                                          1, -1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'orange', 'position': [
                                          1, -1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, 0, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'red', 'position': [
                                          1, 0, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'green', 'position': [
                                          1, 0, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'white', 'position': [
                                          1, 1, -1], 'rotation': [1, 0, 0]},
                                      {'color': 'blue', 'position': [
                                          1, 1, 0], 'rotation': [1, 0, 0]},
                                      {'color': 'white', 'position': [
                                          1, 1, 1], 'rotation': [1, 0, 0]},
                                      {'color': 'white', 'position': [
                                          1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          0, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'green',
                                          'position': [-1, -1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'yellow', 'position': [
                                          1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          0, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'white',
                                          'position': [-1, 0, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'blue', 'position': [
                                          0, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'red',
                                          'position': [-1, 1, 1], 'rotation': [0, 0, 1]},
                                      {'color': 'white',
                                          'position': [-1, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [
                                          0, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [
                                          1, 1, -1], 'rotation': [0, 1, 0]},
                                      {'color': 'white',
                                          'position': [-1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'yellow', 'position': [
                                          0, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [
                                          1, 1, 0], 'rotation': [0, 1, 0]},
                                      {'color': 'yellow',
                                          'position': [-1, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'orange', 'position': [
                                          0, 1, 1], 'rotation': [0, 1, 0]},
                                      {'color': 'red', 'position': [1, 1, 1], 'rotation': [0, 1, 0]}]}

    # When:

    # Then:
    if testCube.toDict() == expectedDictionary:
        print("Test move: " + printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test move: " + printColors.FAIL + "failed" + printColors.RESET)


print("======================================== TESTING ========================================")
'''
test_squareInit()
print("---")
test_cubeInit()
print("---")
test_getSquaresOnFace()
print("---")
test_getRotationMatrix()
print("---")
test_doMove()
'''
print("=========================================================================================")
