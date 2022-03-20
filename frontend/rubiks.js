import * as THREE from './three.js-dev/build/three.module.js';
import { OrbitControls } from './three.js-dev/examples/jsm/controls/OrbitControls.js';
import { FontLoader } from './three.js-dev/examples/jsm/loaders/FontLoader.js'
import { TextGeometry } from './three.js-dev/examples/jsm/geometries/TextGeometry.js';
//import { AnimationClip, AnimationMixer, QuaternionKeyframeTrack, Clock } from './three.js-dev/build/three.module.js';
import { exportAngle, exportAxis, exportMatrix, exportSquaresToTurn, getSquaresOnFace, solveCube, exportSolution, getCubeState, exportCubeState } from './networking.js'

/*
=========================================================================================
World Building
=========================================================================================
*/

let camera, controls, scene, renderer;
let cubeSquares
let counter

createScene();
setCameraControls();
setLighting()
animate();

function createScene() {
    // build world
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0xfaebe3);

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.set(100, -200, -400);
    camera.up.set(0, -1, 0);

    window.addEventListener('resize', onWindowResize);

}

// build cube
let allFloats = []
cubeSquares = buildCube();

function buildCube(state = "wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy") {
    let allSquares = []
    let sideWidth = 20;
    let separation = 1.1;
    let floatDist = 80;

    const geometrySquare = new THREE.PlaneGeometry(sideWidth, sideWidth);
    const materialRed = new THREE.MeshPhongMaterial({ color: 0xde3421, flatShading: true });
    const materialOrange = new THREE.MeshPhongMaterial({ color: 0xc47806, flatShading: true })
    const materialYellow = new THREE.MeshPhongMaterial({ color: 0xeaed32, flatShading: true })
    const materialWhite = new THREE.MeshPhongMaterial({ color: 0xfffff7, flatShading: true })
    const materialGreen = new THREE.MeshPhongMaterial({ color: 0x2bcc2e, flatShading: true })
    const materialBlue = new THREE.MeshPhongMaterial({ color: 0x3e78d6, flatShading: true })

    const materialBlack = new THREE.MeshPhongMaterial({ color: 0x000000, flatShading: true })
    const geometryBlack = new THREE.PlaneGeometry(sideWidth * separation, sideWidth * separation);

    let stateIndex = -1
    let getColourFromCode = {
        "w": materialWhite,
        "o": materialOrange,
        "g": materialGreen,
        "r": materialRed,
        "b": materialBlue,
        "y": materialYellow,
    }

    // top
    for (let i = -1; i < 2; i++) {
        for (let k = -1; k < 2; k++) {
            stateIndex++
            let colorCode = state[stateIndex]
            let color = getColourFromCode[colorCode]

            const square = new THREE.Mesh(geometrySquare, color)
            square.position.x = k * sideWidth * separation;
            square.position.y = -sideWidth * separation * 1.5;
            square.position.z = -i * sideWidth * separation;
            square.rotation.x = Math.PI / 2;
            square.rotation.y = 0;
            square.rotation.z = 0;
            square.updateMatrix();
            scene.add(square);
            allSquares.push(square)

            const floatingSquare = new THREE.Mesh(geometrySquare, color)
            floatingSquare.position.z = floatDist
            floatingSquare.rotation.y = - Math.PI;
            floatingSquare.updateMatrix();
            scene.add(floatingSquare);
            square.add(floatingSquare)
            allFloats.push(floatingSquare)

            const blackSquare = new THREE.Mesh(geometryBlack, materialBlack)
            blackSquare.rotation.y = - Math.PI;
            blackSquare.updateMatrix();
            scene.add(blackSquare);
            square.add(blackSquare)
        }
    }

    // left
    for (let j = -1; j < 2; j++) {
        for (let k = -1; k < 2; k++) {
            stateIndex++
            let colorCode = state[stateIndex]
            let color = getColourFromCode[colorCode]

            const square = new THREE.Mesh(geometrySquare, color)
            square.position.x = -sideWidth * separation * 1.5;
            square.position.y = j * sideWidth * separation;
            square.position.z = -k * sideWidth * separation;
            square.rotation.x = 0;
            square.rotation.y = -Math.PI / 2;
            square.rotation.z = 0;
            square.updateMatrix();
            scene.add(square);
            allSquares.push(square)

            const floatingSquare = new THREE.Mesh(geometrySquare, color)
            floatingSquare.position.z = floatDist
            floatingSquare.rotation.y = - Math.PI;
            floatingSquare.updateMatrix();
            scene.add(floatingSquare);
            square.add(floatingSquare)
            allFloats.push(floatingSquare)

            const blackSquare = new THREE.Mesh(geometryBlack, materialBlack)
            blackSquare.rotation.y = - Math.PI;
            blackSquare.updateMatrix();
            scene.add(blackSquare);
            square.add(blackSquare)
        }
    }

    // front
    for (let i = -1; i < 2; i++) {
        for (let j = -1; j < 2; j++) {
            stateIndex++
            let colorCode = state[stateIndex]
            let color = getColourFromCode[colorCode]

            const square = new THREE.Mesh(geometrySquare, color)
            square.position.x = j * sideWidth * separation;
            square.position.y = i * sideWidth * separation;
            square.position.z = -sideWidth * separation * 1.5;
            square.rotation.x = 0;
            square.rotation.y = Math.PI;
            square.rotation.z = 0;
            square.updateMatrix();
            scene.add(square);
            allSquares.push(square)

            const floatingSquare = new THREE.Mesh(geometrySquare, color)
            floatingSquare.position.z = floatDist
            floatingSquare.rotation.y = - Math.PI;
            floatingSquare.updateMatrix();
            scene.add(floatingSquare);
            square.add(floatingSquare)
            allFloats.push(floatingSquare)

            const blackSquare = new THREE.Mesh(geometryBlack, materialBlack)
            blackSquare.rotation.y = - Math.PI;
            blackSquare.updateMatrix();
            scene.add(blackSquare);
            square.add(blackSquare)
        }
    }

    // right
    for (let j = -1; j < 2; j++) {
        for (let k = -1; k < 2; k++) {
            stateIndex++
            let colorCode = state[stateIndex]
            let color = getColourFromCode[colorCode]

            const square = new THREE.Mesh(geometrySquare, color)
            square.position.x = sideWidth * separation * 1.5;
            square.position.y = j * sideWidth * separation;
            square.position.z = k * sideWidth * separation;
            square.rotation.x = 0;
            square.rotation.y = Math.PI / 2;
            square.rotation.z = 0;
            square.updateMatrix();
            scene.add(square);
            allSquares.push(square)

            const floatingSquare = new THREE.Mesh(geometrySquare, color)
            floatingSquare.position.z = floatDist
            floatingSquare.rotation.y = - Math.PI;
            floatingSquare.updateMatrix();
            scene.add(floatingSquare);
            square.add(floatingSquare)
            allFloats.push(floatingSquare)

            const blackSquare = new THREE.Mesh(geometryBlack, materialBlack)
            blackSquare.rotation.y = - Math.PI;
            blackSquare.updateMatrix();
            scene.add(blackSquare);
            square.add(blackSquare)
        }
    }

    // back
    for (let i = -1; i < 2; i++) {
        for (let j = -1; j < 2; j++) {
            stateIndex++
            let colorCode = state[stateIndex]
            let color = getColourFromCode[colorCode]

            const square = new THREE.Mesh(geometrySquare, color)
            square.position.x = -j * sideWidth * separation;
            square.position.y = i * sideWidth * separation;
            square.position.z = sideWidth * separation * 1.5;
            square.rotation.x = 0;
            square.rotation.y = 0;
            square.rotation.z = 0;
            square.updateMatrix();
            scene.add(square);
            allSquares.push(square)

            const floatingSquare = new THREE.Mesh(geometrySquare, color)
            floatingSquare.position.z = floatDist
            floatingSquare.rotation.y = - Math.PI;
            floatingSquare.updateMatrix();
            scene.add(floatingSquare);
            square.add(floatingSquare)
            allFloats.push(floatingSquare)

            const blackSquare = new THREE.Mesh(geometryBlack, materialBlack)
            blackSquare.rotation.y = - Math.PI;
            blackSquare.updateMatrix();
            scene.add(blackSquare);
            square.add(blackSquare)
        }
    }

    // bottom
    for (let i = -1; i < 2; i++) {
        for (let k = -1; k < 2; k++) {
            stateIndex++
            let colorCode = state[stateIndex]
            let color = getColourFromCode[colorCode]

            const square = new THREE.Mesh(geometrySquare, color)
            square.position.x = k * sideWidth * separation;
            square.position.y = sideWidth * separation * 1.5;
            square.position.z = i * sideWidth * separation;
            square.rotation.x = -Math.PI / 2;
            square.rotation.y = 0;
            square.rotation.z = 0;
            square.updateMatrix();
            scene.add(square);
            allSquares.push(square)

            const floatingSquare = new THREE.Mesh(geometrySquare, color)
            floatingSquare.position.z = floatDist
            floatingSquare.rotation.y = - Math.PI;
            floatingSquare.updateMatrix();
            scene.add(floatingSquare);
            square.add(floatingSquare)
            allFloats.push(floatingSquare)

            const blackSquare = new THREE.Mesh(geometryBlack, materialBlack)
            blackSquare.rotation.y = - Math.PI;
            blackSquare.updateMatrix();
            scene.add(blackSquare);
            square.add(blackSquare)
        }
    }

    for (var square in allFloats) {
        allFloats[square].visible = false
    }

    var loader = new FontLoader();
    var textMaterial = new THREE.MeshPhongMaterial({ color: 0x000000 });
    let labelText = ["U", "L", "F", "R", "B", "D"]
    let labelPosition = [[-5, -34, -5], [-34, 5, 5], [-5, 5, -34], [34, 5, -5], [5, 5, 34], [-5, 34, 5]]
    let labelRotation = [[1, 0, 0], [2, 3, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0], [3, 0, 0]]
    loader.load('./three.js-dev/examples/fonts/helvetiker_bold.typeface.json', function (font) {
        for (var i in labelText) {
            var textGeometry = new TextGeometry(labelText[i], {
                font: font,
                size: 10,
                height: 0.01,
                curveSegments: 12,
            });
            var label = new THREE.Mesh(textGeometry, textMaterial);
            label.position.x = labelPosition[i][0];
            label.position.y = labelPosition[i][1];
            label.position.z = labelPosition[i][2];
            label.rotation.x = labelRotation[i][0] * Math.PI / 2;
            label.rotation.y = labelRotation[i][1] * Math.PI / 2;
            label.rotation.z = labelRotation[i][2] * Math.PI / 2;

            scene.add(label);
        };

    })

    return allSquares
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    render()
}

