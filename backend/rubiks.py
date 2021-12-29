import numpy as np

#import cube

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