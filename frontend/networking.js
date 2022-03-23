/*
=========================================================================================
Define a general request function
=========================================================================================
*/

function request(endpoint, mode, callback, body = {}) {
    // creates an xmlhttp request
    var xmlhttp = new XMLHttpRequest();
    // when the page is ready
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            callback(JSON.parse(this.responseText));
        }
    };
    // access this url
    var url = "http://localhost:5000/";
    url += endpoint;
    xmlhttp.open(mode, url, true);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.send(JSON.stringify(body));
}

/*
=========================================================================================
Get the cube solution
=========================================================================================
*/

let exportSolution;

export function solveCube(cube) {
    let request_body = {
        "cube": cube
    };
    request("solve", "POST", processSolve, request_body);
}

function processSolve(response) {
    exportSolution = response;
}

/*
=========================================================================================
Get the rotation matrix, axis and angle
=========================================================================================
*/

let exportSquaresToTurn, exportMatrix, exportAxis, exportAngle;

export function getSquaresOnFace(face) {
    // only send the moveType to 'getSquares'
    let requestBody1 = {
        "face": face[0]
    };
    // send the entire move to get the matrix
    let requestBody2 = {
        "face": face
    };
    request("getSquaresOnFace", "POST", getSquares, requestBody1);
    request("getARotationMatrix", "POST", getMatrix, requestBody2);
}

function getSquares(response) {
    let squaresToTurn = response["squaresOnFace"];
    let positionList = [];
    let rotationList = [];
    // the multiplier that needs to be applied to the position vector 
    // depending on what face the square is on
    let rotationToMultiplier = {
        "1,0,0": "33,22,22",
        "-1,0,0": "33,22,22",
        "0,1,0": "22,33,22",
        "0,-1,0": "22,33,22",
        "0,0,1": "22,22,33",
        "0,0,-1": "22,22,33"
    };
    // for each square that needs to be turned
    for (var square in squaresToTurn) {
        let position = squaresToTurn[square]["position"];
        let rotation = squaresToTurn[square]["rotation"];
        // find what the position needs to be multiplied based of the square's rotation
        let multiplier = rotationToMultiplier[rotation.toString()].split(",");
        // apply the multiplier
        for (let i = 0; i < 3; i++) {
            position[i] *= multiplier[i];
        }
        // push position and rotation into lists to be returned
        positionList.push(position);
        rotationList.push(rotation);
    }
    exportSquaresToTurn = {
        "positionList": positionList,
        "rotationList": rotationList
    };
}

function getMatrix(response) {
    exportMatrix = response["rotationMatrix"];
    exportAxis = response["axis"];
    exportAngle = response["angle"];
}

/*
=========================================================================================
Get the cube state of a cube from a scramble
=========================================================================================
*/

let exportCubeState;

export function getCubeState(scramble) {
    let scrambleList = scramble.split(" ");
    let request_body = {
        "scramble": scrambleList
    };
    request("getCubeState", "POST", process, request_body);
}

function process(response) {
    exportCubeState = response;
}

/*
=========================================================================================
Exports
=========================================================================================
*/

export { exportSquaresToTurn, exportMatrix, exportAngle, exportAxis, exportSolution, exportCubeState }