function render() {
    renderer.render(scene, camera);
}


function setCameraControls() {
    controls = new OrbitControls(camera, renderer.domElement);
    controls.listenToKeyEvents(window); // optional

    controls.enableDamping = true;
    controls.dampingFactor = 0.1;

    controls.screenSpacePanning = false;

    controls.minDistance = 200;
    controls.maxDistance = 400;

    controls.maxPolarAngle = Math.PI;
    controls.minPolarAngle = -Math.PI;
}

function setLighting() {

    const dirLight1 = new THREE.DirectionalLight(0xffffff);
    dirLight1.position.set(1, 1, 1);
    scene.add(dirLight1);

    const dirLight2 = new THREE.DirectionalLight(0xffffff);
    dirLight2.position.set(- 1, - 1, - 1);
    scene.add(dirLight2);


    const ambientLight = new THREE.AmbientLight(0xffffff);
    scene.add(ambientLight);
}

function onWindowResize() {

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize(window.innerWidth, window.innerHeight);

}

/*
=========================================================================================
Functionality
=========================================================================================
*/

function findSquaresToTurn() {
    let resultSquaresToTurn = []
    let positionList = exportSquaresToTurn['positionList']

    // for each position 
    for (var i in positionList) {
        let aPosition = positionList[i]
        // find the corresponding square
        for (let i = 0; i < 54; i++) {
            let square = cubeSquares[i]
            if (
                aPosition[0] == square.position.x
                && aPosition[1] == square.position.y
                && aPosition[2] == square.position.z
            ) {
                // and add that to an array
                resultSquaresToTurn.push(square)
            }
        }
    }
    let result = {
        "resultSquaresToTurn": resultSquaresToTurn
    }
    return result
}

