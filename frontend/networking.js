// Only set it if you're using a POST request - It probably won't break but it will only be used then
// It should be a JSON Object
// A callback is the function you want called when you receive a response
// It should have the signature functionName(JSONObject)
function request(endpoint, mode, callback, body = {}) {

    // Defines the reqeust with very little information
    var xmlhttp = new XMLHttpRequest();

    // Tells the request what to do once it gets a successful response
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            callback(JSON.parse(this.responseText));
        }
    };

    // This part tells the request
    // a. Where to send it via the <url>
    // b. How to send it via the "POST" or "GET" in <mode>
    // c. Unknown true variable
    var url = "http://localhost:5000/";
    url += endpoint
    xmlhttp.open(mode, url, true);

    // This bit is only necessary in a POST request
    // It tells the request that the encoding is going to be JSON
    // An alternate could be XML don't do this to yourself
    xmlhttp.setRequestHeader("Content-Type", "application/json");

    // This executes the request as defined above with the request_data provided
    // It also changes the JSON object provided to a string that can be sent https
    xmlhttp.send(JSON.stringify(body));
}

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