import * as THREE from './three.js-dev/build/three.module.js';
import { OrbitControls } from './three.js-dev/examples/jsm/controls/OrbitControls.js';
//import { AnimationClip, AnimationMixer, QuaternionKeyframeTrack, Clock } from './three.js-dev/build/three.module.js';
import { exportAngle, exportAxis, exportMatrix, exportSquaresToTurn } from './networking.js'

/*
=========================================================================================
World Building
=========================================================================================
*/

let camera, controls, scene, renderer, clock, mixer;
let startStop = false
let cubeSquares
createScene();
setCameraControls();
setLighting()
animate();
//render()

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

    //const animationGroup = new THREE.AnimationObjectGroup();

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

        /*
        // define animation tracks, clips and mixer
        const xAxis = new THREE.Vector3(1, 0, 0);
        const qInitial = new THREE.Quaternion().setFromAxisAngle(xAxis, 0);
        const qFinal = new THREE.Quaternion().setFromAxisAngle(xAxis, Math.PI);
        const quaternionKF = new THREE.QuaternionKeyframeTrack('.quaternion', [0, 1, 2], [qInitial.x, qInitial.y, qInitial.z, qInitial.w, qFinal.x, qFinal.y, qFinal.z, qFinal.w, qInitial.x, qInitial.y, qInitial.z, qInitial.w]);
        const colorKF = new THREE.ColorKeyframeTrack('.material.color', [0, 1, 2], [1, 0, 0, 0, 1, 0, 0, 0, 1], THREE.InterpolateDiscrete);
        const opacityKF = new THREE.NumberKeyframeTrack('.material.opacity', [0, 1, 2], [1, 0, 1]);
        // create clip
        const clip = new THREE.AnimationClip('default', 3, [quaternionKF, colorKF, opacityKF]);
        mixer = new THREE.AnimationMixer(animationGroup);
        const clipAction = mixer.clipAction(clip);
        clipAction.play();
        clock = new THREE.Clock();
        */

        return allSquares
    }

}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    render()
}

function render() {
    //const delta = clock.getDelta();
    //if (mixer) { mixer.update(delta); }
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
                if (aRotation[0] == 1) { sideR.push(square) }
                if (aRotation[0] == -1) { sideL.push(square) }
                if (aRotation[1] == 1) { sideD.push(square) }
                if (aRotation[1] == -1) { sideU.push(square) }
                if (aRotation[2] == 1) { sideB.push(square) }
                if (aRotation[2] == -1) { sideF.push(square) }
            }
        }
    }

    // find which face has 9 squares. that will be the face we're rotating
    let resultSquaresOnOtherSide
    if (sideR.length == 9) { resultSquaresOnOtherSide = sideL.concat(sideD, sideU, sideB, sideF) }
    if (sideL.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideD, sideU, sideB, sideF) }
    if (sideD.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideL, sideU, sideB, sideF) }
    if (sideU.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideL, sideD, sideB, sideF) }
    if (sideB.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideL, sideD, sideU, sideF) }
    if (sideF.length == 9) { resultSquaresOnOtherSide = sideR.concat(sideL, sideD, sideU, sideB) }

    console.log("resultSquaresOnOtherSide", resultSquaresOnOtherSide)

    console.log("resultSquaresToTurn", resultSquaresToTurn)

    let result = {
        "resultSquaresOnOtherSide": resultSquaresOnOtherSide,
        "resultSquaresToTurn": resultSquaresToTurn
    }
    return result
}


function turnSquares() {
    //define the axis and angle of rotation
    let axis = new THREE.Vector3(0, 0, 0);
    if (exportAxis == "X") {
        axis.set(1, 0, 0);
    } else if (exportAxis == "Y") {
        axis.set(0, 1, 0);
    } else if (exportAxis == "Z") {
        axis.set(0, 0, 1);
    }
    let angle = exportAngle * Math.PI / 2

    const quaternion = new THREE.Quaternion();
    quaternion.setFromAxisAngle(axis, angle)

    //find the squares to turn
    let resultSquares = findSquaresToTurn()
    let squaresToTurn = resultSquares['resultSquaresToTurn']
    let squaresOnOtherSide = resultSquares['resultSquaresOnOtherSide']
    console.log("squaresOnOtherSide", squaresOnOtherSide)

    //==== new stuff


    //ROTATES BOTTOM LAYER SMOOTHLY WITH ANIMATION
    function render3() {

        var matrix = new THREE.Matrix4();
        matrix.makeRotationY(Math.PI / 100);

        requestAnimationFrame(render3);
        for (var square in squaresToTurn) {
            if (startStop == true) {
                squaresToTurn[square].applyMatrix4(matrix);
            } else { break }
            renderer.render(scene, camera);

        }

    }
    render3();

};

function test3() {
    turnSquares()
}

function play() {
    startStop = !startStop
    console.log("after", startStop)
}

document.getElementById("test3").addEventListener("click", test3);
document.getElementById("play").addEventListener("click", play);


//=========== animation? who knows

/* CREATES A SMALL SQUARE ORBITING 
//Make an object 
var geometry = new THREE.BoxGeometry(10, 10, 10);
var material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
var object = new THREE.Mesh(geometry, material);
object.position.z = -70
scene.add(object);
//Create a matrix
var matrix = new THREE.Matrix4();
//Rotate the matrix
matrix.makeRotationY(Math.PI / 100);
var render3 = function () {
    requestAnimationFrame(render3);
    object.position.applyMatrix4(matrix);
    renderer.render(scene, camera);
};
render3();*/

/*ROTATES BOTTOM LAYER WITH NO IN BETWEEN ANIMATION
    // rotate the position of the squares
    for (var square in squaresToTurn) {
        let position = squaresToTurn[square].position
        const vector = new THREE.Vector3(position.x, position.y, position.z);
        vector.applyQuaternion(quaternion);
        squaresToTurn[square].position.x = Math.round(vector.x)
        squaresToTurn[square].position.y = Math.round(vector.y)
        squaresToTurn[square].position.z = Math.round(vector.z)
    }
    // rotate the rotation of the squreas
    for (var square in squaresOnOtherSide) {
        squaresOnOtherSide[square].rotateOnAxis(axis, angle)
    }
    */

/* BROKEN AF
function play() {
    let resultSquares = findSquaresToTurn()
    let squaresToTurn = resultSquares['resultSquaresToTurn']
    let squaresOnOtherSide = resultSquares['resultSquaresOnOtherSide']
    const quaternionKF = new QuaternionKeyframeTrack(
        '.rotationtrack',
        [0, 1],
        [0, 0, 0, 0, 0.9992290362407227, 0, -0.039259815759073224, 0]);
    const clip = new AnimationClip('rotationclip', -1, [quaternionKF]);
    for (var square in squaresToTurn) {
        function setupModel(data) {
            const model = data.scene.children[0];
            const clip = data.animations[0];
            const mixer = new AnimationMixer(model);
            const action = mixer.clipAction(clip);
            action.play();
            model.tick = (delta) => mixer.update(delta);
            return model;
        }
        setupModel()
    }
}
function stop() {
    action.stop()
}*/