function turnSquares() {
    //find the squares to turn
    let resultSquares = findSquaresToTurn()
    let squaresToTurn = resultSquares['resultSquaresToTurn']

    let targetAxis = exportAxis
    let targetAngle = exportAngle

    let divider = 30
    //rotates the layer
    function rotator() {
        //define the axis and angle of rotation
        let axis = new THREE.Vector3(0, 0, 0);
        if (targetAxis == "X") {
            axis.set(1, 0, 0);
        } else if (targetAxis == "Y") {
            axis.set(0, 1, 0);
        } else if (targetAxis == "Z") {
            axis.set(0, 0, 1);
        }
        let angle = targetAngle * Math.PI / divider

        var matrix = new THREE.Matrix4();
        matrix.makeRotationAxis(axis, angle)

        if (counter < divider / 2) {
            requestAnimationFrame(rotator);
            for (var square in squaresToTurn) {
                squaresToTurn[square].applyMatrix4(matrix);
            }
            counter += 1
        }
        if (counter == divider / 2) {
            for (var square in squaresToTurn) {
                let xyz = ["x", "y", "z"]
                for (var i in xyz) {
                    squaresToTurn[square].position[xyz[i]] = Math.round(squaresToTurn[square].position[xyz[i]])
                }
            }
        }

        renderer.render(scene, camera);
    }
    rotator()
}

