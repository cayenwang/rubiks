function request(endpoint, mode, callback, body = {}) {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            callback(JSON.parse(this.responseText));
        }
    };
    var url = "http://localhost:5000/";
    url += endpoint
    xmlhttp.open(mode, url, true);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.send(JSON.stringify(body));
}

document.getElementById("solve").addEventListener("click", solveCube);
document.getElementById("getSquaresOnFaceU").addEventListener("click", function () { getSquaresOnFace('U') });

function solveCube() {
    let request_body = {
        "cube": "yybgwwogrorbroybbgyogogwoygyoogrgwbwwbgybwbbrwrrwyryor"
    };
    request("solve", "POST", processResponse, request_body);
}

function processResponse(response) {
    console.log(response);
}
//----------------------
let exportSquaresToTurn

function getSquaresOnFace(face) {
    let requestBody = {
        "face": face
    }
    request("getSquaresOnFace", "POST", turn, requestBody)
}

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
    exportSquaresToTurn = positionList
}

export { exportSquaresToTurn }