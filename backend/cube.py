import numpy as np

class square:
    def __init__(self, pos, rot, color): 
        self.pos = pos #position of the square [x,y,z]
        self.rot = rot #rotation/direction the square is facing [x,y,z]
        self.color = color #R O Y W G B

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

    def buildCube(self,state): 
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

        #top
        for i in [1,0,-1]: # i is the row / z index
            for j in [-1,0,1]: # j is the column / x index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square( [j,-1,i], [0,-1,0], color ) )

        #left
        for i in [-1,0,1]: # i is the row / y index
            for j in [1,0,-1]: # j is the column / z index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square( [-1,i,j], [-1,0,0], color ) )

        #front
        for i in [-1,0,1]: # i is the row / y index
            for j in [-1,0,1]: # j is the column / x index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square( [j,i,-1], [0,0,-1], color ) )

        #right
        for i in [-1,0,1]: # i is the row / y index
            for j in [-1,0,1]: # j is the column / z index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square( [1,i,j], [1,0,0], color ) )

        #back
        for i in [-1,0,1]: # i is the row / y index
            for j in [1,0,-1]: # j is the column / x index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square( [j,i,1], [0,0,1], color ) )

        #bottom
        for i in [-1,0,1]: # i is the row / z index
            for j in [-1,0,1]: # j is the column / x index
                stateIndex += 1
                colorCode = state[stateIndex]
                color = getColourFromCode[colorCode]
                self.squares.append(square( [j,1,i], [0,1,0], color ) )

    def getSquaresOnFace(self, face): #face: U D L R F B
        rotationOfFace = {
            "R": [1, 0, 0],
            "L": [-1, 0, 0],
            "D": [0, 1, 0],
            "U": [0, -1, 0],
            "B": [0, 0, 1],
            "F": [0, 0, -1]
        }
        correctLayer = rotationOfFace[face]
        for i in [0,1,2]:
            if abs(correctLayer[i]) == 1: layerIndex = i
        resultSquares = []
        for square in self.squares:
            if square.pos[layerIndex] == correctLayer[layerIndex]:
                resultSquares.append(square)
        return resultSquares

    @staticmethod
    def getRotationMatrix(axis, angle): #axis: "X" "Y" "Z"; angle: 1(90CW) 2(180) -1(90ACW)
        RotationMatrix = []
        theta = angle * np.pi / 2
        if axis == "X":
            RotationMatrix = [[1, 0, 0],
                            [0, int(np.cos(theta)), -int(np.sin(theta))],
                            [0, int(np.sin(theta)), int(np.cos(theta))]]
        if axis == "Y":
            RotationMatrix = [[int(np.cos(theta)), 0, int(np.sin(theta))],
                            [0, 1, 0],
                            [-int(np.sin(theta)), 0, int(np.cos(theta))]]
        if axis == "Z":
            RotationMatrix = [[int(np.cos(theta)), -int(np.sin(theta)), 0],
                            [int(np.sin(theta)), int(np.cos(theta)), 0],
                            [0, 0, 1]]
        return RotationMatrix

    def doMove(self,move): #move: eg. "U" "F'" "D2"
    

        '''
        for square in GetSquaresOnDFace()
		cube.square.position = RotateYCW(cube.square.position)
		cube.square.orientation = RotateYCW(cube.square.orientation)
        '''
    
    def toDict(self):
        attributes = {
            "squares": []
        }
        for square in self.squares:
            attributes["squares"].append(square.toDict())
        return attributes