function completeTurn(face) {
    getSquaresOnFace(face)
    setTimeout(() => { counter = 0; turnSquares() }, 500)
}

// buttons
{
    document.getElementById("TurnR").addEventListener("click", function () { completeTurn("R") });
    document.getElementById("TurnL").addEventListener("click", function () { completeTurn("L") });
    document.getElementById("TurnD").addEventListener("click", function () { completeTurn("D") });
    document.getElementById("TurnU").addEventListener("click", function () { completeTurn("U") });
    document.getElementById("TurnB").addEventListener("click", function () { completeTurn("B") });
    document.getElementById("TurnF").addEventListener("click", function () { completeTurn("F") });
    document.getElementById("TurnR'").addEventListener("click", function () { completeTurn("R'") });
    document.getElementById("TurnL'").addEventListener("click", function () { completeTurn("L'") });
    document.getElementById("TurnD'").addEventListener("click", function () { completeTurn("D'") });
    document.getElementById("TurnU'").addEventListener("click", function () { completeTurn("U'") });
    document.getElementById("TurnB'").addEventListener("click", function () { completeTurn("B'") });
    document.getElementById("TurnF'").addEventListener("click", function () { completeTurn("F'") });
    document.getElementById("TurnR2").addEventListener("click", function () { completeTurn("R2") });
    document.getElementById("TurnL2").addEventListener("click", function () { completeTurn("L2") });
    document.getElementById("TurnD2").addEventListener("click", function () { completeTurn("D2") });
    document.getElementById("TurnU2").addEventListener("click", function () { completeTurn("U2") });
    document.getElementById("TurnB2").addEventListener("click", function () { completeTurn("B2") });
    document.getElementById("TurnF2").addEventListener("click", function () { completeTurn("F2") });

    document.getElementById("TurnM").addEventListener("click", function () { completeTurn("M") });
    document.getElementById("TurnE").addEventListener("click", function () { completeTurn("E") });
    document.getElementById("TurnS").addEventListener("click", function () { completeTurn("S") });
    document.getElementById("TurnM'").addEventListener("click", function () { completeTurn("M'") });
    document.getElementById("TurnE'").addEventListener("click", function () { completeTurn("E'") });
    document.getElementById("TurnS'").addEventListener("click", function () { completeTurn("S'") });
    document.getElementById("TurnM2").addEventListener("click", function () { completeTurn("M2") });
    document.getElementById("TurnE2").addEventListener("click", function () { completeTurn("E2") });
    document.getElementById("TurnS2").addEventListener("click", function () { completeTurn("S2") });

    document.getElementById("TurnX").addEventListener("click", function () { completeTurn("X") });
    document.getElementById("TurnY").addEventListener("click", function () { completeTurn("Y") });
    document.getElementById("TurnZ").addEventListener("click", function () { completeTurn("Z") });
    document.getElementById("TurnX'").addEventListener("click", function () { completeTurn("X'") });
    document.getElementById("TurnY'").addEventListener("click", function () { completeTurn("Y'") });
    document.getElementById("TurnZ'").addEventListener("click", function () { completeTurn("Z'") });
    document.getElementById("TurnX2").addEventListener("click", function () { completeTurn("X2") });
    document.getElementById("TurnY2").addEventListener("click", function () { completeTurn("Y2") });
    document.getElementById("TurnZ2").addEventListener("click", function () { completeTurn("Z2") });

    document.getElementById("Turnr").addEventListener("click", function () { completeTurn("r") });
    document.getElementById("Turnl").addEventListener("click", function () { completeTurn("l") });
    document.getElementById("Turnd").addEventListener("click", function () { completeTurn("d") });
    document.getElementById("Turnu").addEventListener("click", function () { completeTurn("u") });
    document.getElementById("Turnb").addEventListener("click", function () { completeTurn("b") });
    document.getElementById("Turnf").addEventListener("click", function () { completeTurn("f") });
    document.getElementById("Turnr'").addEventListener("click", function () { completeTurn("r'") });
    document.getElementById("Turnl'").addEventListener("click", function () { completeTurn("l'") });
    document.getElementById("Turnd'").addEventListener("click", function () { completeTurn("d'") });
    document.getElementById("Turnu'").addEventListener("click", function () { completeTurn("u'") });
    document.getElementById("Turnb'").addEventListener("click", function () { completeTurn("b'") });
    document.getElementById("Turnf'").addEventListener("click", function () { completeTurn("f'") });
    document.getElementById("Turnr2").addEventListener("click", function () { completeTurn("r2") });
    document.getElementById("Turnl2").addEventListener("click", function () { completeTurn("l2") });
    document.getElementById("Turnd2").addEventListener("click", function () { completeTurn("d2") });
    document.getElementById("Turnu2").addEventListener("click", function () { completeTurn("u2") });
    document.getElementById("Turnb2").addEventListener("click", function () { completeTurn("b2") });
    document.getElementById("Turnf2").addEventListener("click", function () { completeTurn("f2") });
}

