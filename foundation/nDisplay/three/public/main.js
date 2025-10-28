// import * as THREE from './static/three/three.core.js';
import * as THREE from './static/three/three.module.js';
// import {GLTFLoader} from './static/three/GLTFLoader.js';
import {SVGLoader} from './static/three/SVGLoader.js';
import {Recorder} from './static/mediaRecorder/recorder.js';

// import {asyncCreateTextMesh} from './static/custom/TextMeshCreater.js';
// import {asyncCreateLatexMesh} from './static/custom/LatexMeshCreater.js';

// import {mesh as cylinder_mesh} from './static/meshes/mesh_cylinder.js';
// import {mesh as wall_mesh} from './static/meshes/mesh_wall.js';
// import {mesh as trench_mesh} from './static/meshes/mesh_trench.js';
// import {mesh as resistor_outline_mesh} from './static/meshes/mesh_resistor_outline.js';
// import {MeshResistor} from './static/meshes/MeshResistor.js';
// import {MeshCapacitor} from './static/meshes/MeshCapacitor.js';

import {GuiControls} from './static/custom/GuiControls.js';
// import {ComponentResistor} from './static/meshes/ComponentResistor.js';
// import {ComponentBattery} from './static/meshes/ComponentBattery.js';
// import {ComponentDiode} from './static/meshes/ComponentDiode.js';
// import {ComponentCapacitor} from './static/meshes/ComponentCapacitor.js';
// import {ComponentInductor} from './static/meshes/ComponentInductor.js';
// import {ComponentOscillator} from './static/meshes/ComponentOscillator.js';
// import {ComponentTransistor} from './static/meshes/ComponentTransistor.js';
// import {ComponentACSignalGenerator} from './static/meshes/ComponentACSignalGenerator.js';
// import {Wire} from './static/meshes/Wire.js';

// import {DCTwoResistorSeries} from './static/pieces/dc_twoResistor_series.js';
import {DCTwoResistorParallel} from './static/pieces/dc_twoResistor_parallel.js';
// import {Q2_3_5_aMoreComplexCircuit__P84} from './static/pieces/foundations_of_analog_and_digital_electronic_circuits_anantAgarwal/Q2_3_5_aMoreComplexCircuit__P84.js';
// import {Q3_21__P18} from './static/pieces/3000_solved_problems_in_electric_circuits__syedANasar/Q3_21__P18.js';



let camera, scene, renderer;
scene = new THREE.Scene();
scene.background = new THREE.Color( 0x808080 );
const fov = 45;//Camera frustum vertical field of view
const aspect = window.innerWidth / window.innerHeight; //Camera frustum aspect ratio
const near = 1;//Camera frustum near plane
const far = 10000;//Camera frustum far plane

camera = new THREE.PerspectiveCamera( fov, window.innerWidth / window.innerHeight, near, far );
camera.position.set( 0, 20, -80 );// camera.position.set( 0, 0, -50 );//OG camera.position, try moving the camera by animation.....?<<<<<<<<<<<<<<<<<<how to run one animation function after another....?
renderer = new THREE.WebGLRenderer( { antialias: true } );
renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( window.innerWidth, window.innerHeight );

document.body.appendChild( renderer.domElement );

// const axesHelper = new THREE.AxesHelper(5);
// scene.add(axesHelper);

//add pointlight TODO light seems to have no difference for MeshBasicMaterial, because i didn't generate UV
// const light = new THREE.PointLight(0xffffff, 1, 1000, 2);//color, intensity, range_of_light, decay_of_light
// light.position.set(5, 5, -20);
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

//controls
// const controls = new OrbitControls( camera, renderer.domElement );
const controls = new GuiControls(camera, scene, renderer.domElement);
controls.target.set( 0, 0, 0 );
controls.update();

controls.addEventListener( 'change', render );

const audioContext = new (window.AudioContext||window.webkitAudioContext)();


// const circuit = new DCTwoResistorSeries(scene, camera, renderer, audioContext, controls, []);
const circuit = new DCTwoResistorParallel(scene, camera, renderer, audioContext, controls, []);
// const circuit = new Q3_21__P18(scene, camera, renderer, controls, []);
// const circuit = new Q3_21__P18(scene, camera, renderer, controls, []);
// const circuit = new Q2_3_5_aMoreComplexCircuit__P84(scene, camera, renderer, controls, []);




const rD = circuit.act();
//spread the returnDictionary into this environment: (ChatGPT says cannot get local scope representation)
scene = rD['scene']; camera = rD['camera']; renderer = rD['renderer']; 
//const resistor0 = rD['meshes']['resistor0']; const battery0 = rD['meshes']['battery0']; const resistor1 = rD['meshes']['resistor1'];
//const wireBetween01 = rD['meshes']['wireBetween01']; 
// const wireBetween10 = rD['meshes']['wireBetween10'];
// const wireBetween11 = rD['meshes']['wireBetween11'];
// const animate = rD['animate'];
// console.log('circuit network:', circuit.getNetworkGraph());
// console.log('circuit network stringify:', JSON.stringify(circuit.getNetworkGraph()));
// console.log('circuit id__type: ', circuit.id__type);
// console.log('circuit edge__solderableIndices: ', circuit.edge__solderableIndices);


window.addEventListener( 'resize', onWindowResize );

render();
