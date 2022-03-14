import * as THREE from './three.js-dev/build/three.module.js';
import { OrbitControls } from './three.js-dev/examples/jsm/controls/OrbitControls.js';
//import { AnimationClip, AnimationMixer, QuaternionKeyframeTrack, Clock } from './three.js-dev/build/three.module.js';
import { exportAngle, exportAxis, exportMatrix, exportSquaresToTurn, getSquaresOnFace, solveCube, exportSolution } from './networking.js'

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
    camera.up.set(0, -1, 0)

    window.addEventListener('resize', onWindowResize);

}

// build cube
cubeSquares = buildCube();

function buildCube(state = "wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy") {
    let allSquares = []
    let sideWidth = 20;
    let separation = 1.1;

    const geometrySquare = new THREE.PlaneGeometry(sideWidth, sideWidth);
    const materialRed = new THREE.MeshPhongMaterial({ color: 0xde3421, flatShading: true });
    const materialOrange = new THREE.MeshPhongMaterial({ color: 0xc47806, flatShading: true })
    const materialYellow = new THREE.MeshPhongMaterial({ color: 0xeaed32, flatShading: true })
    const materialWhite = new THREE.MeshPhongMaterial({ color: 0xfffff7, flatShading: true })
    const materialGreen = new THREE.MeshPhongMaterial({ color: 0x2bcc2e, flatShading: true })
    const materialBlue = new THREE.MeshPhongMaterial({ color: 0x3e78d6, flatShading: true })

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
        }
    }

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

    let divider = 50
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

/*
=========================================================================================
Solve
=========================================================================================
*/


let cubeState

document.getElementById("solve").addEventListener("click", function () {
    solveCube(cubeState)
    setTimeout(() => { console.log(exportSolution) }, 500)
});

document.getElementById("submitCubeState").addEventListener("click", function () {
    cubeState = document.getElementById("cubeState").value
    console.log("cubestate", cubeState)
    for (let i = scene.children.length - 1; i >= 0; i--) {
        if (scene.children[i].type === "Mesh")
            scene.remove(scene.children[i]);
    }
    buildCube(cubeState)
});

function doSolve() {
    let solution = exportSolution["moves"];

    (function loop(i) {
        setTimeout(function () {
            console.log(solution[solution.length - i])
            completeTurn(solution[solution.length - i])
            if (--i) loop(i)
        }, 1000)
    })(solution.length)

}

function overallSolve() {
    solveCube()
    setTimeout(() => { doSolve() }, 500)
}

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

document.getElementById("TurnX").addEventListener("click", function () { completeTurn("X") });
document.getElementById("TurnY").addEventListener("click", function () { completeTurn("Y") });
document.getElementById("TurnZ").addEventListener("click", function () { completeTurn("Z") });

document.getElementById("Turnr").addEventListener("click", function () { completeTurn("r") });
document.getElementById("Turnl").addEventListener("click", function () { completeTurn("l") });
document.getElementById("Turnd").addEventListener("click", function () { completeTurn("d") });
document.getElementById("Turnu").addEventListener("click", function () { completeTurn("u") });
document.getElementById("Turnb").addEventListener("click", function () { completeTurn("b") });
document.getElementById("Turnf").addEventListener("click", function () { completeTurn("f") });


document.getElementById("wholeSolve").addEventListener("click", function () { overallSolve() });
