function turn(response) {
    let squaresToTurn = response["squaresOnFace"]
    let positionList = []
    let rotationToMultiplier = {
        "1,0,0": "33,22,22",
        "-1,0,0": "33,22,22",
        "0,1,0": "22,33,22",
        "0,-1,0": "22,33,22",
        "0,0,1": "22,22,33",
        "0,0,-1": "22,22,33"
    }
    for (var square in squaresToTurn) {
        let position = squaresToTurn[square]["position"]
        let rotation = squaresToTurn[square]["rotation"]
        let multiplier = rotationToMultiplier[rotation.toString()].split(",")
        for (let i = 0; i < 3; i++) {
            position[i] *= multiplier[i]
        }
        positionList.push(position)
    }
    console.log(positionList)
    return positionList
}

export { exportSquaresToTurn }