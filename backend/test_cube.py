#import pytest
import sys,os

rootDirectory = os.path.abspath("../backend")
sys.path.append(rootDirectory)
print(os.path.exists(rootDirectory))

import cube


# Test square initialisation
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
