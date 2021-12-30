crossSolution = {
    # (position,orientation): sequence of moves

    # in top layer facing up
    "([0, -1, -1], [0, -1, 0])": [],  # solved
    "([1, -1, 0], [0, -1, 0])": ["R'", "U'", "R", "U"],  # in UR pointing U
    "([0, -1, 1], [0, -1, 0])": ["B2", "D2", "F2"],  # in UB pointing U
    "([-1, -1, 0], [0, -1, 0])": ["L", "U", "L'", "U'"],  # in UL pointing U

    # in top layer facing out
    "([0, -1, -1], [0, 0, -1])": ["F", "U'", "R", "U"],  # in UF pointing F
    "([1, -1, 0], [1, 0, 0])": ["R'", "F'"],  # in UR pointing R
    "([0, -1, 1], [0, 0, 1])": ["U", "R'", "U'", "F'"],  # in UB pointing B
    "([-1, -1, 0], [-1, 0, 0])": ["L", "F"],  # in UL pointing L

    # in middle layer
    "([-1, 0, -1], [0, 0, -1])": ["U", "L'", "U'"],  # in LF pointing F
    "([1, 0, -1], [0, 0, -1])": ["U'", "R", "U"],  # in FR pointing F
    "([1, 0, -1], [1, 0, 0])": ["F'"],  # in FR pointing R
    "([1, 0, 1], [1, 0, 0])": ["U2", "B", "U2"],  # in RB pointing R
    "([1, 0, 1], [0, 0, 1])": ["U'", "R'", "U"],  # in RB pointing B
    "([-1, 0, 1], [0, 0, 1])": ["U", "L", "U'"],  # in BL pointing B
    "([-1, 0, 1], [-1, 0, 0])": ["U2", "B'", "U2"],  # in BL pointing L
    "([-1, 0, -1], [-1, 0, 0])": ["F"],  # in LF pointing L

    # in bottom layer facing out
    "([0, 1, -1], [0, 0, -1])": ["F'", "U'", "R", "U"],  # in DF pointing F
    "([1, 1, 0], [1, 0, 0])": ["U'", "R", "U", "F'"],  # in DR pointing R
    "([0, 1, 1], [0, 0, 1])": ["D'", "U'", "R", "U", "F'"],  # in DB pointing B
    "([-1, 1, 0], [-1, 0, 0])": ["U", "L'", "U'", "F"],  # in DL pointing L

    # in bottom layer facing down
    "([0, 1, -1], [0, 1, 0])": ["F2"],  # in DF pointing D
    "([1, 1, 0], [0, 1, 0])": ["D'", "F2"],  # in DR pointing D
    "([0, 1, 1], [0, 1, 0])": ["D2", "F2"],  # in DB pointing D
    "([-1, 1, 0], [0, 1, 0])": ["D", "F2"],  # in DL pointing D
}
