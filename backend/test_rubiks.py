import rubiks

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
        print("Test square initialisation: " + printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test square initialisation: " + printColors.FAIL + "failed" + printColors.RESET)
'''

# Test rotation matrix
def test_getRotationMatrix():
    # Given:
    testAxis = "Y"
    testAngle = 2
    expectedMatrix = [[-1,0,0],[0,1,0],[0,0,-1]]
    # When:

    # Then:
    if rubiks.getRotationMatrix(testAxis,testAngle) == expectedMatrix:
        print("Test getting rotation matrix: " + printColors.PASS + "passed" + printColors.RESET)
    else:
        print("Test getting rotation matrix: " + printColors.FAIL + "failed" + printColors.RESET)

test_getRotationMatrix()