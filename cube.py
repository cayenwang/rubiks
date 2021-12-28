import numpy as np

class square:
    def __init__(self, pos, rot, color): 
        self.pos = pos #position of the square [x,y,z]
        self.rot = rot #rotation/direction the square is facing [x,y,z]
        self.color = color #R O Y W G B

switcherFaceDirection = {
    "R": [1, 0, 0],
    "L": [-1, 0, 0],
    "D": [0, 1, 0],
    "U": [0, -1, 0],
    "B": [0, 0, 1],
    "F": [0, 0, -1]
}

class cube:
    def __init__(self):
        self.squares=[] #array of all the squares that comprise the cube
        self._buildCube()
        
    '''    
    def _buildCube(self):
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                self.squares.append(square([1,j,k],[1,0,0],"R"))
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                self.squares.append(square([-1,j,k],[-1,0,0],"O"))
        for i in [-1,0,1]:
            for k in [-1,0,1]:
                self.squares.append(square([i,1,k],[0,1,0],"Y"))
        for i in [-1,0,1]:
            for k in [-1,0,1]:
                self.squares.append(square([i,-1,k],[0,-1,0],"W"))
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                self.squares.append(square([i,j,-1],[0,0,-1],"G"))
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                self.squares.append(square([i,j,1],[0,0,1],"B"))
    '''
        
    def _getSquaresOnFace(self, face): #face: U D L R F B
        faceDirection = switcherFaceDirection[face]
        resultSquares = []
        for square in self.squares:
            for i in faceDirection:
                if True:
                    place = i
            if square.pos[place] == faceDirection[place]:
                resultSquares.append(square)

RubiksCube = cube()
print(RubiksCube.squares)
#print(cube._getSquaresOnFace(RubiksCube,"U"))

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