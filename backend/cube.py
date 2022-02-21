import numpy as np
import json


class square:  # tested
    def __init__(self, pos, rot, color):
        self.pos = pos  # position of the square [x,y,z]
        self.rot = rot  # rotation/direction the square is facing [x,y,z]
        self.color = color  # R O Y W G B

    def toDict(self):
        attributes = {
            "position": self.pos,
            "rotation": self.rot,
            "color": self.color
        }
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
        # is "wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy" or "123456789123456789123456789123456789123456789123456789"

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
        rotationOfFace = {
            "R": [1, 0, 0],
            "L": [-1, 0, 0],
            "D": [0, 1, 0],
            "U": [0, -1, 0],
            "B": [0, 0, 1],
            "F": [0, 0, -1]

        }
        correctLayer = rotationOfFace[face]
        for i in [0, 1, 2]:
            if abs(correctLayer[i]) == 1:
                layerIndex = i
        resultSquares = []
        for square in self.squares:
            if square.pos[layerIndex] == correctLayer[layerIndex]:
                resultSquares.append(square)

        return resultSquares

    @staticmethod
    # axis: "X" "Y" "Z"; angle: 1(90CW) 2(180) -1(90ACW)
    def getRotationMatrix(axis, angle):  # tested
        RotationMatrix = []
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
        # extracting the face that should be turned in the inputted move
        moveType = move[0]
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

        if abs(moveAngle) == 1:
            angle = moveAngle * angleOf90CW
        else:
            angle = moveAngle

        rotationMatrix = self.getRotationMatrix(axis, angle)

        return moveType, rotationMatrix

    def doMove(self, move):  # tested
        moveType, rotationMatrix = self.moveToRotationMatrix(move)

        if moveType in ["R", "L", "D", "U", "B", "F"]:
            for square in self.getSquaresOnFace(moveType):
                for i in range(54):
                    if square == self.squares[i]:
                        self.squares[i].pos = list(np.matmul(
                            rotationMatrix, self.squares[i].pos))
                        self.squares[i].rot = list(np.matmul(
                            rotationMatrix, self.squares[i].rot))

        elif moveType in ["X", "Y", "Z"]:
            for i in range(54):
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
                if square not in self.getSquaresOnFace(oppositeFace[moveType]):
                    for i in range(54):
                        if square == self.squares[i]:
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
                if (square not in self.getSquaresOnFace(parallelFaces[moveType][0])) and (square not in self.getSquaresOnFace(parallelFaces[moveType][1])):
                    for i in range(54):
                        if square == self.squares[i]:
                            self.squares[i].pos = list(np.matmul(
                                rotationMatrix, self.squares[i].pos))
                            self.squares[i].rot = list(np.matmul(
                                rotationMatrix, self.squares[i].rot))

    def toDict(self):  # tested
        attributes = {
            "squares": []
        }
        for square in self.squares:
            attributes["squares"].append(square.toDict())
        return attributes


if __name__ == "__main__":
    cube = cube()
    cube.buildCube("yybgwwogrorbroybbgyogogwoygyoogrgwbwwbgybwbbrwrrwyryor")
    cube.getSquaresOnFace("F")
