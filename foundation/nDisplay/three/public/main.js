// import * as THREE from './static/three/three.core.js';
import * as THREE from './static/three/three.module.js';
// import {GLTFLoader} from './static/three/GLTFLoader.js';
import {SVGLoader} from './static/three/SVGLoader.js';

import {asyncCreateTextMesh} from './static/custom/TextMeshCreater.js';

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
import {DCTwoResistorSeries} from './static/pieces/dc_twoResistor_series.js';
import {DCTwoResistorParallel} from './static/pieces/dc_twoResistor_parallel.js';



let camera, scene, renderer;
scene = new THREE.Scene();
scene.background = new THREE.Color( 0x808080 );
const fov = 45;//Camera frustum vertical field of view
const aspect = window.innerWidth / window.innerHeight; //Camera frustum aspect ratio
const near = 1;//Camera frustum near plane
const far = 10000;//Camera frustum far plane

camera = new THREE.PerspectiveCamera( fov, window.innerWidth / window.innerHeight, near, far );
camera.position.set( 0, 0, -50 );
renderer = new THREE.WebGLRenderer( { antialias: true } );
renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( window.innerWidth, window.innerHeight );

document.body.appendChild( renderer.domElement );

const axesHelper = new THREE.AxesHelper(5);
scene.add(axesHelper);

//add pointlight TODO light seems to have no difference for MeshBasicMaterial, because i didn't generate UV
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

// const circuit = new DCTwoResistorSeries(scene, camera, renderer, {});
const circuit = new DCTwoResistorParallel(scene, camera, renderer, {});
const rD = circuit.act();
//spread the returnDictionary into this environment: (ChatGPT says cannot get local scope representation)
scene = rD['scene']; camera = rD['camera']; renderer = rD['renderer']; 
const resistor0 = rD['meshes']['resistor0']; const battery0 = rD['meshes']['battery0']; const resistor1 = rD['meshes']['resistor1'];
const wireBetween01 = rD['meshes']['wireBetween01']; 
// const wireBetween10 = rD['meshes']['wireBetween10'];
// const wireBetween11 = rD['meshes']['wireBetween11'];
const animate = rD['animate'];
console.log('circuit network:', circuit.getNetworkGraph());
console.log('circuit network stringify:', JSON.stringify(circuit.getNetworkGraph()));
console.log('circuit id__type: ', circuit.id__type);
// console.log('sending data to: ', findEquationsAndSolve_url);
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const request = new Request(findEquationsAndSolve_url, {
    method:"POST", 
    headers: {'X-CSRFToken':csrftoken},
    mode:'same-origin',
    body:JSON.stringify({
    'networkGraph':JSON.stringify(circuit.getNetworkGraph()).replaceAll('"', ''), //because keys gets converted to string internally in javscript, and we want everything to be in integers
        'id__type':circuit.id__type,
        'id__positiveLeadsDirections':circuit.id__positiveLeadsDirections
    })
});
// fetch(request).then(response => {//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<uncomment after you put Latex on THREE.scene
//     console.log('response: ', response);
//     console.log(response.body);
// }).catch(error => {
//     console.log('error: ', error);
// });

//test out SVG=>THREE.js setup Courtesy of ChatGPT
function getCleanSVG(math) {
  const svgNode = MathJax.tex2svg(math, {display: true});
  const svg = svgNode.querySelector("svg");

  // Clean style to avoid CSS inheritance issues
  svg.removeAttribute("style");

  // Serialize to string
  return new XMLSerializer().serializeToString(svg);
}
const svgString = getCleanSVG("x^2 + y^2 = z^2");
const blob = new Blob([svgString], {type: "image/svg+xml"});
const url = URL.createObjectURL(blob);

const loader = new SVGLoader();
loader.load(url, (data) => {
  const paths = data.paths;
  const group = new THREE.Group();

  for (const path of paths) {
    const material = new THREE.MeshBasicMaterial({
      color: path.color,
      side: THREE.DoubleSide,
      depthWrite: false
    });

    const shapes = path.toShapes(true);
    for (const shape of shapes) {
      const geometry = new THREE.ShapeGeometry(shape);
      const mesh = new THREE.Mesh(geometry, material);
      group.add(mesh);
    }
  }

  scene.add(group);
});
//



//controls
// const controls = new OrbitControls( camera, renderer.domElement );
const controls = new GuiControls(camera, scene, renderer.domElement);
controls.target.set( 0, 0, 0 );
controls.update();

controls.addEventListener( 'change', render );

window.addEventListener( 'resize', onWindowResize );

render();

renderer.setAnimationLoop( animate );