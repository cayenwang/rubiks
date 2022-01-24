f2lSolution = {
    # taken off http://www.rubiksplace.com/speedcubing/F2L-algorithms/
    # transcribed in order (1-24)

    # (cornerRotation, edgePosition, edgeRotation): sequence of moves

    # corner on top, FL color facing side, edge colors match
    "([0, 0, -1], [1, -1, 0], [0, -1, 0])": ["R'", "F", "R", "F'"],  # 1
    "([1, 0, 0], [0, -1, -1], [0, 0, -1])": ["F", "R'", "F'", "R"],  # 2
    "([0, 0, -1], [0, -1, 1], [0, -1, 0])": ["U'", "R", "U", "R'", "U2", "R", "U'", "R'"],  # 3
    "([1, 0, 0], [-1, -1, 0], [-1, 0, 0])": ["Y'", "U", "R'", "U'", "R", "U2", "R'", "U", "R", "Y"],  # 4
    "([0, 0, -1], [-1, -1, 0], [0, -1, 0])": ["U'", "R", "U2'", "R'", "U2", "R", "U'", "R'"],  # 5
    "([1, 0, 0], [0, -1, 1], [0, 0, 1])": ["Y'", "U", "R'", "U2", "R", "U2'", "R'", "U", "R", "Y"],  # 6
    "([0, 0, -1], [0, -1, -1], [0, -1, 0])": ["Y'", "R'", "U", "R", "U'", "Y", "U'", "R", "U", "R'"],  # 7
    "([1, 0, 0], [1, -1, 0], [1, 0, 0])": ["R", "U'", "R'", "U", "Y'", "U", "R'", "U'", "R", "Y"],  # 8

    # corner on top, FL color facing side, edge colors opposite
    "([0, 0, -1], [-1, -1, 0], [-1, 0, 0])": ["Y'", "R'", "U'", "R", "Y"],  # 9
    "([1, 0, 0], [0, -1, 1], [0, -1, 0])": ["R", "U", "R'"],  # 10
    "([0, 0, -1], [0, -1, 1], [0, 0, 1])": ["Y'", "U", "R'", "U'", "R", "U'R'", "U'", "R", "Y"],  # 11
    "([1, 0, 0], [-1, -1, 0], [0, -1, 0])": ["U'", "R", "U", "R'", "U", "R", "U", "R'"],  # 12
    "([0, 0, -1], [1, -1, 0], [1, 0, 0])": ["U'", "R", "U2'", "R'", "Y'", "U", "R'", "U'", "R", "Y"],  # 13
    "([1, 0, 0], [0, -1, -1], [0, -1, 0])": ["R'", "U2", "R2", "U", "R2'", "U", "R"],  # 14
    "([0, 0, -1], [0, -1, -1], [0, 0, -1])": ["Y'", "U", "R'", "U", "R", "U'", "R'", "U'", "R", "Y"],  # 15
    "([1, 0, 0], [1, -1, 0], [0, -1, 0])": ["U'", "R", "U'", "R'", "U", "R", "U", "R'"],  # 16

    # corner on top, FL color facing up
    "([0, -1, 0], [1, -1, 0], [0, -1, 0])": ["R", "U2'", "R'", "U'", "R", "U", "R'"],  # 17
    "([0, -1, 0], [0, -1, -1], [0, 0, -1])": ["Y'", "R'", "U2", "R", "U", "R'", "U'", "R", "Y"],  # 18
    "([0, -1, 0], [0, -1, 1], [0, -1, 0])": ["U", "R", "U2", "R'", "U", "R", "U'", "R'"],  # 19
    "([0, -1, 0], [-1, -1, 0], [-1, 0, 0])": ["Y'", "U'", "R'", "U2", "R", "U'", "R'", "U", "R", "Y"],  # 20
    "([0, -1, 0], [-1, -1, 0], [0, -1, 0])": ["U2", "R", "U", "R'", "U", "R", "U'", "R'"],  # 21
    "([0, -1, 0], [0, -1, 1], [0, 0, 1])": ["Y'", "U2", "R'", "U'", "R", "U'", "R'", "U", "R", "Y"],  # 22
    "([0, -1, 0], [0, -1, -1], [0, -1, 0])": ["Y'", "U", "R'", "U2", "R", "Y", "R", "U2", "R'", "U", "R", "U'", "R'"],  # 23
    "([0, -1, 0], [1, -1, 0], [1, 0, 0])": ["U'", "R", "U2'", "R'", "Y'", "R'", "U2", "R", "U'", "R'", "U", "R", "Y"]  # 24
}