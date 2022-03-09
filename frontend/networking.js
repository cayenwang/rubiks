

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

function getSquaresOnFace(face) {
    requestBody = {
        "face": face
    }
    request("getSquaresOnFace", "POST", turn, requestBody)
}

function turn(response) {
    let squaresToTurn = response["squaresOnFace"]
    console.log(squaresToTurn)
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
        position = squaresToTurn[square]["position"]
        rotation = squaresToTurn[square]["rotation"]
        multiplier = rotationToMultiplier[rotation.toString()].split(",")


        positionList.push(position)
    }
    console.log(positionList)
}


//=========================

function solveCube() {
    request_body = {
        "cube": "yybgwwogrorbroybbgyogogwoygyoogrgwbwwbgybwbbrwrrwyryor"
    };
    request("solve", "POST", processResponse, request_body);
}

function testPost() {
    // An example of how you'd make a POST request
    request_body = {
        "language": "python"
    }
    request("jsonExample", "POST", processResponse, request_body);
}
function getRandomisedCube() {
    // An example of how you'd make a GET request
    request("getRandomisedCube", "GET", processResponse);
}

function processResponse(response) {
    console.log(response);
}