/*
=========================================================================================
Page
=========================================================================================
*/

let cubeState
let solutionIndex = 0

document.getElementById("submitCubeScramble").addEventListener("click", submit);
function submit() {
    let cubeScramble = document.getElementById("cubeScramble").value
    if (validateScramble(cubeScramble)) {
        getCubeState(cubeScramble)
        setTimeout(() => {
            cubeState = exportCubeState["cubeState"]
            console.log("cubestate", cubeState)
            for (let i = scene.children.length - 1; i >= 0; i--) {
                if (scene.children[i].type === "Mesh")
                    scene.remove(scene.children[i]);
            }
            cubeSquares = buildCube(cubeState)
        }, 500)
    } else { document.getElementById("cubeScramble").value = 'Invalid Scramble' }
}

function validateScramble(scramble) {
    let scrambleList = scramble.split(" ")
    let result = true
    let allowedFaces = ["R", "L", "D", "U", "B", "F", "M", "E", "S", "X", "Y", "Z", "r", "l", "d", "u", "b", "f"]
    let allowedAngles = ["'", "2"]
    for (var i in scrambleList) {
        let temp = scrambleList[i]
        if (allowedFaces.includes(temp[0]) == false) {
            result = false
        } else if (temp.length > 2) {
            result = false
        } else if (temp.length == 2 && allowedAngles.includes(temp[1]) == false) {
            result = false
        }
    }
    return result
}

