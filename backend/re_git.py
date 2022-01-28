# Procedure that carries out an inputted sequence of moves, in the format of an array, on the cube in memory:


def doSequenceOfMoves(cube, sequence):
    for move in sequence:
        cube.doMove(move)
