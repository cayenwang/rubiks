import * as THREE from './three.js-dev/build/three.module.js';
import { OrbitControls } from './three.js-dev/examples/jsm/controls/OrbitControls.js';
//import { AnimationClip, AnimationMixer, QuaternionKeyframeTrack, Clock } from './three.js-dev/build/three.module.js';
import { exportAngle, exportAxis, exportMatrix, exportSquaresToTurn, getSquaresOnFace } from './networking.js'

/*
=========================================================================================
World Building
=========================================================================================
*/

let camera, controls, scene, renderer;
let startStop = false
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
    camera.position.set(400, 200, -100);

    window.addEventListener('resize', onWindowResize);

    // build cube
    let scramble = "yybgwwogrorbroybbgyogogwoygyoogrgwbwwbgybwbbrwrrwyryor";
    cubeSquares = buildCube(scramble);

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
    let rotationList = exportSquaresToTurn['rotationList']
    let sideR = [], sideL = [], sideD = [], sideU = [], sideB = [], sideF = []

    // for each position 
    for (var i in positionList) {
        let aPosition = positionList[i]
        let aRotation = rotationList[i]
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

                // and also add it to an array corresponding to its rotation
                // if (aRotation[0] == 1) { sideR.push(square) }
                // if (aRotation[0] == -1) { sideL.push(square) }
                // if (aRotation[1] == 1) { sideD.push(square) }
                // if (aRotation[1] == -1) { sideU.push(square) }
                // if (aRotation[2] == 1) { sideB.push(square) }
                // if (aRotation[2] == -1) { sideF.push(square) }
            }
        }
    }
    /*
    // find which face has 9 squares. that will be the face we're rotating
    let resultSquaresOnOtherSide
    if (sideR.length == 9) { resultSquaresOnOtherSide = sideL.concat(sideD, sideU, sideB, sideF) }
    if (sideL.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideD, sideU, sideB, sideF) }
    if (sideD.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideL, sideU, sideB, sideF) }
    if (sideU.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideL, sideD, sideB, sideF) }
    if (sideB.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideL, sideD, sideU, sideF) }
    if (sideF.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideL, sideD, sideU, sideB) }
    */
    let result = {
        //"resultSquaresOnOtherSide": resultSquaresOnOtherSide,
        "resultSquaresToTurn": resultSquaresToTurn
    }
    return result
}

function turnSquares() {
    //find the squares to turn
    let resultSquares = findSquaresToTurn()
    let squaresToTurnPleaseBeUnique = resultSquares['resultSquaresToTurn']
    console.log(squaresToTurnPleaseBeUnique)

    let targetAxis = exportAxis
    let targetAngle = exportAngle

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
        let angle = targetAngle * Math.PI / 100

        var matrix = new THREE.Matrix4();
        matrix.makeRotationAxis(axis, angle)

        if (counter < 50) {
            requestAnimationFrame(rotator);
            for (var square in squaresToTurnPleaseBeUnique) {
                squaresToTurnPleaseBeUnique[square].applyMatrix4(matrix);

            }
            counter += 1
        }
        if (counter == 50) {
            for (var square in squaresToTurnPleaseBeUnique) {
                let xyz = ["x", "y", "z"]
                for (var i in xyz) {
                    if (squaresToTurnPleaseBeUnique[square].position[xyz[i]] < -27) { squaresToTurnPleaseBeUnique[square].position[xyz[i]] = -33 }
                    if (
                        (squaresToTurnPleaseBeUnique[square].position[xyz[i]] > -27)
                        && (squaresToTurnPleaseBeUnique[square].position[xyz[i]] < -10)) {
                        squaresToTurnPleaseBeUnique[square].position[xyz[i]] = -22
                    }
                    if (
                        (squaresToTurnPleaseBeUnique[square].position[xyz[i]] > -10)
                        && (squaresToTurnPleaseBeUnique[square].position[xyz[i]] < 10)) {
                        squaresToTurnPleaseBeUnique[square].position[xyz[i]] = 0
                    }
                    if (
                        (squaresToTurnPleaseBeUnique[square].position[xyz[i]] > 10)
                        && (squaresToTurnPleaseBeUnique[square].position[xyz[i]] < 27)) {
                        squaresToTurnPleaseBeUnique[square].position[xyz[i]] = 22
                    }
                    if (squaresToTurnPleaseBeUnique[square].position[xyz[i]] > 27) { squaresToTurnPleaseBeUnique[square].position[xyz[i]] = 33 }
                }
            }
        }

        renderer.render(scene, camera);
    }
    rotator()
}

function completeTurn(face) {
    getSquaresOnFace(face)
    setTimeout(() => { counter = 0; turnSquares() }, 500);

}


document.getElementById("completeU").addEventListener("click", function () { completeTurn("U") });
document.getElementById("completeF").addEventListener("click", function () { completeTurn("F") });
document.getElementById("play").addEventListener("click", play);
