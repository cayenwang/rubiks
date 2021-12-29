#import pytest

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
    if testSquare.toDict() == expectedDictionary:
        print('Test square initialisation passed')
    else: 
        print('Test square initialisation failed')

# Test cube initialisation
def test_cubeInit():
    # Given:
    testCube = cube.cube()
    testCube.buildCube("wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy")
    expectedDictionary = {
        'squares': [{'position': [-1, -1, 1], 'rotation': [0, -1, 0], 'color': 'white'}, 
                    {'position': [0, -1, 1], 'rotation': [0, -1, 0], 'color': 'white'}, 
                    {'position': [1, -1, 1], 'rotation': [0, -1, 0], 'color': 'white'}, 
                    {'position': [-1, -1, 0], 'rotation': [0, -1, 0], 'color': 'white'}, 
                    {'position': [0, -1, 0], 'rotation': [0, -1, 0], 'color': 'white'}, 
                    {'position': [1, -1, 0], 'rotation': [0, -1, 0], 'color': 'white'}, 
                    {'position': [-1, -1, -1], 'rotation': [0, -1, 0], 'color': 'white'}, 
                    {'position': [0, -1, -1], 'rotation': [0, -1, 0], 'color': 'white'}, 
                    {'position': [1, -1, -1], 'rotation': [0, -1, 0], 'color': 'white'}, 
                    {'position': [-1, -1, 1], 'rotation': [-1, 0, 0], 'color': 'orange'}, 
                    {'position': [-1, -1, 0], 'rotation': [-1, 0, 0], 'color': 'orange'}, 
                    {'position': [-1, -1, -1], 'rotation': [-1, 0, 0], 'color': 'orange'}, 
                    {'position': [-1, 0, 1], 'rotation': [-1, 0, 0], 'color': 'orange'}, 
                    {'position': [-1, 0, 0], 'rotation': [-1, 0, 0], 'color': 'orange'}, 
                    {'position': [-1, 0, -1], 'rotation': [-1, 0, 0], 'color': 'orange'}, 
                    {'position': [-1, 1, 1], 'rotation': [-1, 0, 0], 'color': 'orange'}, 
                    {'position': [-1, 1, 0], 'rotation': [-1, 0, 0], 'color': 'orange'}, 
                    {'position': [-1, 1, -1], 'rotation': [-1, 0, 0], 'color': 'orange'}, 
                    {'position': [-1, -1, -1], 'rotation': [0, 0, -1], 'color': 'green'}, 
                    {'position': [0, -1, -1], 'rotation': [0, 0, -1], 'color': 'green'}, 
                    {'position': [1, -1, -1], 'rotation': [0, 0, -1], 'color': 'green'}, 
                    {'position': [-1, 0, -1], 'rotation': [0, 0, -1], 'color': 'green'}, 
                    {'position': [0, 0, -1], 'rotation': [0, 0, -1], 'color': 'green'}, 
                    {'position': [1, 0, -1], 'rotation': [0, 0, -1], 'color': 'green'}, 
                    {'position': [-1, 1, -1], 'rotation': [0, 0, -1], 'color': 'green'}, 
                    {'position': [0, 1, -1], 'rotation': [0, 0, -1], 'color': 'green'}, 
                    {'position': [1, 1, -1], 'rotation': [0, 0, -1], 'color': 'green'}, 
                    {'position': [1, -1, -1], 'rotation': [1, 0, 0], 'color': 'red'}, 
                    {'position': [1, -1, 0], 'rotation': [1, 0, 0], 'color': 'red'}, 
                    {'position': [1, -1, 1], 'rotation': [1, 0, 0], 'color': 'red'}, 
                    {'position': [1, 0, -1], 'rotation': [1, 0, 0], 'color': 'red'}, 
                    {'position': [1, 0, 0], 'rotation': [1, 0, 0], 'color': 'red'}, 
                    {'position': [1, 0, 1], 'rotation': [1, 0, 0], 'color': 'red'}, 
                    {'position': [1, 1, -1], 'rotation': [1, 0, 0], 'color': 'red'}, 
                    {'position': [1, 1, 0], 'rotation': [1, 0, 0], 'color': 'red'}, 
                    {'position': [1, 1, 1], 'rotation': [1, 0, 0], 'color': 'red'}, 
                    {'position': [1, -1, 1], 'rotation': [0, 0, 1], 'color': 'blue'}, 
                    {'position': [0, -1, 1], 'rotation': [0, 0, 1], 'color': 'blue'}, 
                    {'position': [-1, -1, 1], 'rotation': [0, 0, 1], 'color': 'blue'}, 
                    {'position': [1, 0, 1], 'rotation': [0, 0, 1], 'color': 'blue'}, 
                    {'position': [0, 0, 1], 'rotation': [0, 0, 1], 'color': 'blue'}, 
                    {'position': [-1, 0, 1], 'rotation': [0, 0, 1], 'color': 'blue'}, 
                    {'position': [1, 1, 1], 'rotation': [0, 0, 1], 'color': 'blue'}, 
                    {'position': [0, 1, 1], 'rotation': [0, 0, 1], 'color': 'blue'}, 
                    {'position': [-1, 1, 1], 'rotation': [0, 0, 1], 'color': 'blue'}, 
                    {'position': [-1, 1, -1], 'rotation': [0, 1, 0], 'color': 'yellow'}, 
                    {'position': [0, 1, -1], 'rotation': [0, 1, 0], 'color': 'yellow'}, 
                    {'position': [1, 1, -1], 'rotation': [0, 1, 0], 'color': 'yellow'}, 
                    {'position': [-1, 1, 0], 'rotation': [0, 1, 0], 'color': 'yellow'}, 
                    {'position': [0, 1, 0], 'rotation': [0, 1, 0], 'color': 'yellow'}, 
                    {'position': [1, 1, 0], 'rotation': [0, 1, 0], 'color': 'yellow'}, 
                    {'position': [-1, 1, 1], 'rotation': [0, 1, 0], 'color': 'yellow'}, 
                    {'position': [0, 1, 1], 'rotation': [0, 1, 0], 'color': 'yellow'}, 
                    {'position': [1, 1, 1], 'rotation': [0, 1, 0], 'color': 'yellow'}]
    }
    # When:

    # Then:
    if testCube.toDict() == expectedDictionary:   
        print('Test cube initialisation passed')
    else:
        print('Test cube initialisation failed')


test_squareInit()
test_cubeInit()