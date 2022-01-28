# Procedure that carries out an inputted sequence of moves, in the format of an array, on the cube in memory:


def doSequenceOfMoves(cube, sequence):
    for move in sequence:
        print("before:", repr(move), cube.toDict()["squares"][0])
        print('----------')
        cube.doMove(move)
        print("after:", repr(move), cube.toDict()["squares"][0])
        print('----------')
