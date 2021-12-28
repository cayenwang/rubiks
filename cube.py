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