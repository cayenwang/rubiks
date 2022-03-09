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

function solveCube() {
    request_body = {
        "cube": "yybgwwogrorbroybbgyogogwoygyoogrgwbwwbgybwbbrwrrwyryor"
    };
    request("solve", "POST", processResponse, request_body);
}

function processResponse(response) {
    console.log(response);
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

