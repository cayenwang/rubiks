'''crossSolution = {
    # (position,orientation): sequence of moves

    # in top layer facing up
    "([0, -1, -1], [0, -1, 0])": [],  # solved
    "([1, -1, 0], [0, -1, 0])": ["R'", "U'", "R", "U"],  # in UR pointing U
    
}'''

moveCornerToU = {
    # position: sequence of moves

    # in top layer (solved)
    [-1, -1, 1]: [],
    [1, -1, 1]: [],
    [-1, -1, -1]: [],
    [1, -1, -1]: [],

    # in bottom layer
    [-1, 1, 1]: ["R'", "U'", "R", "U"],
    [1, 1, 1]: ["L", "U", "L'", "U'"],
    [-1, 1, -1]: ["L'", "U'", "L", "U"],
    [1, 1, -1]: ["R", "U", "R'", "U'"]
}
