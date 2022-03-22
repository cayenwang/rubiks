import numpy as np


class square:  # tested
    def __init__(self, pos, rot, color):
        self.pos = pos  # position of the square [x,y,z]
        self.rot = rot  # rotation/direction the square is facing [x,y,z]
        self.color = color

    def toDict(self):
        attributes = {
            "position": [0, 0, 0],
            "rotation": [0, 0, 0],
            "color": self.color
        }
        # make sure that all attributes are in int's not int64's
        # this is so the squares can be JSON.dump'ed
        for i in [0, 1, 2]:
            attributes["position"][i] = int(self.pos[i])
            attributes["rotation"][i] = int(self.rot[i])
        return attributes


class cube:
    def __init__(self):
        self.squares = []
        # how many cube rotations in each axis the cube is from white up, green front
        self.offsetFromOriginal = [0, 0, 0]

    def buildCube(self, state):  # tested
        # "state" is a string with all the colours on the cube, where:
        #     www               123
        #     www               456
        #     www               789
        # ooo ggg rrr bbb   123 123 123 123
        # ooo ggg rrr bbb   456 456 456 456
        # ooo ggg rrr bbb   789 789 789 789
        #     yyy               123
        #     yyy               456
        #     yyy               789
        # is "wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy"
        # or "123456789123456789123456789123456789123456789123456789"

        stateIndex = -1
        getColourFromCode = {
            "w":  "white",
            "o":  "orange",
            "g":  "green",
            "r":  "red",
            "b":  "blue",
            "y":  "yellow",
        }

        # top
        for i in [1, 0, -1]:  # i is the row / z index
            for j in [-1, 0, 1]:  # j is the column / x index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square([j, -1, i], [0, -1, 0], color))

        # left
        for i in [-1, 0, 1]:  # i is the row / y index
            for j in [1, 0, -1]:  # j is the column / z index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square([-1, i, j], [-1, 0, 0], color))

        # front
        for i in [-1, 0, 1]:  # i is the row / y index
            for j in [-1, 0, 1]:  # j is the column / x index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square([j, i, -1], [0, 0, -1], color))

        # right
        for i in [-1, 0, 1]:  # i is the row / y index
            for j in [-1, 0, 1]:  # j is the column / z index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square([1, i, j], [1, 0, 0], color))

        # back
        for i in [-1, 0, 1]:  # i is the row / y index
            for j in [1, 0, -1]:  # j is the column / x index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square([j, i, 1], [0, 0, 1], color))

        # bottom
        for i in [-1, 0, 1]:  # i is the row / z index
            for j in [-1, 0, 1]:  # j is the column / x index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square([j, 1, i], [0, 1, 0], color))

    def getSquaresOnFace(self, face):  # tested
        # all squares on "X" face have [x,y,z] rotation
        rotationOfFace = {
            "R": [1, 0, 0],
            "L": [-1, 0, 0],
            "D": [0, 1, 0],
            "U": [0, -1, 0],
            "B": [0, 0, 1],
            "F": [0, 0, -1]
        }
        # get the rotation of the face
        correctLayer = rotationOfFace[face]
        # find the index in correctLayer where there's a 1 or -1
        # this index is where we expect to find a 1 or -1 if a square is in the layer
        # eg. [1,0,1] is in R layer ([1,0,0]) and B layer ([0,0,1])
        # because it has an 1 in 0th index and in 2nd index
        for i in [0, 1, 2]:
            if abs(correctLayer[i]) == 1:
                layerIndex = i
        # find all the squares that have a 1 or -1 in square.position[index_identified_above]
        resultSquares = []
        for square in self.squares:
            if square.pos[layerIndex] == correctLayer[layerIndex]:
                resultSquares.append(square)

        return resultSquares

    @staticmethod
    # axis: "X" "Y" "Z"; angle: 1(90CW) 2(180) -1(90ACW)
    def getRotationMatrix(axis, angle):  # tested
        RotationMatrix = []
        # angle needs to be multiplied by pi/2 to convert into radians
        theta = angle * np.pi / 2
        if axis == "X":
            RotationMatrix = [[1, 0, 0],
                              [0, round(np.cos(theta)), -round(np.sin(theta))],
                              [0, round(np.sin(theta)), round(np.cos(theta))]]
        if axis == "Y":
            RotationMatrix = [[round(np.cos(theta)), 0, round(np.sin(theta))],
                              [0, 1, 0],
                              [-round(np.sin(theta)), 0, round(np.cos(theta))]]
        if axis == "Z":
            RotationMatrix = [[round(np.cos(theta)), -round(np.sin(theta)), 0],
                              [round(np.sin(theta)), round(np.cos(theta)), 0],
                              [0, 0, 1]]
        return RotationMatrix

    def moveToRotationMatrix(self, move):
        # label of all the squares that needs to be turned (ignoring the angle to turn it)
        # eg. d, d' and d2 all turn the same squares. moveType is just the d
        moveType = move[0]
        # finds the primary face that is being rotated (eg R' and r both produce R)
        moveFace = move[0].upper()

        # seeing how far the face should be turned
        if len(move) == 1:
            moveAngle = 1
        elif move[1] == "'":
            moveAngle = -1
        elif move[1] == "2":
            moveAngle = 2

        moveToAxisAndAngle = {
            "R": ["X", -1],
            "L": ["X", 1],
            "D": ["Y", -1],
            "U": ["Y", 1],
            "B": ["Z", -1],
            "F": ["Z", 1],
            "X": ["X", -1],
            "Y": ["Y", 1],
            "Z": ["Z", 1],
            "M": ["X", 1],
            "E": ["Y", -1],
            "S": ["Z", 1]
        }

        # in order to rotate the desired face, which axis must squares be rotated about
        axis = moveToAxisAndAngle[moveFace][0]
        # the angle which would turn the face 90 degrees clockwise
        angleOf90CW = moveToAxisAndAngle[moveFace][1]

        # angle is the actual angle that needs to be put into the rotation matrix
        if abs(moveAngle) == 1:
            angle = moveAngle * angleOf90CW
        else:
            angle = moveAngle

        rotationMatrix = self.getRotationMatrix(axis, angle)

        return moveType, rotationMatrix, axis, angle

    def doMove(self, move):  # tested
        squaresToMove = []
        # a and b are dummy variables
        moveType, rotationMatrix, a, b = self.moveToRotationMatrix(move)

        # depending on what type of move we are dealing with, the set of squares
        # that are rotated will vary
        if moveType in ["R", "L", "D", "U", "B", "F"]:
            # rotate all squares in getSquaresOnFace()
            for square in self.getSquaresOnFace(moveType):
                for i in range(54):
                    if square == self.squares[i]:
                        squaresToMove.append(self.squares[i])
                        self.squares[i].pos = list(np.matmul(
                            rotationMatrix, self.squares[i].pos))
                        self.squares[i].rot = list(np.matmul(
                            rotationMatrix, self.squares[i].rot))

        elif moveType in ["X", "Y", "Z"]:
            # rotate all squares
            for i in range(54):
                squaresToMove.append(self.squares[i])
                self.squares[i].pos = list(np.matmul(
                    rotationMatrix, self.squares[i].pos))
                self.squares[i].rot = list(np.matmul(
                    rotationMatrix, self.squares[i].rot))

        elif moveType in ["r", "l", "d", "u", "b", "f"]:
            oppositeFace = {
                "r": "L",
                "l": "R",
                "d": "U",
                "u": "D",
                "b": "F",
                "f": "B"
            }
            for square in self.squares:
                # rotate all squares not on the opposite face
                if square not in self.getSquaresOnFace(oppositeFace[moveType]):
                    for i in range(54):
                        if square == self.squares[i]:
                            squaresToMove.append(self.squares[i])
                            self.squares[i].pos = list(np.matmul(
                                rotationMatrix, self.squares[i].pos))
                            self.squares[i].rot = list(np.matmul(
                                rotationMatrix, self.squares[i].rot))

        elif moveType in ["M", "E", "S"]:
            parallelFaces = {
                "M": ["L", "R"],
                "E": ["U", "D"],
                "S": ["F", "B"]
            }
            for square in self.squares:
                # rotate all squares not on the two layers parallel to the slice move
                if (square not in self.getSquaresOnFace(parallelFaces[moveType][0])) and \
                        (square not in self.getSquaresOnFace(parallelFaces[moveType][1])):
                    for i in range(54):
                        if square == self.squares[i]:
                            squaresToMove.append(self.squares[i])
                            self.squares[i].pos = list(np.matmul(
                                rotationMatrix, self.squares[i].pos))
                            self.squares[i].rot = list(np.matmul(
                                rotationMatrix, self.squares[i].rot))

        return squaresToMove

    def decompose(self):
        cubeState = ''
        getCodeFromColor = {
            "white": "w",
            "orange": "o",
            "green": "g",
            "red": "r",
            "blue": "b",
            "yellow": "y",
        }
        # top
        for i in [1, 0, -1]:  # i is the row / z index
            for j in [-1, 0, 1]:  # j is the column / x index
                for square in self.squares:
                    if square.rot == [0, -1, 0] and square.pos == [j, -1, i]:
                        code = getCodeFromColor[square.color]
                        cubeState = cubeState + code

        # left
        for i in [-1, 0, 1]:  # i is the row / y index
            for j in [1, 0, -1]:  # j is the column / z index
                for square in self.squares:
                    if square.rot == [-1, 0, 0] and square.pos == [-1, i, j]:
                        code = getCodeFromColor[square.color]
                        cubeState = cubeState + code

        # front
        for i in [-1, 0, 1]:  # i is the row / y index
            for j in [-1, 0, 1]:  # j is the column / x index
                for square in self.squares:
                    if square.rot == [0, 0, -1] and square.pos == [j, i, -1]:
                        code = getCodeFromColor[square.color]
                        cubeState = cubeState + code

        # right
        for i in [-1, 0, 1]:  # i is the row / y index
            for j in [-1, 0, 1]:  # j is the column / z index
                for square in self.squares:
                    if square.rot == [1, 0, 0] and square.pos == [1, i, j]:
                        code = getCodeFromColor[square.color]
                        cubeState = cubeState + code

        # back
        for i in [-1, 0, 1]:  # i is the row / y index
            for j in [1, 0, -1]:  # j is the column / x index
                for square in self.squares:
                    if square.rot == [0, 0, 1] and square.pos == [j, i, 1]:
                        code = getCodeFromColor[square.color]
                        cubeState = cubeState + code

        # bottom
        for i in [-1, 0, 1]:  # i is the row / z index
            for j in [-1, 0, 1]:  # j is the column / x index
                for square in self.squares:
                    if square.rot == [0, 1, 0] and square.pos == [j, 1, i]:
                        code = getCodeFromColor[square.color]
                        cubeState = cubeState + code

        return cubeState

    def toDict(self):  # tested
        attributes = {
            "squares": []
        }
        for square in self.squares:
            attributes["squares"].append(square.toDict())
        return attributes