function doSolve() {
    let solution = exportSolution["moves"];
    (function loop(i) {
        setTimeout(function () {
            if (startStop && solutionIndex < solution.length) {
                completeTurn(solution[solutionIndex])
                //setTimeout(function () {
                updateNotationText(solution[solutionIndex])
                //}, 500)
                solutionIndex += 1
                let progressBarWidth = document.getElementById('bar').offsetWidth
                progressBarWidth = (progressBarWidth - 20) * solutionIndex / solution.length + 20
                document.getElementById("progress").style.width = progressBarWidth + 'px';
                if (--i) loop(i)
            } else if (solutionIndex == solution.length) {
                document.getElementById("wholeSolve").style.display = "inline"
                document.getElementById("playPause").style.display = "none"
                solutionIndex = 0
                play()
                return
            } else { loop(i) }
        }, 1000)
    })(1000)
}

function updateNotationText(move) {
    let faceToText = {
        "R": "<b>right</b> face",
        "L": "<b>left</b> face",
        "U": "<b>top</b> face",
        "D": "<b>bottom</b> face",
        "F": "<b>front</b> face",
        "B": "<b>back</b> face",
        "M": "<b>middle</b> slice",
        "E": "<b>equatorial</b> slice",
        "S": "<b>standing</b> slice",
        "X": "<b>whole cube</b>",
        "Y": "<b>whole cube</b>",
        "Z": "<b>whole cube</b>",
        "r": "<b>two right</b> layers",
        "l": "<b>two left</b> layers",
        "u": "<b>two top</b> layers",
        "d": "<b>two bottom</b> layers",
        "f": "<b>two front</b> layers",
        "b": "<b>two back</b> layers",
    }
    let angleToText = {
        "1": "<b>90</b> degrees <b>clockwise</b>",
        "'": "<b>90</b> degrees <b>anticlockwise</b>",
        "2": "<b>180</b> degrees",
    }
    let face = move[0]
    let angle
    if (move.length == 1) { angle = 1 }
    else { angle = move[1] }
    let text = "Turn the " + faceToText[face] + " " + angleToText[angle]
    document.getElementById("solutionExplanation").innerHTML = text
}

let notationToggle = false
document.getElementById("solutionExplanation").style.display = "none";
document.getElementById("longInstruction").addEventListener("click", displayLong);
function displayLong() {
    notationToggle = !notationToggle
    if (notationToggle) {
        document.getElementById("solutionExplanation").style.display = "block";
        document.getElementById("solutionText").style.display = "none";
    } else {
        document.getElementById("solutionExplanation").style.display = "none";
        document.getElementById("solutionText").style.display = "block";
    }
}

