import numpy as np


# axis: "X" "Y" "Z"; angle: 1(90CW) 2(180) -1(90ACW)
def getRotationMatrix(axis, angle):
    RotationMatrix = []
    theta = angle * np.pi / 2
    if axis == "X":
        RotationMatrix = [[1, 0, 0],
                          [0, np.cos(theta), np.sin(theta)],
                          [0, np.sin(theta), np.cos(theta)]]
    if axis == "Y":
        RotationMatrix = [[np.cos(theta), 0, np.sin(theta)],
                          [0, 1, 0],
                          [np.sin(theta), 0, np.cos(theta)]]
    if axis == "Z":
        RotationMatrix = [[np.cos(theta), np.sin(theta), 0],
                          [np.sin(theta), np.cos(theta), 0],
                          [0, 0, 1]]
    return RotationMatrix
