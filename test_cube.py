import pytest

# Test square initialisation
import cube

def test_squareInit():
    # Given:
    testSquare = cube.square([0,0,0], [0,1,0], "red")
    expectedDictionary = {
            "position": [0,0,0],
            "rotation": [0,1,0],
            "color": "red"
        }
    # When:

    # Then:
    assert testSquare.toDict() == expectedDictionary


# Test cube initialisation
def test_cubeInit():
    # Given:
    testCube = cube.cube()
    testCube.buildCube("wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy")
    print(testCube.toDict())
    
test_cubeInit()