document.getElementById("playPause").style.display = "none";
document.getElementById("solutionText").style.display = "none";
document.getElementById("wholeSolve").addEventListener("click", overallSolve);
function overallSolve() {
    solveCube(exportCubeState["cubeState"])
    console.log(exportCubeState["cubeState"])
    document.getElementById("wholeSolve").style.display = "none"
    document.getElementById("playPause").style.display = "inline"
    setTimeout(() => {
        doSolve();
        let showSolution = ""
        let solution = exportSolution["moves"]
        for (var move in solution) {
            showSolution = showSolution.concat(solution[move], " ")
        }
        document.getElementById("solutionText").innerHTML = showSolution
        document.getElementById("solutionText").style.display = "inline";
    }, 2000)
}

function randomScramble() {
    var indexToMove = {
        0: "U",
        1: "U'",
        2: "U2",
        3: "D",
        4: "D'",
        5: "D2",
        6: "L",
        7: "L'",
        8: "L2",
        9: "R",
        10: "R'",
        11: "R2",
        12: "B",
        13: "B'",
        14: "B2",
        15: "F",
        16: "F'",
        17: "F2",
        18: "F2",
    }
    let scramble = ''
    for (var i = 0; i < 20; i++) {
        let index = Math.floor(Math.random() * 17)
        scramble = scramble.concat(indexToMove[index], " ")
    }
    scramble = scramble.slice(0, -1)
    console.log(scramble)

    return scramble
}

document.getElementById("randomScramble").addEventListener("click", randomAndSubmit);
function randomAndSubmit() {
    let scramble = randomScramble()
    document.getElementById("cubeScramble").value = scramble
    submit()
}

document.getElementById("scrambleForm").style.display = "none";
let displayForm = false
document.getElementById("inputScramble").addEventListener("click", showForm);
function showForm() {
    displayForm = !displayForm
    if (displayForm) {
        document.getElementById("scrambleForm").style.display = "inline"
    } else {
        document.getElementById("scrambleForm").style.display = "none"
    }
}

let startStop = false
document.getElementById("playPause").addEventListener("click", play);
function play() {
    startStop = !startStop
    if (startStop) {
        document.getElementById("playPause").innerHTML = "Pause"
        for (var i = 0; i < document.getElementById("basicMoves").children.length; i++) {
            document.getElementById("basicMoves").children[i].style.backgroundColor = "#e1e1e2"
            document.getElementById("basicMoves").children[i].disabled = true;
        }
        for (var i = 0; i < document.getElementById("leftMoves").children.length; i++) {
            document.getElementById("leftMoves").children[i].style.backgroundColor = "#e1e1e2"
            document.getElementById("leftMoves").children[i].disabled = true;
        }
        for (var i = 0; i < document.getElementById("bottomMoves").children.length; i++) {
            document.getElementById("bottomMoves").children[i].style.backgroundColor = "#e1e1e2"
            document.getElementById("bottomMoves").children[i].disabled = true;
        }
        document.getElementById("stepForward").style.backgroundColor = "#e1e1e2"
        document.getElementById("stepForward").disabled = true;
        document.getElementById("stepBackward").style.backgroundColor = "#e1e1e2"
        document.getElementById("stepBackward").disabled = true;
        document.getElementById("randomScramble").style.backgroundColor = "#e1e1e2"
        document.getElementById("randomScramble").disabled = true;
    } else {
        document.getElementById("playPause").innerHTML = "Play"
        for (var i = 0; i < document.getElementById("basicMoves").children.length; i++) {
            document.getElementById("basicMoves").children[i].style.backgroundColor = "#ffe8dc"
            document.getElementById("basicMoves").children[i].disabled = false;
        }
        for (var i = 0; i < document.getElementById("leftMoves").children.length; i++) {
            document.getElementById("leftMoves").children[i].style.backgroundColor = "#fcd1b8"
            document.getElementById("leftMoves").children[i].disabled = false;
        }
        for (var i = 0; i < document.getElementById("bottomMoves").children.length; i++) {
            document.getElementById("bottomMoves").children[i].style.backgroundColor = "#fcd1b8"
            document.getElementById("bottomMoves").children[i].disabled = false;
        }
        document.getElementById("stepForward").style.backgroundColor = "#fcd1b8"
        document.getElementById("stepForward").disabled = false;
        document.getElementById("stepBackward").style.backgroundColor = "#fcd1b8"
        document.getElementById("stepBackward").disabled = false;
        document.getElementById("randomScramble").style.backgroundColor = "#fcd1b8"
        document.getElementById("randomScramble").disabled = false;
    }
}


