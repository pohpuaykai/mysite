// import * as THREE from './static/three/three.core.js';
import * as THREE from './static/three/three.module.js';
import {OrbitControls} from './static/three/OrbitControls.js';
import {TextGeometry} from './static/three/TextGeometry.js';
import {FontLoader} from './static/three/FontLoader.js';
import {GLTFLoader} from './static/three/GLTFLoader.js';

import {mesh as cylinder_mesh} from './static/meshes/mesh_cylinder.js';




let camera, scene, renderer;
scene = new THREE.Scene();
scene.background = new THREE.Color( 0xf0f0f0 );
const fov = 45;//Camera frustum vertical field of view
const aspect = window.innerWidth / window.innerHeight; //Camera frustum aspect ratio
const near = 1;//Camera frustum near plane
const far = 10000;//Camera frustum far plane

camera = new THREE.PerspectiveCamera( fov, window.innerWidth / window.innerHeight, near, far );
camera.position.set( 0, - 400, 600 );
renderer = new THREE.WebGLRenderer( { antialias: true } );
renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( window.innerWidth, window.innerHeight );

document.body.appendChild( renderer.domElement );

function render() {
    renderer.render(scene, camera);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    
    renderer.setSize(window.innerWidth, window.innerHeight);
    
    render();
}
//cubeTutorial();

//permanentFUNCTIONS
function addCube(size, color) {

    //THE CUBE
    const geometry = new THREE.BoxGeometry( size.x, size.y, size.z );
    const material = new THREE.MeshBasicMaterial( { color: color } );
    const cube = new THREE.Mesh( geometry, material );
    scene.add( cube );
    function animate() {

        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        render();
    }
    return animate;

}
// let animate = addCube({x:64, y:64, z:64}, 0x00ff00)

// renderer.setAnimationLoop( animate );


scene.add(cylinder_mesh); render();

function addText(message, position, color, materialName) {
    const loader = new FontLoader();
    loader.load('fonts/helvetiker_regular.typeface.json', function(font){
        let material;
        if (materialName == 'line') {

        // console.log(color);
            material = new THREE.LineBasicMaterial( {
                color: color,
                side: THREE.DoubleSide
            } );
            // console.log(material);
        } else if (materialName == 'mesh') {

        // console.log(color);
            material = new THREE.MeshBasicMaterial( {
                color: color,
                transparent: true,
                opacity: 0.4,
                side: THREE.DoubleSide
            } );
            // console.log(material);
        }

        // console.log(color);
        //
        const shapes = font.generateShapes( message, 100 );
        const geometry = new THREE.ShapeGeometry( shapes );
        geometry.computeBoundingBox();
        const xMid = - 0.5 * ( geometry.boundingBox.max.x - geometry.boundingBox.min.x );

        if (materialName == 'line') {

            // make line shape ( N.B. edge view remains visible )
            const holeShapes = [];

            for ( let i = 0; i < shapes.length; i ++ ) {
                const shape = shapes[ i ];
                if ( shape.holes && shape.holes.length > 0 ) {
                    for ( let j = 0; j < shape.holes.length; j ++ ) {
                        const hole = shape.holes[ j ];
                        holeShapes.push( hole );
                    }
                }
            }

            shapes.push( ...holeShapes );
            const lineText = new THREE.Object3D();
            for ( let i = 0; i < shapes.length; i ++ ) {
                const shape = shapes[ i ];
                const points = shape.getPoints();
                const geometry = new THREE.BufferGeometry().setFromPoints( points );
                geometry.translate( xMid, 0, 0 );
                const lineMesh = new THREE.Line( geometry, material );
                lineText.add( lineMesh );

            }
            scene.add( lineText );
        } else if (materialName == 'mesh') {
            geometry.translate( xMid, 0, 0 );
            // make shape ( N.B. edge view not visible )
            const text = new THREE.Mesh( geometry, material );
            text.position.x = position.x;
            text.position.y = position.y;
            text.position.z = position.z;
            scene.add( text );

        }


        render();
    });
}
// addText("   Three.js\nSimple text.", {x:0, y:0, z:-150}, 0x006699, 'line');
// addText("   Three.js\nSimple text.", {x:0, y:0, z:-150}, 0x006699, 'mesh');


//controls

const controls = new OrbitControls( camera, renderer.domElement );
controls.target.set( 0, 0, 0 );
controls.update();

controls.addEventListener( 'change', render );

window.addEventListener( 'resize', onWindowResize );


//permanentFUNCTIONS
