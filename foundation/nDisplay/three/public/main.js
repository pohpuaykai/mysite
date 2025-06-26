// import * as THREE from './static/three/three.core.js';
import * as THREE from './static/three/three.module.js';
import {OrbitControls} from './static/three/OrbitControls.js';
// import {TextGeometry} from './static/three/TextGeometry.js';
// import {FontLoader} from './static/three/FontLoader.js';
import {GLTFLoader} from './static/three/GLTFLoader.js';

import {asyncCreateTextMesh} from './static/custom/TextMeshCreater.js';

// import {mesh as cylinder_mesh} from './static/meshes/mesh_cylinder.js';
// import {mesh as wall_mesh} from './static/meshes/mesh_wall.js';
// import {mesh as trench_mesh} from './static/meshes/mesh_trench.js';
// import {mesh as resistor_outline_mesh} from './static/meshes/mesh_resistor_outline.js';
// import {MeshResistor} from './static/meshes/MeshResistor.js';
// import {MeshCapacitor} from './static/meshes/MeshCapacitor.js';
import {ComponentResistor} from './static/meshes/ComponentResistor.js';
import {ComponentBattery} from './static/meshes/ComponentBattery.js';
import {ComponentDiode} from './static/meshes/ComponentDiode.js';
import {ComponentCapacitor} from './static/meshes/ComponentCapacitor.js';
import {ComponentInductor} from './static/meshes/ComponentInductor.js';
import {ComponentOscillator} from './static/meshes/ComponentOscillator.js';
import {ComponentTransistor} from './static/meshes/ComponentTransistor.js';
import {ComponentACSignalGenerator} from './static/meshes/ComponentACSignalGenerator.js';




let camera, scene, renderer;
scene = new THREE.Scene();
scene.background = new THREE.Color( 0x808080 );
const fov = 45;//Camera frustum vertical field of view
const aspect = window.innerWidth / window.innerHeight; //Camera frustum aspect ratio
const near = 1;//Camera frustum near plane
const far = 10000;//Camera frustum far plane

camera = new THREE.PerspectiveCamera( fov, window.innerWidth / window.innerHeight, near, far );
camera.position.set( 0, 0, 10 );
renderer = new THREE.WebGLRenderer( { antialias: true } );
renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( window.innerWidth, window.innerHeight );

document.body.appendChild( renderer.domElement );

//add pointlight TODO light seems to have no difference for MeshBasicMaterial
// const light = new THREE.PointLight(0xffffff, 1, 10, 2);//color, intensity, range_of_light, decay_of_light
// light.position.set(5, 5, 5);
// scene.add(light);

function render() {
    renderer.render(scene, camera);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    
    renderer.setSize(window.innerWidth, window.innerHeight);
    
    render();
}

//permanentFUNCTIONS

// cylinder_mesh.position.set(0, 0, 0);
// scene.add(cylinder_mesh); render();
// scene.add(wall_mesh); render();
// scene.add(trench_mesh); render();
// scene.add(resistor_outline_mesh); render();

// const resistor0 = new MeshResistor({x:0, y:0, z:-10});
// resistor0.rotation.set(0, 0, Math.PI/2);
// scene.add(resistor0);render();

// const resistor1 = new MeshResistor({x:0, y:15, z:-10});
// resistor1.rotation.set(0, 0, Math.PI/2);
// scene.add(resistor1);render();

// console.log('boundingBox of resistor1: ');
// console.log(resistor1.geometry.boundingBox);
// // resistor1.geometry.computeBoundingBox();
// // console.log(resistor1.geometry.boundingBox);
// console.log(resistor1.leftConnectionBox);
// console.log(resistor1.rightConnectionBox);
//draw orthogonal wires to connection resistors, example call: wire(resistor0, resistor1); and it should return the wire object, wire should take at most 3 bends, works like text?

// const testCapacitor0 = new MeshCapacitor({x:0, y:0, z:10});
// scene.add(testCapacitor0); render();



// const resistor0 = new ComponentResistor({x:0, y:0, z:10});
// scene.add(resistor0); render();

// const battery0 = new ComponentBattery({x:0, y:0, z:10});
// scene.add(battery0); render();

// const diode0 = new ComponentDiode({x:0, y:0, z:10});
// scene.add(diode0); render();


// const capacitor0 = new ComponentCapacitor({x:0, y:0, z:0});
// scene.add(capacitor0); render();

// const inductor0 = new ComponentInductor({x:0, y:0, z:10});
// scene.add(inductor0); render();

const oscillator0 = new ComponentOscillator({x:0, y:0, z:10});
scene.add(oscillator0); render();

// const transistor0 = new ComponentTransistor({x:0, y:0, z:10});
// scene.add(transistor0); render();

// const acSignalGenerator0 = new ComponentACSignalGenerator({x:0, y:0, z:10});
// scene.add(acSignalGenerator0); render();


asyncCreateTextMesh("These are 11.6 kOhm -+2% Vishal Resistor", {x:0, y:4, z:0}, 0x006699, 'mesh', 1, function(textMesh){
    scene.add(textMesh); render();
});

//after placing all the Object3D into the scene, then we can start trying to animate the scene
function animate(){
    let rotatingObject = inductor0;
    // rotatingObject.rotation.x += (Math.PI/(360*6));
    // rotatingObject.rotation.y += (Math.PI/(360*6));
    // rotatingObject.rotation.z += (Math.PI/(360*6));
    render();
}

//controls

const controls = new OrbitControls( camera, renderer.domElement );
controls.target.set( 0, 0, 0 );
controls.update();

controls.addEventListener( 'change', render );

window.addEventListener( 'resize', onWindowResize );


//permanentFUNCTIONS
render();

renderer.setAnimationLoop( animate );