document.getElementById("stepForward").addEventListener("click", forwardOneMove);
function forwardOneMove() {
    let solution = exportSolution["moves"];
    console.log(solution[solutionIndex])
    updateNotationText(solution[solutionIndex])
    completeTurn(solution[solutionIndex])
    solutionIndex += 1
    console.log(solutionIndex)
    let progressBarWidth = document.getElementById('bar').offsetWidth
    progressBarWidth = (progressBarWidth - 20) * solutionIndex / solution.length + 20
    document.getElementById("progress").style.width = progressBarWidth + 'px';
    if (solutionIndex == solution.length) {
        document.getElementById("wholeSolve").style.display = "inline"
        document.getElementById("playPause").style.display = "none"
    }
}

document.getElementById("stepBackward").addEventListener("click", backwardOneMove);
function backwardOneMove() {
    solutionIndex -= 1
    console.log(solutionIndex)
    let solution = exportSolution["moves"];
    let move = solution[solutionIndex]
    let inverseMove = move[0]
    let direction
    let inverse = {
        "1": "'",
        "'": "",
        "2": "2"
    }
    if (move.length == 2) {
        direction = move[1]
    } else { direction = 1 }
    let inverseDirection = inverse[direction]
    inverseMove = inverseMove + inverseDirection
    console.log(inverseMove)
    updateNotationText(solution[solutionIndex])
    completeTurn(inverseMove)
    let progressBarWidth = document.getElementById('bar').offsetWidth
    progressBarWidth = (progressBarWidth - 20) * solutionIndex / solution.length + 20
    document.getElementById("progress").style.width = progressBarWidth + 'px';
}

let backToggle = false
document.getElementById("showBackSides").addEventListener("click", showBack);
function showBack() {
    backToggle = !backToggle
    if (backToggle) {
        for (var square in allFloats) {
            allFloats[square].visible = true
        }
    } else {
        for (var square in allFloats) {
            allFloats[square].visible = false
        }
    }
}

let howToToggle = false
document.getElementById("howTo").style.display = "none";
document.getElementById("showHowTo").addEventListener("click", showHowTo);
function showHowTo() {
    howToToggle = !howToToggle
    if (howToToggle) {
        document.getElementById("howTo").style.display = "block";
    } else {
        document.getElementById("howTo").style.display = "none";
    }
}

let moreMovesToggle = false
document.getElementById("bottomMoves").style.display = "none";
document.getElementById("leftMoves").style.display = "none";
document.getElementById("moreMoves").addEventListener("click", showMoreMoves);
function showMoreMoves() {
    moreMovesToggle = !moreMovesToggle
    if (moreMovesToggle) {
        document.getElementById("bottomMoves").style.display = "block";
        document.getElementById("leftMoves").style.display = "block";
        document.getElementById("moveButtons").style.width = "320px";
        document.getElementById("moveButtons").style.height = "350px";
        document.getElementById("movesTitle").innerHTML = "All Moves";
        document.getElementById("moreMoves").style.top = "20px";
        document.getElementById("moreMoves").innerHTML = "Show Fewer Moves";
    } else {
        document.getElementById("bottomMoves").style.display = "none";
        document.getElementById("leftMoves").style.display = "none";
        document.getElementById("moveButtons").style.width = "160px";
        document.getElementById("moveButtons").style.height = "240px";
        document.getElementById("movesTitle").innerHTML = "Basic Moves";
        document.getElementById("moreMoves").style.top = "225px";
        document.getElementById("moreMoves").innerHTML = "Show More Moves";
    }
}

